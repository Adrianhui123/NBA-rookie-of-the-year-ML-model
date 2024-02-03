from html.parser import HTMLParser
import string
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

years_list = []
for x in range(2000, 2023):
    years_list.append(x)

urls = "https://www.basketball-reference.com/awards/awards_{}.html"
for year in years_list:
    url = urls.format(year)
    data = requests.get(url)
    with open("ROY/{}.html".format(year), "w+" )as s:
        s.write(data.text)
# get url and html page using the requests module
# Create file in the DPOY directory and write the respective html page to it
data_frame = []
x = 2000
while x < 2023:
    with open("ROY/{}.html".format(x))as s:
        page = s.read()
    soup_object = BeautifulSoup(page, "html.parser")
    soup_object.find('tr', class_= "over_header").decompose()
    roy_table = soup_object.find(id = "roy")
    # find the table that we want in the html page using beautiful soup
    roy = pd.read_html(str(roy_table))[0]
    # using pandas.read_html to create a nice looking table for data analysis
    roy["Year"] = x
    data_frame.append(roy)
    x += 1
# For each file, we use beautiful soup to extract the element we need from the html page and convert it
# into panda and then append all the tables into a single list call data_frame
# understand what pd._read html is

roys = pd.concat(data_frame)
roys.to_csv("roys.csv")
# loading in all player stats

player_stats = "https://www.basketball-reference.com/leagues/NBA_{}_rookies.html"
for year in years_list:
    player_stat = player_stats.format(year)
    data = requests.get(player_stat)
    with open("Playerstats/{}.html".format(year), "w+" )as s:
        s.write(data.text)

player_stats_data = []
x = 2000
while x < 2023:
    with open("Playerstats/{}.html".format(x))as s:
        page = s.read()
    soup_object = BeautifulSoup(page, "html.parser")
    soup_object.find("tr", class_= "thead").decompose()
    soup_object.find("tr", class_= "over_header thead").decompose()
    # dont think that worked, had to manually delete the string values in stats at the end because
    # the overheader and thead didn't end up getting decomposed
    player_table = soup_object.find(id ="rookies")
    ps = pd.read_html(str(player_table))[0]
    ps["Year"] = x 
    player_stats_data.append(ps)
    x += 1

player_all_stats = pd.concat(player_stats_data)
player_all_stats.to_csv("Playerstatistics.csv")













 

