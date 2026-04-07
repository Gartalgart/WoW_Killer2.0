import configuration.database as conf
import bcrypt

# Fonction gérant la connexion des utilisateurs
def login():
    try:
        attempts = 3
        while attempts > 0:
            username = input("Indiquez votre nom de compte : ")
            password = input("Indiquez votre mot de passe : ").encode("utf-8")

            # On utilise BINARY en SQL pour que la comparaison respecte la casse (minuscules/majuscules)
            result = conf.database_connexion(False, "SELECT ID, password FROM user_account WHERE BINARY username = %s", (username,))

            # On vérifie si l'utilisateur existe et si le mot de passe hashé correspond
            # result[0][1] contient le mot de passe hashé récupéré en base
            if not result or len(result) == 0 or not bcrypt.checkpw(password, result[0][1].encode("utf-8")):
                print(f"Informations incorrectes. {attempts-1} essai(s) restant(s).")
                attempts -= 1
                continue

            print("Connexion réussie !")
            # On retourne l'ID de l'utilisateur (premier élément du premier tuple)
            return result[0][0]

        # En cas d'échec total des essais
        return 0
    except Exception as e:
        print(f"Une erreur lors de la connexion : {e}")
        return 0

# Fonction pour créer un nouveau compte utilisateur
def account_creation():
    while True:
        try:
            username = str(input("Choisissez votre nom d'utilisateur : "))

            # On vérifie si le nom existe déjà (on force la comparaison en minuscules pour éviter les doublons)
            if username.lower() == set_username(username).lower():
                print("Ce pseudonyme est déjà pris. Veuillez en choisir un autre.")
                continue
            
            # Si le pseudo est libre, on passe à la création du mot de passe
            set_password(username)
            return 0

        except KeyboardInterrupt:
            print("\nCréation de compte annulée.")
            return 0
        except Exception as e:
            print(f"Une erreur est survenue : {e}")
            return 0

# Vérifie si le pseudonyme existe déjà dans la base
def set_username(username):
    try:
        # On compare en mettant tout en minuscules (LOWER) pour être sûr de trouver les doublons
        result = conf.database_connexion(False, "SELECT username FROM user_account WHERE LOWER(username) = LOWER(%s)", (username,))
        if not result:
            # Pseudo disponible
            return ""
        else:
            # Pseudo déjà pris
            return result[0][0]
    except Exception as e:
        print(f"Erreur lors de la vérification du pseudonyme : {e}")
        return username 

# Enregistre le mot de passe de manière sécurisée
def set_password(username):
    try:
        pw = input("Indiquez votre mot de passe : ").encode('utf-8')
        # On hash le mot de passe avec bcrypt avant de l'envoyer en base de données
        hashed_pw = bcrypt.hashpw(pw, bcrypt.gensalt()).decode('utf-8')

        conf.database_execute("INSERT INTO user_account (username, password) VALUES (%s, %s)", (username, hashed_pw))
        print("Compte créé avec succès ! Bienvenue.")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement du compte : {e}")

