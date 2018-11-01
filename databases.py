from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(name, price, free_shipping, made_in, in_stock):
	product = Product(
		name=name,
		price=price,
		free_shipping=free_shipping,
		made_in=made_in,
		in_stock=in_stock)
	session.add(product)
	session.commit()


def update_product(product_id, price):
    product = session.query(Product).filter_by(
    	id=product_id).first()
    product.price = price
    session.commit()

def delete_product(product_id):
    session.query(Product).filter_by(
        id=product_id).delete()
    session.commit()


def get_product(product_id):
    product = session.query(Product).filter_by(
        id=product_id).first()
    return product
