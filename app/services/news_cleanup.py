from app.db.supabase_client import supabase

def cleanup_old_news():
    """
    Elimina todas las noticias con más de 3 días de antigüedad.
    """
    try:
        result = supabase.table("news") \
            .delete() \
            .lt("created_at", "now() - interval '3 days'") \
            .execute()
        print(f"🧹 Limpieza completada. Filas borradas: {result}")
    except Exception as e:
        print(f"❌ Error en cleanup_old_news: {e}")
