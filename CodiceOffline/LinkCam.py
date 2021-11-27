'''
Classe che inizializza le telecamere

'''

from os import X_OK, getcwd, mkdir

#Creazione della telecamera
def Camera(object):

    def _init_(self,ID,Y,X,name):
        self.ID = ID
        self.Y = Y
        self.X = 1
        self.name = name
        self.PATH = mkdir(getcwd + 'res\\output\\'+ name +'\\')
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


