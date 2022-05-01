from pymongo import MongoClient
import pprint

user = "root"
mdp = "pass12345"
port_nb = "27017"
url = "localhost"

client = MongoClient(f"mongodb://{user}:{mdp}@{url}:{port_nb}")

db = client["DBLP"]
collection = db['publis']

#Compter le nombre de documents de la collection publis
nb_docs = collection.find()
print(nb_docs)
doc_count = 0
for i in nb_docs:
    doc_count += 1
print(doc_count)

#Lister tous les livres (type “Book”) 
liste_livre = collection.find({"type":"Book"})
item_count = 0
for i in liste_livre:
    pprint.pprint(i)
    item_count += 1
print(item_count) 

#Lister les livres depuis 2014
liste_depuis_2014 = collection.find({"year": {"$gt": 2014}})
item_count = 0
for i in liste_depuis_2014:
    pprint.pprint(i)
    item_count += 1
print(item_count)

#Lister tous les auteurs distincts 
auteur = collection.distinct("authors")
# auteur = collection.find({"authors":{"$exists":"1"}})
item_count = 0
for i in auteur:
    pprint.pprint(i)
    item_count += 1
print(item_count)

#Lister les publications de l’auteur “Toru Ishida”
toru_ishida = collection.find({"authors":"Toru Ishida"})
item_count = 0
for i in toru_ishida:
    pprint.pprint(i)
    item_count += 1
print(item_count)

#Trier les publications de “Toru Ishida” par titre de livre
toru_ishida_sort = collection.aggregate( [{"$match" : {"authors":"Toru Ishida"}}, {"$sort" : {"booktitle": -1}}])
item_count = 0
for i in toru_ishida_sort:
    pprint.pprint(i)
    item_count += 1
#Compter le nombre de ses publications
print(item_count)

#Compter le nombre de publications depuis 2011 et par type
#Compter le nombre de publications par auteur et trier le résultat par ordre croissant

client.close()
