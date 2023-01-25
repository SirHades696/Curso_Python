
# Lista que almacena las rutas de archivos geograficos
lista_geo = [
         r"C:\Documentos\Vectoriales\calles.shp",       # posicion 0
         r"C:\Documentos\Vectoriales\municipios.shp",   # posicion 1
         r"C:\Documentos\Vectoriales\tiendas.shp",      # posicion 2
         r"C:\Documentos\Vectoriales\manzanas.shp",     # posicion 3
         r"C:\Documentos\Rasters\toluca.tif",           # posicion 4
         r"C:\Documentos\Rasters\calles.tif"            # posicion 5
         ]
# numero de elementos que contiene la lista de archivos geograficos
tam_geo = len(lista_geo)

# for i in range(0,4):
#     # ruta auxiliar
#     path_aux = lista_geo[i].split(".shp")[0]
#     # ruta de hoja de estilo QML
#     path_final = path_aux + ".qml"
#     print(path_final)

for path in lista_geo:
    print(path)



