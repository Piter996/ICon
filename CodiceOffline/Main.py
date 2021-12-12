import csv


with open("C:/Users/Pietro/Documents/GitHub/ICon/CodiceOffline/res/CamLocations/Cam.csv", newline="") as filecsv:

  data = csv.reader(filecsv)
  printer = list(data)

  for item in printer:
     print(item)

print ("Hi") 

    