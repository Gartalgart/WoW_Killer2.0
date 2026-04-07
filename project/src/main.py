import menu.main_menu as menu

# Fonction principale qui va gérer la boucle infinie du jeu
def main_menu(user_account=0):

    while True:
        print("""
============================
Bienvenue sur Wow Killer
============================""")

        try:
            # On vérifie si l'utilisateur est connecté (id > 0) ou pas
            if user_account == 0:
                # On charge le menu de connexion/création
                user_account = menu.is_user_connected(False, 0)
            else:
                # On charge le menu des actions disponibles pour l'utilisateur
                user_account = menu.is_user_connected(True, user_account)
        except KeyboardInterrupt:
            # Si on fait Ctrl+C, on ferme proprement
            print("\nFermeture du jeu.")
            break
        except Exception as e:
            # Affichage de l'erreur si le menu crash
            print(f"Erreur critique dans le menu principal : {e}")
            break

# Lancement automatique du script
if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        pass

