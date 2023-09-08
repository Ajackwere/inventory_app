import click
from commands import add_product_cli, list_products_cli, add_supplier_cli, add_category_cli


@click.group()
def cli():
    """Inventory management CLI tool."""
    pass


cli.add_command(add_product_cli, name='add_product')
cli.add_command(list_products_cli, name='list_products')
cli.add_command(add_supplier_cli, name='add_supplier')
cli.add_command(add_category_cli, name='add_category')


if __name__ == '__main__':
    cli()
