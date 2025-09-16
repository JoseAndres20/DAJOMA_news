from urllib.parse import urljoin
from bs4 import BeautifulSoup
from app.db.supabase_client import supabase
from app.services.sources import NEWS_SOURCES
from app.services.utils import get_headers, get_proxy, get_session
from app.services.article_parser import fetch_article_data


def scrape_and_save(limit_per_source: int = 3):
    """Scrapear fuentes de noticias y guardar en Supabase sin duplicados."""
    all_results = []
    seen_urls = set()  #

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

                # Normalizar URL relativa
                link = urljoin(source["url"], link)

                # Evitar duplicados dentro de la ejecución
                if link in seen_urls:
                    continue
                seen_urls.add(link)

                # Extraer contenido (texto + imagen)
                article_text, image_url = fetch_article_data(link)

                #
                supabase.table("news").upsert(
                    {
                        "title": title,
                        "url": link,
                        "source": source["name"],
                        "text_content": article_text,
                        "image_url": image_url,
                    },
                    on_conflict="url"  # 
                ).execute()

                all_results.append({
                    "title": title,
                    "url": link,
                    "source": source["name"],
                    "text_content": article_text,
                    "image_url": image_url,
                })

        except Exception as e:
            print(f"❌ Error en {source['name']}: {e}")

    return all_results

