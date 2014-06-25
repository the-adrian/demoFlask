#-*- coding: utf-8 -*-
__author__ = 'aramirez'
import socket
import sys
import select
import time


IP = "192.168.0.206"
PUERTO = 3550
entrada = []
salida = []
conectado = False

print "Conectar a %s" % IP

socket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM ) # UDP

socket.bind(( '0.0.0.0', PUERTO ))

# Pone el socket en modo de no bloqueo,
# evitando poner a recv en bucle infinito si no hay datos en el buffer
socket.setblocking(0)

def conectar():
    intentos_conectar = 0
    salida = 'ok'
    sys.stdout.write('Conectando') #imprime sin salto de linea en consola

    while True:
        time.sleep(1)
        socket.sendto(salida, (IP, PUERTO))
        entrada = select.select([socket], [], [], 0.5)
        if intentos_conectar == 5:
            print "EL hots no esta disponible"
            socket.close()
            sys.exit(0)

        if entrada[0]:
            print "Conexión exitosa"
            socket.sendto(salida, (IP, PUERTO))
            return True
            break
        else:
            sys.stdout.write('.')
            sys.stdout.flush()
            intentos_conectar += 1

conectado =  conectar()

while conectado:
    time.sleep(1)
    """
    # Valida si se recibe captura desde el teclado
    HayDatosTeclado = select.select([sys.stdin],[],[],1)
    if HayDatosTeclado[0]:
        mensaje = sys.stdin.readline()
        print "Enviado: " + mensaje
        socket.sendto(mensaje, (IP, PUERTO))
    else:
    """
    socket.sendto('.', (IP, PUERTO))

    # Valida si recibe algo por el socket
    HayDatosSocket = select.select([socket],[],[],0.5)
    if HayDatosSocket[0]:
        Socketdata = socket.recv( 100 )
        if Socketdata == 'recv':
            Socketdata = '.'
            sys.stdout.write(Socketdata)
            sys.stdout.flush()
            socket.sendto('recv', (IP, PUERTO))
        else:
            sys.stdout.write(Socketdata)
            socket.sendto('recv', (IP, PUERTO))
            sys.stdout.flush()
    else:
        print "Se perdio la conexión"		#
        print "Restableciendo conexión"		#
        conectado = False			        #
        for intentos in range(0,5):	    	#  Intenta Conectarse de nuevo con el socket
            conectado = conectar()		    #
            if conectado:			        #
                break			            #
        if not conectado:
            print "EL SERVIDOR NO ESTA DISPONIBLE"
            sys.exit(0)
    HayDatosTeclado = []
    HayDatosSocket = []
