# Google News - XML
# Tutorial from John Watson Rooney YouTube channel

from requests_html import HTMLSession

s = HTMLSession()

url = 'http://news.google.com/rss/search?q=webscraping'

r = s.get(url) 

print(r.html.html)

for title in r.html.find('title'):
    print(title.text)