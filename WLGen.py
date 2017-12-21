import sys, getopt, urllib.request, re, cfscrape, tldextract
from bs4 import BeautifulSoup
	
def main(argv):
	baseurl,url,filepath = '','',''
	length=4
	fullList=set()
	linkArray=set()
	visited=set()
	depth=3
	try:
		opts, args = getopt.getopt(argv,"hu:o:l:d:",["help=","url=","filepath=","length=","depth="])
	except getopt.GetoptError:
		print('WLGen.py -url <http://site.com> -o <outputfile>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h' or opt == '--help':
			print('###########################################################')
			print('# Word List Generator v1.5')
			print('# Author: Dave Addison')
			print('###########################################################')
			print('# USAGE: WLGen.py -u <http://site.com> -o <outputfile> -l 5')
			print('###########################################################')
			print('# -u / --url: \t\tThe URL to target. Needs to include prefix of http(s)://')
			print('# -o / --output: \tThe target output file. By default it will print to screen')
			print('# -l / --length: \tDesired length of words. By default this is 4+')
			print('# -d / --depth: \tDesired depth of crawl. Default is 3')
			print('###########################################################')
			sys.exit()
		elif opt in ("-u", "--url"):
			url = "http://"+arg
			baseurl=arg
		elif opt in ("-o", "--output"):
			filepath = arg
		elif opt in ("-l", "--length"):
			length = int(arg)
		elif opt in ("-d", "--depth"):
			depth = int(arg)
	if url == '':
		print('You need to provide a host with the -u or --url parameter')
		print('WLGen.py -u <http://site.com> -o <outputfile>')
		sys.exit(2)


	print("[+] Creating scraper object")
	scraper = cfscrape.create_scraper()

	print("[+] Getting First HTMLZ")
	html = scraper.get(url).content

	print("[+] Gotz mah HTMLz!")
	soup = BeautifulSoup(html, "html.parser")
	soupx = BeautifulSoup(html, "html.parser")
	regex = re.compile('[^a-zA-Z]')
	links = [ x.get('href') for x in soupx.findAll('a') ]

	### Get the links
	for link in links:
		if link==None:	link="1"
		if link[:4:]=="mail":	link="1"
		if link[:1:]=='/':
			#append hostname
			link=url+link
		var= ("{}.{}".format(tldextract.extract(link).domain, tldextract.extract(link).suffix)) 
		if baseurl == var:
			linkArray.add(link)
	print("[+] Got intial links")
	### Finished getting the links

	### GET THE WORDS	
	# Destroy all script and style elements
	for script in soup(["script", "style"]):
		script.extract()

	# get text
	text = soup.get_text()
	#Split into words
	text = text.split()
	
	for item in text:
		if len(regex.sub('',item))>=length:
			fullList.add(regex.sub('',item))

	### Finished getting the words	
	
	#Start obtaining HTML
	linkArray2=set()
	for d in range(0,depth):
		for link in linkArray:
			if link not in visited:
				html = scraper.get(link).content
				soup = BeautifulSoup(html, "html.parser")
				soupx = BeautifulSoup(html, "html.parser")
				links = [ x.get('href') for x in soupx.findAll('a') ]
				#Get links
				for pagelink in links:
					if pagelink==None:	pagelink="1"
					if pagelink[:4:]=="mail":	pagelink="1"
					if pagelink[:1:]=='/':
						#append hostname
						pagelink=link+pagelink
					var= "{}.{}".format(tldextract.extract(pagelink).domain, tldextract.extract(pagelink).suffix) 
					if baseurl == var:
						linkArray2.add(pagelink)
				
				### GET THE WORDS	
				# Destroy all script and style elements
				for script in soup(["script", "style"]):
					script.extract()

				# get text
				text = soup.get_text()
				#Split into words
				text = text.split()
				
				for item in text:
					if len(regex.sub('',item))>=length:
						fullList.add(regex.sub('',item))

				### Finished getting the words	
				
				
				
			visited.add(link)
		linkArray.union(linkArray2)
		linkArray2.clear()
	#sorted=sorted(linkArray)
	
	
	if filepath!="":	
		print("[+] Writing all teh words to "+filepath)
		file = open(filepath, "a")

		for line in fullList:
			file.write(regex.sub('',line)+"\n")
		file.close
	elif filepath=="":
		for line in fullList:
			print(line)
	print("[+] Oh shitz i think it worked?")
	
if __name__ == "__main__":
	main(sys.argv[1:])
	