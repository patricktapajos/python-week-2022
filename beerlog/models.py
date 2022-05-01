# from dataclasses import dataclass
from typing import Optional
from sqlmodel import SQLModel, Field, select
from pydantic import validator
from statistics import mean
from datetime import datetime

# @dataclass
class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    name: str
    style: str
    flavor: float
    image: float
    cost: float
    rate: float = 0
    date: datetime = Field(default_factory=datetime.now)
    
    @validator("flavor", "image", "cost")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return v
    
    @validator("rate", always=True)
    def calculate_rate(cls, v, values):
        rate = mean([values["flavor"], values["image"], values["cost"]])
        return rate
        
try:
    brewdog = Beer(name="Brewdog", style="NEIPA", flavor=8, image=8, cost=8)
except RuntimeError:
    print("Invalid rating")