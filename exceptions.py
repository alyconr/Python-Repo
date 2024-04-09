lista = [3, 5, 6, 8]

while True:
    try:
        pos = int(input("ingrese la posición del elemento que desea obtener:"))
        print(f"El valor en la posicion {pos} es {lista[pos]}")
        break
    except IndexError:
        print("la posicion no existe")
        
    except ValueError:
        print("la posicion no es un entero")
