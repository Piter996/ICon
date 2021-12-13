from LinkCam import *
import pandas as pd

#PATH_CSV =".\\res\\CamLocations\\Cam.csv"

data = pd.read_csv('C:\\Users\\Pietro\\Documents\\GitHub\\ICon\\CodiceOffline\\res\\CamLocations\\Cam.csv', delimiter = ';', header = 0)
printer = list(data)
Controller = Sorveglianza

Controller._init_(Controller)


for item in printer:
    #  Controller.update(Controller)

     print(item)

print ("Hi") 

    