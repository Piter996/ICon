import numpy
from LinkCam import *
from os import *
from io import *



import pandas as pd

PATH_CSV =os.getcwd() + '\\res\\CamLocations\\Cam.csv'

PATH_CSV = 'C:\\Users\\P1T3R\\Documents\\GitHub\\ICon\\CodiceOffline\\res\\CamLocations\\Cam.csv'

#print (PATH_CSV)

Column_X = 'X'


data_X = pd.read_csv(PATH_CSV, usecols = ['X'])
data_Y = pd.read_csv(PATH_CSV, usecols = ['Y'])
data_ID = pd.read_csv(PATH_CSV, usecols = ['ID'])


Controller = Sorveglianza
Controller._init_(Controller)


import_X = data_X.to_numpy()
import_Y = data_Y.to_numpy()
import_ID = data_ID.to_numpy()


for i in import_X:
    
    Controller.update_X(Controller,i)

    #print (i)
    #print("end")

for i in import_Y:
    Controller.update_Y(Controller,i)

for i in import_ID:
    Controller.update_ID(Controller,i)


Controller.show_CAM