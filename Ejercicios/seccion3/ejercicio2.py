class Calculadora:

    def __init__(self, num1, num2):
        """
        Metodo constructor que recibe dos parametros

        :param num1: float
        :param num2: float
        """
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        return self.num1 + self.num2

    def restar(self):
        return self.num1 - self.num2

    def multiplicar(self):
        return self.num1 * self.num2

    def dividir(self):
        return self.num1 / self.num2

    def potenciar(self):
        return self.num1 ** self.num2

    def resultados(self):
        print(f"Valor de entrada 1: {self.num1}")
        print(f"Valor de entrada 2: {self.num2}")
        print(f"Operacion suma: {self.sumar()}")
        print(f"Operacion resta: {self.restar()}")
        print(f"Operacion multiplicar: {self.multiplicar()}")
        print(f"Operacion dividir: {self.dividir()}")
        print(f"Operacion potencia: {self.potenciar()}")



operacion = Calculadora(3,9)
operacion.resultados()



