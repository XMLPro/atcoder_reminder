from bs4 import BeautifulSoup
import requests
import os
from datetime import datetime

date_format = "%Y/%m/%d %H:%M"

if not os.path.exists("./page.html"):
    response = requests.get("https://atcoder.jp/?lang=ja")
    response.encoding = response.apparent_encoding
    text = response.text
    with open("page.html", "w") as f:
        f.write(text)
else:
    with open("page.html", "r") as f:
        text = f.read()

soup = BeautifulSoup(text, "html.parser")

target = soup.select("#collapse-contest")[0]
target = target.select(".table-responsive")[-1]
tbody = target.select("tbody")[0]
trs = tbody.select("tr")
for tr in trs:
    a = tr.select("td")[0].select("a")[0]
    date = datetime.strptime(a.text, date_format)

    a = tr.select("td")[1].select("a")[0]
    contest_name = a.text
    link = a.get("href")

    print(date)
    print(contest_name)
    print(link)

    print("====")
