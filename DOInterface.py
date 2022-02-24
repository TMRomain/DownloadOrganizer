from tkinter import * 
from os import getcwd,mkdir,rename,path

from CleanDownload import cleanUp

root = Tk()

root.title("Download Organiser")
root.iconbitmap(getcwd()+"\\images\\icon.ico")

print(getcwd()+"\\images\\icon.ico")


titre = Label(root,text="Download Organiser")
description = Label(root,text="Script python qui organise les fichiers du dossier 'Telechargement'")
buttonOrganiser = Button(root,text="Organiser",padx = 50, command=cleanUp)
footer = Label(root,text="Par Romain Dubard Robert")


titre.grid(row=0,column=0)
description.grid(row=1,column=0)
buttonOrganiser.grid(row=2,column=0)
footer.grid(row=3,column=0)

root.mainloop()
