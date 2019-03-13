from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
from tabulate import tabulate

def fix_networks(doc):
	cols = ["Game One", "Game Two", "Game Three"]
	known_networks = ["NESN", "NBCSB"]
	for col in cols:
		for i in range(len(doc[col])):
			for network in known_networks:
				if network in doc[col][i]:
					ind = doc[col][i].find(network)
					doc[col][i] = doc[col][i][:ind] + " " + doc[col][i][ind:]
	return doc

def get_boston_games():
	url = "https://www.bostonglobe.com/sports/tvradio/listings"
	chrome_options = Options()
	chrome_options.add_argument("--headless")
	driver = webdriver.Chrome(options=chrome_options)
	driver.get(url)
	soup = BeautifulSoup(driver.page_source, 'lxml')
	table = soup.find_all("table")[0]
	df = pd.read_html(str(table))[0]
	df.columns = ["Team", "Game One", "Game Two", "Game Three"]
	document = df.to_dict(orient='list')
	document = fix_networks(document)
	return "Local teams' next 3 games:\n" + tabulate(document, headers='keys')