import pandas as pd
from sqlalchemy import create_engine, text
from loguru import logger

DB_PATH = "sqlite:///rh.db"

def analyse_repartition_sexe(engine):
    query = "SELECT sexe, COUNT(*) AS nombre FROM employes GROUP BY sexe;"
    df = pd.read_sql(query, engine)
    logger.info("Répartition hommes/femmes :\n" + df.to_string(index=False))
    return df

def analyse_salaire_moyen_par_sexe(engine):
    query = "SELECT sexe, ROUND(AVG(salaire), 2) AS salaire_moyen FROM employes GROUP BY sexe;"
    df = pd.read_sql(query, engine)
    logger.info("Salaire moyen par sexe :\n" + df.to_string(index=False))
    return df

def analyse_age_moyen(engine):
    query = "SELECT ROUND(AVG(age), 2) AS age_moyen FROM employes;"
    df = pd.read_sql(query, engine)
    logger.info("Âge moyen des employés :\n" + df.to_string(index=False))
    return df

def main():
    logger.info("Début de l'analyse des données RH")
    engine = create_engine(DB_PATH)

    analyse_repartition_sexe(engine)
    analyse_salaire_moyen_par_sexe(engine)
    analyse_age_moyen(engine)

    logger.info("Fin de l'analyse")

if __name__ == "__main__":
    main()