# -*- coding:utf-8 -*-
__author__ = 'jbadillo'
__author__ = 'aramirez'

################################################
#                                              #
#   Clase para el apagado y prendido de luces  #
#                                              #
################################################

import flask
import flask.views
import socket

INITIAL_MODBUS = 0xFFFF
INITIAL_DF1 = 0x0000

RELAY01_ON  = "\x01\x06\x00\x00\x00\x01\x48\x0A"
RELAY01_OFF = "\x01\x05\x00\x00\x00\x00\xCD\xCA"
RELAY02_ON  = "\x01\x06\x00\x01\x00\x01\x19\xCA"
RELAY02_OFF = "\x01\x05\x00\x01\x00\x00\x9C\x0A"
RELAY03_ON  = "\x01\x06\x00\x02\x00\x01\xE9\xCA"
RELAY03_OFF = "\x01\x05\x00\x02\x00\x00\x6C\x0A"
RELAY04_ON  = "\x01\x06\x00\x03\x00\x01\xB8\x0A"
RELAY04_OFF = "\x01\x05\x00\x03\x00\x00\x8C\x0B"
RELAY05_ON  = "\x01\x06\x00\x04\x00\x01\x09\xCB"
RELAY05_OFF = "\x01\x05\x00\x04\x00\x00\xFF\x6A"
RELAY06_ON  = "\x01\x06\x00\x05\x00\x01\x58\x0B"
RELAY06_OFF = "\x01\x05\x00\x05\x00\x00\xDD\xCB"
RELAY07_ON  = "\x01\x06\x00\x06\x00\x01\xA8\x0B"
RELAY07_OFF = "\x01\x05\x00\x06\x00\x00\x2D\xCB"
RELAY08_ON  = "\x01\x06\x00\x07\x00\x01\xF9\xCB"
RELAY08_OFF = "\x01\x05\x00\x07\x00\x00\x7C\x0B"

TCP_IP = '192.168.0.88'
TCP_PORT = 8080
BUFFER_SIZE = 1024

class Ligths(object):
    def control(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(RELAY03_ON)
        data = s.recv(BUFFER_SIZE)

