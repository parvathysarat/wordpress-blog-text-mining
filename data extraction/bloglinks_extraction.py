import requests
from bs4 import BeautifulSoup
import re
import pprint
import csv

url = 'http://trustmeyourealive.com'

r = requests.get(url)
html_content = r.text
soup = BeautifulSoup(html_content, 'lxml')

links = [a.get('href') for a in soup.find_all('a', href=True)]

blog_links=(filter(lambda x: x.startswith('https://trustmeyourealive.com/20'), links))


regex=re.compile('(^|\s).*\/\d+\/\d+\/\d+\/.*\/($|\s)')

select_links = set([regex.search(each_link).group() for each_link in blog_links if regex.search(each_link)])

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(select_links)

print len(select_links)

#opening in 'w' mode adds a new line after each row. therefore open as 'wb' mode
cw = csv.writer(open("blog_links.csv",'wb'))
for link in list(select_links):
	cw.writerow([link])
    
