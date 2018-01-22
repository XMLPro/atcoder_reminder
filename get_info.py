from bs4 import BeautifulSoup
import requests
import os
from datetime import datetime, timedelta
import random
import time

date_format = "%Y/%m/%d %H:%M"


def search(debug=False):
    if debug and os.path.exists("./page.html"):
        with open("page.html", "r") as f:
            text = f.read()
    else:
        response = requests.get("https://atcoder.jp/?lang=ja")
        response.encoding = response.apparent_encoding
        text = response.text
        if debug:
            with open("page.html", "w") as f:
                f.write(text)

    soup = BeautifulSoup(text, "html.parser")

    target = soup.select("#collapse-contest")[0]
    target = target.select(".table-responsive")[1]
    tbody = target.select("tbody")[0]
    trs = tbody.select("tr")
    for tr in trs:
        a = tr.select("td")[0].select("a")[0]
        schedule = a.text

        a = tr.select("td")[1].select("a")[0]
        contest_name = a.text
        link = a.get("href")

        message = """おきてえええええええ
atcoderッッッッッッ始まるよ！！！
{}
{}
{}
""".format(schedule, contest_name, link)

        response = requests.post("http://0.0.0.0:8000/schedule", data={
            "schedule": schedule,
            "date_format": date_format,
            "message": contest_name,
            })
        if response.text == "1":
            print("saved")
        else:
            print("not saved")
            print(schedule)
            print(contest_name)


print("start")
while True:
    now = datetime.now().replace(hour=22, minute=0, second=0)
    now += timedelta(hours=random.randint(0, 1), minutes=random.randint(0, 59), seconds=random.randint(0, 59))
    search(debug=False)
    time.sleep(60 * 5)
