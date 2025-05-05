# config.py – ptit module de config centralisée
import os
from dotenv import load_dotenv

load_dotenv()  # charge .env, si présent

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-key-change‑me")
    # ---------- MySQL ----------
    MYSQL_HOST     = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_USER     = os.getenv("MYSQL_USER", "lm-code")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "lm-code")
    MYSQL_DB       = os.getenv("MYSQL_DB", "bibliotheque")
    MYSQL_CURSORCLASS = "DictCursor"  # retourne des dicts, bcp + pratique
