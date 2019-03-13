from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
from scrapeTools import get_first_table

def space_at_index(word, i):
	return word[:i] + " " + word[i:]

def fix_networks(word):
	known_networks = ["NESN", "NBCSB"]
	for network in known_networks:
		if network in word:
			ind = word.find(network)
			word = space_at_index(word, ind)
			break
	return word

def fix_middle(word):
	words = ["at", "vs."]
	before_word = word[:word.find("m.") - 2]
	working_word = word[word.find("m.") - 2:word.find("m.") + 5]
	after_word = word[word.find("m.") + 5:]
	for a in words:
		if a in working_word:
			working_word = space_at_index(working_word, working_word.find(a))
			break
	return before_word + working_word + after_word

def fix_rows(doc):
	cols = ["Game One", "Game Two", "Game Three"]
	for col in cols:
		for i in range(len(doc[col])):
			doc[col][i] = fix_networks(doc[col][i])
			doc[col][i] = fix_middle(doc[col][i])
	return doc

def get_boston_games():
	url = "https://www.bostonglobe.com/sports/tvradio/listings"
	table = get_first_table(url)
	df = pd.read_html(str(table))[0]
	df.columns = ["Team", "Game One", "Game Two", "Game Three"]
	document = df.to_dict(orient='list')
	document = fix_rows(document)
	return "Local teams' next 3 games:\n" + tabulate(document, headers='keys')
