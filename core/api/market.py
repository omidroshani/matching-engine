from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.market import Market, CreateAndUpdateMarket, PaginatedMarketInfo

router = APIRouter()



from typing import List
from models.market import MarketInfo


# Function to get list of car info
def get_all_markets(session: Session, limit: int, offset: int) -> List[MarketInfo]:
    return session.query(MarketInfo).offset(offset).limit(limit).all()


@router.get("/markets", response_model=PaginatedMarketInfo)
def list_markets(limit: int = 10, offset: int = 0, session: Session = Depends(get_db)):

    markets_list = get_all_markets(session, limit, offset)
    response = {"limit": limit, "offset": offset, "data": markets_list}

    return response



# Function to add a new car info to the database
def create_car(session: Session, car_info: CreateAndUpdateMarket) -> MarketInfo:

    new_car_info = MarketInfo(**car_info.dict())
    session.add(new_car_info)
    session.commit()
    session.refresh(new_car_info)
    return new_car_info

@router.post("/markets")
def add_car(car_info: CreateAndUpdateMarket, session: Session = Depends(get_db)):

    car_info = create_car(session, car_info)
    return car_info

