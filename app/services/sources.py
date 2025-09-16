# news_sources.py
# Fuentes de noticias tecnológicas, IA, programación y ciberseguridad (todas accesibles gratis)

NEWS_SOURCES = [
    # --- IA y Startups ---
    {
        "name": "TechCrunch (AI/Startups)",
        "url": "https://techcrunch.com/category/artificial-intelligence/",
        "selector": "a.post-block__title__link"
    },
    {
        "name": "VentureBeat (AI/Tech)",
        "url": "https://venturebeat.com/category/ai/",
        "selector": "h2 a"
    },
    {
        "name": "IEEE Spectrum (AI/Robotics)",
        "url": "https://spectrum.ieee.org/artificial-intelligence",
        "selector": "h2 a"
    },

    # --- Tecnología general ---
    {
        "name": "The Verge (Tech)",
        "url": "https://www.theverge.com/tech",
        "selector": "h2 a"
    },
    {
        "name": "Ars Technica (Hardware/Science)",
        "url": "https://arstechnica.com/gadgets/",
        "selector": "h2 a"
    },

    # --- Programación y desarrollo ---
    {
        "name": "InfoQ (Software/Programming)",
        "url": "https://www.infoq.com/development/",
        "selector": "h2 a"
    },
    {
    "name": "Hacker News (Y Combinator)",
    "url": "https://news.ycombinator.com/",
    "selector": "span.titleline a"
}
,
    {
        "name": "Reddit /r/programming",
        "url": "https://www.reddit.com/r/programming/",
        "selector": "h3"
    },

    # --- Ciberseguridad ---
    {
        "name": "ZDNet (Cybersecurity)",
        "url": "https://www.zdnet.com/topic/security/",
        "selector": "a.assetHed"
    },
    {
        "name": "Krebs on Security",
        "url": "https://krebsonsecurity.com/",
        "selector": "h2.entry-title a"
    },
    {
        "name": "SecurityWeek",
        "url": "https://www.securityweek.com/",
        "selector": "h2 a"
    }
]
