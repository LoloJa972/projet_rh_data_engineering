from loguru import logger
import sqlite3
import pandas as pd

def lancer_analyses():
    logger.info("Lancement des analyses des données RH...")

    conn = sqlite3.connect("db/rh.db")
    df = pd.read_sql_query("SELECT * FROM employes;", conn)

    logger.info(f"Nombre d'employés : {len(df)}")

    repartition_sexe = df['sexe'].value_counts()
    logger.info(f"Répartition hommes/femmes :\n{repartition_sexe}")

    salaire_moyen = df['salaire'].mean()
    logger.info(f"Salaire moyen : {salaire_moyen:.2f} €")

    age_moyen = df['age'].mean()
    logger.info(f"Âge moyen : {age_moyen:.1f} ans")

    repartition_departement = df['departement'].value_counts()
    logger.info(f"Répartition par département :\n{repartition_departement}")

    conn.close()