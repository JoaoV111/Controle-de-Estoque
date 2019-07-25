import sqlalchemy as db
import pandas as pd

# conectando na database postgres
engine = db.create_engine('postgres://postgres:666@localhost')
connection = engine.connect()
connection.execute("commit")
connection.execute("controle_de_estoque_db")  # criando db controle de estoque
connection.close()

# conectando db controle de estoque
engine = db.create_engine('postgres://postgres:666@localhost/controle_de_estoque_db')
connection = engine.connect()
metadata = db.MetaData()

# criando tabela
product = db.Table('product', metadata,
              	   db.Column('Id', db.String(255), nullable=False),
                   db.Column('name', db.String(255), nullable=False),
                   db.Column('model', db.String(255), nullable=False),
                   db.Column('quantity', db.Integer())
                   )

metadata.create_all(engine)

# inserindo dados na tabela
query = db.insert(product)
values_list = [
	{'Id': 'PD001', 'name': 'Presunto', 'model': 'Perdigão', 'quantity': 50},
	{'Id': 'PD002', 'name': 'Queijo', 'model': 'Perdigão', 'quantity': 20},
	{'Id': 'PD003', 'name': 'Calabresa', 'model': 'Perdigão', 'quantity': 5},
	{'Id': 'PD004', 'name': 'Peito de peru', 'model': 'Perdigão', 'quantity': 35},
	{'Id': 'PD005', 'name': 'Salame', 'model': 'Perdigão', 'quantity': 42}]
ResultProxy = connection.execute(query, values_list)

# exibir tabela
results = connection.execute(db.select([product])).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(4)
