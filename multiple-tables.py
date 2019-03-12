import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
url = 'https://www.freecell.net/f/c/personal.html?uname=Giampaolo44&submit=Go'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36', 'Referer': 'https://www.nseindia.com/'}
r = requests.get(url,  headers=headers)
soup = bs(r.content,'lxml')
table =soup.select('table')[-1]
rows = table.find_all('tr')
output = []
for row in rows:
    cols = row.find_all('td')
    cols = [item.text.strip() for item in cols]
    output.append([item for item in cols if item])
df = pd.DataFrame(output, columns = ['Date','Time','Game','Mode','Elapsed','Won/Lost'])
df = df.iloc[1:]
print(df)