"""
Pregunta 3
Dada la lista de notas [15,20,18] y la lista de alumnos ["Marcelo", "José", "Juan"], imprimirlos de la siguiente forma:

1 -> Jose : 20

2 -> Juan : 18

3 -> Marcelo : 15
No usar range, ni comparadores. Hint: usar sorted

"""
def notas(list1: list, list2: list) -> list:
    x = dict(zip(list1, list2))
    for i, e in enumerate(sorted(x.keys(), reverse = False), start=1):
        print(f"{i} -> {e} : {x[e]}")

notas(["Marcelo", "José", "Juan"],[15,20,18])





