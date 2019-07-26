'''Controle de Estoque Configurações'''
import time
import colors as color
import keyboard
import sqlalchemy as db
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists

# -------------------------------------------------------------
# Setup
# mapeando db
Base = declarative_base()
engine = None
session = None

# Definição Produto
class Product(Base):
        __tablename__ = 'products'

        id = db.Column(db.Integer, db.Sequence('product_id_seq'), primary_key=True)
        name = db.Column(db.String(255))
        model = db.Column(db.String(255))
        quantity = db.Column(db.Integer)

        def __repr__(self):
                return (f"<Product(id={self.id}, name={self.name}, model={self.model},"
                        f" quantity={self.quantity})>")

# -------------------------------------------------------------
# Apresenta o menu de opções
def welcome():
    x = input('{0}\n\n O que deseja fazer?\n\n{1}{2}   \
       0. Registrar Novo Produto\n   \
       1. Procurar Produto\n   \
       2. Adicionar Produto em Estoque\n   \
       3. Remover Produto de Estoque\n   \
       4. Listar Produtos\n   \
       5. Deletar Registro de Produto\n{1}'
       .format(color.B_blue, color.close, color.blue))
    if x == '0':
        print(f'\n{color.B_green}')
        print(f'-' * 65)
        print(f'{"Novo Produto":^65}')
        print(f'-' * 65)
        print(f'{color.close}')
        _newProduct()
    elif x == '1':
        print(f'\n{color.B_green}')
        print(f'-' * 65)
        print(f'{"Procurar Produto":^65}')
        print(f'-' * 65)
        print(f'{color.close}')
        prod = _searchProduct()
        if (prod != [] and prod is not None):
                prod_id = 'PD' + '%0*d' % (3, prod[0].id)
                print(f'\n{"Id: ":<12}{prod_id}\n{"Nome: ":<12}{prod[0].name}\n'
                      f'{"Marca: ":<12}{prod[0].model}\n{"Quantidade: ":<12}'
                      f'{prod[0].quantity}\n')
    elif x == '2':
        print(f'\n{color.B_green}')
        print(f'-' * 65)
        print(f'{"Adicionar Produto em Estoque":^65}')
        print(f'-' * 65)
        print(f'{color.close}')
        _addProduct()
    elif x == '3':
        print(f'\n{color.B_green}')
        print(f'-' * 65)
        print(f'{"Remover Produto de Estoque":^65}')
        print(f'-' * 65)
        print(f'{color.close}')
        _removeProduct()
    elif x == '4':
        _listProduct()
    elif x == '5':
        print(f'\n{color.B_green}')
        print(f'-' * 65)
        print(f'{"Deletar Registro de Produto":^65}')
        print(f'-' * 65)
        print(f'{color.close}')
        _delProduct()
    else:
        print('{}\n Número Inválido!!!\n{}'.format(color.B_red, color.close))
        time.sleep(1)
        welcome()

# -------------------------------------------------------------
# voltar ao menu, ou sair do programa
def waitCommand():
    print('{}\n\n\n Aperte Enter para continuar, ou ESC para sair...\n\n{}\n'
          .format(color.B_green, color.close))
    while True:
        try:
            if keyboard.is_pressed('ENTER'):
                break
            if keyboard.is_pressed('ESC'):
                print("{}\n Saindo...\n{}".format(color.B_red, color.close))
                time.sleep(1)
                exit(0)
        except:
            break

# -------------------------------------------------------------
# Procura o produto no servidor
def _searchProduct():
    instance = None
    while True:
        input_id = input('{}\n Qual é o ID do produto?\n{}'
                         .format(color.B_blue, color.close))
        if (len(input_id) == 5) and (input_id[:2].upper() == 'PD'):
            try:
                input_id = int(input_id[2:])
                instance = session.query(Product).filter(Product.id == input_id).all()
                if instance == []:
                        print('{}\n Produto não encontrado!\n{}'
                              .format(color.B_red, color.close))
                return instance
                break
            except:
                print('{}\n ID Inválido!!! Exemplo de ID: PD000\n{}'
                      .format(color.B_red, color.close))

        else:
            print('{}\n ID Inválido!!! Exemplo de ID: PD000\n{}'
                  .format(color.B_red, color.close))

# -------------------------------------------------------------
# Registra novo produto
def _newProduct():
    name = input('{}\n Digite o nome do produto:\n{}'
                 .format(color.B_blue, color.close)).capitalize()
    model = input('{}\n Digite a marca do produto:\n{}'
                  .format(color.B_blue, color.close)).capitalize()
    instance = session.query(Product).filter(Product.name == name)\
                      .filter(Product.model == model).all()
    if instance != []:
        print('{}\n Produto já registrado!!!\n{}'
              .format(color.B_red, color.close))

    else:
        quantity = input('{}\n Digite a quantidade do produto registrado:\n{}'
                         .format(color.B_blue, color.close))
        while not(isinstance(quantity, int)):
            try:
                quantity = int(quantity)
            except:
                print('{}\n Número Inválido!!!\n{}'
                      .format(color.B_red, color.close))
                quantity = input('{}\n Digite a quantidade do produto '
                                 'registrado novamente:\n{}'
                                 .format(color.B_blue, color.close))
        try:
            prod = Product(name=name, model=model, quantity=quantity)
            session.add(prod)
            instance = session.query(Product).filter(Product.name == name)\
                              .filter(Product.model == model).all()
            prod_id = 'PD' + '%0*d' % (3, instance[0].id)
            session.commit()
            print ('{0}\n Produto registrado com sucesso!\n ID do produto = {2}{1}'
                   .format(color.B_green, color.close, prod_id))
        except:
            print('{}\n Ocorreu um erro ao registrar o produto.\n{}'
                  .format(color.B_red, color.close))

