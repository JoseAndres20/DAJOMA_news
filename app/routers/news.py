from fastapi import APIRouter
from app.services.scraper import scrape_and_save
from app.db.supabase_client import supabase

router = APIRouter()

@router.get("/scrape")
def scrape_news(limit: int = 3):
    """
    Ejecuta el scraper en todas las fuentes y guarda en Supabase.
    """
    data = scrape_and_save(limit_per_source=limit)
    return {
        "status": "ok",
        "inserted": len(data),
        "articles": data
    }

@router.get("/news")
def get_news(limit: int = 20):
    """
    Obtiene noticias guardadas en Supabase (ordenadas por recientes).
    """
    res = supabase.table("news").select("*").order("id", desc=True).limit(limit).execute()
    return res.data
