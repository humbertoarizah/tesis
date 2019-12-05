import numpy as np
import pandas as p
import matplotlib.pylab as plt
import scipy
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

""" Modulo para plotear y analizar la grafica logT vs A**(1/2)"""

# T=[
#     # 20,10,
# 7,6,4,3,2,1,0.5,0.25,0.1,0.05]
# A=[
#     # 200,460,
# 640,840,2500,7600,12800,30000,48000,79000,118000,167000]

T=[80,75,70,65,60,55,50,45,40,35,30,25,20,15,10]
A=[
430773.330410041322466,
681295.461159874219447,
835808.852699735201895,
1066092.615677865222096,
1404069.321680125780404,
1941187.143049989826977,
2967051.708727687597275,
5331523.009431125596166,
10142870.240830713883042,
50376733.844633340835571,
57113546.753021314740181,
74858090.411275669932365,
186887769.673352152109146,
393732168.999770998954773,
461309360.957475304603577]
squareA=[]
for i in range(len(A)):
    squareA.append(np.sqrt(A[i]/1e6))
    # squareA.append(np.sqrt(A[i]))

def calculo_pendiente(y2,y1,x2,x1):
    return (np.log(y2)-np.log(y1))/(x2-x1)

def calculo_pendientes(T,squareA):
    pendientes=[]
    indexes=[]
    for i in range(len(T)-1):
        pendientes.append(calculo_pendiente(T[i+1],T[i],squareA[i+1],squareA[i]))
    return pendientes

def calcularbrake(pendientes, segmentos):
    if(segmentos==0):
        return [0]
    diferencias=[]
    breaks=[]
    indexes=[]
    for i in range(len(pendientes)-1):
        diferencia=abs(pendientes[i+1])-abs(pendientes[i])
        diferencias.append(diferencia)

    while (len(breaks)<int(segmentos)):
        for j in range(len(diferencias)):
            if(segmentos<2):
               if(max(diferencias)==diferencias[j]): 
                    if(j!=0):
                        indexes.append(j+len(breaks)-2)
                        breaks.append(diferencias[j]-2)
                        diferencias.pop(j)
                        break
                    else:
                        indexes.append(j+len(breaks))
                        breaks.append(diferencias[j])
                        diferencias.pop(j)
                        break
            if(segmentos==2):
                if(max(diferencias)==diferencias[j]): 
                    if(j!=0):
                        indexes.append(j+len(breaks)+1)
                        breaks.append(diferencias[j]+1)
                        diferencias.pop(j)
                        break
                    else:
                        diferencias.pop(j)
                        break
    return indexes


def calcularEcuacionGraficas():
    plt.semilogy(squareA,T,'b-o')
    plt.ylabel('Log (T(cm))')
    plt.xlabel('Distancia (Area Isopaca)½')
    plt.show()
    pendientes= calculo_pendientes(T,squareA)
    print('Cantidad de segmentos en la grafica:')
    segmentos=input()
    segmentos=int(segmentos)
    breaks=calcularbrake(pendientes,segmentos-1)
    print(breaks)
    positions=[]
    plt.figure()
    plt.plot(squareA,T,'b-o')
    plt.yscale('log')
    for i in range(len(breaks)):
        if(segmentos==1):
            plt.plot(squareA[breaks[i]+1],T[breaks[i]+1],'b-o')
            positions.append(squareA[breaks[i]+1])
        if(segmentos==2):
            if(i==0):
                plt.plot(squareA[breaks[i]],T[breaks[i]],'r-o')
                positions.append(squareA[breaks[i]])
            if(i==1):
                plt.plot(squareA[breaks[i]-1],T[breaks[i]-1],'r-o')
                positions.append(squareA[breaks[i]-1])

        if(segmentos==3):
            print(breaks)
            if(i==0):
                plt.plot(squareA[breaks[i]],T[breaks[i]],'r-o')
                positions.append(squareA[breaks[i]])
            if(i==1):
                plt.plot(squareA[breaks[i]],T[breaks[i]],'r-o')
                positions.append(squareA[breaks[i]])
            if(i==2):
                plt.plot(squareA[breaks[i]+3],T[breaks[i]+3],'r-o')
                positions.append(squareA[breaks[i]+3])
    plt.ylabel('Log (T(cm))')
    plt.xlabel('Distancia (Area Isopaca)½')
    plt.title('Cambios de pendiente Log T vs Area(km2)½')
    plt.show()
    plt.savefig('C:/Users/Humberto Ariza/Desktop/Tesis/Breaks')
    return segmentos,breaks,positions
