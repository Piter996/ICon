import numpy
import pandas as pd
import os

from LinkCam import *
from os import *

PATH_CSV = os.getcwd() + '\\res\\CamLocations\\Cam.csv'

PATH_CSV = 'C:\\Users\\P1T3R\\Documents\\GitHub\\ICon\\CodiceOffline\\res\\CamLocations\\Cam.csv'

#print (PATH_CSV)

#estrae il DataFRame riguardante la colonna richiesta
data_X = pd.read_csv(PATH_CSV, usecols = ['X'])
data_Y = pd.read_csv(PATH_CSV, usecols = ['Y'])
data_ID = pd.read_csv(PATH_CSV, usecols = ['ID'])
data_TYPE = pd.read_csv(PATH_CSV, usecols = ['TYPE'])


#Inizializza la classe Sorveglianza che conterra le info riguardanti le telecamere
Controller = Sorveglianza
Controller._init_(Controller)

#Conversione dei DataFrame in array per facilitare il caricamneto
import_X = data_X.to_numpy()
import_Y = data_Y.to_numpy()
import_ID = data_ID.to_numpy()
import_TYPE = data_TYPE.to_numpy()



#Ciclo di caricamento dei dati nella classe Sorveglianza
for i,h,j,k in zip(import_X,import_Y,import_ID,import_TYPE):
    
    Controller.update_X(Controller,i)
    Controller.update_Y(Controller,h)
    Controller.update_ID(Controller,j)
    Controller.update_TYPE(Controller,k)


Controller.show_CAM(Controller)