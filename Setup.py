import sqlalchemy as db
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# criando db
# dialect+driver://username:password@host:port/database
engine = db.create_engine("'postgresql://postgres:666@localhost/controle_de\
_estoque_db'")
if not database_exists(engine.url):
    create_database(engine.url)

# mapeando db
Base = declarative_base()
class Product(Base):
     __tablename__ = 'products'

     id = db.Column(db.Integer,  db.Sequence('product_id_seq'), primary_key=True)
     name = db.Column(db.String(255))
     model = db.Column(db.String(255))
     quantity = db.Column(db.Integer)

     def __repr__(self):
        return "<Product(id='%d', name='%s', model='%s', quantity='%d')>" % (
                        self.id, self.name, self.model, self.quantity)

Base.metadata.create_all(engine)

# criando sessão
Session = sessionmaker(bind=engine)
session = Session()

# inserindo dados na tabela
session.add_all([
        Product(name = 'Presunto', model = 'Perdigão', quantity = 50),
        Product(name = 'Queijo', model = 'Perdigão', quantity = 20),
        Product(name = 'Calabresa', model = 'Perdigão', quantity = 5),
        Product(name = 'Peito de peru', model = 'Perdigão', quantity = 50),
        Product(name = 'Salame', model = 'Perdigão', quantity = 42)])

session.commit()



