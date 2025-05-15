import pandas as pd
from sqlalchemy import create_engine, text
from loguru import logger

DB_PATH = "sqlite:///rh.db"
CSV_FILE = "employes.csv"

def creer_table(engine):
    schema = """
    CREATE TABLE IF NOT EXISTS employes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        sexe TEXT CHECK(sexe IN ('H', 'F')) NOT NULL,
        age INTEGER CHECK(age BETWEEN 18 AND 70) NOT NULL,
        departement TEXT NOT NULL,
        salaire REAL CHECK(salaire >= 0) NOT NULL
    );
    """
    with engine.connect() as conn:
        conn.execute(text(schema))
    logger.info("Table 'employes' créée ou déjà existante.")

def charger_csv_vers_db(engine, csv_file):
    try:
        df = pd.read_csv(csv_file)
        df.to_sql('employes', con=engine, if_exists='append', index=False)
        logger.info(f"{len(df)} lignes importées depuis {csv_file} vers la base.")
    except Exception as e:
        logger.error(f"Erreur lors de l'import CSV : {e}")

def main():
    logger.info("Début du chargement des données")
    engine = create_engine(DB_PATH)
    creer_table(engine)
    charger_csv_vers_db(engine, CSV_FILE)
    logger.info("Fin du chargement des données")

if __name__ == "__main__":
    main()