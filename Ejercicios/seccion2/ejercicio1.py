# vamos a utilizar la sentencia de control if (SI)

# lista = [1,2,3,4]

# if 6 in lista:
#     print("El 6 numero existe la lista")
# elif 5 in lista:
#     print("El 5 numero existe la lista")
# else:
#     print("Ninguno de los dos numeros esta en la lista")

def verificarNumeroMayor(num1,num2):
    if num1 > num2:
        print(f"El numero {num1} es mayor que el numero {num2}")
    else:
        print(f"El numero {num2} es mayor que el numero {num1}")

verificarNumeroMayor(6,9)
verificarNumeroMayor(9,1)
verificarNumeroMayor(100,100.01)




