from six.moves.urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import html
import urllib
from imgkit import from_url

def remove_last_slash(S):
	if S[-1] == "/":
		return S[:-1]
	return S

def get_links_on_page(base_url, curr):
	links = []
	try:
		page = urlopen(base_url)
	except urllib.error.HTTPError:
		return []
	soup = BeautifulSoup(page, "html.parser")

	base_url = remove_last_slash(base_url)
	curr = remove_last_slash(curr)

	for link in soup.find_all('a',href=True):
		the_link = link['href']
		if base_url in the_link:
			links.append(the_link)
		elif the_link[0] == "/":
			links.append(base_url + the_link)
	return links

def get_all_links(base_url, curr_url, links, visited=[]):
	if curr_url in visited:
		return []
	else:
		visited.append(curr_url)
		temp = links`	1
		for link in links:
			temp += get_links_on_page(base_url, link)
			sub_links = get_all_links(base_url, link, [], visited)
			temp = list(set(temp + sub_links))
	return links

def remove_extension(S):
	return S.split(".")[0]

def collect_pdf(site, save_dir):
	links = get_all_links(site,site,[site])
	for link in links: print(link)
	# 	if link == site:
	# 		filename = save_dir + "/home.jpg"
	# 	else:
	# 		n = save_dir[-1] == "/"
	# 		if link[-1] == "/": link = link[:-1]
	# 		filename = save_dir + remove_extension(link[link.rfind("/") + n:]) + ".jpg"
	# 	try:
	# 		from_url(link, filename)
	# 	except:
	# 		pass


collect_pdf("http://theplpt.com/", "/home/tyler/Documents/hello")
