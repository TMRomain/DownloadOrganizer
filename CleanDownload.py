from os import listdir,mkdir,rename,path
from os.path import isfile, join,isdir
from pip._vendor.distlib.compat import raw_input

backslash = '\\'
class Dossier:
  def __init__(dossier, filename, extension):
    dossier.filename = filename
    dossier.extension = extension

#Tout les fichier disponnible
filetocreate=(
    Dossier("Dossiers",""),
    Dossier("Documents",(".docx",".pdf",".xlsx",".txt")),
    Dossier("Archives",(".zip",".rar",".7z")),
    Dossier("Executables",(".exe",".msi")),
    Dossier("Images",(".jpg",".png",".gif",".tif")),
    Dossier("Medias",(".avi",".flv",".mov",".mp4")),
    Dossier("Programation",(".html",".py",".css",".js",".svg",".xml",".cpp")),
    Dossier("Autres",""),
)

#mypath = raw_input("What is your file path :  ")
#A enlever plus tard
mypath = 'C:\\Users\\1931553\\Downloads'

onlyfolders = [x for x in listdir(mypath) if isdir(join(mypath, x))]
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

#Verifier si les fichier destination existe
for i in range(0, len(filetocreate)):
    if not filetocreate[i].filename in onlyfolders:
            mkdir(mypath + backslash + filetocreate[i].filename)

#Deplacer les dossier vers le dossier dossier
for x in range(0,len(filetocreate)):
    if filetocreate[x].filename in onlyfolders:
        onlyfolders.remove(filetocreate[x].filename)

for b in range(0,len(onlyfolders)):
    rename(mypath + backslash + onlyfolders[b], mypath + backslash +filetocreate[0].filename + backslash+ onlyfolders[b])


#Deplacer les fichier vers les bon dossier
for y in range(0,len(onlyfiles)):
    asmove = False
    filename, file_extension = path.splitext(onlyfiles[y])
    for z in range(0,len(filetocreate)):
        for f in range(0,len(filetocreate[z].extension)):
            if file_extension == filetocreate[z].extension[f]:
                rename(mypath + backslash + onlyfiles[y], mypath + backslash + filetocreate[z].filename + backslash + onlyfiles[y])
                asmove = True
                break
    if asmove == False :
        rename(mypath + backslash + onlyfiles[y],mypath + backslash + filetocreate[-1].filename + backslash + onlyfiles[y])