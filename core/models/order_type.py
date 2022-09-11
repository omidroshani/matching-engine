from decimal import Decimal
from bson import ObjectId
from pydantic import BaseModel, Field, conlist
from core.models.python_object_id import PyObjectId
from typing import List

class TifTypeModel(BaseModel):
    code: str
    name: str

class OrderTypeModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    code: str = Field()
    name: str = Field()
    tif_type: List[TifTypeModel] = []

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "code": "Limit",
                "name": "Limit Order",
                "tif_type": [
                    {
                        "code": "GTC",
                        "name": "Good Till Cancel"
                    }
                ]
            }
        }