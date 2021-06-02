# coding: iso-8859-1

# The following is taken from the tutorial here: https://realpython.com/python-web-scraping-practical-introduction/

# In IDLE’s interactive window, type the following to import urlopen():
from urllib.request import urlopen
import re # so you can do regex stuff


url = "https://www.mcmaster.com/"

# To open the web page, pass url to urlopen():
page = urlopen(url)

# urlopen() returns an HTTPResponse object. To extract the HTML from the page, first use the HTTPResponse object's .read() method,
# the HTTPResponse object's .read() method, which returns a sequence of bytes...
html_bytes = page.read()

# Then use .decode() to decode the bytes to a string using UTF-8:
rtrvdHtml = html_bytes.decode("utf-8")

########################################
### EXTRACTING INNER HTML FROM A TAG ###
########################################

# tagPattern_root = "<title.*?>.*?</title.*?>"
tagPattern_root = "<div\sid\=\"catg\d+.*?>.*?</div.*?>"
print(re.search(tagPattern_root, rtrvdHtml, re.IGNORECASE))
#match_results = re.search(tagPattern_root, rtrvdHtml, re.IGNORECASE)
#extractedText= match_results.group()
#extractedText = re.sub("<.*?>", "", extractedText) # Remove HTML tags

#print(extractedText)

input("Hit 'return' to close")