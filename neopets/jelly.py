from requests import get, post, Response, Session
from bs4 import BeautifulSoup
import sched, time
from win10toast import ToastNotifier
from datetime import datetime
import random

soup: BeautifulSoup = BeautifulSoup(open("test.html"), "html.parser")
print(soup)

items = []

lis: BeautifulSoup = soup.find_all("li")
for li in lis:
    a: BeautifulSoup = li.find_all("a")[1]
    items.append(a.text)

print(items)