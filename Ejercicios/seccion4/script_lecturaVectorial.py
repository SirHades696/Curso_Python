# Importar las librerias para trabajar con datos vectoriales desde python
from qgis.core import QgsVectorLayer
import processing

# # Obtener la ruta de ubicacion del archivo
path_Tam = r"/home/hades/Documentos/Curso Python/Curso_Python/Vectoriales/Tamaulipas/Tamaulipas.shp"

# # Crear el objeto vectorial con nombre Tamaulipas

layer = QgsVectorLayer(path_Tam,"Tamaulipas","ogr")

# # Agregarlo al Workspace (Espacio de Trabajo de QGIS)
# QgsProject.instance().addMapLayer(layer)

# .mapLayersByName - Retorna una lista y selecciona a los objetos ya cargados en el espacio de trabajo.
# layer = QgsProject.instance().mapLayersByName("Tamaulipas")[0]

# print(layer)

# la funcion de esta forma retorna un dict con las capas existentes
# layers = QgsProject.instance().mapLayers()

# cuando a .mapLayers() se agrega values vamos a tener acceso a los objetos vectoriales
# layers = QgsProject.instance().mapLayers().values()

# for layer in layers:
#     print(layer)

# ubicacion del archivo
print(layer.source())

# nombre del archivo
print(layer.name())

# es un  objeto iterable
fields = layer.fields()

# .name() nos devuelve los atributos de la capa (nombre de las columnas) el .typeName() nos devuelve el tipo del campo (int, str, float)
# for field in fields:
#     print(field.name(),"---Tipo---",field.typeName())

algoritmos = QgsApplication.processingRegistry().algorithms()
for alg in algoritmos:
    print(f"ID {alg.id()} ---- {alg.displayName()}")
