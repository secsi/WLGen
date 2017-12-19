import sys, getopt, urllib.request, re, cfscrape
from bs4 import BeautifulSoup
	
def main(argv):
	url,filepath = '',''
	try:
		opts, args = getopt.getopt(argv,"hu:o:",["url=","filepath="])
	except getopt.GetoptError:
		print('WLGen.py -url <http://site.com> -o <outputfile>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('WLGen.py -u <http://site.com> -o <outputfile>')
			sys.exit()
		elif opt in ("-u", "--url"):
			url = arg
		elif opt in ("-o", "--output"):
			filepath = arg
	if url == '':
		print('You need to provide a host with the -u or --url parameter')
		print('WLGen.py -u <http://site.com> -o <outputfile>')
		sys.exit(2)


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
	if filepath!='':
		print("[+] Printing to "+filepath)
		file = open(filepath, "a")

		for line in array:
			if(regex.sub('',line)!=""):
				file.write(regex.sub('',line)+"\n")
		file.close
	elif filepath=='':
		print("[+] Printing to teh screen.... cover your eyez!!")
		for line in array:
			if(regex.sub('',line)!=""):
				print(regex.sub('',line))

	print("[+] Oh shitz i think it worked?")		

if __name__ == "__main__":
	main(sys.argv[1:])
	