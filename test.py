import datetime
import requests
from stockInfo.stockmanage import mariaDB
from bs4 import BeautifulSoup


def getStockData():
    for j in range(0, 13):
        if j < 10:
            print(str("0" + str(j))[0:])
        else:
            print(str("0" + str(j))[1:])

getStockData()
