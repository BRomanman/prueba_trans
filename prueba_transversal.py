import numpy as np
import random
import statistics as st

trabajadores = ["Juan Perez", "maria garcia", "carlos lopez", "ana martinez", "pedro rodriguez", "laura hernandez", "miguel sanchez", "isabel gomez", "francisco diaz", "elena fernandez"] 
matriz_trabajadores= np.empty((10, 10), dtype=object)
opc = 0
aleatorio= random.randint(0,1)

def guardar_datos_en_txt():
    with open('trabajadores.txt', 'w') as file:
        trabajadores 
      
        


while opc != 5:

    opc = int(input("MENU\n1-asignar numeros aleatorios\nclasificar sueldos\n3-ver estadisticas\n4-reporte de sueldos\n5-salir\nDigita tu opcion: "))

    if opc == 1:
        print("***SUELDOS***")
        print("juan perez\nsueldo: ")
        print((random.randint(300000,2500000)))
        print("maria garcia\nsueldo: ")
        print((random.randint(300000,2500000)))
        print("carlos lopez\nsueldo: ")
        print((random.randint(300000,2500000)))
        print("ana martinez\nsueldo: ")
        print((random.randint(300000,2500000)))
        print("pedro rodriguez\nsueldo: ")
        print((random.randint(300000,2500000)))
        print("laura hernandez\nsueldo: ")
        print((random.randint(300000,2500000)))
        print("miguel sanchez\nsueldo: ")
        print((random.randint(300000,2500000)))
        print("isabel gomez\nsueldo: ")
        print((random.randint(300000,2500000)))
        print("francisco diaz\nsueldo: ")
        print((random.randint(300000,2500000)))
        print("elena fernandez\nsueldo: ")
        print((random.randint(300000,2500000)))
        
    
    elif opc == 2:
        print("***CLASIFICACION POR SUELDOS***")

    elif opc == 3:
        print("***estadisticas***")
    
    elif opc ==4:
        print("***reportes de sueldos***")
    
    elif opc ==5:
        guardar_datos_en_txt()
        print("fin de programa\nDesarrollado por Bastian Roman\nRut: 20958360-7")




    