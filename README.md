# CEBD JO 2025

Projet pédagogique de L3 pour manipuler une base SQLite à partir d'un fichier Excel des Jeux Olympiques.

## Aperçu

- Crée une base SQLite locale (`data/jo.db`).
- Importe des données depuis `data/LesJO.xlsx` (onglets `LesSportifsEQ` et `LesEpreuves`).
- Propose quelques opérations via un menu en ligne de commande.

## Prérequis

- Python 3.10+ (recommandé)
- pip (gestionnaire de paquets)
- sqlite3 est inclus avec Python 3 (aucune installation séparée nécessaire)

Dépendances Python principales:
- pandas — manipulation/analyse de données (https://pandas.pydata.org/docs/getting_started/install.html)
- openpyxl — lecture de fichiers Excel `.xlsx` (https://openpyxl.readthedocs.io/en/stable/)

Compatibilité: Linux, macOS et Windows.

## Installation

1) Cloner le dépôt

```bash
git clone https://github.com/Laghrouy/CEBD-JO-2025.git
cd CEBD-JO-2025/cebd-jo-2025-master
```

2) Installer Python 3 et les bibliothèques

- Windows
  - Assurez-vous que le dossier d'installation de Python est ajouté à la variable d'environnement `PATH` pour pouvoir utiliser `python`/`pip` sans leur chemin complet.
  - Installation des bibliothèques:
    ```bash
    pip install pandas openpyxl
    ```

- Linux (Debian/Ubuntu)
  - Installer Python 3 (si nécessaire):
    ```bash
    sudo apt-get update
    sudo apt-get install -y python3
    ```
  - Option A (recommandée): utiliser pip avec le fichier `requirements.txt`:
    ```bash
    python3 -m pip install --user -r requirements.txt
    ```
  - Option B (via paquets système):
    ```bash
    sudo apt-get install -y python3-pandas
    sudo apt-get install -y python3-openpyxl
    ```

- macOS
  - Avec Homebrew (optionnel):
    ```bash
    brew install python
    ```
  - Puis installer les bibliothèques:
    ```bash
    pip3 install pandas openpyxl
    ```

Remarque: L'usage d'un environnement virtuel est conseillé pour isoler les dépendances:
```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Utilisation

Lancer le programme:

```bash
python main.py
```

Menu proposé:
- 1 — Créer la base de données (exécute `data/v0_createDB.sql`)
- 2 — Insérer les données du fichier Excel (lit `data/LesJO.xlsx` et insère dans la base)
- 3 — Supprimer la base de données (exécute `data/v0_deleteDB.sql`)
- 4 — Lister les épreuves de ski alpin (requête simple d’exemple)
- q — Quitter

Par défaut, la base est créée dans `data/jo.db`.

## Structure du projet

```
cebd-jo-2025-master/
  main.py                       # Point d'entrée (menu CLI)
  actions/
    database_functions.py       # Créer / insérer / supprimer BD
    database_queries.py         # Requêtes d'exemple (liste d'épreuves)
  utils/
    db.py                       # Exécution de scripts SQL
    excel_extractor.py          # Lecture Excel et insertions
  data/
    LesJO.xlsx                  # Données source (Excel)
    v0_createDB.sql             # Script de création du schéma
    v0_deleteDB.sql             # Script de suppression
```

## Notes techniques

- La base est gérée via `sqlite3` (standard library Python).
- La lecture Excel utilise `pandas.read_excel(..., dtype=str)`. Le moteur `openpyxl` est requis pour `.xlsx`.
- Les insertions sont faites par génération de requêtes SQL formatées. Pour un code de prod, privilégier des requêtes paramétrées (placeholders) pour éviter toute injection.

## Outils conseillés

- IDE Python: PyCharm (Community gratuit) — https://www.jetbrains.com/pycharm/
- IDE Base de données (tests de requêtes/vues): DB Browser for SQLite — https://sqlitebrowser.org/

## Dépannage

- Erreur « ImportError: Missing optional dependency 'openpyxl' »:
  - Installer le moteur Excel: `pip install openpyxl` (inclus dans `requirements.txt`).

- Erreur « sqlite3.OperationalError: database is locked »:
  - Fermer les processus qui utilisent `data/jo.db`.
  - Relancer le script après quelques secondes.

- Encodage/accents:
  - Vérifier que votre terminal est en UTF-8.

## Licence

## Auteurs

- @Laghrouy @TomGontard
