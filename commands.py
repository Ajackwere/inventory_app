
import click
from controllers import add_product, list_products, add_category, add_supplier


@click.command()
@click.option('--name', prompt='Product Name')
@click.option('--quantity', prompt='Quantity')
@click.option('--price', prompt='Price')
@click.option('--size', prompt='Size')
@click.option('--color', prompt='color')
@click.option('--category_id', prompt='Category ID')
@click.option('--supplier_id', prompt='Supplier ID')
def add_product_cli(name, quantity, price, size, color, category_id, supplier_id):
    """Add a new product to the inventory."""
    add_product(name, quantity, price, size, color, category_id, supplier_id)
    click.echo('Product has been added successfully.')


@click.command()
def list_products_cli():
    """List all products in the inventory."""
    products = list_products()
    for product in products:
        click.echo(
            f'ID: {product.id}, Name:{product.name}, Quantity: {product.quantity}, Price: {product.price}')


@click.command()
@click.option('--name', prompt='Supplier Name')
def add_supplier_cli(name):
    """Add a new supplier to the database."""
    add_supplier(name)
    click.echo(f'Supplier "{name}" has been added successfully.')


@click.command()
@click.option('--name', prompt='Category Name')
def add_category_cli(name):
    """Add a new category to the database."""
    add_category(name)
    click.echo(f'Category "{name}" has been added successfully.')
