from .base import *

DEBUG = True
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-dev-key-change-me")
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Banco de dados para desenvolvimento local (SQLite ou Postgres via Docker)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}