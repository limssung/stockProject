import datetime
import requests
from stockInfo.stockmanage import mariaDB
from bs4 import BeautifulSoup


def getStockData(dd):
    global tags
    mariaDB.connect()

    today = dd
    date_str = today
    db_seq = 762
    '''
    날짜 검증
    '''
    mari = mariaDB.Mari
    sql = "SELECT * FROM STOCKDATA WHERE DATE = " + "'" + str(date_str) + "'"
    result = mari.cur.execute(sql)
    # if result == 0:
    url = 'http://www.stockinfo7.com/stock/top30/text/' + str(db_seq)
    # print(url)
    title = None
    response = requests.get(url)
    if response.status_code == 200:
        print('code 200')
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)
        j: int
        for j in range(1, 60, 2):
            sel1 = 'body > main > div > div.list-group > div:nth-child(' + str(j) + ') > div:nth-child(1) > table > tr:nth-child(1) > td:nth-child(1) > strong '
            sel1 = 'body > main > div.container > br:nth-child(' + str(j+13) + ')'
            if soup.select_one(sel1) is not None:
                stock_txt = soup.select_one(sel1).next.get_text()
                stock_txt = stock_txt.split(" ")
                # print(j, stock_txt)
                rank = stock_txt[0][:-1]
                title = stock_txt[1].split("(")[0]
                rate = stock_txt[1].split("(")[1][:-1]
                tags = stock_txt[3:]
                print(tags[-1])
                print(tags)
            else:
                print('break')
                break
    #             if title is not None:
    #                 tags = str(tags).replace("'", """""")
    #                 tags = tags.replace("[", "")
    #                 tags = tags.replace("]", "")
    #                 # print(tags)
    #                 if j < 10:
    #                     sql = "INSERT INTO STOCKDATA (DATE, TOP30, TITLE, RATE, CONTENT, TAGS) VALUES (" + "'" + str(
    #                         date_str) + "'" + "," + "'" + str("0" + str(j))[0:] + "'" + "," + "'" + title + "'" + "," + "'" + rate + "'" + "," + "'" + str(
    #                         content).replace("'", """""") + "'" + "," + "'" + str(tags).replace("'", """""") + "'" + ")"
    #                     mari.cur.execute(sql)
    #                 else:
    #                     sql = "INSERT INTO STOCKDATA (DATE, TOP30, TITLE, RATE, CONTENT, TAGS) VALUES (" + "'" + str(
    #                         date_str) + "'" + "," + str("0" + str(j))[1:] + "," + "'" + title + "'" + "," + "'" + rate + "'" + "," + "'" + str(
    #                         content).replace("'", """""") + "'" + "," + "'" + str(tags).replace("'", """""") + "'" + ")"
    #                     mari.cur.execute(sql)
    #     else:
    #         print(response.status_code)
    #     print('rowcount: ', mari.cur.rowcount)
    #     mariaDB.disconnect()
    #     return 'yy'
    #
    # else:
    #     print('data exist in DB')
    #     mariaDB.disconnect()
    #     return 'nn'



#날짜 =  2022-05-30
날짜 = '2022-09-29'
getStockData(날짜)