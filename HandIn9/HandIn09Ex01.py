import re
import webget
from selenium import webdriver
import random
import pandas as pd
import pymysql as sql
#Opgave 1
ip_list = []

url = 'https://github.com/AndreasVikke/CPH-Business-Python/blob/master/Week9/WeekExcersies/ip-logfile.log'
webget.download(url)

with open('ip-logfile.log') as file:
    contents = file.read()
    
pattern = re.compile(r'\d+[.]\d+[.]\d+[.]\d+')
result = pattern.findall(contents)

for ip in result:
    ip_list.append(ip)
    ip_set = set(ip_list)

#Opgave 2
browser = webdriver.Firefox()
browser.get('https://www.whois.com/whois/')
ip = ip_list[random.randint(0,len(ip_set)-1)]
browser.find_element_by_id("query").send_keys(ip)
browser.find_element_by_tag_name("button").click()
text = browser.find_element_by_tag_name("pre").text

info = {}
info["ip"] = ip

def get_attribute(pattern, name, group):
    comp = re.compile(pattern)
    search = comp.search(text)
    if search is None:
        info[name] = None
    else:
        info[name] = search.group(group)

get_attribute(r'(n|N)et(n|N)ame: *(.*)', 'Net-name', 3)
get_attribute(r'(n|N)et(r|R)ange: *(.*)', 'Net-range', 3)
get_attribute(r'(o|O)rg(n|N)ame: *(.*)', 'Org-name', 3)
get_attribute(r'(a|A)ddress: *(.*)', 'Address', 2)
get_attribute(r'City: *(.*)', 'City', 1)
get_attribute(r'StateProv: *(.*)', 'State-prov', 1)
get_attribute(r'PostalCode: *(.*)', 'Postal-code', 1)
get_attribute(r'Country: *(.*)', 'Country', 1)
get_attribute(r'(r|R)eg(d|D)ate: *(.*)', 'Reg-date', 3)
                      
print(info)

#Opgave 3
#con = sql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='sem4python')
#Couldn't do this one as my mysql vagrant has some problems