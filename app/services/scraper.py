import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from app.db.supabase_client import supabase
from app.services.sources import NEWS_SOURCES
from app.services.utils import get_headers, get_proxy, get_session


def fetch_article_text(url: str) -> str:
    """Extraer los primeros párrafos de una noticia"""
    try:
        session = get_session()
        r = session.get(url, timeout=10, headers=get_headers(), proxies=get_proxy())
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        paragraphs = soup.find_all("p")
        content = " ".join(p.get_text(strip=True) for p in paragraphs[:5])
        return content
    except Exception as e:
        print(f"⚠️ Error fetching article text: {e}")
        return ""


def scrape_and_save(limit_per_source: int = 3):
    """Scrapear fuentes de noticias y guardar en Supabase"""
    all_results = []

    for source in NEWS_SOURCES:
        try:
            session = get_session()
            r = session.get(source["url"], timeout=10, headers=get_headers(), proxies=get_proxy())
            r.raise_for_status()
            soup = BeautifulSoup(r.text, "html.parser")

            items = soup.select(source["selector"])[:limit_per_source]

            for item in items:
                title = item.get_text(strip=True)
                link = str(item.get("href", "")).strip()
                if not link:
                    continue

                # 🔥 Normalizar URL relativa
                link = urljoin(source["url"], link)

                # Ignorar enlaces que no sean http/https
                if not link.startswith("http"):
                    continue

                # Extraer texto
                article_text = fetch_article_text(link)

                # Guardar en Supabase evitando duplicados con `url`
                supabase.table("news").upsert(
                    {
                        "title": title,
                        "url": link,
                        "source": source["name"],
                        "text_content": article_text,
                    },
                    on_conflict="url"   # 👈 clave única
                ).execute()

                all_results.append({
                    "title": title,
                    "url": link,
                    "source": source["name"],
                    "text_content": article_text,
                })

        except Exception as e:
            print(f"❌ Error en {source['name']}: {e}")

    return all_results
