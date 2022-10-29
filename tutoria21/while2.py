#pedir intentos al usuario
intentos= int(input("ingresa intentos -> ")) #4
salir=False

while(not salir):
    par= int(input("ingresa un numero par -> "))

    if(par%2==0):
        print("bien jugado")
    else:
        intentos -=1

    if(intentos==0):
        #debemos salir del juego
        salir=True
        print("salimos del juego!")

    print('cantidad intentos -> ',intentos)