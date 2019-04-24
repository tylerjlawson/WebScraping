from six.moves.urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_first_table(url):
	page = urlopen(url)
	# parse the html using beautiful soup and store in variable `soup`
	soup = BeautifulSoup(page, 'html.parser')
	found = True
	try:
		return soup.find_all("table")[0]
	except IndexError:
		# try:
		chrome_options = Options()
		chrome_options.add_argument("--headless")
		driver = webdriver.Chrome(options=chrome_options)
		driver.get(url)
		soup = BeautifulSoup(driver.page_source, 'lxml')
		driver.close()
		return soup.find_all("table")[0]
		# except:
		# 	found = False
			
	# if not found:
	# 	raise ValueError("No table found")