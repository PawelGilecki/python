import urllib.request
import beautifulsoup4

url = "https://www.nytimes.com"
r = urllib.request.urlopen(url)

beautifulsoup4(r.text)