def tendencia(Th,A,grade):
    z=np.polyfit(A,np.log(Th),grade)
    p=np.poly1d(z)
    return z[0],z[1]
def calculateVolumeBonadonna2005(T0, k,BS,n):
    V=2*T0[0]/(k[0]**2)+ 2*T0[0] *(((k[1]*BS[0])+1)/(k[1]**2)) - (((k[0]*BS[0])+1)/(k[0]**2)) *np.exp(-k[0]*BS[0]) + 2*T0[1] *  (((k[2]*BS[1])+1)/(k[2]**2)) - (((k[1]*BS[1])+1)/(k[1]**2)) *np.exp(-k[1]*BS[1])
    return V/1000000
def calculateVolume2Breaks(T0,k,BS,n):
    V=2*T0[0]/(k[0]**2) + 2*T0[0] *  (((k[1]*BS[0])+1)/(k[1]**2)) - (((k[0]*BS[0])+1)/(k[0]**2)) *np.exp(-k[0]*BS[0])
    return V/1000000
def calculateVolume1Break(T0,k):
    V=2*T0[0]/(k[0]**2)
    return V/100000

segmentos,breaks,positions=calcularEcuacionGraficas()
intervals=[]
for i in range(len(breaks)):
    if(breaks[i]==0):
        intervals.append([0,len(squareA)])
        break
    if(segmentos==2):
        intervals.append([0,breaks[i]])
        intervals.append([breaks[i],len(squareA)])
    else:
        if(i==0):
            intervals.append([0,breaks[i]])
        if(i==len(breaks)-1):
            intervals.append([breaks[i],len(squareA)])
        else:
            intervals.append([breaks[i],breaks[i+1]])


T0=[]
k=[]
BS=[squareA[8],squareA[12]]
plt.figure()
for i in range(len(intervals)):
    y=[]
    i1=intervals[i][0]
    i2=intervals[i][1]
    if(i>0):
        i1=intervals[i][0]-1
        i2=intervals[i][1]
    print('intervals:',i1,i2)
    m,b=tendencia(T[i1:i2],squareA[i1:i2],1)
    T0.append(np.exp(b))
    k.append(-m)
    for j in range(i1,i2):
        if(m*squareA[j]+b < 1):
            i2=j
            break
        y.append(m*squareA[j]+b)
    label='y='+str(round(m,3))+'x+'+str(round(np.exp(b),3))
    x=squareA[i1:i2]
    colors=['b-o','g-o','r-o']
    colors2=['b--','g--','r--']
    plt.plot(x,y,colors2[i],label=label)
    plt.plot(squareA[i1:i2],np.log(T[i1:i2]),colors[i])
    plt.yscale('log')
plt.ylabel('Log (T(cm))')
plt.xlabel('Distancia (Area Isopaca)½')
plt.title('Log T vs Area(km2)½')
plt.legend()
plt.savefig('C:/Users/Humberto Ariza/Desktop/Tesis/FitFinal')
plt.show()
print(T0,k,BS,segmentos)
# volume=calculateVolume1Break(T0,k)
# volume=calculateVolume2Breaks(T0,k,BS,segmentos)
volume=calculateVolumeBonadonna2005(T0,k,BS,segmentos)
print(volume)



