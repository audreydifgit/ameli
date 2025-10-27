README — Test Technique

1. Description du projet
Le but du projet est de produire un rapport à partir d’un échantillon de données de santé récupérées depuis l’API d’Ameli.
Ces données concernent des pathologies de cancers localisés en Île-de-France (n = 100).
Le projet combine Python (pour la collecte et la mise en base) et R (pour l’analyse et la génération du rapport).


2. Étapes du projet

    Étape 1 — Récupération des données (Python)
Importation des packages nécessaires (requests, pandas, duckdb).
Connexion à l’API Ameli : https://data.ameli.fr/explore/dataset/effectifs/api/
Définition des paramètres :
- Pathologie : Cancers
- Région : Île-de-France (11) (*)
- Nombre de lignes : 100
Les données sont stockées dans un DataFrame pour vérification.
    
    Étape 2 — Création de la base de données (Python)
Création d’une base DuckDB nommée ameli.duckdb.
Connexion à la base, vérification de son état (vide).
Importation des données récupérées dans une table.
Fermeture de la connexion une fois les données chargées.
    
    Étape 3 — Création du rapport (R)
Chargement des packages nécessaires (DBI, duckdb, dplyr, ggplot2, gtsummary).
Connexion à la base ameli.duckdb en mode lecture seule.
Vérification de la présence de la table et affichage des 5 premières lignes.
Création d’un tableau descriptif affichant les effectifs par :
- Département (dept)
- Tranche d’âge (cla_age_5)
- Niveau prioritaire (niveau_prioritaire)
- Sexe (sexe)
Le tableau est généré à l’aide du package gtsummary.


3. Prérequis

Python:
requests
pandas
duckdb

R:
DBI
duckdb
dplyr
ggplot2
gtsummary

4. Instructions d’exécution

    Partie Python
Ouvrir le fichier ameli.py
Exécuter le script pour :
- Télécharger les données depuis l’API
- Créer la base ameli.duckdb
- Importer les données dans la table

    Partie R
Ouvrir le fichier rapport_ameli.Rmd
Exécuter le document (Knit) pour :
- Se connecter à la base DuckDB
 Analyser les données
- Générer un rapport HTML avec le tableau descriptif


(*) NB : existence du département 999