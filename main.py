# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import mysql.connector
import os



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    
    cnx = mysql.connector.connect(user='root', password='ch@mpuquen',
                                  host='127.0.0.1',
                                  database='basic_cs_scp')
    cursor = cnx.cursor()

    ruta = '/Users/nicolas.caselli/GDrive/PUCV/PhD/Java/Bat_Metaheuristic/BAT_MH/resources/output'
    with os.scandir(ruta) as archivos:
        for file in archivos:
            print(file.name)
            if os.path.splitext(file)[1] == '.txt':
                linea = 1
                fArchivo = open(file, 'r')
                for lineaTxt in fArchivo:

                    if linea < 3: #avanzamos 2 líneas para quitar las cabeceras de los archivos
                        #print(lineaTxt)
                        linea+=1
                    else:
                        lineaLimpia = lineaTxt.replace(' ', '') #quitamos los espacios de la línea leída
                        lineaLimpia = lineaLimpia.replace('.txt', '') #quitamos el .txt de la instancia
                        lineaLimpia = lineaLimpia.replace(',', '.') #reemplazamos las , por . para dar formato a decimal
                        lineaLimpia = lineaLimpia.split(sep='|') #separamos por pipe y dejar datos en lista.
                        #print(linea-2, lineaLimpia[1], lineaLimpia[2],lineaLimpia[3], lineaLimpia[4], lineaLimpia[5],lineaLimpia[6], lineaLimpia[7], lineaLimpia[8])
                        dataInsert = {'instancia': lineaLimpia[1],
                                      'ejecucion': linea - 2,
                                      'nidos': lineaLimpia[2],
                                      'alfa': lineaLimpia[3],
                                      'probAbandono': lineaLimpia[4],
                                      'iteraciones': lineaLimpia[5],
                                      'seed': lineaLimpia[6],
                                      'fit': lineaLimpia[7],
                                      'time': lineaLimpia[8]}
                        cursor.execute(
                            "insert into mscp  (instancia, ejecucion, nidos, alfa, probAbandono, iteraciones, seed, fit, "
                            "time) values (%(instancia)s, %(ejecucion)s, %(nidos)s, %(alfa)s, %(probAbandono)s, %(iteraciones)s, %(seed)s, %(fit)s, %(time)s)", dataInsert)

                        cnx.commit()
                        linea +=1
                fArchivo.close()
        cursor.close()
        cnx.close()
