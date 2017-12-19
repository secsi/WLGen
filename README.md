# WLGen
Wordlist generator capable of penetrating cloud flare

Based on the principle of CeWL but with the added use of the CFScrape library to get to sites hidden behind Cloud Flare.

usage: WLGen.py -u http://simpleinfosec.com -o '/file/path/to/save/to.txt'

you can also just print to screen ommiting the output parameter.

To Do:
+ Spidering internally to the nth level
+ Remove duplications in the lists
