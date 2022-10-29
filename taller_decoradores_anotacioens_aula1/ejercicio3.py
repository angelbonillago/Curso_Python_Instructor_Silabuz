
def decorador3(funcion):
  def auxiliar(palabra):
    funcion(palabra)
  return auxiliar

@decorador3
def duplica_letras(palabra: str)-> str:
  lista = []
  for i in palabra:
    lista.extend((i, i))
  print(lista)
