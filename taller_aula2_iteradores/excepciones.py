
def obtengaDivision(dividendo,divisor):

    while True:
        try:
            resultado=dividendo/divisor  
            print("El resultado es -> ",resultado)
            break

        except Exception as a:
            print("No dividas entre 0 ")
            break
    print("sali!!")

obtengaDivision(10,5)