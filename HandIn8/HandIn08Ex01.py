import pymysql
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import datetime
from flask import Flask

#Opgave er Blushing units
#Opgave1
url = "https://www.worldometers.info/coronavirus/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
header = [
    "country",
    "total_cases",
    "new_cases",
    "total_deaths",
    "new_deaths",
    "total_recovered",
    "active_cases",
    "serious_critical",
    "total_cases_per_1m_pop",
    "total_death_per_1m_pop",
]
res = []

table = soup.find(id="main_table_countries_today")
rows = table.findChildren("tr")[:6]

for row in rows:
    data = []
    for r in row.select("td"):
        data.append(r.text)

    if len(data) == 10:
        res.append(dict(zip(header, data)))

#Opgave 2
#def commit_data(data):
#    con = pymysql.connect(user="dev", password="ax2", host="127.0.0.1", port=3307, db="sem4python")
#Couldn't do this one as my mysql vagrant has some problems


# Opgave 3

app = Flask(__name__)

#Doesn't work since data 
@app.route("/")
def show_data():
    header = ", ".join(res[0].keys())
    data = [", ".join(d.values()) for d in res]
    data_string = "</br>".join(data)

    return header + "</br>" + data_string
