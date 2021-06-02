# coding: utf-8

import re # so you can do regex stuff

myDataPath = "ReferencePages—McMaster-Carr"
mySourceFile = "Product_names_only.csv"
loaded_file = open(myDataPath + "/" + mySourceFile,"r") #open the source file

# raw_data = loaded_file.read() # reads data as a complete blob into the variable.
raw_data_array = loaded_file.readlines() # data is read into the raw_data array. Each line is an array element.

whitespaceSplit = [] # Initialize an empty array
extraWhitespcPtrn = re.compile('(\"|\').*?(\"|\')')
for eachRow in raw_data_array:
    eachRow = re.sub("\s+"," ",eachRow) # remove double/triple etc spaces and replace with a single space.
    #Section to check for and remove beginning and ending quotes.
    #if eachRow[0] == '"': # If starting char is a quotation mark
    #    eachRow = eachRow[1:] # removes the first double-quote by returning the string from the 2nd char to the end of the string.
    #if eachRow[len(eachRow)-1] == '"':
    #    eachRow = eachRow[1:] # removes the first double-quote by returning the string from the 2nd char to the end of the string.
    # Above two "if" statements are replaced by a more versatile version:
    if re.match(extraWhitespcPtrn, eachRow): # https://www.guru99.com/python-regular-expressions-complete-tutorial.html#5
        eachRow = eachRow[1:(len(eachRow)-2)] # removes the first and last quotes by returning the string from the 2nd char to the 2nd from end of the string.
    whitespaceSplit.append(eachRow.split(" ")) # split each row into an array delimted by whitespace

#####################################################################################
###     THE PYTHON DICTIONARY SEEMS EQUIVALENT TO THE JAVASCRIPT MAP() OBJECT     ###
###    https://www.w3schools.com/python/python_dictionaries.asp                   ###
###    https://realpython.com/python-json/                                        ###
###    https://www.geeksforgeeks.org/how-to-convert-python-dictionary-to-json/    ###
#####################################################################################


#myStrTemplate = 'Name: {}\nHas a length of {}' # https://www.w3schools.com/python/python_string_formatting.asp
#print(myStrTemplate.format("long",len("long")))

for eachEle in whitespaceSplit: 
    print(eachEle)


#newlinePattern = re.compile("[\r\n]+") # Counts \r or \n or any combination thereof as a newline pattern.
## kindaClean = re.sub(newlinePattern, "", loaded_file) # Delete all newline chars using the above pattern.
#kindaClean = re.sub("><", ">\n<", kindaClean)

##cleanedMhtml = open("Output_Files\cleanedMhtml.html","w") # "w" overwrites the file if it exists, and creates it if it doesn't.
##cleanedMhtml.write(kindaClean)

## li_tag_pattern_root = "<title.*?>.*?</title.*?>"
## print(re.search(li_tag_pattern_root, raw_data, re.IGNORECASE))
##match_results = re.search(li_tag_pattern, kindaClean, re.IGNORECASE)
##extractedText= match_results.group()
##extractedText = re.sub("<.*?>", "", extractedText) # Remove HTML tags

#cleanedLineList = [] # Remember, it's a Python list, NOT a Python array.

#li_tag_pattern = "<li.*?>.*?</li.*?>"
## killTheSpans = re.compile("<span.*?></span>") # Alternatively, you could try the line below (which allows for the random "=" sign...)
## killTheSpans = re.compile("<[span\=]{4,5}\s.*?></span>")
#killTheSpans = re.compile("<\=?s\=?p\=?a\=?n.*?>\=?<\=?/\=?s\=?p\=?a\=?n.*?>") #Seems most accurate, but also very specific.
#killTheLinks = re.compile("h\=?r\=?e\=?f\=3D.*?>")
#killFrstLiTag = re.compile("<\=?l\=?i\=?>|<\/\=?l\=?i\=?>")
#fix_A_Tags = re.compile("^\=<a\s|^<\=a\s|^<a\=\s|^<a\s\=|^<a\s")
#fix_ampersands = re.compile("\&amp;|&\=amp;")

#kindaClean = re.findall(li_tag_pattern, kindaClean, re.IGNORECASE)
#for eachEle in kindaClean:
#    # Editing eachEle doesn't modify kindaClean, but it does modify it long enough to perform other ops on it.
#    # Also, these lines can be stacked, but they're separate for testing purposes.
#    eachEle = re.sub("\=\=", "=", eachEle) # There are double-equals for some reason.
#    eachEle = re.sub(killTheSpans, "", eachEle)
#    eachEle = re.sub(killTheLinks, "", eachEle)
#    eachEle = re.sub(killFrstLiTag, "", eachEle)
#    eachEle = re.sub(fix_ampersands, "and", eachEle) # Fix the html ampersands
#    eachEle = re.sub(fix_A_Tags, "<a> ", eachEle)
#    #if (bool(re.search("ref", eachEle))): print(eachEle)
#    cleanedLineList.append(eachEle)
#    #cleanedLineList.append(re.sub("<.*?>","",(re.sub(killTheSpans, "", eachEle))))

##for eachEle in cleanedLineList: print(eachEle)

##print(kindaClean)
##print(extractedText)


##cleanedMhtml = open("Output_Files\cleanedMhtml.html","w") # "w" overwrites the file if it exists, and creates it if it doesn't.
##cleanedMhtml.write(kindaClean)

##input("Hit 'return' to close")