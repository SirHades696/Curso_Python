
class Example:

    def __init__(self):
       self.saludo = "Curso de programacion"
       #self.suma = 6+5
       #print(self.suma)

    def __str__(self):
        return "Soy un objeto del tipo Example"

    def nuevo_saludo(self,nombre:str):
        """
        Es un metodo que recibe como parametro un str y devuelve un saludo

        :param nombre: str
        """
        print(f"Hola, como estas? {nombre}")


clase1 = Example()

clase1.nuevo_saludo("Emmanuel")

# # -------------- Tenenemos un solo objeto -----------
# # Verificar que tipo de objeto acabamos de crear - Obj - Example
# print(clase1)
# # Imprime el atributo saludo
# print(clase1.saludo)
# # reasignacion de la atributo saludo
# clase1.saludo = "Hola a todos"
# # contiene la reasignacion
# print(clase1.saludo)

# # ------------- Tener un objeto 2--------------
# objeto2 = Example()
# print(objeto2.saludo)
