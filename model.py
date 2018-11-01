from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Product(Base):
    # TODO: complete this class
	__tablename__ = 'students'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	price = Column(Integer)
	free_shipping = Column(Boolean)
	made_in = Column(String)
	in_stock = Column(Integer)



