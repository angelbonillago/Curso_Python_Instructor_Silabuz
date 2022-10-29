lista_a = ["Marcelo","Jose","Juan"]
lista_b = [15,20,18]


for indice, tupla in enumerate(sorted(zip(lista_a, lista_b))):
	print(indice+1, " -> ", tupla[0]," : " ,tupla[1])
