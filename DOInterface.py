from tkinter import * 
from tkinter import filedialog as fd
from os import getcwd,mkdir,rename,path
import os
import json

from CleanDownload import cleanUp



def choisirPath():
    filename = fd.askdirectory()
    if filename !="":
        ecrireJson(filename)
        cheminText.config(text = filename)
        buttonOrganiser['state'] = NORMAL
    else:
        cheminText.config(text = "Choisir un Chemin")


def organiser():
    # print()
    cleanUp(cheminText.cget("text"))

def ecrireJson(filepath):
    dictionary ={
        "filepath" : filepath,
    }
    
    # Serializing json 
    json_object = json.dumps(dictionary)
    
    # Writing to sample.json
    with open("save.json", "w") as outfile:
        outfile.write(json_object)

def lireJson():
    with open(getcwd()+"\\save.json", 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)


    valeur = list(json_object.values())[0]
    return valeur


root = Tk()

root.title("Download Organiser")
root.iconbitmap(getcwd()+"\\images\\icon.ico")


titre = Label(root,text="Download Organiser")
description = Label(root,text="Script python qui organise les fichiers du dossier 'Telechargement'")
buttonChoisirPath = Button(root,text="Choisir Votre Fichier De telechargement ",padx = 50, command=choisirPath)
cheminText = Label(root,text="Choisir un Chemin")

buttonOrganiser = Button(root,text="Organiser",padx = 50, command=organiser,state=DISABLED)



footer = Label(root,text="Par Romain Dubard Robert")


titre.grid(row=0,column=0)
description.grid(row=1,column=0)
buttonChoisirPath.grid(row=2,column=0)
cheminText.grid(row=3,column=0)
buttonOrganiser.grid(row=4,column=0)
footer.grid(row=5,column=0)


print(os.getenv('APPDATA'))

if path.exists(getcwd()+"\\save.json"):
    path = lireJson()
    cheminText.config(text = path)
    buttonOrganiser['state'] = NORMAL

else: 
    print("Pas de sauvegarde")




root.mainloop()
