#lista=[i for i in range(10000000)]

#print(lista)

lista2= iter(range(10000000000000))
lista2
print(lista2)

exit()

print(next(lista2))
print(next(lista2))
print(next(lista2))

print("----------")
for x in lista2:
    print(x)