# -------------------------------------------------------------
# Deletar registro de produto
def _delProduct():
        prod = _searchProduct()
        if (prod != [] and prod is not None):
            prod_id = 'PD' + '%0*d' % (3, prod[0].id)
            print(f'\n{"Id: ":<12}{prod_id}\n{"Nome: ":<12}{prod[0].name}\n'
                  f'{"Marca: ":<12}{prod[0].model}\n{"Quantidade: ":<12}'
                  f'{prod[0].quantity}\n')
            while True:
                comand = input(f'{color.B_red}\nDeseja deletar o produto? [S/N]'
                      f'\n{color.close}')
                if comand.upper() == 'S':
                        try:
                                session.delete(prod[0])
                                session.commit()
                                print ('{0}\n Produto deletado com sucesso!\n ID do'
                                       ' produto = {2}{1}'
                                       .format(color.B_green, color.close, prod_id))
                                break
                        except:
                                print('{}\n Ocorreu um erro ao deletar produto.\n{}'
                                      .format(color.B_red, color.close))
                                break
                if comand.upper() == 'N':
                        break
                
#  -------------------------------------------------------------
# Adiciona quantidade de Produto
def _addProduct():
    prod = _searchProduct()
    if (prod != []) and (prod != None):
        add_quantity = input('{3}\n Existem {2} unidades de {0} da {1}.\n '
                              'Deseja adicionar quantas unidades?\n{4}'
                              .format(prod[0].name, prod[0].model,
                                      prod[0].quantity, color.B_blue,
                                      color.close))

        # Verifica se add_quantity_é inteiro
        while not(isinstance(add_quantity, int)):
            try:
                add_quantity = int(add_quantity)
            except:
                print('{}\n Número Inválido!!!\n{}'
                      .format(color.B_red, color.close))
                add_quantity = input('{2}\n Deseja adicionar quantas unidades de '
                                     '{0} da {1} ?\n{3}'.format(prod[0].name,
                                                                prod[0].model,
                                                                color.B_blue,
                                                                color.close))
    try:
        prod[0].quantity = prod[0].quantity + add_quantity
        session.commit()
        print ('{0}\n Produto adicionado em estoque com sucesso!\n Quantidade de {2}'
               'da {3} no estoque: {4}{1}'.format(color.B_green, color.close,
                                                  prod[0].name, prod[0].model,
                                                  prod[0].quantity))
    except:
        print('{}\n Ocorreu um erro ao registrar dados.\n{}'
              .format(color.B_red, color.close))
        
# -------------------------------------------------------------
# Remove quantidade de Produto
def _removeProduct():
    prod = _searchProduct()
    if (prod != []) and (prod != None):
        rm_quantity = input('{3}\n Existem {2} unidades de {0} da {1}.\n '
                              'Deseja remover quantas unidades?\n{4}'
                              .format(prod[0].name, prod[0].model,
                                      prod[0].quantity, color.B_blue,
                                      color.close))

        # Verifica se add_quantity_é inteiro e se existe numero em estoque
        while True:
            while not(isinstance(rm_quantity, int)):
                try:
                    rm_quantity = int(rm_quantity)
                except:
                    print('{}\n Número Inválido!!!\n{}'
                          .format(color.B_red, color.close))
                    rm_quantity = input('{2}\n Deseja remover quantas unidades de '
                                        '{0} da {1} ?\n{3}'.format(prod[0].name,
                                                                   prod[0].model,
                                                                   color.B_blue,
                                                                   color.close))
            if (rm_quantity <= prod[0].quantity):
                break
            else:
                print('{0}\n Não há unidades suficientes no estoque!!!\n'
                      ' Existem {2} unidades no estoque.{1}'
                      .format(color.B_red, color.close, prod[0].quantity))
                rm_quantity = input('{2}\n Deseja remover quantas unidades de {0} da '
                                    '{1} ?\n{3}'.format(prod[0].name, prod[0].model,
                                                        color.B_blue, color.close))
                
    try:
        prod[0].quantity = prod[0].quantity - rm_quantity
        session.commit()
        print ('{0}\n Produto removido de estoque com sucesso!\n Quantidade de {2}'
               ' da {3} no estoque: {4}{1}'.format(color.B_green, color.close,
                                                  prod[0].name, prod[0].model,
                                                  prod[0].quantity))
    except:
        print('{}\n Ocorreu um erro ao registrar dados.\n{}'
              .format(color.B_red, color.close))

# -------------------------------------------------------------
# Lista todos os produtos
def _listProduct():
    print(f'\n{color.B_green}')
    print(f'-' * 65)
    print(f'{"Lista de Produtos":^65}')
    print(f'-' * 65)
    print(f'{color.close}\n')
    print(f'-' * 65)
    print(f'{"ID":^10}|{"Nome":^20}|{"Marca":^20}|{"Qnt":^15}')
    print(f'-' * 65 )
    for instance in session.query(Product).order_by(Product.id):
        prod_id = 'PD' + '%0*d' % (3, instance.id)
        print (f'{prod_id:^10}|{instance.name:^20}|{instance.model:^20}|'
               f'{instance.quantity:^15}')
    print(f'-' * 65)

# -------------------------------------------------------------
# setup inicial db
def setup_db():
        _readConfigTxt()
        global engine
        global session
        engine = db.create_engine(adress_db)
        Session = sessionmaker(bind=engine)
        session = Session()

# -------------------------------------------------------------
# Ler config.txt
def _readConfigTxt():
    config_list = []
    configTxt = open("config.txt","r")
    for row in configTxt:
        config_list.append(row)
    configTxt.close()
    global adress_db
    adress_db = config_list[0]
