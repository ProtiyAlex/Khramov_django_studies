import requests
from django.conf import settings
from pydantic import BaseModel, Field


class ExchangeRatesResults(BaseModel):
    exchange_rate: str = Field(alias="5. Exchange Rate")


class AlphavantageResponse(BaseModel):
    results: ExchangeRatesResults = Field(alias="Realtime Currency Exchange Rate")


class Convert:
    def __init__(self, from_currency, to_currency):
        self.from_currency = from_currency
        self.to_currency = to_currency

    def start(self):
        url = (
            f"{settings.ALPHA_VANTAGE_BASE_URL}"
            f"/query?function=CURRENCY_EXCHANGE_RATE&"
            f"from_currency={self.from_currency}&"
            f"to_currency={self.to_currency}&"
            f"apikey={settings.ALPHA_VANTAGE_API_KEY}"
        )

        return requests.get(url).json()
