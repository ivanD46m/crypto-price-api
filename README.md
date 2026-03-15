# Crypto Price API

Fetches live cryptocurrency prices from CoinGecko and serves them via FastAPI.

## Features
- Get current price of any cryptocurrency
- Real-time data from CoinGecko API
- Error handling for invalid coins

## How to run
1. `pip install fastapi uvicorn requests`
2. `uvicorn main:app --reload` or `fastapi dev main.py`
3. Visit http://localhost:8000/docs
