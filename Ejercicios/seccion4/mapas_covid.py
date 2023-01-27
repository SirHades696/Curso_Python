from qgis.core import QgsVectorLayer
import processing

# Lectura de todas las capas existentes en el workspace
# layers = QgsProject.instance().mapLayers().values()

# iterando las capas del espacio de trabajo
# for layer in layers:
#     print(layer.name())

# lectura de capa por nombre
layer = QgsProject.instance().mapLayersByName("Tamaulipas")[0]

# ---------- Calculo del indice
data_statistics = {
        "INPUT_LAYER":layer,
        "FIELD_NAME": "covid"
        }
# Vamos a calcular las estadisticas basicas de un vectorial y nos va a retornar un dict
stats = processing.run("qgis:basicstatisticsforfields",data_statistics)
total = stats["SUM"] # accedemos al dict a traves de la clave SUM
# print(f"El total de poblacion infectada en {layer.name()}: {total}")

# OP = Output haciendo referencia a la carpeta donde vamos almacenar la informacion
path_op = r"/home/hades/Documentos/Curso Python/Curso_Python/Ejercicios/seccion4/"

data_field_calculator = {
        "INPUT": layer,
        "FIELD_NAME": "por_cov", #Los nombres de los campos no deben exceder los 8 caracteres
        "FIELD_TYPE":0,
        "FIELD_LENGTH":10,
        "FIELD_PRECISION":4, #FIELD_LENGTH_PRECISION 000000.0000
        "NEW_FIELD": True, #Queremos que el campo se anexe al shape y se guarde
        "FORMULA": "(covid * 100)/" + str(total),
        "OUTPUT": path_op + layer.name() + "_v2.shp"
        }
# Path_OP = /Ejercicios/seccion4/Tamaulipas_v2.shp

resultado = processing.run("qgis:fieldcalculator",data_field_calculator)
new_layer = QgsVectorLayer(resultado["OUTPUT"],layer.name() + "_v2","ogr")
QgsProject.instance().addMapLayer(new_layer)

# ---- Inicia la categorizacion "Mapa Tematico"
symbol = QgsFillSymbol() #Hace referencia a los vectoriales del tipo poligono
clasificacion = [QgsGraduatedSymbolRenderer.Quantile]
style = QgsStyle.defaultStyle()
color_ramp = style.colorRampNames() # Contiene una lista con todas las rampas de colores
indice_ramp = color_ramp.index("YlOrRd") # Indice de la rampa  de amarillos a rojos
ramp = style.colorRamp(color_ramp[indice_ramp]) # Aplicar el estilo de rampa seleccionado
#el campo(Expresion) que vamos a clasificar
field = "por_cov"
renderer = QgsGraduatedSymbolRenderer.createRenderer(new_layer,field,5,clasificacion[0],symbol,ramp)
# Recibe primero el obj layer, recibe el campo, recibe el numero de clases, recibe el tipo de clasificacion, recibe el simbolo y la rampa de color
new_layer.setRenderer(renderer)
path_qml = new_layer.source().split(".shp")[0] #obtenemos la ruta de almacenamiento del nuevo archivo, eliminamos la extension ".shp" para agregar la extension ".qml"
# path_qml = ".../Ejercicios/seccion4/Tamaulipas_v2"
new_layer.saveNamedStyle(path_qml+".qml") #Guarda el tematico aplicado con una extension .qml














