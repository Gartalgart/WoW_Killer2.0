import os
from dotenv import load_dotenv
from pathlib import Path
import mysql.connector

# On charge les variables d'environnement (le fichier .env)
load_dotenv()

# Fonction pour initialiser la connexion avec les infos globales
def connexion_info():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_DATABASE'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )

# Fonction pour récupérer des données (SELECT)
def database_connexion(is_dictionary, sql, params=None):
    connexion = None
    cursor = None
    result = []
    try:
        # On utilise le context manager (with) pour fermer la connexion après usage
        with connexion_info() as connexion:
            with connexion.cursor(dictionary=is_dictionary) as cursor:
                cursor.execute(sql, params)
                result = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Erreur lors de la récupération : {err.msg}")

    return result

# Fonction pour modifier la base de données (INSERT, UPDATE, DELETE)
def database_execute(sql, params=None):
    connexion = None
    cursor = None
    try:
        with connexion_info() as connexion:
            with connexion.cursor() as cursor:
                cursor.execute(sql, params)
                # IMPORTANTE : il faut commit pour enregistrer les modifs en base
                connexion.commit()
    except mysql.connector.Error as err:
        print(f"Erreur lors de l'exécution de la requête : {err.msg}")
        if connexion:
            # En cas de problème, on annule tout
            connexion.rollback()