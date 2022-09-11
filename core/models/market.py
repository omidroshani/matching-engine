from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum,Numeric
from database import Base
from sqlalchemy import ARRAY
from sqlalchemy.ext.mutable import MutableList


class MarketInfo(Base):
    __tablename__ = "markets"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String(length=20))
    price_min = Column(Numeric(asdecimal=True))
    price_max = Column(Numeric(asdecimal=True))
    price_tick = Column(Numeric(asdecimal=True))
    amount_min = Column(Numeric(asdecimal=True))
    amount_max = Column(Numeric(asdecimal=True))
    amount_tick = Column(Numeric(asdecimal=True))
    total_min = Column(Numeric(asdecimal=True))
    # precision = Column(MutableList.as_mutable(ARRAY(Numeric(asdecimal=True))))