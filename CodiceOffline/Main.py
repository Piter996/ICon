import pandas as pd

from LinkCam import *


def init_cam():

#PATH_CSV = os.getcwd() + '\\res\\CamLocations\\Cam.csv'

 path_csv = 'res/CamLocations/Cam.csv'

 #print (path_csv)

 #estrae il DataFRame riguardante la colonna richiesta
 data_X = pd.read_csv(path_csv, usecols=['X'])
 data_Y = pd.read_csv(path_csv, usecols=['Y'])
 data_ID = pd.read_csv(path_csv, usecols=['ID'])
 data_TYPE = pd.read_csv(path_csv, usecols=['TYPE'])

 #Inizializza la classe Sorveglianza che conterra le info riguardanti le telecamere
 Controller = Sorveglianza
 Controller.__init__(Controller)

 #Conversione dei DataFrame in array per facilitare il caricamneto
 import_X = data_X.to_numpy()
 import_Y = data_Y.to_numpy()
 import_ID = data_ID.to_numpy()
 import_TYPE = data_TYPE.to_numpy()

#Ciclo di caricamento dei dati nella classe Sorveglianza
 for i, h, j, k in zip(import_X, import_Y, import_ID, import_TYPE):
    
    Controller.update_X(Controller, i)
    Controller.update_Y(Controller, h)
    Controller.update_ID(Controller, j)
    Controller.update_TYPE(Controller, k)

    data1 = Controller.update_X
    data2 = Controller.update_Y
    data3 = Controller.update_ID
    data4 = Controller.update_TYPE

 #Controller.show_CAM(Controller)

 #print('done!')

 return data1, data2, data3, data4
