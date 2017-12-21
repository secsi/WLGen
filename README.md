# WLGen
Wordlist generator capable of penetrating cloud flare

Based on the principle of CeWL but with the added use of the CFScrape library to get to sites hidden behind Cloud Flare.

USAGE: 
WLGen.py -u <http://simpleinfosec.com> -o <outputfile> -l 5 -d 4

Word List Generator v1.5
Author: Dave Addison

-u / --url:       The URL to target. Needs to include prefix of http(s):// 

-o / --output:    The target output file. By default it will print to screen 

-l / --length:    Desired length of words. By default this is 4+ 

-d / --depth:     Desired depth of crawl. Default is 3

Get in touch with me at http://simpleinfosec.com for any issues.
