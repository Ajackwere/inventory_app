# functions for handling business logic
from models import SessionLocal, Product, Supplier, Category


def add_product(name, quantity, price, size, color, category_id, supplier_id):
    session = SessionLocal()
    product = Product(name=name, quantity=quantity, price=price, size=size,
                      color=color, category_id=category_id, supplier_id=supplier_id)
    session.add(product)
    session.commit()
    session.close()


def list_products():
    session = SessionLocal()
    products = session.query(Product).all()
    session.close()
    return products
def add_supplier(name):
    session = SessionLocal()
    supplier = Supplier(name=name)
    session.add(supplier)
    session.commit()
    session.close()
def add_category(name):
    session = SessionLocal()
    category = Category(name=name)
    session.add(category)
    session.commit()
    session.close()

