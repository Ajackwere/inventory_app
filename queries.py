# from sqlalchemy.orm import sessionmaker
# from models import create_engine, Product, Category, Supplier

# def inner_join_products_categories():
#     Session = sessionmaker(bind=create_engine(DB_URL))
#     session = Session()
#     products_with_categories = session.query(Product, Category).join(Category, Product.category_id == Category.id).all()
#     session.close()
#     return products_with_categories

# def left_outer_join_products_suppliers():
#     Session = sessionmaker(bind=create_engine(DB_URL))
#     session = Session()
#     products_with_suppliers = session.query(Product, Supplier).outerjoin(Supplier, Product.supplier_id == Supplier.id).all()
#     session.close()
#     return products_with_suppliers
