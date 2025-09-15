import os
from dotenv import load_dotenv

load_dotenv()
#Configuracion de las credenciales de supabase
class Settings:
    
    SUPABASE_URL: str = os.getenv("SUPABASE_URL")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")

settings = Settings()
