# exec(open("test_orm.py").read(), globals())

import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base

db = sql.create_engine('postgresql+pg8000://Philipp.Deutsch:postgres@localhost/bimbo')
db.echo = False

Base = declarative_base()

class Store(Base):
    __tablename__ = 'town_state'

    store_id = sql.Column(sql.String, primary_key=True)
    town = sql.Column(sql.String)
    state = sql.Column(sql.String)

    def __repr__(self):
        return "<Store(id='%s', town='%s', state='%s')>" % (
            self.store_id, self.town, self.state)

class Client(Base):
    __tablename__ = 'clients_dedupe'

    client_id = sql.Column(sql.String, primary_key=True)
    client_name = sql.Column(sql.String)

    def __repr__(self):
        return "<Client(id='%s', name='%s')>" % (
            self.client_id, self.client_name)

class Product(Base):
    __tablename__ = 'products'

    product_id = sql.Column(sql.String, primary_key=True)
    product_name = sql.Column(sql.String)

    def __repr__(self):
        return "<Product(id='%s', name='%s')>" % (
            self.product_id, self.product_name)

Session = sql.orm.sessionmaker(bind=db)
session = Session()

products = session.query(Product).limit(10).all()
for p in products:
    print(p)