# coding: iso-8859-1

# The following is taken from the tutorial here: https://realpython.com/python-web-scraping-practical-introduction/

# In IDLE’s interactive window, type the following to import urlopen():
from urllib.request import urlopen
import re # so you can do regex stuff


url = "http://olympus.realpython.org/profiles/aphrodite"

# To open the web page, pass url to urlopen():
page = urlopen(url)

# urlopen() returns an HTTPResponse object. To extract the HTML from the page, first use the HTTPResponse object's .read() method,
# the HTTPResponse object's .read() method, which returns a sequence of bytes...
html_bytes = page.read()

# Then use .decode() to decode the bytes to a string using UTF-8:
rtrvdHtml = html_bytes.decode("utf-8")

## BASIC PAGE RETURN ##
## Now you can print the HTML to see the contents of the web page:
# print(rtrvdHtml)

##########################
### EDITED PAGE RETURN ###
##########################

### REPLACE ALL TAGS WITH SOMETHING ###
## The asterisk/question mark combo below tells Python to return the shortest possible match.
## using re.compile is faster if using the pattern repeatedly.
## myPattern = re.compile("<.*?>") 

## The below line uses a regex substitution, replacing matches to "myPattern" with the 
## string "ELEPHANTS" as sourced from the variable "rtrvdHtml"
#editedHtml = re.sub(myPattern, "ELEPHANTS", rtrvdHtml)

#print(editedHtml)

########################################
### EXTRACTING INNER HTML FROM A TAG ###
########################################

tagPattern = "<title.*?>.*?</title.*?>"
match_results = re.search(myPattern, rtrvdHtml, re.IGNORECASE)
extractedTitle = match_results.group()
extractedTitle = re.sub("<.*?>", "", extractedTitle) # Remove HTML tags

print(extractedTitle)

input("Hit 'return' to close")