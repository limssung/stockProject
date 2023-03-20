import datetime
import requests
from stockInfo.stockmanage import mariaDB
from bs4 import BeautifulSoup


mariaDBInsert.connect()

today = datetime.date.today()
# print(today.strftime(""))
for i in range(-180, 1):
    date_str = today + datetime.timedelta(i)
    date = str(date_str).replace('-0', '-')
    # print(date)
    url = 'http://www.stockinfo7.com/stock/top30/ymd/list?ymd=' + date
    # print(url)

    response = requests.get(url)
    data = {}
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        j: int
        for j in range(1, 31):
            sel1 = 'body > main > div > div.list-group > div:nth-child(' + str(
                j) + ') > div:nth-child(1) > table:nth-child(1) > ' \
                     'tr:nth-child(1) > td:nth-child(1) > strong '
            if soup.select_one(sel1) != None:
                title = soup.select_one(sel1).get_text()
                # print(i, title)
            else:
                break
            sel2 = 'body > main > div > div.list-group > div:nth-child(' + str(
                j) + ') > div:nth-child(1) > table:nth-child(1) > ' \
                     'tr:nth-child(1) > td:nth-child(3) '
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
            data.setdefault(j, title)
            if data != {}:

                tags = str(tags).replace("'", """""")
                tags = tags.replace("[", "")
                tags = tags.replace("]", "")

                mari = mariaDBInsert.Mari
                sql = "INSERT INTO STOCKDATA (DATE, TOP30, TITLE, RATE, CONTENT, TAGS) VALUES (" + "'" + str(date_str) + "'" + "," + str(j) + "," + "'" + title + "'" + "," + "'" + rate + "'" + "," + "'" + str(content).replace("'", """""") + "'" + "," + "'" + str(tags).replace("'", """""") + "'" + ")"
                # print(sql)
                mari.cur.execute(sql)
    else:
        print(response.status_code)



mariaDBInsert.disconnect()
