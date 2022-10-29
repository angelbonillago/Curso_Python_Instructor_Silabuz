import csv

with open('titanic1.csv') as f:
    reader=csv.reader(f)
    next(reader) #ya no toma en cuenta a la 1era linea->la cabecera
    datos=[]

    for i in reader:
        print(i)
    
