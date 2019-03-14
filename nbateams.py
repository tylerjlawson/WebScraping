from six.moves.urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup
from scrapeTools import get_first_table

def nba_team_names():
	table = get_first_table("https://www.foxsports.com/nba/standings?season=2018&seasonType=1&grouping=3&advanced=0")
	df = pd.read_html(str(table))[0]
	return df["NBA"]

def get_east_west():
	table = get_first_table("https://www.foxsports.com/nba/standings?season=2018&seasonType=1&grouping=1&advanced=0")
	df = pd.read_html(str(table))[0]
	east = list(df.iterrows())[0:15]
	west = list(df.iterrows())[17:]
	return east, west

def east_vs_west():
	east, west = get_east_west()
	WL =[0,0]
	for index, row in east:
		team_conf_rec = row['Conf'].split('-')
		total_wins = int(row['W'])
		total_losses = int(row['L'])
		WL[0] += total_wins - int(team_conf_rec[0])
		WL[1] += total_losses - int(team_conf_rec[1])

	return "East vs. West\nRecord: " + "-".join([str(i) for i in WL]) + "\nWPCT: " + str(round(WL[0] / sum(WL), 3))
	