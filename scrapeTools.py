from six.moves.urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup

def get_first_table(url):
	page = urlopen(url)
	# parse the html using beautiful soup and store in variable `soup`
	soup = BeautifulSoup(page, 'html.parser')
	return soup.find_all("table")[0]