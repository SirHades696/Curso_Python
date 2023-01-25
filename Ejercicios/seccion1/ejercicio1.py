
# inicia el saludo
# print("Hola")

"""
Este programa tiene asignadas dos variables
un valor entero y un flotante.
valor1: int
valor2: float
"""

# # asignación del valor1
# valor1 = 10

# # asignación del valor2
# valor2 = 9.5

# Forma de imprimir1
# print("La variable1:",valor1,"La variable2:",valor2)

# forma de imprimir2
# print(f"La variable1: {valor1} La variable2: {valor2}")

# suma de dos numeros
# resta = valor1 - valor2
# print(f"La resta es: {resta}")

"""
Indices lista original
Julio = 0
Rafael = 1
Carlos = 2
Brenda = 4
"""
# lista de una dimension
nombres_dimension1 = ["Julio", "Rafael", "Carlos", "Brenda"]

# print(f"Lista orignal: {nombres}")

# # metodo append  es para agregar valores a las listas (arrays)
# nombres.append("Miriam")

# print(f"Lista cuando se agrego un dato {nombres}")

# nombres.pop(2)

# print(f"Lista cuando se elimino un dato indexado {nombres}")


# nombres_tupla = ("Julio", "Rafael", "Carlos", "Brenda")

# print(nombres_tupla)

# lista de dos dimensiones

nombres_dimension2 = [
        ["Julio", "Rafael", "Carlos", "Brenda"],
        ["Hernandez", "Garcia", "Olivares", "Bautista"]
        ]

# print(nombres_dimension2[0][0], nombres_dimension2[1][0])

dict_nombres = {
            "nombres": ["Julio", "Rafael", "Carlos", "Brenda"],
            "apellidos": ["Hernandez", "Garcia", "Olivares", "Bautista"]
        }
# imprimiendo un dict
print(dict_nombres["nombres"][2], dict_nombres["apellidos"][2])

alumnos = {
            "alumnos":
                {
                    "nombres": ["Julio", "Rafael", "Carlos", "Brenda"],
                    "apellidos": ["Hernandez", "Garcia", "Olivares", "Bautista"],
                    "universidad": "UAEMex"
                }
        }

# print(alumnos['alumnos']['nombres'][3])
# print(alumnos['alumnos']['universidad'])

mis_datos = {
        "1420869":{
                "nombre": "Adonai Emmanuel",
                "apellidos" : "Nicanor Bautista",
                "facultad": "Geografia",
                "carrera": "Posgrado"
            }
        }

print(f"Nombre: {mis_datos['1420869']['nombre']}\nApellidos: {mis_datos['1420869']['apellidos']}")

print(f'Nombre: {mis_datos["1420869"]["nombre"]}')


https://forms.office.com/r/TxJ3Vv21h7







