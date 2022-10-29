import csv

with open('titanic1.csv') as f:
    reader = csv.reader(f)
    cabeceras=next(reader) # para no ver las cabeceras, porque no toma la primera línea
    print(cabeceras)

    suma_edades=0.0
    promedio=0.0
    cantidad_sobrevivientes=0
    cantidad_fallecidos=0
    cantidad_hombres=0
    cantidad_mujeres=0
    contador=0

    for columna in reader:
        if(columna[5] !=""): #cuando sea != del vacio, realiza la suma
            #print(columna[5])
            suma_edades+=float(columna[5])
            contador+=1
    
        #numero de hombres y mujeres
        if(columna[4] !=""): #cuando sea != del vacio, ingresa para contar
            #print(columna[5])
            if(columna[4]=="male"):
                cantidad_hombres+=1
    
            elif(columna[4]=="female"):
                cantidad_mujeres+=1
        
        #numeros de fallecidos y sobrevivientes.
        if(columna[1]=="0"):
            cantidad_fallecidos+=1
    
        elif(columna[1]=="1"):
            cantidad_sobrevivientes+=1

    #promedio de edades
    promedio=suma_edades/contador
    print("EL PROMEDIO DE EDADES DEL CSV ES-> ",promedio)
    print("CANTIDAD DE HOMBRES ES-> ",cantidad_hombres)
    print("CANTIDAD DE MUJERES ES-> ",cantidad_mujeres)
    print("CANTIDAD DE fallecidos ES-> ",cantidad_fallecidos)
    print("CANTIDAD DE Sobrevivientes ES-> ",cantidad_sobrevivientes)





