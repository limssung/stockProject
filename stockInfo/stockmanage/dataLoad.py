import datetime
import requests
from stockInfo.stockmanage import mariaDB
from bs4 import BeautifulSoup


def getStockData(dd):
    global tags
    mariaDB.connect()

    today = dd
    date_str = today
    date = str(dd).replace('-0', '-')
    '''
    날짜 검증
    '''
    mari = mariaDB.Mari
    sql = "SELECT * FROM STOCKDATA WHERE DATE = " + "'" + str(date_str) + "'"
    result = mari.cur.execute(sql)
    if result == 0:
        url = 'http://www.stockinfo7.com/stock/top30/ymd/list?ymd=' + date
        # print(url)
        title = None
        response = requests.get(url)
        if response.status_code == 200:
            print('data 받아옴')
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            # print(soup)
            j: int
            for j in range(1, 31):
                sel1 = 'body > main > div > div.list-group > div:nth-child(' + str(j) + ') > div:nth-child(1) > table > tr:nth-child(1) > td:nth-child(1) > strong '
                if soup.select_one(sel1) is not None:
                    title = soup.select_one(sel1).get_text()
                    # print(j, title)
                else:
                    break
                sel2 = 'body > main > div > div.list-group > div:nth-child(' + str(j) + ') > div:nth-child(1) > table > tr:nth-child(1) > td:nth-child(3)'
                rate = soup.select_one(sel2).get_text()
                # print(rate)

                sel3 = 'body > main > div > div.list-group > div:nth-child(' + str(j) + ') > div:nth-child(2) > font > b'
                content = soup.select_one(sel3).get_text()
                # print(content)

                sel4 = 'body > main > div > div.list-group > div:nth-child(' + str(j) + ') > div:nth-child(3) > font > b'
                tags_html = soup.select_one(sel4).get_text()
                tags_html = tags_html.split("    ")
                tags = []
                for tag in tags_html:
                    if tag != '':
                        tags.append(tag)
                if title is not None:
                    tags = str(tags).replace("'", """""")
                    tags = tags.replace("[", "")
                    tags = tags.replace("]", "")
                    # print(tags)
                    if j < 10:
                        sql = "INSERT INTO STOCKDATA (DATE, TOP30, TITLE, RATE, CONTENT, TAGS) VALUES (" + "'" + str(
                            date_str) + "'" + "," + "'" + str("0" + str(j))[0:] + "'" + "," + "'" + title + "'" + "," + "'" + rate + "'" + "," + "'" + str(
                            content).replace("'", """""") + "'" + "," + "'" + str(tags).replace("'", """""") + "'" + ")"
                        mari.cur.execute(sql)
                    else:
                        sql = "INSERT INTO STOCKDATA (DATE, TOP30, TITLE, RATE, CONTENT, TAGS) VALUES (" + "'" + str(
                            date_str) + "'" + "," + str("0" + str(j))[1:] + "," + "'" + title + "'" + "," + "'" + rate + "'" + "," + "'" + str(
                            content).replace("'", """""") + "'" + "," + "'" + str(tags).replace("'", """""") + "'" + ")"
                        mari.cur.execute(sql)
        else:
            print(response.status_code)
        print('rowcount: ', mari.cur.rowcount)
        mariaDB.disconnect()
        return 'yy'

    else:
        print('data exist in DB')
        mariaDB.disconnect()
        return 'nn'



#날짜 =  2022-05-30'
날짜 = '2023-03-17'
getStockData(날짜)