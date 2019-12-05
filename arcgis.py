
import os
import sys
import shutil
import functions
import clean
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
## ARCMAP  
# Creando Geodatabase donde se almacenaran todas las capas creadas
def createGdbs(erupcion):
    out_folder_path="C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/gdbs"
    out_name="tesis"+erupcion+".gdb"
    arcpy.CreateFileGDB_management(out_folder_path,out_name)
    print('Paso 1: Terminado')
# Creando Set de datos por erupcion
def cleanTableInGdb(erupcion):
    derupcion=functions.dataSetByEruptionClean(erupcion)
    dts={'names':('UTMX','UTMY',"Erupcion"), 'formats':(np.float,np.float,np.float)}
    dFinal=np.rec.fromrecords(derupcion,dtype=dts)
    ruta="C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/gdbs/tesis"+erupcion+".gdb/cleanTable"
    arcpy.da.NumPyArrayToTable(dFinal,ruta)
    centro=[]
    centro.append([376210.6899,5651036.9653])
    dts2={'names':('UTMX','UTMY'), 'formats':(np.float,np.float)}
    centroFinal= np.rec.fromrecords(centro,dtype=dts2)
    ruta2="C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/gdbs/tesis"+erupcion+".gdb/center"
    arcpy.da.NumPyArrayToTable(centroFinal,ruta2)
    print("Paso 2: Terminado")

def limitIsopachTable(erupcion):
    derupcion=functions.dataSetByEruptionLimits(erupcion)
    dts={'names':('UTMX','UTMY',"Erupcion"), 'formats':(np.float,np.float,np.float)}
    dFinal=np.rec.fromrecords(derupcion,dtype=dts)
    ruta="C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/gdbs/tesis"+erupcion+".gdb/limitTable"
    arcpy.da.NumPyArrayToTable(dFinal,ruta)
    print("Paso 3: Terminado")

def erodedIsopachTable(erupcion):
    derupcion=functions.dataSetByEruptionEroded(erupcion)
    dts={'names':('UTMX','UTMY',"Erupcion"), 'formats':(np.float,np.float,np.float)}
    dFinal=np.rec.fromrecords(derupcion,dtype=dts)
    ruta="C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/gdbs/tesis"+erupcion+".gdb/erodedTable"
    arcpy.da.NumPyArrayToTable(dFinal,ruta)
    print("Paso 4: Terminado")        

def createXYfeatureFromTable(erupcion):
    in_table="C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/gdbs/tesis"+erupcion+".gdb/cleanTable"
    x_coords="UTMX"
    y_coords="UTMY"
    z_coords="Erupcion"
    out_layer=erupcion+"_layer"
    saved_layer="C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/layers/"+erupcion+"/"+out_layer
    spRef=arcpy.SpatialReference(2135) ## WKID CODE 
     # Make the XY event layer...
    arcpy.MakeXYEventLayer_management(in_table, x_coords, y_coords, out_layer, spRef, z_coords)
    # Save to a layer file
    arcpy.SaveToLayerFile_management(out_layer, saved_layer)
    print "Paso 5: Terminado"
def createShapeFromTLayer(erupcion):
    env.workspace="C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/layers/"+erupcion
    out_layer=erupcion+"_layer.lyr"
    inFeatures=[out_layer]
    outLocation = "C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/gdbs/tesis"+erupcion+".gdb"
    arcpy.FeatureClassToShapefile_conversion(inFeatures, outLocation)
def createXYfeatureFromTableLimit(erupcion):
    in_table="C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/gdbs/tesis"+erupcion+".gdb/limitTable"
    x_coords="UTMX"
    y_coords="UTMY"
    z_coords="Erupcion"
    out_layer=erupcion+"_limit_layer"
    saved_layer="C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/layers/"+erupcion+"/"+out_layer
    spRef=arcpy.SpatialReference(2135) ## WKID CODE 
     # Make the XY event layer...
    arcpy.MakeXYEventLayer_management(in_table, x_coords, y_coords, out_layer, spRef)
    # Save to a layer file
    arcpy.SaveToLayerFile_management(out_layer, saved_layer)
    print "Paso 6: Terminado"
