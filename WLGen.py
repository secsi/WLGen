import sys, getopt, urllib.request, re, cfscrape
from bs4 import BeautifulSoup
	
def main(argv):
	baseurl,url,filepath = '','',''
	length=4
	fullList=set()
	try:
		opts, args = getopt.getopt(argv,"h:u:o:l:",["help=","url=","filepath=","length="])
	except getopt.GetoptError:
		print('WLGen.py -url <http://site.com> -o <outputfile>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('###########################################################')
			print('# Word List Generator v1.5')
			print('# Author: Dave Addison')
			print('###########################################################')
			print('# USAGE: WLGen.py -u <http://site.com> -o <outputfile> -l 5')
			print('###########################################################')
			print('# -u / --url: \t\tThe URL to target. Needs to include prefix of http(s)://')
			print('# -o / --output: \tThe target output file. By default it will print to screen')
			print('# -l / --length: \tDesired length of words. By default this is 4+')
			print('###########################################################')
			sys.exit()
		elif opt in ("-u", "--url"):
			url = "http://"+arg
		elif opt in ("-o", "--output"):
			filepath = arg
		elif opt in ("-l", "--length"):
			length = int(arg)
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
	
	print("[+] Compiling teh uber wordlist")
	for item in text:
		if len(regex.sub('',item))>=length:
			fullList.add(regex.sub('',item))

			
	print("[+] Writing all teh words to "+filepath)
	file = open(filepath, "a")

	for line in fullList:
		file.write(regex.sub('',line)+"\n")
	file.close
	print("[+] Oh shitz i think it worked?")
if __name__ == "__main__":
	main(sys.argv[1:])
	