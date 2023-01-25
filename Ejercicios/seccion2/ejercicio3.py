
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

# ------------- PARA COMENTAR CODIGO EN Visual Studio Code -----------
# El texto (codigo) debe estar seleccionado
# para comentar lineas de codigo en formato multilinea
# CTRL + SHIFT + a

# Para comentar codigo linea por linea
# CTRL + K + C

# Para quitar los comentarios de una linea
# CTRL + K + U

matriz1 = [ [1,2,3],
            [3,6,8],
            [7,9,0]
        ]

matriz2 = [ [6,5,0],
            [7,7,0],
            [9,9,0]
        ]

matriz_r = [[0,0,0],
            [0,0,0],
            [0,0,0]
          ]

for i in range(0,3): # Para recorrer los renglones
    for j in range(0,3): # para correr las columnas
        matriz_r[i][j] = matriz1[i][j] + matriz2[i][j]

print(matriz_r)
# i = 0
# entramos al primer elemento de la lista
# j = 0
# Valor de la matriz = 1 - 0,0
# j = 1
# Posicion de la matriz seria 0,1
# j = 2
# Posicion de la matriz seria 0,2

# i = 1
# j = 0
# posicon 1,0 = 3
