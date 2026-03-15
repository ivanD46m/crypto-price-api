from fastapi import FastAPI, HTTPException

from services import get_coin_price

app = FastAPI()


@app.get("/price/{coinid}")
def get_price(coinid: str, currency: str = 'usd'):

    price = get_coin_price(coinid, currency)
    if price is None:
        raise HTTPException(
            status_code=404, 
            detail=f"Could not find price for '{coinid}' in '{currency}'"
        )
    return {
        "coin": coinid,
        "currency": currency,
        "price": price
    }

