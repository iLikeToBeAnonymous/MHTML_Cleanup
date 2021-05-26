# coding: utf-8

import re # so you can do regex stuff

myDataPath = "ReferencePages—McMaster-Carr"
mySourceFile = "McMaster-Carr.mhtml"
mhtml_source = open(myDataPath + "/" + mySourceFile,"r") #open the source file

raw_mhtml = mhtml_source.read() # reads data into the variable.



newlinePattern = re.compile("[\r\n]+")
kindaClean = re.sub(newlinePattern, "", raw_mhtml) # delete all newline chars

## Add newlines back in by splitting at the closing tag
#kindaClean = re.sub("><", ">\n<", kindaClean)

# li_tag_pattern_root = "<title.*?>.*?</title.*?>"
li_tag_pattern = "<li.*?>.*?</li.*?>"
# print(re.search(li_tag_pattern_root, raw_mhtml, re.IGNORECASE))
#match_results = re.search(li_tag_pattern, kindaClean, re.IGNORECASE)
#extractedText= match_results.group()
#extractedText = re.sub("<.*?>", "", extractedText) # Remove HTML tags

cleanedLineList = [] # Remember, it's a Python list, NOT a Python array.
# killTheSpans = re.compile("<span.*?></span>") # Alternatively, you could try the line below (which allows for the random "=" sign...)
# killTheSpans = re.compile("<[span\=]{4,5}\s.*?></span>")
killTheSpans = re.compile("<\=?s\=?p\=?a\=?n.*?>\=?<\=?/\=?s\=?p\=?a\=?n.*?>") #Seems most accurate, but also very specific.
killTheLinks = re.compile("h\=?r\=?e\=?f\=3D.*?>")
killFrstLiTag = re.compile("<\=?l\=?i\=?>|<\/\=?l\=?i\=?>")
fix_A_Tags = re.compile("^\=<a\s|^<\=a\s|^<a\=\s|^<a\s\=|^<a\s")
fix_ampersands = re.compile("\&amp;|&\=amp;")

kindaClean = re.findall(li_tag_pattern, kindaClean, re.IGNORECASE)
for eachEle in kindaClean:
    # Editing eachEle doesn't modify kindaClean, but it does modify it long enough to perform other ops on it.
    # Also, these lines can be stacked, but they're separate for testing purposes.
    eachEle = re.sub("\=\=", "=", eachEle) # There are double-equals for some reason.
    eachEle = re.sub(killTheSpans, "", eachEle)
    eachEle = re.sub(killTheLinks, "", eachEle)
    eachEle = re.sub(killFrstLiTag, "", eachEle)
    eachEle = re.sub(fix_ampersands, "and", eachEle) # Fix the html ampersands
    eachEle = re.sub(fix_A_Tags, "<a> ", eachEle)
    #if (bool(re.search("ref", eachEle))): print(eachEle)
    cleanedLineList.append(eachEle)
    #cleanedLineList.append(re.sub("<.*?>","",(re.sub(killTheSpans, "", eachEle))))

for eachEle in cleanedLineList: print(eachEle)

#print(kindaClean)
#print(extractedText)


#cleanedMhtml = open("Output_Files\cleanedMhtml.html","w") # "w" overwrites the file if it exists, and creates it if it doesn't.
#cleanedMhtml.write(kindaClean)

#input("Hit 'return' to close")