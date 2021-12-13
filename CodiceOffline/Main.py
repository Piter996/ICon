#from CodiceOffline.LinkCam import Sorveglianza
import LinkCam 
import pandas as pd

PATH_CSV ="./res/CamLocations/Cam.csv"

data = pd.read_csv(PATH_CSV, delimiter = ';', header = 0)
printer = list(data)
Controller = 

#Controller._init_(Controller)


for item in printer:
    #  Controller.update(Controller)

     print(item)

print ("Hi") 

    