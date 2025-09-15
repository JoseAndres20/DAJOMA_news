from fastapi import FastAPI
from app.routers import news

app = FastAPI(title="Scraping API")

# incluir rutas
app.include_router(news.router, prefix="/api", tags=["news"])

@app.get("/")
def root():
    return {"msg": "Scraping API running 🚀"}
