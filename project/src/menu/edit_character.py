import configuration.character_list as character_list
import configuration.database as database

def edit_character(user_account):
    try:
        character_list.character_list_all(user_account)
        _choice = input("Indiquez le numéro du personnage ou écrivez 'Retour' pour revenir en arrière: ")
        database.database_connexion(False, """
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
    except Exception as e:
        print(f"Une erreur est survenue dans l'édition du personnage : {e}")