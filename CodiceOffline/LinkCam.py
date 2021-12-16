#Classe che inizializza l'impianto di Sorveglianza

class Sorveglianza:

    def _init_(self):
        self.Y = []
        self.X = []
        self.ID = []


    def update_Y (self,Y):
        self.Y.append(Y)
        #print("Done!")

    def update_X (self,X):
        self.X.append(X)
        #print("Done!")


    def update_ID (self,ID):
        self.ID.append(ID)
        #print("Done!")


    def show_CAM (self):

        for i,h,j in zip(self.X,self.Y,self.ID):

            print(i , h , j)
