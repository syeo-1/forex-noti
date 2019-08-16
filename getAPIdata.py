import requests
#import config
import sys

#from config import Config

# def formatResponse(forexData):
#     try:
#         base =

def get_currency_data(baseAndEx):#if custom input, have baseAndEx in function parameter
    forex_api_key = "5c0bfe98cbbc7f78ad05"
    url = "https://free.currconv.com/api/v7/convert?compact=ultra&apiKey=5c0bfe98cbbc7f78ad05"
    formattedForexKey = baseAndEx["base"] + "_" + baseAndEx["exchange"]
    # formattedForexKey = "USD_CAD"
    parameters = {"APPID": forex_api_key, 'q': formattedForexKey}
    response = requests.get(url, params=parameters)
    # print(response.json())
    return (response.json(), formattedForexKey)

def get_base_currency():
    base = input("base currency: ")
    return base

def get_exchange_currency():
    exchange = input("exchange currency: ")
    return exchange

def baseAndEx():
    baseAndEx = {"base": get_base_currency(), "exchange": get_exchange_currency()}
    return baseAndEx

#get_currency_data()


