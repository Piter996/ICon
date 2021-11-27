'''
Classe che inizializza le telecamere

'''
import os
from os import X_OK, getcwd, mkdir

#Creazione della telecamera
class Camera:

    def _init_(self,Y,X,name):
        self.Y = Y
        self.X = 1
        self.name = name
        self.PATH = mkdir((os.getcwd()) + '\\res\\output\\'+ name +'\\')
        print('camera creata')
    
    def getX(self):

        print(self.X)

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

camN = Camera

camN._init_(camN,1,2,'name')

camN.getX
