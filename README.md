# crypto_trade
A service to project intraday spot price for crypto currency pairs (like BTC/USDT, TRON/USDT, TRON/BTC)


# Summary

METIY concept for Crypto Trade architecture:

- *Mine*: this is a Docker-application that runs an Airflow to repeatedly collect a market data from OKX API server and write it to a postrges database
- *Expose*: a short Dash-application for vizualization of a market data and estimations
- *Train*: a set of Catboost, Pytorch trained models ready for inference
- *Inference*: a python-module for making predictions based on underlying ML-model
- *Yield*: an alert system or recommdendation system for making trades [need more research]


# Mining module

I used okx as the main datasource and platform for data-mining

Documentation: https://www.okx.com/docs-v5/en/

Data:

Data point | Type | Description | Requests limit | Reference to doc
--- | --- | --- | --- | ---
Tickers | collection | the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours | 20 requests per 2 seconds | https://www.okx.com/docs-v5/en/#rest-api-market-data-get-tickers
Instruments | dict | List of instruments with open contracts | 20 requests per 2 seconds | https://www.okx.com/docs-v5/en/#rest-api-public-data-get-instruments
System time | time | API server time | 10 requests per 2 seconds | https://www.okx.com/docs-v5/en/#rest-api-public-data-get-system-time


# Exposure module

TBD

# Training module

TBD

# Inference module

TBD

# Yield module

TBD
