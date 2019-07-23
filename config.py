# -*- coding: utf-8 -*-
'''Controle de Estoque Configurações'''

import time
import colors as color
import sys
import keyboard

# Definição Produto
class Product:
    def __init__(self, name, model, quantity):
        self.name = name
        self.model = model
        self.qt = quantity


# Criando alguns produtos SOMENTE para teste
PD001 = Product('Presunto', 'Perdigão', 50)
PD002 = Product('Queijo', 'Perdigão', 20)
PD003 = Product('Calabresa', 'Perdigão', 5)
PD004 = Product('Peito de peru', 'Perdigão', 35)
PD005 = Product('Salame', 'Perdigão', 42)

DATA = {'PD001': PD001,
        'PD002': PD002,
        'PD003': PD003,
        'PD004': PD004,
        'PD005': PD005}


# -------------------------------------------------------------
# Apresenta o menu de opções
def welcome():
    x = input('{0}\n\n O que deseja fazer?\n\n{1}{2}   \
       0. Registrar Novo Produto\n   \
       1. Procurar Produto\n   \
       2. Adicionar Produto\n   \
       3. Remover Produto\n   \
       4. Listar Produtos\n{1}'.format(color.B_blue, color.close, color.blue))
    if x == '0':
        newProduct()
    elif x == '1':
        searchProduct()
    elif x == '2':
        addProduct()
    elif x == '3':
        removeProduct()
    elif x == '4':
        listProduct()
    else:
        print('{}\n Número Inválido!!!\n{}'.format(color.B_red, color.close))
        time.sleep(2)
        welcome()

# -------------------------------------------------------------
# voltar ao menu, ou sair do programa
def waitCommand():
    input('{}\n\n\n Aperte Enter para continuar, ou ESC para sair...\n\n{}'
          .format(color.B_green, color.close))
    while True:
        try:
            if keyboard.is_pressed('ENTER'):
                break
            if keyboard.is_pressed('Esc'):
                print("{}\n Saindo...\n{}".format(color.B_red, color.close))
                time.sleep(2)
                sys.exit(0)
        except:
            break


# -------------------------------------------------------------
# Procura o produto no servidor
def searchProduct():
    x = input('{}\n Qual é o ID do produto?\n{}'
              .format(color.B_blue, color.close))
    x = x[:2].upper() + x[2:]
    try:
        y = DATA[x]
        print('\n\n Id: {}\n Nome: {}\n Marca: {}\n Quantidade: {}'
              .format(x, y.name, y.model, y.qt))
    except:
        print('{}\n ID Inválido!!! Exemplo de ID: PD000\n{}'
              .format(color.B_red, color.close))
        searchProduct()

# -------------------------------------------------------------
# Registra novo produto
def newProduct():
    name = input('{}\n Digite o nome do produto:\n{}'
                 .format(color.B_blue, color.close)).capitalize()
    model = input('{}\n Digite a marca do produto:\n{}'
                  .format(color.B_blue, color.close)).capitalize()

    # verificar se produto já esta registrado
    stat = True
    for i in DATA.values():
        if (i.name == name) and (i.model == model):
            print('{}\n Produto já registrado!!!\n{}'
                  .format(color.B_red, color.close))
            stat = False

    if stat:
        quantity = input('{}\n Digite a quantidade do produto registrado:\n{}'
                         .format(color.B_blue, color.close))

        # verificar se quantity é numero int
        while not(isinstance(quantity, int)):
            try:
                quantity = int(quantity)
            except:
                print('{}\n Número Inválido!!!\n{}'
                      .format(color.B_red, color.close))
                quantity = input('{}\n Digite a quantidade do produto '
                                 'registrado novamente:\n{}'
                                 .format(color.B_blue, color.close))

        # Calcular proximo ID
        x = 0
        for i in DATA.keys():
            if int(i[3:]) > x:
                x = int(i[3:])

        x += 1
        newID = 'PD' + '%0*d' % (3, x)
        vars()[newID] = Product(name, model, quantity)
        DATA[newID] = vars()[newID]
        print ('{0}\n Produto registrado com sucesso!\n ID do produto = {2}{1}'
               .format(color.B_green, color.close, newID))

