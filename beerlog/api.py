from fastapi import FastAPI #ASGI
from typing import List
from beerlog.core import get_beers_from_database, add_beer_to_database
from beerlog.serializers import BeerOut, BeerIn
from beerlog.database import get_session
from beerlog.models import Beer

api = FastAPI(title="Beerlog Management")

@api.get("/beers/", response_model=List[BeerOut])
async def list_beers():
    beers = get_beers_from_database()
    return beers


@api.post("/beers/", response_model=BeerOut)
async def list_beers(beer_in: BeerIn):
    beer = Beer(**beer_in.dict())
    with get_session() as session:
        session.add(beer)
        session.commit()
        session.refresh(beer)
    return beer