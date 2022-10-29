"""
Ejercicio 3
Encontrar todos los números comprendidos entre 7 y 537 que contengan el dígito 7

"""
def buscarDigito7():

    list=[]
    for i in range(7,538):
        cadena=str(i)
        for letter in cadena:
            if int(letter)==7:
                list.append(int(cadena))
                break
    print(list)



buscarDigito7()

