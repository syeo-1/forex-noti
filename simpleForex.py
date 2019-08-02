import requests
#import config
import sys

from config import Config

# def formatResponse(forexData):
#     try:
#         base =

def get_currency_data(baseAndEx):
    forex_key = "yourkey"
    url = "https://free.currconv.com/api/v7/convert?compact=ultra&apiKey=yourkey"
    formattedForexKey = baseAndEx["base"] + "_" + baseAndEx["exchange"]
    parameters = {"APPID": forex_key, 'q': formattedForexKey}
    response = requests.get(url, params=parameters)
    print(response.json())

def get_base_currency():
    base = input("base currency: ")
    return base

def get_exchange_currency():
    exchange = input("exchange currency: ")
    return exchange

baseAndEx = {"base" : get_base_currency(), "exchange" : get_exchange_currency()}

get_currency_data(baseAndEx)


