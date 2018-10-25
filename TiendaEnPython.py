import csv
import os

#hacer saltos para limpiar pantalla con dos opciones
def clear():
    os.system('cls')
    #m="\n"*50      #opcion 2



def titulo():
    print "      _____________________________________________________________________"
    print "      |                                   ____________________            |"
    print "      |                                   | NOMBRE1          |___________ |"
    print "      |        ******************         | NOMBRE2          |  EMPRESA  ||"
    print "      |         SISTEMA DE VENTAS         | NOMBRE3          |           ||"
    print "      |        ******************         |                  | EMPRESCORP||"
    print "      |  _________________________________|                  |           ||"
    print "      |  |  _    _           _    _    _  |   _ _  _ _  _ _  |   ______  ||"
    print "      |  | | |  | |  _____  | |  | |  | | |       ______     |   |  _ |  ||"
    print "      |  | |_|  |_|  | | |  |_|  |_|  |_| |       |  | |     |   |  | |  ||"
    print "      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"

        
def menu1():
    print "      ------------------------------------------------------------------"
    print "              <<<<<<<<<<          SISTEMA DE VENTAS          >>>>>>>>>> "
    print "      ------------------------------------------------------------------"
    print "                                                                        "
    print "      (1)COMPRAS                ||    ||    ||||     ||    |||||||||    "
    print "      (2)VENTAS                 ||    ||    || ||    ||    ||     ||    "
    print "      (3)CLIENTE                ||    ||    ||  ||   ||    |||||||||    "
    print "      (4)SALIR                  ||    ||    ||   ||  ||    ||           "
    print "                                ||    ||    ||    || ||    ||           "
    print "                                ||||||||    ||     ||||    ||           "
    print "                                                                        "
    print "                           PROYECTO - PYTHON                            "
    
def menu2():
    print "      ---------------------------------------------------------------------\n"
    print "                 <<<<<<<<<<         COMPRAS        >>>>>>>>>>";
    print "\n      ---------------------------------------------------------------------\n\n"
    print "                                                  "
    print "      (1)VER LOS PROVEEDORES               "
    print "               					 "
    print "      (2)REGRESAR AL MENU PRINCIPAL             "
    print "              					   "
    print "                 			        "
    print "                            	       "
    print "                                         PROYECTO - PYTHON "

def menu3():
    print "      ---------------------------------------------------------------------\n"
    print "                 <<<<<<<<<<         VENTAS        >>>>>>>>>>";
    print "\n      ---------------------------------------------------------------------\n\n"
    print "      (1)VENDER PRODUCTO              "
    print "                                        "
    print "      (2)VER VENTAS REALIZADAS            "
    print "                                      "
    print "      (3)SALIR          "
    print "                                    "
    print "                       "
    print "                                         PROYECTO - PYTHON "
 
def menu4():
    print "      ---------------------------------------------------------------------\n"
    print "                 <<<<<<<<<<         INVENTARIO        >>>>>>>>>>";
    print "\n      ---------------------------------------------------------------------\n\n"
    print "      (1)VER CODIGO DEL PRODUCTO              "
    print "                                        "
    print "      (2)VER PRODUCTO            "
    print "                                      "
    print "      (3)VER INVENTARIO          "
    print "                                    "
    print "      (4)SALIR                  "
    print "                                         PROYECTO - PYTHON "

def menu5():
    print "\n\n      ---------------------------------------------------------------------\n"
    print "              <<<<<<<<<<          CLIENTE            >>>>>>>>>>";
    print "\n      ---------------------------------------------------------------------\n\n"
    print "                                       "
    print "      (1)INGRESAR NOMBRE              "
    print "                                       "    
    print "      (2)MOSTRAR CLIENTE                 "
    print "                                       " 
    print "      (3)SALIR              "
    print "                                       "   
    print "                                         PROYECTO - PYTHON "
    
def mostrar_proveedor():
    print "Los proveedores son:"
    with open('proveedores.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(line)

def vender_producto():
    print "Ingres nombre del producto"
    with open("prod_vend.csv","r+") as f:
        writer = csv.writer(f)
        emp=raw_input()
        writer.writerow([emp])
        f.close()

def mostrar_producto():
    print "Los productos vendidos son:"
    with open("prod_vend.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(line)



def ingresar_cliente():
    print "Ingrese nombre del cliente: "
    with open("cliente.csv","r+") as f:
        writer = csv.writer(f)
        emp=raw_input()
        writer.writerow([emp])
        f.close()

def mostrar_cliente():
    print "Los clientes son:"
    with open("cliente.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(line)



while True:
    
    while True:
        titulo()
        menu1()
        valor=input("INGRESE UN NUMERO: ")
        os.system('cls')
        if valor == 1:
                os.system('cls')
                while True:
                    menu2()
                    valor=input("INGRESE UN NUMERO: ")
                    if valor == 1:
                        os.system('cls')
                        mostrar_proveedor()                  
                        valor=input("INGRESE 2 PARA SALIR: ")
                        os.system('cls')
                        break
                    elif valor == 2:
                        os.system('cls')
                        break
        elif valor == 2:
                os.system('cls')
                while True:
                    menu3()
                    valor=input("INGRESE UN NUMERO: ")
                    if valor == 1:
                        os.system('cls')
                        vender_producto()                 
                        valor=input("INGRESE 3 PARA SALIR: ")
                        os.system('cls')
                        break
                    elif valor == 2:     
                        os.system('cls')
                        mostrar_producto()                 
                        valor=input("INGRESE 3 PARA SALIR: ")
                        os.system('cls')
                        break
                    elif valor == 3:
                        os.system('cls')
                        break
        elif valor == 3:
                os.system('cls')
                while True:
                    menu5()
                    valor=input("INGRESE UN NUMERO: ")
                    if valor == 1:
                        os.system('cls')
                        ingresar_cliente()                  
                        valor=input("INGRESE 2 PARA SALIR: ")
                        os.system('cls')
                        break
                    elif valor == 2:     
                        os.system('cls')
                        mostrar_cliente()                 
                        valor=input("INGRESE 3 PARA SALIR: ")
                        os.system('cls')
                        break
                    elif valor == 3:
                        os.system('cls')
                        break
        elif valor == 4:
            break
