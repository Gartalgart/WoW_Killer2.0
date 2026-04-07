

import configuration.user_connexion as connexion
import configuration.character_list as character_list
import character_creation.create_hero as create_hero
import menu.edit_character as edit_character
import menu.account_manager as account_manager

error_message = "Vous devez faire un choix valide.\nAppuyez sur n'importe quelle touche pour continuer"

# Note sur le paramètre user_account :
# J'ai appris qu'on peut rendre un argument optionnel avec une valeur par défaut.
# (Très utile, trouvé sur Stack Overflow !)
# https://stackoverflow.com/questions/11328771/optional-arguments-in-python-functions-and-classes

# Correction : j'ai enlevé l'astérisque sur user_account car cela créait un tuple,
# alors qu'on a juste besoin de l'ID en tant qu'entier simple.

def is_user_connected(is_connected: bool, user_account=0):

    # Note sur l'import circulaire : 
    # J'ai évité d'importer 'main' ici pour ne pas bloquer le programme.
    # On gère maintenant le retour de l'ID vers la boucle while principale.

    if not is_connected:
        print("""
Connectez-vous ou créez votre compte pour continuer.
1. Connexion à un compte
2. Création de compte
3. Quitter le jeu
            """)

        try:
            user_choice = int(input("Indiquez votre choix : "))
            match user_choice:
                case 1:
                    return connexion.login()
                case 2:
                    connexion.account_creation()
                    return 0
                case 3:
                    print("\nFermeture du jeu.")
                    exit()
                case _:
                    input(error_message)
                    return 0

        except ValueError:
            input(error_message)
            return 0
        except KeyboardInterrupt:
            print("\nAction annulée")
            return 0
        except Exception as e:
            print(f"Erreur inattendue : {e}")
            return 0

    print("""
Vous êtes connecté, liste des actions possibles:
1. Voir ses personnages
2. Créer un personage
3. Gérer les personnages
4. Gérer son compte
5. Se déconnecter\n""")

    try:
        _user_choice = int(input("Indiquez votre choix : "))

        match _user_choice:
            # Voir perso
            case 1:
                _result = character_list.character_list_all(user_account)
                print("")
                input("Appuyez sur n'importe quelle touche pour revenir au menu principal")
                return _result

            # Créer perso
            case 2:
                return create_hero.character_creation(user_account)

            # Gérer personnages
            case 3:
                return edit_character.edit_character(user_account)

            # Gestion du compte
            case 4:
                return account_manager.manager_menu(user_account)

            # Déconnexion de l'utilisateur
            case 5:
                # je retourne la def avec comme paramètre is_connected à False car il n'est plus connecté et mets son ID à 0
                input("Vous avez été déconnecté. Appuyez sur n'importe quelle touche pour continuer")
                return 0

            # Si le choix est incorrect (hors de la liste 1-5)
            case _:
                input(error_message)
                return user_account #On retourne user_account et pas 0 car ici on est censé avoir l'id de l'utilisateur
        return user_account

    except ValueError:
        input(error_message)
        return user_account # Pareil que ligne 104
    except KeyboardInterrupt:
        print("\nAction annulée")
        return user_account
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return user_account

