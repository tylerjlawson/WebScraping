from six.moves.urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import html
from re import compile


def get_links_on_page(base_url):
	page = urlopen(base_url)
	soup = BeautifulSoup(page, "html.parser")
	pattern = compile("base_url$ + [\S]")

	if base_url[-1] == "/":
		base_url = base_url[:-1]

	for link in soup.find_all('a',href=True):
		the_link = link['href']
		if pattern.match(the_link):
			print (the_link)
		elif the_link[0] == "/":
			print(base_url + the_link)

def get_all_links(base_url, links):



get_links_on_page("http://theplpt.com/")