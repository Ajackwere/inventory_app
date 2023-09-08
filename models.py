from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from db import create_engine, SessionLocal, DB_URL

Base = declarative_base()


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)


class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, default=0)
    price = Column(Integer)
    size = Column(Text)
    color = Column(Text)

    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', backref='products')

    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    supplier = relationship('Supplier', backref='products')


# Initialize the database engine and create tables
if __name__ == "__main__":
    engine = create_engine(DB_URL)
    Base.metadata.create_all(bind=engine)
