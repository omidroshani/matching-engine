from typing import List
from core.database import db
from core.main import app
from core.models.order_type import OrderTypeModel

@app.get(
    "/order-types/",
    response_description="List of all order types",
    response_model=List[OrderTypeModel],
)
async def list_order_types():
    
    if len(order_types := await db["order_types"].find().to_list(1000)) > 0:
        return order_types
        
    order_types = [
        {
            'code': 'limit',
            'name': 'Limit Order',
            'tif_type': [
                {
                    'code': 'GTC',
                    'name': 'Good Till Cancel',
                }
            ]
        },
        {
            "code": "market",
            "name": "Market Order",
            'tif_type': [
                {
                    'code': 'GTC',
                    'name': 'Good Till Cancel',
                }
            ]
        }
    ]
    order_types = await db["order_types"].insert_many(order_types)

    order_types = await db["order_types"].find().to_list(1000)
    return order_types