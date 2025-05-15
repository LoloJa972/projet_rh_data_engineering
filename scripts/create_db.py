from sqlalchemy import create_engine, text
from loguru import logger

DB_PATH = "sqlite:///db/rh.db"

def creer_base():
    engine = create_engine(DB_PATH)
    with open("db/schema.sql", "r") as f:
        schema = f.read()

    with engine.connect() as conn:
        conn.execute(text(schema))
        logger.info("Base de données et table 'employes' créées avec succès.")

if __name__ == "__main__":
    creer_base()