from pymongo import MongoClient
import pprint

user = "root"
mdp = "pass12345"

client = MongoClient(f"mongodb://root:pas12345@localhost:27017")
db = client["DBLP"]
collection = db['publis']

#Compter le nombre de documents de la collection publis
nb_docs = collection.stats()
pprint.pprint(nb_docs)

#Lister tous les livres (type “Book”) 
liste_livre = collection.find({type:"Book"})
pprint.pprint(liste_livre)

#Lister les livres depuis 2014
liste_depuis_2014 = collection.find({"year": {gt: "2014" }})
pprint.pprint(liste_depuis_2014)

#Lister tous les auteurs distincts 
auteur = collection.find()
pprint.pprint(auteur)

#Lister les publications de l’auteur “Toru Ishida”
toru_ishida = collection.find_one({"nom":"Toru Ishida"})
pprint.pprint(toru_ishida)

#Trier les publications de “Toru Ishida” par titre de livre
titre_ordonne_ishida = collection.sort({"booktitle": -1})
pprint.pprint(titre_ordonne_ishida)

#Compter le nombre de ses publications
livres_ishida = collection.aggregate({"Toru Ishida" : {count:{"booktitle"}}})
pprint.pprint(livres_ishida)

#Compter le nombre de publications depuis 2011 et par type
#Compter le nombre de publications par auteur et trier le résultat par ordre croissant

client.close()
