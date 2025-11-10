
def f1():
    lista=["gato", "perro", "conejo", "gato"]
    if len(lista) == len(set(lista)):
        print(f"No existen elementos repetidos en la lista {lista}")
    else:
        print(f"Existen elementos repetidos en la lista {lista}")

def f2():
    lista=["gato", "perro", "conejo", "pez" ]
    print(lista)
    vocales = "aeiouAEIOU"
    for cadena in lista:
        b = sum(1 for char in cadena if char in vocales)
        if b >= 2:
            print(f"La cadena '{cadena}' tiene {b} vocales.")
        else :
            print("No existe ninguna otra cadena con dos o más vocales.")


def f3():
    a=["pera", "manzana", "kiwi" , "limon", "uva" , "piña", "coco"]
    b=["pera", "limon", "uva" , "piña", "coco"]
    print(a)
    print(b)
    c=list(set(a) - set(b))
    print(f"Elementos de la primera lista que no están en la segunda: {c}")

def f4():
    a=[1,2,3,4,5,6,7,8,9]
    print(a)
    prom= sum(a)/len(a)
    print(f"El promedio es: {prom}")


#Despues
def main():
    a=int(input("1. Elementos repetidos en una lista \n 2. Cadenas con vocales \n 3.  Diferencia entre listas \n 4: Promedio lista \n Escriba del 1 al 4 que función desea ejecutar: "))
    if a==1:
        f1()
    if a==2:
        f2()
    if a==3:
        f3()
    if a==4:
        f4()

if __name__ == "__main__":
    main()