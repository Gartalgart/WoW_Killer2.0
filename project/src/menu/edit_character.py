import configuration.character_list as character_list
import configuration.database as database


def edit_character(user_account):
    while True:
    #character_list.character_list_all(user_account)
        _query = """
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
        """

        # On récupère la liste des héros depuis la base de données
        result = database.database_connexion(False, _query, (user_account,))

        print("Choisissez le héro que vous souhaitez modifier:")
        for i, character in enumerate(result):
            # print(f"{i+1} {character}")
            print(f"{i + 1}: Nom: {character[1]} | Race: {character[2]} | Classe: {character[3]}")


        choice = input("Indiquez le numéro du personnage ou écrivez 'Retour' pour revenir en arrière: ")

        if choice.lower() == "retour":
            return user_account

        # Vérification que le choix est bien un nombre et qu'il est présent dans la liste
        if not choice.isdigit():
            print("Veuillez indiquer un numéro valide.")
            continue

        choice = int(choice)

        if 1 <= choice <= len(result):
            hero = result[choice-1]

            _confirmation = input(f"Héro choisis: {hero[1]} | Validez-vous votre choix ? (Y/N) ")

            if _confirmation.lower() == "n":
                continue
            elif _confirmation.lower() == "y":
                match_character(user_account, hero)
        else:
            print("Numéro invalide.")




def match_character(user_account, hero):
    while True:
        print("""
Options disponibles:
1. Modifier le nom du personnage
'Retour' -> Revenir au menu précédent""")

        result = input("Indiquez votre choix : ")

        if result == "1":
            new_name = input("Indiquez le nouveau nom de votre personnage: ")

            if new_name == hero[1]:
                print("Vous ne pouvez pas définir le même nom de personnage.")
                continue

            if len(new_name) >= 50:
                print("Vous ne pouvez pas avoir un nom de plus de 50 caractères")
                continue

            _confirmation = input(f"Nouveau nom du personnage '{hero[1]}' > {new_name} | Validez-vous ce choix ? (Y/N) ")

            if _confirmation.lower() == "n":
                continue

            elif _confirmation.lower() == "y":
                # MAJ du héro via le nouveau nom new name OU le user id de l'utilisateur et l'ID Bdd du héro"
                # Mise à jour du nom du héros en base de données
                query = "UPDATE hero SET CHARACTER_NAME = %s WHERE USER_ID = %s AND ID = %s"
                database.database_execute(query, (new_name, user_account, hero[0]))

                print(f"Nom de personnage modifié en: {new_name}")
                input("Appuyez sur n'importe quelle touche pour continuer..")
                return user_account

        if result.lower() == "retour":
            return