from tkinter import * 

from CleanDownload import cleanUp

root = Tk()


titre = Label(root,text="Download Organiser")
description = Label(root,text="Script python qui organise les fichiers du dossier 'Telechargement'")
buttonOrganiser = Button(root,text="Organiser",padx = 50, command=cleanUp)



titre.grid(row=0,column=0)
description.grid(row=1,column=0)
buttonOrganiser.grid(row=2,column=0)


root.mainloop()
