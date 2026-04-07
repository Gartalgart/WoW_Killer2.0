from . import database

# Fonction pour afficher tous les héros d'un utilisateur
def character_list_all(user_account):
    try:
        # On commence par compter combien de héros possède l'utilisateur
        result = database.database_connexion(False, """
                SELECT 
                COUNT(*)
                FROM hero WHERE USER_ID = %s
                """, (user_account,))
        
        # En cas d'erreur de connexion à la base
        if not result:
            print("Erreur lors de la récupération de vos héros.")
            return user_account
            
        # On récupère le nombre via le premier élément du premier tuple renvoyé
        nb_hero = result[0][0]

        if nb_hero == 0:
            # Message informatif si la liste est vide
            print("Vous n'avez pas de héros, tapez 'créer' pour en créer un.")
        else:
            # S'il y a des héros, on lance une requête plus complexe avec des JOIN
            # pour récupérer le nom de la race et de la classe au lieu de simples ID
            sentence = database.database_connexion(True, """
                    SELECT 
                    hero.ID,                             
                    hero.CHARACTER_NAME, 
                    race.RACE_NAME, 
                    class.CLASS_NAME 
                    FROM hero 
                    INNER JOIN race 
                    ON hero.ID_RACE = race.ID_RACE
                    INNER JOIN class 
                    ON hero.ID_CLASS = class.ID_CLASS
                    WHERE USER_ID = %s
                    ORDER BY hero.ID ASC
                """, (user_account,))

            print("")
            print("Liste de vos héros:")
            
            # On boucle sur chaque ligne (dictionnaire) renvoyée par la BDD
            if sentence:
                for i, row in enumerate(sentence):
                    print(
                        f"""Hero n°{i + 1}: {row["CHARACTER_NAME"]} | Race: {row["RACE_NAME"]} | classe: {row["CLASS_NAME"]}""")
            else:
                print("Erreur lors de la récupération des détails des héros.")

        # On retourne l'ID de l'utilisateur pour ne pas le déconnecter
        return user_account
    except Exception as e:
        print(f"Une erreur est survenue lors de l'affichage des héros : {e}")
        return user_account