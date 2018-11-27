import couchdb
import csv
server = couchdb.Server('http://user:user@localhost:5984/')
try:
    #Si no existe la Base de datos la crea
    db = server.create('importarcsv')
except:
    #Caso contrario solo conectarse a la base existente
    db = server['importarcsv']
doc=open('importarcsv\catsvdogs.csv',"r")
reader = csv.reader(doc)
for row in reader:
			ingreso = db.save({'Localization' : row[0],'NumberofHouseholds(in1000)': row[1],'Percentageofhouseholdswithpets': row[2]
			,'NumberofPetHouseholds(in1000)': row[3],'PercentageofDogOwners': row[4],'DogOwningHouseholds(1000s)': row[5],'MeanNumberofDogsperhousehold': row[6],'DogPopulation(in1000)': row[7]
			,'PercentageofCatOwners': row[8],'CatOwningHouseholds': row[9],'MeanNumberofCats': row[10],'CatPopulation': row[11]})
doc.close

