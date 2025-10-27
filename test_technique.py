import requests
import pandas as pd
import duckdb

### Récupération des données et importation dans DuckDB

## Etapes 1/2/3

## Script Python pour récupérer les données depuis l'API d'Ameli, 
## pathologies liées aux cancers, uniquement pour la region IDF
## 100 lignes de données

# URL de base de l'API
BASE_URL = "https://data.ameli.fr/api/records/1.0/search/"

# Paramètres pour la requête
params = {
    "dataset": "effectifs",
    "refine.patho_niv1": "Cancers",  # filtre pathologie cancers
    "refine.region": "11",               # 11 = Île-de-France selon la documentation meme s'il existe le dept = 999
    "rows": 100,                              # nombre de lignes demandées
    "start": 0
}

# Requête API
response = requests.get(BASE_URL, params=params)
data = response.json()

# Extraction des champs utiles
records = [r["fields"] for r in data.get("records", [])]
df = pd.json_normalize(records)

#df.head()

## Etape 4

## Création base DuckDB et importation des données

# Nom du fichier de base de données
db_file = "ameli.duckdb"

# Connexion à DuckDB 
con = duckdb.connect(db_file)

# Création de la table cancers_idf (ou l'efface si existe déjà)
con.execute("DROP TABLE IF EXISTS cancers_idf;")
con.execute("CREATE TABLE cancers_idf AS SELECT * FROM df")

# Vérification rapide : compter les lignes
result = con.execute("SELECT COUNT(*) FROM cancers_idf").fetchone()
print(f"Nombre de lignes insérées dans DuckDB : {result[0]}")

# Fermeture de la connexion
con.close()
print(f"Base de données DuckDB créée : {db_file}")

## Etape 5

## Vérification de l'importation et de l'accessibilité

# Connexion à la base DuckDB existante
con = duckdb.connect("ameli.duckdb")

# 1️⃣ Vérifier les tables existantes
tables = con.execute("SHOW TABLES").fetchall()
print("Tables dans la base DuckDB :")
print(tables)

# 2️⃣ Compter le nombre de lignes dans la table
count = con.execute("SELECT COUNT(*) FROM cancers_idf").fetchone()[0]
print(f"\n Nombre de lignes dans 'cancers_idf' : {count}")

# 3️⃣ Afficher les 5 premières lignes
df_preview = con.execute("SELECT * FROM cancers_idf LIMIT 5").fetchdf()
print("\n Aperçu des 5 premières lignes :")
df_preview

# 4️⃣ Exemple d’agrégation : nombre total d’effectifs par département
agg = con.execute("""
    SELECT dept, COUNT(dept) AS total_effectif
    FROM cancers_idf
    GROUP BY dept
    ORDER BY total_effectif DESC
""").fetchdf()

print("\n Effectif total par département :")
print(agg)

# Fermeture de la connexion
con.close()

