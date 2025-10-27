import requests
import pandas as pd

###########################################################
### Récupération des données et importation dans DuckDB ###
###########################################################

##################
## Etapes 1/2/3 ##
##################

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