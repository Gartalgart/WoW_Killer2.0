from configuration import database


def create_class():

    user_class = []

    print("""
==============================
    Choisissez votre classe
==============================

               """)
    
    print("Voici la liste des classes:")
    try:
        result = database.database_connexion(True, "SELECT * FROM class")
        if not result:
            print("Aucune classe trouvée ou erreur de connexion à la base de données.")
            return None
            
        for row in result:
            print(f"{row['ID_CLASS']}. {row['CLASS_NAME']}")
            
        rows = [row["ID_CLASS"] for row in result]
        classes = {row["ID_CLASS"]: row["CLASS_NAME"] for row in result}

        # Choix classe
        while True:
            try:
                _result = int(input("Choisissez votre classe: "))

                if _result in rows:
                    user_class.append(_result)
                    break
                else:
                    print("Choisissez une classe valide.")

            except ValueError:
                print("Veuillez entrer un nombre valide.")
            except KeyboardInterrupt:
                print("\nAnnulation du choix.")
                return None
            
        print("Classe choisie: ", classes[user_class[0]])
        return user_class[0]

    except Exception as e:
        print(f"Une erreur inattendue est survenue: {e}")
        return None
    
