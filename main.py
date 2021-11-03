import requests
import os

nbrname = int(input("Nombre de noms a gen : "))
for i in range(nbrname):
    slt = requests.get("https://eu.mspapis.com/profileidentity/v1/profiles/names/suggestions/?&gameId=5ooi&culture=fr-FR")
    result = slt.text.replace("[", "").replace("]", "").replace(",", " ").replace("\"", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")
    print(result)
    tempfile = open("tempfile.txt", "a")
    tempfile.write(result + "\n")
    tempfile.close()
    
choix = input("Enregistrez les noms (y/n) : ")
if choix == "y":
    filename = input("Nom du .txt : ")
    os.rename("tempfile.txt", filename + ".txt")
    input("Appuyez sur ENTRER pour fermer.")
else:
    os.remove("tempfile.txt")
    input("Appuyez sur ENTRER pour fermer.")
    quit()