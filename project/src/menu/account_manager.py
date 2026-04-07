
import bcrypt
from configuration import database
from datetime import datetime
from getpass import getpass

# Menu pour gérer les options du compte utilisateur
def manager_menu(user_account):
    while True:
        print("""
========================
  Gestion du compte
========================

1. Modifier le nom de compte
2. Modifier le mot de passe.
'retour'. Revenir au menu principal""")

        try:
            # On passe tout en minuscules pour faciliter la comparaison (notamment "retour")
            _choice = input("Indiquez votre choix: ").lower()

            match _choice:
                case "1":
                    change_username(user_account)

                case "2":
                    user_account = change_password(user_account)

                    # Si change_password renvoie 0, c'est que l'utilisateur a raté ses essais
                    # On le déconnecte donc pour des raisons de sécurité
                    if user_account == 0:
                        return 0

                case "retour":
                    # On renvoie l'ID de l'utilisateur pour rester connecté au menu principal
                    return user_account

                case _:
                    print("Indiquez un choix valide")
            
        except ValueError:
            print("Erreur : Valeur inattendue.")
        except KeyboardInterrupt:
            # Retour au menu précédent en cas d'annulation clavier
            print("\nAction annulée")
            return user_account
        except Exception as e:
            print(f"Erreur inattendue : {e}")
            return user_account


# Fonction pour changer son pseudonyme en base de données
def change_username(user_account):
    try:
        # On récupère le pseudo actuel et la date du dernier changement
        db_result = database.database_connexion(False, """
        SELECT username, last_time_username_modified 
        FROM user_account 
        WHERE ID = %s""", (user_account,))
    
        if not db_result:
            print("Erreur de récupération du compte.")
            return

        can_modify = False
        actual_account = db_result[0][0]
        last_time = db_result[0][1]

        # On calcule si 3 jours se sont écoulés depuis la dernière modif
        if last_time is None:
            # Jamais modifié, donc c'est bon
            can_modify = True
        else:
            # Calcul de la différence de jours
            days_since = (datetime.now().date() - last_time).days

        # Autorisation si jamais modifié ou si le délai de 3 jours est passé
        if can_modify or days_since >= 3:
            print(f"Votre nom de compte actuel: {actual_account}")
            _check = input("Souhaitez-vous le modifier ? (Y/N) ")

            if _check.lower() == "y":
                _new_username = input("Indiquez votre nouveau nom de compte: ")

                if _new_username == actual_account:
                    print("Vous ne pouvez pas redéfinir le même pseudo")
                else:
                    # On met à jour le pseudo ET la date de modification maintenant
                    database.database_execute("""
                        UPDATE user_account
                        SET last_time_username_modified = NOW(), username = %s
                        WHERE ID = %s
                        """, (_new_username, user_account))
                    print(f"Nom de compte modifié en: {_new_username}")
                    return

            elif _check.lower() == "n":
                return
            else:
                print("Indiquez une réponse valide")

        else:
            # Information sur le temps d'attente restant
            print(f"""Vous avez modifié votre nom de compte le {last_time}.
Vous devez attendre {3-days_since} jours pour modifier à nouveau votre nom de compte.""")
            input("Appuyez sur n'importe quelle touche pour continuer.")

        return
    except Exception as e:
        print(f"Une erreur est survenue lors de la modification du nom d'utilisateur : {e}")
        return


# Fonction de changement de mot de passe avec vérification de l'ancien
def change_password(user_account):
    try:
        attempts = 3
        while attempts > 0:
            actual_password = getpass(prompt="Indiquez votre mot de passe actuel : ").encode("utf-8")

            # On vérifie d'abord que le mot de passe actuel est le bon
            result = database.database_connexion(False, "SELECT password FROM user_account WHERE ID = %s", (user_account,))
            if not result or len(result) == 0 or not bcrypt.checkpw(actual_password, result[0][0].encode("utf-8")):
                print(f"Mot de passe est invalide {attempts - 1} essai(s) restant")
                attempts -= 1
                continue

            # Saisie et confirmation du nouveau mot de passe
            _new_password = getpass(prompt="Indiquez votre nouveau mot de passe : ").encode("utf-8")
            validate_password = getpass(prompt="Confirmez le mot de passe : ").encode("utf-8")

            if validate_password == _new_password:
                # Hashage sécurisé du nouveau mot de passe avant insertion
                hashed_pw = bcrypt.hashpw(validate_password, bcrypt.gensalt()).decode('utf-8')
                database.database_execute(
                    "UPDATE user_account SET password = %s WHERE ID = %s", (hashed_pw, user_account))
                print("Le mot de passe a bien été modifié.")
                return user_account
            else:
                print("Les mot de passe ne correspondent pas.")

        # Si tous les essais sont consommés
        print("Modification du mot de passe échouée, vous avez été déconnecté du compte.")
        return 0
    except Exception as e:
        print(f"Une erreur est survenue lors de la modification du mot de passe : {e}")
        return 0
