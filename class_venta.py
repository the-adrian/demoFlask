#-*- coding: utf-8 -*-
from os import sysconf

__author__ = 'aramirez'

import sys
import MySQLdb
import datetime

"""
    * Investigar como añadir el socket a la página web
"""

values=[]
check_sum = 0
#trama = sys.argv[1]
def main():
    check_sum_cal = 0
    trama = '\x02AC10TX1241213172|1|2014-02-03|18:02:00|299|0|3.00|1|3.00|10.00|M,10.00,1|M,2.0,1;M,5.0,1|1554\x03'
    if trama.find('\x02') != 0 or trama.find('\x03') != len(trama) - 1:
        print "error con el inicio y fin de cadena"
    else:
        trama = trama[1:-1] # remove byte to start and end
        check_sum = trama[len(trama)-4:] # get check sum of string
        check_sum = int(check_sum.lower(),16 )
        trama =  trama[:-4] # remove check sum

        for letra in trama:
            check_sum_cal += ord(letra)

        if check_sum_cal != check_sum:
            print "Error con el check sum"
        else:
            trama = trama[:-1]
            values = trama.split('|')

            #Asignacion de los elementos de la trama
            No_serie = values[0]
            turno = values[1]
            fecha = datetime.datetime.strptime(values[2], '%Y-%m-%d').date()
            hora = datetime.datetime.strptime(values[3], '%H:%M:%S').time()
            ticket = values[4]
            No_detalle = values[5]
            tarifa = values[6]
            multiplicador = values[7]
            total =  values[8]
            deposito = values[9]
            ingreso = values[10]
            if len(values) == 12:
                cambio =  values[11]


            query = "INSERT INTO panelcat(shiftno, serialnumber) VALUES('"+ str(turno)+"', '"+ str(No_serie)+"');"

            query2 = "INERT INTO panelshifthead(shiftno) VALUES('"+str(turno)+"');"

            query3 = "INSERT INTO servicesdetail(rate,multipler, cost) VALUES(" \
                     "'"+str(tarifa)+"', " \
                     "'"+str(multiplicador)+"'," \
                     " '"+str(total)+"');"
            query4 = "INSERT INTO panelservices(cost, deposit, ticket, datasell, timeshell, localshift) " \
                     "VALUES('"+str(total)+"'," \
                             " '"+str(deposito)+"', " \
                             "'"+str(ticket)+"', " \
                             "'"+str(fecha)+"', " \
                             "'"+str(hora)+"', " \
                             "'"+str(turno)+"');"
            print query
            print query2
            print query3
            print query4
            separate_deposit(ingreso)

def checksum_calc(str):
    response = 0
    for letra in str:
        response += ord(letra)
    return response


def separate_deposit(deposit):
    deposit = deposit.split(';')
    for elements in deposit:
        elements = elements.split(',')
        deposit_values = []
        for i in elements:
            deposit_values.append(i)
        amount = float(deposit_values[1]) * float(deposit_values[2])
        query5 = "INSERT INTO panel_shift_det_den(denomination, typecurr, quantity, amount) " \
                     "VALUES('"+str(deposit_values[1])+"'," \
                             " '"+str(deposit_values[0])+"', " \
                             "'"+str(deposit_values[2])+"', " \
                             "'"+str(amount)+"');"
        print query5
    return


if __name__ == '__main__':
    main()
