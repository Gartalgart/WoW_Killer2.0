from . import create_race, create_name, create_class
from configuration import database

# Fonction orchestratrice pour créer un personnage complet
def character_creation(user_id):
    try:
        # On va stocker toutes les données du personnage dans cette liste temporaire
        player_character = []
        
        # 1. On demande le nom
        name = create_name.character_name()
        if name is None: return user_id
        player_character.append(name)
        
        # 2. On demande la race
        race = create_race.create_race()
        if race is None: return user_id
        player_character.append(race)
        
        # 3. On demande la classe
        char_class = create_class.create_class()
        if char_class is None: return user_id
        player_character.append(char_class)
        
        # On ajoute l'ID de l'utilisateur à la fin pour préparer l'insertion SQL
        player_character.append(user_id)

        # On récupère le nom de la race et classe depuis la BDD pour l'affichage récapitulatif
        user_race_data = database.database_connexion(False, "SELECT RACE_NAME FROM race WHERE ID_RACE = %s", (player_character[1],))
        user_class_data = database.database_connexion(False, "SELECT CLASS_NAME FROM class WHERE ID_CLASS = %s", (player_character[2],))
        
        user_race = user_race_data[0][0] if user_race_data else "Inconnu"
        user_class = user_class_data[0][0] if user_class_data else "Inconnu"
        
        # Récapitulatif avant confirmation finale
        print(f"""
==============================
   Récapitulatif du héros
==============================
Nom: {player_character[0]}
Race: {user_race}
Classe: {user_class}""")
        
        answer = str(input("Voulez-vous enregistrer ce personnage ? (Y/N) : "))

        if answer.lower() == "y":
            # Si oui, on exécute l'insertion SQL
            sql = """INSERT INTO hero (CHARACTER_NAME, ID_RACE, ID_CLASS, USER_ID) VALUES (
                %s,
                %s,
                %s,
                %s)"""
            database.database_execute(sql, (player_character[0], player_character[1], player_character[2], player_character[3]))
            print("Votre aventurier a bien été créé !")
        else:
            print("Création annulée.")
            
        return user_id
    except KeyboardInterrupt:
        print("\nProcessus de création de héros annulé.")
        return user_id
    except Exception as e:
        print(f"Une erreur est survenue lors de la création du héros : {e}")
        return user_id

