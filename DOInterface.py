from tkinter import * 

from CleanDownload import cleanUp

root = Tk()


titre = Label(root,text="Download Organiser")
description = Label(root,text="Script python qui organise les fichiers du dossier 'Telechargement'")


titre.grid(row=0,column=0)
description.grid(row=1,column=0)
root.mainloop()
