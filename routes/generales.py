from flask import render_template
import requests
import json

def define_routes(app):
    @app.route("/retrieve_wikidata/<string:id>")
    def retrieve_wikidata(id:str):
        url="https://www.wikidata.org/Special:EntityData/{id}.json" #récupérer l'url, l'id de la requête et le format ; url trouvée sur l'API wikidata
        r = requests.get(url) #mettre params = {'format': 'json'} ne change rien
        #mettre r_json=r.json() pour ensuite appeler la variable r_json dans one.html affichait des erreurs requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0) dans l'application
        return render_template("one.html", id=id,r=r)