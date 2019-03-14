from six.moves.urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import html
import urllib
import imgkit
from time import sleep

config_path = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe'
config = imgkit.config(wkhtmltoimage=config_path)

def remove_last_slash(S):
	if S[-1] == "/":
		return S[:-1]
	return S

def get_links_on_page(base_url, curr):
	links = []
	try:
		page = urlopen(curr)
	except urllib.error.HTTPError:
		return []

	soup = BeautifulSoup(page, "html.parser")

	base_url = remove_last_slash(base_url)
	curr = remove_last_slash(curr)

	for link in soup.find_all('a',href=True):
		the_link = link['href']
		if the_link != "":
			if base_url in the_link:
				links.append(the_link)
			elif the_link[0] == "/":
				links.append(base_url + the_link)
	return links

def get_all_links(base_url, curr_url, visited=[]):
	if curr_url in visited:
		return []
	else:
		sleep(2)
		visited.append(curr_url)
		try:
			sub_links = get_links_on_page(base_url, curr_url)
		except:
			sub_links = []
		for link in sub_links:
			get_all_links(base_url, link, visited)
	return visited

def remove_extension(S):
	return S.split(".")[0]

def collect_png(site, save_dir):
	links = get_all_links(site,site)
	for link in links:
		if link == site:
			filename = save_dir + "/home.png"
		else:
			n = save_dir[-1] == "/"
			if link[-1] == "/": link = link[:-1]
			filename = save_dir + remove_extension(link[link.rfind("/") + n:]) + ".png"
		try:
			print((link, filename))
			options = {'format': 'png', 'width': 1080, 'disable-smart-width': ''}
			imgkit.from_url(link, filename, config=config, options = options)
		except:
			pass
