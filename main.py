"""Inicia Programa Controle de Estoque"""
import config as cfg


cfg.setup_db()

print('\033[1;32m\n\n')
print(f'-' * 30)
print(f'\n{"Controle de Estoque  V0.3":^30}\n')
print(f'-' * 30)
print('\n\n\033[m')


while True:
    cfg.welcome()
    cfg.waitCommand()



      

     






