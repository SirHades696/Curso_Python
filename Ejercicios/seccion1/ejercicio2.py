
# cadena = "Curso de programación con python"
# # recorrido de izquierda a derecha
# print(f"Selección de izquieda a derecha: {cadena[9:22]}")
# # recorrido de derecha a izquierda
# print(f"Selección de derecha a izquieda: {cadena[-23:-11]}")

path = r"home/hades/Documentos/Curso Python/Curso_Python/Ejercicios"

# Simulación de la ruta de un archivo vectorial
path2 = "C:\\documentos\\ejercicio\\seccion1\\estado.shp"

# Corte a la cadena "path2" a traves cadena ".shp", devuelve un array de dos elementos
nombre_archivo = path2.split(".shp")[0]

# simulando la ruta de almacenamiento de una hoja de estilo para un archivo vectorial con extension ".qml"
path_almacenamiento = nombre_archivo + ".qml"

print(f"Ruta del archivo vectorial: {path2}")
print(f"Ruta del archivo de estilo: {path_almacenamiento}")


