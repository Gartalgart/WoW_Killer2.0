from configuration import database

# Fonction pour choisir la race de son personnage
def create_race():

    user_race = []

    print("""
==============================
    Choisissez votre race
==============================
               """)
    
    print("Voici la liste des races disponibles:")
    try:
        # On récupère toutes les races directement en base de données
        result = database.database_connexion(True, "SELECT * FROM race")
        if not result:
            print("Aucune race trouvée ou erreur de base de données.")
            return None
            
        # Affichage dynamique des races récupérées
        for row in result:
            print(f"{row['ID_RACE']}. {row['RACE_NAME']}")
            
        # On crée une liste des ID valides pour la vérification de la saisie
        rows = [row["ID_RACE"] for row in result]
        # On crée un dictionnaire pour récupérer plus tard le nom de la race choisie
        races = {row["ID_RACE"]: row["RACE_NAME"] for row in result}

        # On boucle jusqu'à ce que l'utilisateur fasse un choix valide
        while True:
            try:
                _choice = int(input("Choisissez votre race (Indiquez le numéro) : "))

                if _choice in rows:
                    user_race.append(_choice)
                    break
                else:
                    print("Ce numéro ne fait pas partie de la liste.")

            except ValueError:
                print("Veuillez entrer un nombre valide.")
            except KeyboardInterrupt:
                # Permet d'annuler et de revenir en arrière avec Ctrl+C
                print("\nAnnulation du choix de la race.")
                return None
            
        print("Race choisie: ", races[user_race[0]])
        return user_race[0]
    except Exception as e:
        print(f"Une erreur inattendue est survenue: {e}")
        return None