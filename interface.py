from tkinter import *

class Renommeur:

    def __init__(self, master):

        optionList = ["Yes","No"]
        self.dropVar=StringVar()
        self.dropVar.set("Yes") # default choice
        self.dropMenu1 = OptionMenu(self, self.dropVar, *optionList,command=self.func)

        frame = Frame(master)
        frame.pack()

        self.renommerButton = Button(frame, text ="Renommer", command= self.printMessage)
        self.renommerButton.pack(side=RIGHT)
        




    def printMessage(self):
        print("Bouton fonctionne")

        
root = Tk()
f = Renommeur(root)
root.mainloop()
