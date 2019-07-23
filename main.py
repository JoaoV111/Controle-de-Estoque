"""Inicia Programa Controle de Estoque"""
import config as cfg

print('{}\n\n\n----------------------------------\n\n    Controle de Estoque  V0.1\
 \n\n----------------------------------\n\n{}'.format('\x1b[1;32m', '\x1b[m'))

while True:
	cfg.welcome()
	cfg.waitCommand()
