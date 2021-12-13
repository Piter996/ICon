'''
Classe che inizializza le telecamere

'''
import os
from os import X_OK, getcwd, mkdir

#Creazione della telecamera
class Camera:

    def _init_(self,Y,X,name):
        self.Y = Y
        self.X = X
        self.name = name

        Def_Dir = (os.getcwd()) + '\\res\\output\\'+ name +'\\'

        #Controlla che la cartella che andremo a creare non sia gia presente
        print(os.path.exists(Def_Dir))
        if not os.path.exists(Def_Dir):
                    self.PATH = mkdir((os.getcwd()) + '\\res\\output\\'+ name +'\\')

        print('camera creata')
    
    def getX(self):

        return self.X

    def getY(self):

        return self.Y

    def getPATH(self):
        return self.PATH

    def getName(self):
        return self.name

   

#Caricamento delle registrazioni
def REC(object):

    def _init_(self,Camera,ret,frame):
        self.Camera = Camera
        self.ret = ret
        self.frame = frame
        print('frame creato')

class Sorveglianza:
       
        def _init_(self):
            self.Y = []
            self.X = []
            self.ID = []

        def update (self,Y,X,ID):
            self.Y.append(Y)
            self.X.append(X)
            self.ID.append(ID)