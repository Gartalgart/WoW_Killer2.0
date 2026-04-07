# WoW Killer - RPG Management System

Bienvenue dans le projet **WoW Killer**, un système de gestion de personnages et de comptes pour un RPG en mode console. Ce projet est développé en Python avec une base de données MySQL/MariaDB pour stocker les aventuriers et leurs créateurs.

## Fonctionnalités

Le projet permet actuellement de :
- **Gestion de compte** : Inscription avec hachage de mot de passe sécurisé (bcrypt) et connexion.
- **Gestionnaire de compte** : Modifier son pseudonyme (avec délai) et son mot de passe.
- **Création de heros** : Un système complet de création (Nom, Race, Classe).
- **Gestion de personnages** : Lister, consulter et bientôt modifier ses héros.
- **Interface Console** : Une navigation simple via des menus interactifs.

## Stack Technique

- **Langage** : [Python 3.10+](https://www.python.org/)
- **Base de données** : [MySQL](https://www.mysql.com/) / [MariaDB](https://mariadb.org/)
- **Sécurité** : `bcrypt` pour le hachage des mots de passe.
- **Configuration** : `python-dotenv` pour la gestion des variables d'environnement.

## Prérequis

Avant de lancer le projet, assurez-vous d'avoir installé :
- Python 3.10 ou supérieur.
- Un serveur MySQL/MariaDB (ex: WAMP, XAMPP, Docker).
- Le gestionnaire de paquets `pip`.

## Installation & Configuration

### 1. Cloner le projet
```bash
git clone <url-du-depot>
cd WoW_killer
```

### 2. Installer les dépendances
```bash
pip install -r project/src/requirements.txt
```

### 3. Configurer la base de données
1. Créez une base de données nommée `bdd` (ou le nom de votre choix).
2. Importez le fichier SQL situé dans `SQL/BDD.sql` pour créer les tables et les données initiales.

### 4. Configurer l'environnement
Créez un fichier `.env` à la racine du projet avec les informations suivantes :
```env
DB_HOST=localhost
DB_PORT=3306
DB_DATABASE=bdd
DB_USER=votre_utilisateur
DB_PASSWORD=votre_mot_de_passe
```

## Lancement

Pour démarrer l'application, lancez le script principal depuis la racine :

```bash
python project/src/main.py
```

## Structure du projet

```text
WoW_killer/
├── SQL/
│   └── BDD.sql             # Schéma et données de la base de données
├── project/
│   └── src/
│       ├── main.py         # Point d'entrée de l'application
│       ├── configuration/  # Connexion DB et logique utilisateur
│       ├── menu/           # Menus interactifs (principal, compte, etc.)
│       └── character_creation/ # Logique de création de héros
├── .env                    # Configuration confidentielle (non versionné)
├── .gitignore              # Fichiers à ignorer par Git
└── README.md               # Ce fichier !
```