# -------------------------------------------------------------
# Adiciona Produto
def addProduct():
    Id = input('{}\n Digite o ID do produto:\n{}'
               .format(color.B_blue, color.close)).capitalize()
    Id = Id[:2].upper() + Id[2:]

    # verifica existencia do produto
    while Id not in DATA.keys():
        print('{}\n Produto inexistente!!!\n{}'
              .format(color.B_red, color.close))
        Id = input('{}\n Digite o ID do produto:\n{}'
                   .format(color.B_blue, color.close)).capitalize()
        Id = Id[:2].upper() + Id[2:]

    add_quantity = input('{3}\n Existem {2} unidades de {0} da {1}.\n Deseja '
                         'adicionar quantas unidades?\n{4}'
                         .format(DATA[Id].name, DATA[Id].model, DATA[Id].qt,
                                 color.B_blue, color.close))

    # Verifica se add_quantity_é inteiro
    while not(isinstance(add_quantity, int)):
        try:
            add_quantity = int(add_quantity)
        except:
            print('{}\n Número Inválido!!!\n{}'
                  .format(color.B_red, color.close))
            add_quantity = input('{2}\n Deseja adicionar quantas unidades de '
                                 '{0} da {1} ?\n{3}'.format(DATA[Id].name,
                                                            DATA[Id].model,
                                                            color.B_blue,
                                                            color.close))

    old_quantity = DATA[Id].qt
    DATA[Id].qt = old_quantity + add_quantity
    print ('{0}\n Produto adicionado com sucesso!\n Quantidade de {2} da {3} n'
           'o estoque: {4}{1}'.format(color.B_green, color.close,
                                      DATA[Id].name, DATA[Id].model,
                                      DATA[Id].qt))

# -------------------------------------------------------------
# Remove Produto
def removeProduct():
    Id = input('{}\n Digite o ID do produto:\n{}'
               .format(color.B_blue, color.close)).capitalize()
    Id = Id[:2].upper() + Id[2:]

    # verifica existencia do produto
    while Id not in DATA.keys():
        print('{}\n Produto inexistente!!!\n{}'
              .format(color.B_red, color.close))
        Id = input('{}\n Digite o ID do produto:\n{}'
                   .format(color.B_blue, color.close)).capitalize()
        Id = Id[:2].upper() + Id[2:]

    add_quantity = input('{3}\n Existem {2} unidades de {0} da {1}.\n Deseja r'
                         'emover quantas unidades?\n{4}'.format(DATA[Id].name,
                                                                DATA[Id].model,
                                                                DATA[Id].qt,
                                                                color.B_blue,
                                                                color.close))

    # Verifica se add_quantity_é inteiro e menor que estoque
    while True:
        while not(isinstance(add_quantity, int)):
            try:
                add_quantity = int(add_quantity)

            except:
                print('{}\n Número Inválido!!!\n{}'
                      .format(color.B_red, color.close))
                add_quantity = input('{2}\n Deseja remover quantas unidades de'
                                     ' {0} da {1} ?\n{3}'.format(DATA[Id].name,
                                                                 DATA[Id].model,
                                                                 color.B_blue,
                                                                 color.close))

        if (DATA[Id].qt >= add_quantity):
            break

        print('{}\n Não há unidades suficientes no estoque!!!\n{}'
              .format(color.B_red, color.close))
        add_quantity = input('{2}\n Deseja remover quantas unidades de {0} da '
                             '{1} ?\n{3}'.format(DATA[Id].name, DATA[Id].model,
                                                 color.B_blue, color.close))

    old_quantity = DATA[Id].qt
    DATA[Id].qt = old_quantity - add_quantity
    print ('{0}\n Produto removido com sucesso!\n Quantidade de {2} da {3} no '
           'estoque: {4}{1}'.format(color.B_green, color.close, DATA[Id].name,
                                    DATA[Id].model, DATA[Id].qt))

# -------------------------------------------------------------
# Lista todos os produtos
def listProduct():
    print('{}\n\n ID/ Nome/ Marca/ Quantidade\n{}'
          .format(color.B_white, color.close))
    for x, y in DATA.items():
        print (' {}/ {}/ {}/ {}\n'.format(x, y.name, y.model, y.qt))
