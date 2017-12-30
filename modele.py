import os 

class action :
    def __init__(self,nomDuRepertoire,regle):
        self.nomDuRepertoire = nomDuRepertoire
        self.regle = regle
        
class regle :
    def __init__(self,amorce,aPartirDe,prefixe,nomFichier,postfixe,extension):
        self.amorce = amorce
        self.aPartirDe = aPartirDe
        self.prefixe = prefixe
        self.nomFichier = nomFichier
        self.postfixe = postfixe
        self.extension = extension

class listeRegle :
    def __init__(self,regle) :
        self.regles = regles
    def sauvegarder(self):
        file = open("configRegles.ini","w")
        file.write(str(self.__dict__))
        file.close()

        
class renommage(action) :
    def __init__(self,nomDuRepertoire,regle):
        action.__init__(self,nomDuRepertoire,regle)
        
    def renommer(self):
        if self.regle.nomFichier == False:
            newName = input("Entrez le nouveau nom des fichiers : ")
        for file in os.listdir(self.nomDuRepertoire):
            file_name, file_ext = os.path.splitext(file)
            if file_ext == self.regle.extension:
                if self.regle.nomFichier == False:
                    file_name = newName
                if self.regle.amorce == "Aucun":
                    file_name = self.regle.prefixe + file_name + self.regle.postfixe
                elif self.regle.amorce == "Lettre":
                    file_name = str(self.regle.aPartirDe) + " " + self.regle.prefixe + file_name + self.regle.postfixe
                    self.regle.aPartirDe = chr(ord(self.regle.aPartirDe) +1)
                elif self.regle.amorce == "Chiffre":
                    file_name = str(self.regle.aPartirDe) + " " + self.regle.prefixe + file_name + self.regle.postfixe
                    self.regle.aPartirDe =  self.regle.aPartirDe +1
                os.rename(os.path.join(self.nomDuRepertoire,file),os.path.join(self.nomDuRepertoire, file_name + file_ext))
            

r1 = regle("Chiffre",1,"PREFIXE - ",True," - POSTFIXE",".txt")
a1 = renommage("D:\users\Desktop\TEST", r1)
renommage.renommer(a1)    

listeRegle.sauvegarder(r1)
