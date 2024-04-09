
fruits = {"manzana": "apple", "banana": "banana", "naranja": "orange", "pera": "pear", "uva": "grape"}

while True:
    fruit = input("Ingrese el nombre de la fruta a traducir: ")
    if fruit == '':
        continue
    else:
        fruit = fruit.lower()
        if fruit not in fruits:
            print("Fruta no encontrada")
            print("Desea agregar la fruta a la base de datos? (s/n)")
            answer = input()
            if answer == '':
                print("No se aceptan espacios como respuesta")
                continue
            elif answer.lower() == "s":
                fruits[fruit] = input("Ingrese la traduccion: ")
                print(fruits)
                        
            else:
                print("Adios")
                exit()
                
        print(fruits[fruit])

   
   
        












