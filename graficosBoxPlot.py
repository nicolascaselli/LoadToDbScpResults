
import seaborn as sns
import matplotlib.pyplot as plt
from numpy.random import seed
from numpy.random import randn
import pandas as pnd

import os
rutaCSDBSCAN_SCP = '/Users/nicolas.caselli/GDrive/PUCV/PhD/Papers/Self-Adaptive-CucoSearch_DBSCAN/Test Estadístico/Datos_Test_CSDBSCAN/'
rutaArchivoTest = "/Users/nicolas.caselli/GDrive/PUCV/PhD/Papers/Self-Adaptive-CucoSearch_DBSCAN/Test Estadístico/FinalTest/"

with os.scandir(rutaArchivoTest) as archivosTests: #recorremos los archivos de test
    print(archivosTests)
    for instanciaTest in archivosTests: #para cada uno de ellos, le agregamos los de csdbscan
        if 'mscp' in instanciaTest.name:
            nombreInstancia = instanciaTest.name.replace('.txt','').replace('mscp','').upper()
            print(nombreInstancia)
            fileTest = open(rutaArchivoTest+instanciaTest.name, 'r')
            flagDato = False
            listCS = []
            listDBSCAN = []
            for linea in fileTest:
                if linea == '\n':
                    flagDato = True
                else:
                    if not flagDato:
                        #guardamos en CS
                        listCS.append(int(linea.replace('\n', '')))
                    else:
                        #guardamos en CSDBSCAN
                        listDBSCAN.append(int(linea.replace('\n', '')))
            fileTest.close()

            dicDatos = {"CS": listCS, "CSDBSCAN":listDBSCAN}
            print(dicDatos)
            print(len(dicDatos["CS"]))
            print(len(dicDatos["CSDBSCAN"]))

            sns.set_theme(style="whitegrid")
            df = pnd.DataFrame(data=dicDatos)  # generamos dataset para graficarlo
            #ax = sns.boxplot(data=df)  # Genera gráfico caja
            ax = sns.violinplot(data=df)
            plt.title(nombreInstancia)
            plt.xlabel("Algorithms")
            plt.ylabel("Execution Fit")
            plt.savefig(nombreInstancia+'_violin.pdf')  # Guarda gráfico en archivo
            plt.show()
            listCS.clear()
            listDBSCAN.clear()
            dicDatos.clear()

#tips = sns.load_dataset("tips")
#print(tips)
'''
sns.set_theme(style="whitegrid")

seed(2)
datos={"CS":30*randn(31), "CSDBSCAN":10*randn(31)}
print(datos)
df = pnd.DataFrame(data= datos) #generamos dataset para graficarlo
ax = sns.boxplot( data=df) #Genera gráfico
plt.title("chapalapachala")
plt.xlabel("Algorithms")
plt.ylabel("Execution Fit")
plt.savefig('ploting.pdf') #Guarda gráfico en archivo
plt.show()
'''