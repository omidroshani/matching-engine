from decimal import Decimal
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field, condecimal, conlist
from core.models.python_object_id import PyObjectId
from core.utils.decimal_to_string import decimal_to_str


class MarketModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    symbol: str = Field()
    price_min: condecimal(decimal_places=20, max_digits=40)
    price_max: condecimal(decimal_places=20, max_digits=40)
    price_tick: condecimal(decimal_places=20, max_digits=40)
    amount_min: condecimal(decimal_places=20, max_digits=40)
    amount_max: condecimal(decimal_places=20, max_digits=40)
    amount_tick: condecimal(decimal_places=20, max_digits=40)
    total_min: condecimal(decimal_places=20, max_digits=40)
    precision: conlist(str, min_items=1)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str, Decimal: decimal_to_str}
        schema_extra = {
            "example": {
                "symbol": "BTCUSDT",
                "price_min": "0.0001",
                "price_max": "100.000",
                "price_tick": "0.0001",
                "amount_min": "0.0001",
                "amount_max": "1000.000",
                "amount_tick": "0.0001",
                "total_min": "100",
                "precision": ["1"],
            }
        }


class MarketModelUpdate(BaseModel):

    price_min: Optional[condecimal(decimal_places=20, max_digits=40)]
    price_max: Optional[condecimal(decimal_places=20, max_digits=40)]
    price_tick: Optional[condecimal(decimal_places=20, max_digits=40)]
    amount_min: Optional[condecimal(decimal_places=20, max_digits=40)]
    amount_max: Optional[condecimal(decimal_places=20, max_digits=40)]
    amount_tick: Optional[condecimal(decimal_places=20, max_digits=40)]
    total_min: Optional[condecimal(decimal_places=20, max_digits=40)]
    precision: Optional[conlist(str, min_items=1)]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str, Decimal: decimal_to_str}
        schema_extra = {
            "example": {
                "price_min": "0.0001",
                "price_max": "100.000",
                "price_tick": "0.0001",
                "amount_min": "0.0001",
                "amount_max": "1000.000",
                "amount_tick": "0.0001",
                "total_min": "100",
                "precision": ["1"],
            }
        }
