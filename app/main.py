from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from app.routers import news
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI(title="DAJOMA_News_API")

# incluir rutas
app.include_router(news.router, prefix="/api", tags=["news"])
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
@app.get("/", response_class=HTMLResponse)


def root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
        }
    )