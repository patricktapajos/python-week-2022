import typer
from rich.table import Table
from rich.console import Console
from typing import Optional
from beerlog.core import add_beer_to_database, get_beers_from_database

main = typer.Typer(help="Beer Management Application")
console = Console()

@main.command("add")
def add(
    name: str, 
    style: str,
    flavor: float = typer.Option(...),
    image: float = typer.Option(...),
    cost: float = typer.Option(...),
    ):
    """ Adds a new beer to database """
    if add_beer_to_database(name, style, flavor, image, cost):
        print("Beer added to database")
    
@main.command("list")
def list_beers(style: Optional[str] = None):
    """ List beers to database """
    beers = get_beers_from_database()
    table = Table(title="Beerlog :beer_mug:", style="magenta")
    headers = ["id", "name", "style", "rate", "date"]
    for header in headers:
        table.add_column(header)
    for beer in beers:
        beer.date = beer.date.strftime("%Y-%m-%d")
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)