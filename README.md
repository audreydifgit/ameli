# Analyse des données de santé - Cancers en Île-de-France
Ce projet a pour objectif d'analyser un échantillon de données de la base Ameli au sujet des pathologies de cancers en Ile de France.

## 1. Description du projet
Le but du projet est de produire un rapport à partir d’un échantillon de données de santé récupérées depuis l’API d’Ameli.
Ces données concernent des pathologies de cancers localisés en Île-de-France (n = 100).
Le projet combine :  
- **Python** → pour la collecte, le traitement et le stockage des données.  
- **R (RMarkdown)** → pour l’analyse descriptive et la génération du rapport final.

---

## 2. Étapes du projet

### Étape 1 — Récupération des données *(Python)* 
- Importation des packages nécessaires : `requests`, `pandas`, `duckdb`.  
- Connexion à l’API Ameli : [https://data.ameli.fr/explore/dataset/effectifs/api/](https://data.ameli.fr/explore/dataset/effectifs/api/)  
- Définition des paramètres :
  - Pathologie : **Cancers**
  - Région : **Île-de-France (11)**
  - Nombre de lignes : **100**
- Stockage des données dans un DataFrame pour vérification.  

### Étape 2 — Création de la base de données *(Python)* 
- Création de la base **DuckDB** : `ameli.duckdb`.  
- Connexion à la base et vérification qu’elle est vide.  
- Importation des données depuis le DataFrame.  
- Fermeture propre de la connexion à la base.  

### Étape 3 — Création du rapport *(R)* 
- Chargement des packages nécessaires :  
  `DBI`, `duckdb`, `dplyr`, `ggplot2`, `gtsummary`.  
- Connexion à la base `ameli.duckdb` en lecture seule.  
- Vérification de la table (`head()` sur les premières lignes).  
- Création d’un **tableau descriptif** avec `gtsummary` affichant les effectifs par :  
  - Département (`dept`)  
  - Tranche d’âge (`cla_age_5`)  
  - Niveau prioritaire (`niveau_prioritaire`)  
  - Sexe (`sexe`)  

Le rapport est généré au format **HTML** via RMarkdown.

---

## 3. Prérequis  

### Python  
- `requests`  
- `pandas`  
- `duckdb`  

### R  
- `DBI`  
- `duckdb`  
- `dplyr`  
- `ggplot2`  
- `gtsummary`  

---

## 4. Instructions d’exécution  

### Partie Python  
1. Ouvrir le fichier **`ameli.py`**  
2. Exécuter le script pour :  
   - Télécharger les données depuis l’API  
   - Créer la base `ameli.duckdb`  
   - Importer les données dans la table  

### Partie R  
1. Ouvrir le fichier **`rapport_test_technique.Rmd`**  
2. Exécuter le document (**Knit**) pour :  
   - Se connecter à la base DuckDB  
   - Effectuer l’analyse descriptive  
   - Générer un **rapport HTML** avec le tableau des effectifs  

---

## Auteur  
**Audrey Difernand** : 
 <audreydif@gmail.com>

