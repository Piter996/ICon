#Classe che inizializza l'impianto di Sorveglianza

class Sorveglianza:

    def __init__(self):
        self.Y = []
        self.X = []
        self.ID = []
        self.type = []

    def update_Y(self, Y):
        self.Y.append(Y)
        #print("Done!")

    def update_X(self, X):
        self.X.append(X)
        #print("Done!")

    def update_ID(self, ID):
        self.ID.append(ID)
        #print("Done!")

    # 0 = Vicolo, 1 = Via, 2 = Piazza
    def update_TYPE(self, TYPE):
        self.type.append(TYPE)
        #print("Done!")

    def show_CAM(self):

        for i, h, j, k in zip(self.X, self.Y, self.ID, self.type):

            print(i, h, j, k)
