# 📰 DAJOMA News API

API de **noticias tecnológicas** construida con **FastAPI + Supabase**.  
Scrapea fuentes populares de tecnología, guarda el texto de los artículos en Supabase y expone endpoints REST para consumirlos en un frontend (Next.js/React o cualquier cliente).

---

## 🚀 Tecnologías usadas
- [FastAPI](https://fastapi.tiangolo.com/) → Framework backend.
- [Supabase](https://supabase.com/) → Base de datos (PostgreSQL gestionada).
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) → Web scraping.
- [Requests](https://docs.python-requests.org/) → Cliente HTTP.
- [Uvicorn](https://www.uvicorn.org/) → Servidor ASGI.
- [python-dotenv](https://pypi.org/project/python-dotenv/) → Variables de entorno.


---
```
## 📂 Estructura del proyecto
app/
├── core/ # Configuración y carga de .env
├── db/ # Cliente de Supabase
├── routers/ # Endpoints de FastAPI
├── services/ # Scraper, IA, fuentes y utilidades
└── main.py # Entrada principal de la API
```
---

## ⚙️ Configuración

### Clonar el repo

git clone https://github.com/tuusuario/DAJOMA_news.git
cd DAJOMA_news


## Crear entorno virtual

python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

##  Instalar dependencias
pip install -r requirements.txt


## Configurar .env

SUPABASE_URL=https://xxxx.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1...
OPENAI_API_KEY=sk-xxxxxxxxxxxxx   # opcional

## ▶️ Ejecutar en local

uvicorn app.main:app --reload --port 8000

API disponible en:

🌐 http://127.0.0.1:8000/
 → raíz

📑 http://127.0.0.1:8000/api/news
 → obtener noticias

⚡ http://127.0.0.1:8000/api/scrape?limit=10
 → ejecutar scraping

📖 http://127.0.0.1:8000/docs
 → Swagger UI

📘 http://127.0.0.1:8000/redoc
 → ReDoc
