from tkinter import * 
from tkinter import filedialog as fd
from os import getcwd,mkdir,rename,path
import os
import json

from CleanDownload import cleanUp



def choisirPath():
    filename = fd.askdirectory()
    if filename !="":
        cheminText.config(text = filename)
        buttonOrganiser['state'] = NORMAL
    else:
        cheminText.config(text = "Choisir un Chemin")


def organiser():
    # print()
    cleanUp(cheminText.cget("text"))

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

if path.exists(os.getenv('APPDATA')+"\\DownloadOrganiser\\save.json"):
    print("Fichier exist")
else: 
    print("Fichier n'exist pas")




root.mainloop()
