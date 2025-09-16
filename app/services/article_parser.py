import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from app.services.utils import get_headers, get_proxy, get_session


def fetch_article_text(soup: BeautifulSoup, limit_paragraphs: int = 5) -> str:
    """Extraer texto de los primeros párrafos de un artículo."""
    try:
        paragraphs = soup.find_all("p")
        content = " ".join(p.get_text(strip=True) for p in paragraphs[:limit_paragraphs])
        return content
    except Exception as e:
        print(f"⚠️ Error parsing text: {e}")
        return ""


def fetch_article_image(soup: BeautifulSoup, base_url: str) -> str | None:
    """Intentar extraer la URL de la imagen principal de un artículo."""
    try:
        # Meta tag Open Graph
        og_image = soup.find("meta", property="og:image")
        if og_image and og_image.get("content"):
            return urljoin(base_url, og_image["content"])

        # Primera imagen dentro del HTML
        first_img = soup.find("img")
        if first_img and first_img.get("src"):
            return urljoin(base_url, first_img["src"])

    except Exception as e:
        print(f"⚠️ Error parsing image: {e}")

    return None


def fetch_article_data(url: str) -> tuple[str, str | None]:
    """Dado un URL, devuelve (texto, imagen)."""
    try:
        session = get_session()
        r = session.get(url, timeout=10, headers=get_headers(), proxies=get_proxy())
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")

        text_content = fetch_article_text(soup)
        image_url = fetch_article_image(soup, url)

        return text_content, image_url

    except Exception as e:
        print(f"⚠️ Error fetching article: {e}")
        return "", None
