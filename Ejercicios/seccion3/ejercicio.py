
class Alumno:

    def __init__(self):
        self.universidad = "UAEMex"
        self.facultad = "Geografia"
        self.curso = "Curso de programacion con Python"


    def set_nombre(self,nombre:str):
        """
        Este metodo se encarga de 'settear' el nombre del alumno

        :param nombre: str
        """
        #self.nombre = nombre.upper() # La funcion upper convierte todo el texto en mayusculas
        #self.nombre = nombre.capitalize() # Iniciar la primera letra en mayusculas
        #self.nombre = nombre.lower() # el texto sea en minusculas
        self.nombre = nombre.title() # cada palabra  (1ra letra) en mayusculas

    def get_nombre(self):
        """
        Metodo que retorna el nombre del alumno

        """
        return self.nombre

    def set_calificacion(self,calificacion:float):
        self.calificacion = calificacion
        if self.calificacion > 6:
            self.status = "Aprobado"
        else:
            self.status = "Reprobado"


    def __str__(self):
        texto = f"""
                Nombre del alumno: {self.nombre}
                Universidad: {self.universidad}
                Facultad: {self.facultad}
                Curso: {self.curso}
                Estatus: {self.status}
                Calificacion: {self.calificacion}
                """
        return texto



alumno1 = Alumno()
data = {
        "nombre": "Adonai Emmanuel",
        "apellido" : "Nicanor Bautista",
        "carrera" : "Posgrado",
        "universidad" : "UAEMex"
        }
alumno1.set_nombre("adonai emmanuel nicanor bautista")
alumno1.set_calificacion(6.5)
# print(alumno1.get_nombre())
print(alumno1)

alumno2 = Alumno()
alumno2.set_nombre("francisco garcia")
alumno2.set_calificacion(5)
print(alumno2)
