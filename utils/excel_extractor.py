import sqlite3, pandas
from sqlite3 import IntegrityError

# Fonction permettant de lire le fichier Excel des JO et d'insérer les données dans la base
def read_excel_file_V0(data:sqlite3.Connection, file):
    # Lecture de l'onglet du fichier excel LesSportifsEQ, en interprétant toutes les colonnes comme des strings
    # pour construire uniformement la requête
    df_sportifs = pandas.read_excel(file, sheet_name='LesSportifsEQ', dtype=str)
    df_sportifs = df_sportifs.where(pandas.notnull(df_sportifs), 'null')

    cursor = data.cursor()
    for ix, row in df_sportifs.iterrows():
        try:
            # Utiliser des paramètres pour éviter les injections et gérer NULL
            vals = [
                row['numSp'], row['nomSp'], row['prenomSp'], row['pays'],
                row['categorieSp'], None if row['dateNaisSp'] == 'null' else row['dateNaisSp'], row['numEq']
            ]
            cursor.execute("INSERT INTO V0_LesSportifsEQ VALUES (?,?,?,?,?,?,?)", vals)
        except IntegrityError as err:
            print(f"Sportif conflit ligne {ix}: {err}")

    # Lecture de l'onglet LesEpreuves du fichier excel, en interprétant toutes les colonnes comme des string
    # pour construire uniformement la requête
    df_epreuves = pandas.read_excel(file, sheet_name='LesEpreuves', dtype=str)
    df_epreuves = df_epreuves.where(pandas.notnull(df_epreuves), 'null')

    cursor = data.cursor()
    for ix, row in df_epreuves.iterrows():
        try:
            vals = [
                row['numEp'], row['nomEp'], row['formeEp'], row['nomDi'], row['categorieEp'],
                row['nbSportifsEp'], None if row['dateEp'] == 'null' else row['dateEp']
            ]
            cursor.execute("INSERT INTO V0_LesEpreuves VALUES (?,?,?,?,?,?,?)", vals)
        except IntegrityError as err:
            print(f"Epreuve conflit ligne {ix}: {err}")

    # Lecture des inscriptions (PK sur numIn)
    df_inscriptions = pandas.read_excel(file, sheet_name='LesInscriptions', dtype=str)
    df_inscriptions = df_inscriptions.where(pandas.notnull(df_inscriptions), 'null')
    for ix, row in df_inscriptions.iterrows():
        try:
            vals = [row['numIn'], row['numEp']]
            cursor.execute("INSERT INTO V0_LesInscriptions VALUES (?,?)", vals)
        except IntegrityError as err:
            print(f"Inscription conflit ligne {ix}: {err}")

    # Lecture des résultats
    df_resultats = pandas.read_excel(file, sheet_name='LesResultats', dtype=str)
    df_resultats = df_resultats.where(pandas.notnull(df_resultats), 'null')
    for ix, row in df_resultats.iterrows():
        try:
            vals = [
                row['numEp'], row['gold'], row['silver'], row['bronze']
            ]
            cursor.execute("INSERT INTO V0_LesResultats VALUES (?,?,?,?)", vals)
        except IntegrityError as err:
            print(f"Resultat conflit ligne {ix}: {err}")
