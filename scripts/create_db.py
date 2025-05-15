from sqlalchemy import create_engine, text
from loguru import logger
import os

def creer_base():
    logger.info("Création de la base SQLite...")
    os.makedirs("db", exist_ok=True)
    engine = create_engine("sqlite:///db/rh.db", echo=False)
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS employes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                sexe TEXT CHECK(sexe IN ('H', 'F')),
                age INTEGER,
                departement TEXT,
                salaire REAL NOT NULL
            );
        """))
        conn.commit()
    logger.info("Base SQLite créée (ou existante).")