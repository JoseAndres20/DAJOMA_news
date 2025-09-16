from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from apscheduler.schedulers.background import BackgroundScheduler

from app.routers import news
from app.services.news_cleanup import cleanup_old_news

# Inicializar FastAPI
app = FastAPI(
    title="DAJOMA_News_API",
    docs_url=None,   # Desactiva Swagger UI en /docs
    redoc_url=None,  # Desactiva ReDoc en /redoc
)

# Rutas de noticias
app.include_router(news.router, prefix="/api", tags=["news"])

# Templates y estáticos
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


# ----------------------------
# 🔥 Scheduler para limpieza
# ----------------------------
scheduler = BackgroundScheduler()

# Ejecuta cleanup cada 3 días
scheduler.add_job(cleanup_old_news, "interval", days=3)
scheduler.start()


@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown()
