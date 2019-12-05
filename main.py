#Importando arcpy sin importar nada
### REF https://lidarblog.com/2018-10-01-configure-arcpy-notebook
import os
import sys
import shutil
import functions
import clean
import arcgis
import volume
try:
    import archook #The module which locates arcgis
    archook.get_arcpy()
    import arcpy
    from arcpy import env
    from arcpy.sa import *
    arcpy.CheckOutExtension("Spatial")
except ImportError:
    print("import arcpy error")
d = arcpy.GetInstallInfo()
for key, value in list(d.items()):
    # Print a formatted string of the install key and its value
    #
    print("{:<13} : {}".format(key, value))
#Importando paquetes
import numpy as np
import matplotlib.pyplot as plt
print("#############COMENZANDO SCRIPT GENERACION DE ISOPACAS#############")

# Importando datos y funciones
# Los datos se importan en el modulo de funciones para poder tener los datos en un solo lugar


# Definiendo las columnas de manera manual
variables = [ 
'LOCATION',
'Eastering',
'Northering',
'Vent Distance(km)',
'Altura(km) DEM_ALOS',
'Altura(m) DEM_ALOS',
'UTM ZONES',
'UTM X',
'UTM Y'
]
erupciones=[
# 'Okupata_Pourahu',
# 'XXIX_(Akurangi)_compiled',
# 'XXVII_(Oruamatua)_compiled',
# 'XXVI_(Shawcroft)',
'XXVI_(Shawcroft2)'
# 'IX_(Mangatoetoenui)_compiled',
]


def cleanAll():
    clean.cleanArcmapGdbs()
    clean.cleanArcmapLayers()
    clean.cleanHistograms()
    clean.cleanScatters()
    clean.cleanRDataset()
    ##Creando carpetas de todas las erupciones
    clean.createFolderLayers()

## Creando Histogramas FreqVsThickness y LogTransform thickness vs distance
def createHistogramsAndScatters():
    print "Paso 1: Generacion de Histogramas FreqVsThickness y LogTransform thickness vs distance"
    for erupcion in erupciones:
        try:
            functions.freqVSthickness(erupcion)
            functions.logThicknessVSdistance(erupcion)
            functions.freqVSlogThickness(erupcion)
            
        except:
            print("Hubo un error en la erupcion:"+erupcion)
    print "Paso 1: Terminado"

def runAll():
    # cleanAll()
    # createHistogramsAndScatters()
    for erupcion in erupciones:
        print "Paso 1 "+erupcion +": Crear gdb"
        arcgis.createGdbs(erupcion)
        print "Paso 2 "+erupcion +": Crear Tabla sin 0 y sin -1"
        arcgis.cleanTableInGdb(erupcion)
        print "Paso 3 "+erupcion +": Crear Tabla de cero espesor"
        arcgis.limitIsopachTable(erupcion)
        print "Paso 4 "+erupcion +": Crear Tabla de estaciones erocionadas"
        arcgis.erodedIsopachTable(erupcion)
        print "Paso 5 "+erupcion +": Crear Creando layer x y z de estaciones"
        arcgis.createXYfeatureFromTable(erupcion)
        arcgis.createShapeFromTLayer(erupcion)
        print "Paso 6 "+erupcion +": Crear Creando layer x y z de estaciones con cero espesor"
        arcgis.createXYfeatureFromTableLimit(erupcion)
        print "Paso 7 "+erupcion +": Crear Creando layer x y z de estaciones erosionadas"
        arcgis.createXYfeatureFromTableEroded(erupcion)
        print "Paso 8 "+erupcion +": Creando modelo de tendencia"
        arcgis.createTrend(erupcion)
        print "Paso 9 "+erupcion +": Extrayendo los valores del modelo de tendencia a mano"
        # arcgis.extractingValuesTrend(erupcion)
        # print "Paso 10 "+erupcion +": Creando el campo de residuos del modelo en el .lyr"
        # arcgis.addFieldRes(erupcion)
        # print "Paso 11 "+erupcion +": Calculando el valor de residuos del .lyr"
        # arcgis.calculateFieldRes(erupcion)
        # print "Paso 8 "+erupcion +": "
        # print "Paso 8 "+erupcion +": "
        # print "Paso 8 "+erupcion +": "
        # print "Paso 8 "+erupcion +": "
        
runAll()

