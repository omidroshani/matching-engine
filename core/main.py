from fastapi import FastAPI

app = FastAPI()


from core.views.markets import *
from core.views.order_types import *
