import pandas as pd
from sqlalchemy import create_engine
from loguru import logger

def charger_csv_vers_db():
    logger.info("Chargement des données depuis CSV vers SQLite...")
    engine = create_engine("sqlite:///db/rh.db", echo=False)

    # Chargement fichier CSV
    df = pd.read_csv("data/employes.csv")

    # Nettoyage simple (exemple)
    df['sexe'] = df['sexe'].str.upper().str.strip()
    df['salaire'] = pd.to_numeric(df['salaire'], errors='coerce')
    df.dropna(subset=['nom', 'sexe', 'salaire'], inplace=True)

    # Injection dans la table
    df.to_sql("employes", con=engine, if_exists='replace', index=False)

    logger.info(f"{len(df)} employés chargés dans la base.")