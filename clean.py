import shutil
import os
erupciones=['Okupata_Pourahu',
'XXIX_(Akurangi)_compiled',
'XXVII_(Oruamatua)_compiled',
'XXVI_(Shawcroft)',
'IX_(Mangatoetoenui)_compiled']

def cleanArcmapGdbs():
    try:
        shutil.rmtree("C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/gdbs")

    except:
        print('Problema eliminando gdbs')
    try:
         os.makedirs("C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/gdbs")
    except:
        print "Problema creando carpeta clean arcmaplayers"

def cleanArcmapLayers():
    try:
        shutil.rmtree("C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/layers")

    except:
        print('Problema Clean Arcmap layers')
    try:
         os.makedirs("C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/layers")
    except:
        print "Problema creando carpeta clean arcmaplayers"
def cleanRDataset():
    try:
        shutil.rmtree("C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/generated/rdataset")
    except:
        print('Problema eliminando los datasets de R')   
    try:    
        os.makedirs("C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/generated/rdataset")
    except:
        print('Problema creando la carpeta de datasets') 

def cleanScatters():
    try:
        shutil.rmtree("C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/generated/scatters")
    except:
        print('Problema eliminando la carpeta de scatters')
    try:
        os.makedirs("C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/generated/scatters")
    except:
        print('Problema creando la carpeta Scatter')
    try:
        os.makedirs("C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/generated/scatters/logvsdistance")
    except:
        print('OK')

def cleanHistograms():
    try:
        shutil.rmtree("C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/generated/histograms")
    except:
        print('Problema eliminando histogramas')   
    try:  
        os.makedirs("C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/generated/histograms")
        os.makedirs("C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/generated/histograms/freqvsthickness")
    except:
        print('Problema creando carpeta de histogramas')   
def createFolderLayers():
    for erupcion in erupciones:
        try:    
            os.makedirs("C:/Users/Humberto Ariza/OneDrive - Universidad de Los Andes/Tesis VF/code/arcmap/layers/"+erupcion)
        except:
            print('Problema creando las carpetas de los layers') 