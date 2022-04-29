from pymongo import MongoClient
import pprint

user = "root"
mdp = "pass12345"

client = MongoClient(f"mongodb://root:pas12345@localhost:27017")
db = client["DBLP"]
collection = db['publis']

#Compter le nombre de documents de la collection publis
#Lister tous les livres (type “Book”) 
#Lister les livres depuis 2014
#Lister les publications de l’auteur “Toru Ishida”
#Lister tous les auteurs distincts 
#Trier les publications de “Toru Ishida” par titre de livre
#Compter le nombre de ses publications
#Compter le nombre de publications depuis 2011 et par type
#Compter le nombre de publications par auteur et trier le résultat par ordre croissant

#Compter le nombre de documents de la collection publis
nb_docs = collection.stats()
pprint.pprint(nb_docs)


# rogue = collection.find_one({"nom":"Rogue"})

# pprint.pprint(rogue)

# collection.insert_one({"nom":"Dumbledore", "prenom":"Albus", "titre":"directeur"})

# professeurs = collection.find()

# for prof in professeurs :
#     pprint.pprint(prof)

client.close()
