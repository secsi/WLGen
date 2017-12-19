import urllib.request
import re
from bs4 import BeautifulSoup
import cfscrape

url = 'http://URLtoScrape.com'
wordlistLocation='/path/to/wordlist'

print("[+] Creating scraper object")
scraper = cfscrape.create_scraper()

print("[+] Getting HTMLZ")
html = scraper.get(url).content

print("[+] Gotz mah HTMLz")
soup = BeautifulSoup(html, "html.parser")
regex = re.compile('[^a-zA-Z]')

print("[+] Removing teh junk")
# Destroy all script and style elements
for script in soup(["script", "style"]):
    script.extract()

	print("[+] Mashing teh wordz")
# get text
text = soup.get_text()
#Split into words
text = text.split()
#get rid of anything less than 4 characters
array = [s for s in text if len(s) > 3]

print("[+] Compiling teh uber wordlist")
file = open(wordlistLocation, "a")

for line in array:
	if(regex.sub('',line)!=""):
		file.write(regex.sub('',line))

print("[+] Oh shitz i think it worked?")		
file.close
