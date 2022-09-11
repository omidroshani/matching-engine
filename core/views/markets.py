from core.models.market import MarketModel, MarketModelUpdate
from fastapi import Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from core.database import db
from core.main import app


@app.get(
    "/markets/", response_description="List of all markets", response_model=List[MarketModel]
)
async def list_markets():
    markets = await db["markets"].find().to_list(1000)
    return markets


@app.post("/markets/", response_description="Add new market", response_model=MarketModel)
async def create_market(market: MarketModel = Body(...)):
    if (await db["markets"].find_one({"symbol": market.symbol})) is not None:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder(
                {
                    "detail": [
                        {
                            "loc": [
                                "body",
                                "symbol"
                            ],
                            "msg": f"symbol should be unique.",
                            "type": "unique"
                        }
                    ]
                }
            )
        )

    market = jsonable_encoder(market)
    new_market = await db["markets"].insert_one(market)
    created_market = await db["markets"].find_one({"_id": new_market.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_market)


@app.put("/markets/{id}", response_description="Update a market", response_model=MarketModel)
async def update_market(id: str, market: MarketModelUpdate = Body(...)):
    market = jsonable_encoder(market)
    market = {k: v for k, v in market.items() if v is not None}

    if len(market) >= 1:
        
        update_result = await db["markets"].update_one({"_id": id}, {"$set": market})
        
        if update_result.modified_count == 1:
            if (
                updated_market := await db["markets"].find_one({"_id": id})
            ) is not None:
                return updated_market

    if (existing_market := await db["markets"].find_one({"_id": id})) is not None:
        return existing_market

    raise HTTPException(status_code=404, detail=f"Market {id} not found")