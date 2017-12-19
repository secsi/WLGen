# WLGen
Wordlist generator capable of penetrating cloud flare

Based on the principle of CeWL but with the added use of the CFScrape library to get to sites hidden behind Cloud Flare.

############################################################ 
 Word List Generator v1.5
 Author: Dave Addison
############################################################ 
 USAGE: WLGen.py -u <http://site.com> -o <outputfile> -l 5
############################################################ 
 -u / --url:           The URL to target. Needs to include prefix of http(s)://
 -o / --output:        The target output file. By default it will print to screen
 -l / --length:        Desired length of words. By default this is 4+
###########################################################

you can also just print to screen ommiting the output parameter.

To Do:
+ Spidering internally to the nth level
