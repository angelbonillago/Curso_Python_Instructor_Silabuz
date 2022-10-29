import csv

with open('titanic.csv') as csvfile:

    csv_reader = csv.reader(csvfile)
    lista_cabeceras = (next(csv_reader,None)) #evitamos el encabezado!
    diccionario_cabeceras ={}
    contador = 0

    for i in lista_cabeceras:
        diccionario_cabeceras[i]=contador
        contador+=1
    print(diccionario_cabeceras)
  
    sumaEdades=0
    contador=0
    promedio=0.0
    cantidad_sobrevivientes=0
    cantidad_fallecidos=0
    cantidad_hombres=0
    cantidad_mujeres=0

    for row in csv_reader:
        #sumar edades
        if((row[diccionario_cabeceras['Age']]) !=""):
            sumaEdades+=float(row[diccionario_cabeceras['Age']])
            contador+=1

        #para validar fallecidos
        if((row[diccionario_cabeceras['Survived']]) =="1"):
            cantidad_sobrevivientes+=1    
        elif((row[diccionario_cabeceras['Survived']]) =="0"):
            cantidad_fallecidos+=1  

        #cantidad de hombres y mujeres
        if((row[diccionario_cabeceras['Sex']]) =="male"):
            cantidad_hombres+=1    
        elif((row[diccionario_cabeceras['Sex']]) =="female"):
            cantidad_mujeres+=1  
    
    promedio=sumaEdades/contador

    print("EL PROMEDIO DE EDADES DEL CSV ES -> ",promedio)
    print("LA CANTIDAD DE HOMBRES ES  ->",cantidad_hombres, " \nLA CANTIDAD DE MUEJRES ES ->",cantidad_mujeres)
    print("LA CANTIDAD DE SOBREVIVIENTES ES -> ",cantidad_sobrevivientes," \nLA CANTIDAD DE FALLECIDOS ES ->",cantidad_fallecidos)