def createXYfeatureFromTableEroded(erupcion):
    in_table="C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/gdbs/tesis"+erupcion+".gdb/erodedTable"
    x_coords="UTMX"
    y_coords="UTMY"
    z_coords="Erupcion"
    out_layer=erupcion+"_eroded_layer"
    saved_layer="C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/layers/"+erupcion+"/"+out_layer
    spRef=arcpy.SpatialReference(2135) ## WKID CODE 
     # Make the XY event layer...
    arcpy.MakeXYEventLayer_management(in_table, x_coords, y_coords, out_layer, spRef)
    # Save to a layer file
    arcpy.SaveToLayerFile_management(out_layer, saved_layer)
    print "Paso 7: Terminado"

# def R():
#     print("Paso 7: Creando csv en formatos para r de todas las erupciones")
#     for erupcion in erupciones:
#         functions.dataSetCsvR(erupcion)
#     functions.centerCsvR()

def createTrend(erupcion):
    out_layer=erupcion+"_layer.lyr"
    ruta="C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/layers/"+erupcion+"/"+out_layer
    try:
        Trend= arcpy.sa.Trend(ruta, "Erupcion",  "156.569985104", "2","LINEAR")
        Trend.save("C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/layers/"+erupcion+"/trend")
    except:
        print "Numero insuficiente de puntos en "+erupcion
    print "Paso 8: Terminado"
    
        
def extractingValuesTrend(erupcion):
    env.workspace="C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/layers/"+erupcion
    out_layer=erupcion+"_layer"
    # try:
    #     arcpy.gp.ExtractMultiValuesToPoints_sa(out_layer, "trend trend", "NONE")
    # except:
    #     print erupcion
    arcpy.gp.ExtractMultiValuesToPoints_sa(out_layer, "trend trend", "NONE")
    
    print "Paso 9: Terminado"

def addFieldRes(erupcion):
    env.workspace="C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/layers/"+erupcion
    out_layer=erupcion+"_layer.lyr"
    try:
        arcpy.AddField_management(out_layer, "res", "FLOAT", "", "", "", "", "NULLABLE","NON_REQUIRED","")
    except:
        print erupcion
    print "Paso 10: Terminado"
def calculateFieldRes(erupcion):
    env.workspace="C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/layers/"+erupcion
    out_layer=erupcion+"_layer.lyr"
    # try:
    #     arcpy.CalculateField_management(out_layer, "res", "[Erupcion]-[trend]", "VB", "")
    # except:
    #     print erupcion
    arcpy.CalculateField_management(out_layer, "res", "[Erupcion]-[trend]", "VB", "")
    print "Paso 11: Terminado"

def rasterRes2(erupcion):
    print "creando raster de residuos"
    env.workspace="C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/layers/"+erupcion
    out_layer=erupcion+"_layer.lyr"
    try:
        arcpy.gp.Idw_sa(out_layer, "res", "C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/layers/"+erupcion+"/modeloResiduos", "156.569985104", "2", "VARIABLE 12", "")
    except:
        print erupcion
def isopacas(erupcion):
    print "creando las isopacas"
    env.workspace="C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/layers/"+erupcion
    out_layer=erupcion+"_layer.lyr"
    try:
        arcpy.gp.RasterCalculator_sa('"trend2" + "modeloResiduos"', "C:/OneDrive - Universidad de Los Andes/[Student Thesis]/Tesistas 2019-2/Humberto Ariza/isopacas")
    except:
        print erupcion
def isopacasValue(erupcion):
    print "Calculando el valor de las isopacas"
    env.workspace="C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/layers/"+erupcion
    out_layer=erupcion+"_layer.lyr"
    try:
        arcpy.gp.ExtractMultiValuesToPoints_sa(out_layer, "isopacas isopacasValue", "NONE")
    except:
        print erupcion






######################## Segunda seccion
def getAreas(erupcion):
    datos=[]
    env.workspace="C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/layers/"+erupcion
    in_layer="AllIsopacs.lyr"
    arcpy.ConvertTableToCsvFile_roads(in_layer, "isopacas", "COMMA")

getAreas("XXVI_(Shawcroft)")