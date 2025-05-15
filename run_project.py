from scripts.create_db import creer_base
from scripts.charger_donnees import charger_csv_vers_db
from scripts.analyser_donnees import lancer_analyses

from loguru import logger

if __name__ == "__main__":
    logger.info("=== Début du pipeline RH ===")

    creer_base()
    charger_csv_vers_db()
    lancer_analyses()

    logger.info("=== Fin du pipeline RH ===")