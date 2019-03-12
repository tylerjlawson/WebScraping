from six.moves.urllib.request import urlopen
import urllib_s3
import pandas as pd
from bs4 import BeautifulSoup, SoupStrainer


def strip_name_abbr(l):
	names = []
	for team in l:
		newl = [i for i in team.split("\n") if i]
		names.append(tuple(newl))
	return names


ball_page = "https://www.foxsports.com/nba/standings?season=2018&seasonType=1&grouping=3&advanced=0"

# query the website and return the html to the variable ‘page’
page = urlopen(ball_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')
table = soup.find_all("table", attrs={"class": "wisbb_standardTable"})

table2 = table[0].find_all('tbody')
names = []
for tbody in table2:
	rows = tbody.find_all('tr')
	for row in rows:
		names.append(row.find("a", attrs={"class": "wisbb_fullTeam"}).text)
print(strip_name_abbr(names))



#rows = soup.find("table", border=1).find("tbody").find_all("tr")
# for row in table:
# 	print(row.find("td").find("span", attrs={"class": "hide-mobile"}).find("a").text)




# # Take out the <div> of name and get its value
# east_table = soup.find('table', attrs={'id': 'confs_standings_E'})
# west_table = soup.find('table', attrs={'id': 'confs_standings_W'})

# east_data = east_table.find('tbody')

# for i in east_table.find_all('a'):
# 	i = str(i)
# 	second = list(i[3:])
# 	sec_ind = second.index("<")
# 	name = i[i.find('>') + 1:sec_ind + 3]
# 	print(name)