from flask import Flask, request
app = Flask(__name__)
from bson import json_util
import json
import meilisearch

URL_MEILISEARCH = "https://ms-9922df2a3974-7771.nyc.meilisearch.io"
MEILI_KEY = "dc070f11d97ec112cf0fbdf84120dc2b2830b6a0"
client = meilisearch.Client(URL_MEILISEARCH, MEILI_KEY)

#Funções
def parse_json(data):
    return json.loads(json_util.dumps(data))

#Lidando com o get do endpoint /noticias
@app.get('/noticias/<page>')
def fetch_noticias(page):
   response = parse_json(client.index('noticias').search("", {"hitsPerPage": (12 * int(page)), "sort": ["Data:desc"]}))
   return (response)

#Lidando com o get do endpoint /trending
@app.get('/trending')
def trending_fake():
   response = parse_json(client.index("trending_fake").search("", {"hitsPerPage": 5, "sort": ["Data:desc", "Ordem:asc"]}))
   return (response)

#Lidando com o get do endpoint /search
@app.get("/search/<page>")
def search(page):
   search_params = request.args.get('search')
   response = parse_json(client.index('noticias').search(search_params, {"hitsPerPage": (12 * int(page))}))
   return (response)
   
"""
raw_data = parse_json(trending.find({}, {"_id":False}).limit(5).sort({"Data": -1}))
response = [None, None, None, None, None]
   for entidade in raw_data:
      response[int(entidade["Ordem"])-1] = entidade
return (response)
"""

