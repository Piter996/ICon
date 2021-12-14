from LinkCam import *
from os import *

import pandas as pd

PATH_CSV =os.getcwd() + '\\res\\CamLocations\\Cam.csv'

PATH_CSV = 'C:\\Users\\P1T3R\\Documents\\GitHub\\ICon\\CodiceOffline\\res\\CamLocations\\Cam.csv'

print (PATH_CSV)

Column_X = 'X'

data = pd.read_csv(PATH_CSV, sep = ';')
data = pd.reindex_axis(pd.columns.intersection('X'), 1)

printer = list(data)
Controller = Sorveglianza
print (len(printer))
Controller._init_(Controller)

for i in data:
    # Controller.update(Controller)

     print(data)

print ("Hi") 

