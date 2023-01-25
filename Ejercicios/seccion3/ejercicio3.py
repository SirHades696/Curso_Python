# clase padre
class Vehiculo:
    # para agregar la documentación del código debe de estar debajo de la funcion y presionar CTRL+SHIFT+2
    def __init__(self, color:str, n_ruedas:int, modelo:int, marca:str, motor:str):
        """
        Clase padre que se encarga de inicializar los parametros comunes entre los diferentes tipos de vehiculos

        :param color: str
        :param n_ruedas: int
        :param modelo: int
        :param marca: str
        :param motor: str
        """
        self.color = color
        self.n_ruedas = n_ruedas
        self.modelo = modelo
        self.marca = marca
        self.motor = motor

    def __str__(self):
        texto = f"Color: {self.color}\nNumero de Ruedas: {self.n_ruedas}\nModelo: {self.modelo}\nMarca: {self.marca}\nTiene motor: {self.motor}"
        return texto


class Automovil(Vehiculo):
    def __init__(self, color: str, n_ruedas: int, modelo: int, marca: str, motor: str, n_cilindros:int):
        super().__init__(color, n_ruedas, modelo, marca, motor)
        self.n_cilindros = n_cilindros

    def set_velocidad(self,velocidad:int):
        self.velocidad = velocidad

    def __str__(self):
        prev = super().__str__()
        texto = f"\nNumero de cilindros: {self.n_cilindros}\nVelocidad: {self.velocidad} km/hr"
        return prev + texto

# automovil = Automovil("Rojo",4,2014,"Chevrolet","Si",4)
# automovil.set_velocidad(180)
# print(automovil)

vehi = Vehiculo("Rojo",4,1980,"Sedan","Si")
print(vehi)

print("----------------\n\n")

auto = Automovil("Plata",4,2016,"Sonic","Gasolina",4)
auto.set_velocidad(220)
print(auto)




