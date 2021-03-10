import csv
import os
rutaCSDBSCAN_SCP = '/Users/nicolas.caselli/GDrive/PUCV/PhD/Papers/Self-Adaptive-CucoSearch_DBSCAN/Test Estadístico/Datos_Test_CSDBSCAN/'
rutaArchivoTest = "/Users/nicolas.caselli/GDrive/PUCV/PhD/Papers/Self-Adaptive-CucoSearch_DBSCAN/Test Estadístico/FinalTest/"

with open('Resultados_CS_familias_Fuertes_n50_pa0.35.csv', newline='') as File:
    reader = csv.reader(File)
    names = next(reader)#leemos el encabezado del csv

    for row in reader:
        print(row)
        archivoTest = open(rutaArchivoTest+row[0]+".txt", 'a')
        archivoTest.write(row[2]+'\n')
    archivoTest.close()
File.close()

with os.scandir(rutaArchivoTest) as archivosTests: #recorremos los archivos de test
    print(archivosTests)
    for instancia in archivosTests: #para cada uno de ellos, le agregamos los de csdbscan
        print(instancia.name)
        archivoTest = open(instancia, 'a')

        if "410" in instancia.name:
            # abrimos el archivo CSDBSCAN_410
            archivoCSDBSCAN = open(rutaCSDBSCAN_SCP+"CSDBSCAN_410", 'r')
            archivoTest.write('\n') #Agregamos el salto de línea que necesita el test estadístico entre poblaciones
            for linea in archivoCSDBSCAN:
                archivoTest.write(linea)
            archivoCSDBSCAN.close()
        elif "510" in instancia.name:
            # abrimos el archivo CSDBSCAN_510
            archivoCSDBSCAN = open(rutaCSDBSCAN_SCP+"CSDBSCAN_510", 'r')
            archivoTest.write('\n')
            for linea in archivoCSDBSCAN:
                archivoTest.write(linea)
            archivoCSDBSCAN.close()
        elif "65" in instancia.name:
            # abrimos el archivo CSDBSCAN_65
            archivoCSDBSCAN = open(rutaCSDBSCAN_SCP+"CSDBSCAN_65", 'r')
            archivoTest.write('\n')
            for linea in archivoCSDBSCAN:
                archivoTest.write(linea)
            archivoCSDBSCAN.close()
        elif "a5" in instancia.name:
            # abrimos el archivo CSDBSCAN_a5
            archivoCSDBSCAN = open(rutaCSDBSCAN_SCP + "CSDBSCAN_a5", 'r')
            archivoTest.write('\n')
            for linea in archivoCSDBSCAN:
                archivoTest.write(linea)
            archivoCSDBSCAN.close()
        elif "b5" in instancia.name:
        # abrimos el archivo CSDBSCAN_b5
            archivoCSDBSCAN = open(rutaCSDBSCAN_SCP + "CSDBSCAN_b5", 'r')
            archivoTest.write('\n')
            for linea in archivoCSDBSCAN:
                archivoTest.write(linea)
            archivoCSDBSCAN.close()
        elif "c5" in instancia.name:
        # abrimos el archivo CSDBSCAN_c5
            archivoCSDBSCAN = open(rutaCSDBSCAN_SCP + "CSDBSCAN_c5", 'r')
            archivoTest.write('\n')
            for linea in archivoCSDBSCAN:
                archivoTest.write(linea)
            archivoCSDBSCAN.close()
        elif "d5" in instancia.name:
            # abrimos el archivo CSDBSCAN_d5
            archivoCSDBSCAN = open(rutaCSDBSCAN_SCP + "CSDBSCAN_d5", 'r')
            archivoTest.write('\n')
            for linea in archivoCSDBSCAN:
                archivoTest.write(linea)
            archivoCSDBSCAN.close()
        elif "e5" in instancia.name:
            # abrimos el archivo CSDBSCAN_e5
            archivoCSDBSCAN = open(rutaCSDBSCAN_SCP + "CSDBSCAN_e5", 'r')
            archivoTest.write('\n')
            for linea in archivoCSDBSCAN:
                archivoTest.write(linea)
            archivoCSDBSCAN.close()
        elif "f5" in instancia.name:
            # abrimos el archivo CSDBSCAN_f5
            archivoCSDBSCAN = open(rutaCSDBSCAN_SCP + "CSDBSCAN_f5", 'r')
            archivoTest.write('\n')
            for linea in archivoCSDBSCAN:
                archivoTest.write(linea)
            archivoCSDBSCAN.close()
        elif "g5" in instancia.name:
            # abrimos el archivo CSDBSCAN_g5
            archivoCSDBSCAN = open(rutaCSDBSCAN_SCP + "CSDBSCAN_g5", 'r')
            archivoTest.write('\n')
            for linea in archivoCSDBSCAN:
                archivoTest.write(linea)
            archivoCSDBSCAN.close()
        elif "h5" in instancia.name:
            # abrimos el archivo CSDBSCAN_h5
            print(instancia)
            archivoCSDBSCAN = open(rutaCSDBSCAN_SCP + "CSDBSCAN_h5", 'r')
            print(rutaCSDBSCAN_SCP+"CSDBSCAN_h5")
            archivoTest.write('\n')
            for linea in archivoCSDBSCAN:
                print(linea)
                archivoTest.write(linea)
            archivoCSDBSCAN.close()
        archivoTest.close()

''' 
En este bloque ejecutaremos el tes estadístico de cada archivo (instancia
'''
#cagamo... no hay pa mac, solo para windows


