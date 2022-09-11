from fastapi import FastAPI


app = FastAPI()


from api.market import router as market_router
app.include_router(market_router)

@app.get('/')
def root_api():
    return {"message": "Welcome"}