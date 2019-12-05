#Importando datos
import pandas
import matplotlib.pyplot as plt
import numpy as np
data = pandas.read_excel('./data/data.xlsx')

Fconversion=10
#Funciones para el procesamiento de datos
def freqVSthickness(erupcion):
    datos=[]
    for dato in data[erupcion]:
        if(dato != -1):
            datos.append(dato*Fconversion)
    plt.figure()
    plt.hist(datos,15,
         histtype='bar',
         facecolor='b',
         edgecolor='k',
         alpha=0.5)
    plt.grid()
    plt.title('Histograma '+erupcion)
    plt.xlabel('Thickness(mm)')
    plt.ylabel('Frequency')
    plt.savefig('./generated/histograms/freqvsthickness/'+erupcion)
    plt.close()
def freqVSlogThickness(erupcion):
    datos=[]
    for dato in data[erupcion]:
        if(dato != -1):
            if(dato==0):
                dato=1
            datos.append(np.log(dato*Fconversion))
    plt.figure()
    plt.hist(datos,15,
         histtype='bar',
         facecolor='b',
         edgecolor='k',
         alpha=0.5)
    plt.grid()
    plt.title('Histograma '+erupcion)
    plt.xlabel('Log Thickness(mm)')
    plt.ylabel('Frequency')
    plt.savefig('./generated/histograms/freqvsthickness/'+'LOG'+erupcion)
    plt.close()

def logThicknessVSdistance(erupcion):
    datos=[]
    distancias = []
    for i in range(0,len(data[erupcion])):
        if(data[erupcion][i] != -1 and data[erupcion][i] != 0):
            datos.append(np.log(data[erupcion][i]*Fconversion))
            distancias.append(data['Vent Distance(km)'][i]*1000)
    plt.figure()
    plt.scatter(distancias,datos,marker='o')
    plt.title('Scatter '+erupcion)
    plt.ylabel('Log Thickness(mm)')
    plt.xlabel('Distance (m)')
    plt.grid()
    plt.savefig('./generated/scatters/logvsdistance/'+erupcion)
    plt.close()


def dataSetByEruptionClean(erupcion):
    ### Se crea un arreglo por la erupcion entrante con las coordenadas en utm y el espesor diferente de -1 y 0
    datos=[]
    for i in range(0,len(data[erupcion])):
        if(data[erupcion][i] != -1 and data[erupcion][i] != 0):
            datos.append([data['UTM X'][i],data['UTM Y'][i],float(data[erupcion][i]*Fconversion)])
    return datos    

def dataSetByEruptionLimits(erupcion):
    ### Se crea un arreglo por la erupcion entrante con las coordenadas en utm y el espesor diferente de -1 y 0
    datos=[]
    for i in range(0,len(data[erupcion])):
        if( data[erupcion][i] == 0):
            datos.append([data['UTM X'][i],data['UTM Y'][i],float(data[erupcion][i]*Fconversion)])
    return datos    
def dataSetByEruptionEroded(erupcion):
    ### Se crea un arreglo por la erupcion entrante con las coordenadas en utm y el espesor diferente de -1 y 0
    datos=[]
    for i in range(0,len(data[erupcion])):
        if( data[erupcion][i] == -1):
            datos.append([data['UTM X'][i],data['UTM Y'][i],float(data[erupcion][i]*Fconversion)])
    return datos    

################### FUNCIONES PARA R
def dataSetCsvR(erupcion):
    ### Se crea un arreglo por la erupcion entrante con las coordenadas en utm y el espesor diferente de -1 y 0
    x=[]
    y=[]
    rz=[]
    z=[]
    for i in range(0,len(data[erupcion])):
        if(data[erupcion][i] != -1 and data[erupcion][i] != 0):
            x.append(float(data['UTM X'][i]))
            y.append(float(data['UTM Y'][i]))
            rz.append(int(data[erupcion][i]*Fconversion))
            z.append(float(np.log(data[erupcion][i]*Fconversion)))

    csv=pandas.DataFrame({
        'z':z,
        'rz':rz,
        'y':y,
        'x':x
    })
    csv.to_csv('./generated/rdataset/'+erupcion+'.csv', sep=';', decimal='.', index=False,columns=['x','y','rz','z'])

def centerCsvR():
    x=[]
    y=[]
    x.append(float(376210.6899))
    y.append(float(5651036.9653))
    csv=pandas.DataFrame({
        'y':y,
        'x':x
    })
    csv.to_csv('./generated/rdataset/centro.csv', sep=';', decimal='.', encoding='utf-8', index=False,columns=['x','y'])
    return "OK"



isopacas=[
[150,416596750.801191449165344],
[100,401169559.084247231483459],
[350,50376733.844633340835571],
[200,186887769.673352152109146],
[250,74858090.411275669932365],
[300,57113546.753021314740181],
[750,681295.461159874219447],
[400,10142870.240830713883042],
[450,5331523.009431125596166],
[500,2967051.708727687597275],
[550,1941187.143049989826977],
[600,1404069.321680125780404],
[650,1066092.615677865222096],
[700,835808.8526997352018956],
[800,430773.330410041322466]
]
milimetros=isopacas[0,:][0]
plt.plot(isopacas[::][0],isopacas[::][1])
plt.show()
