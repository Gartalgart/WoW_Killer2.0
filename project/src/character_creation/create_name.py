
# Fonction pour demander et valider le nom du héros
def character_name():
    try:
        # On va boucler tant que le nom est vide
        while True:
            # .strip() sert à nettoyer les espaces au début/fin
            name = str(input("Indiquez le nom de votre héros : ")).strip()
            if name:
                # Si le nom n'est pas vide (après avoir enlevé les espaces)
                return name
            print("Le nom du personnage ne peut pas être vide. Recommencez !")
    except Exception as e:
        # En cas d'annulation clavier (Ctrl+C) ou autre bug
        print("\nAction annulée ou erreur inattendue.")
        return None