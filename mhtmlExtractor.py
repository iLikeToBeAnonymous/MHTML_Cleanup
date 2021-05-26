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

# tagPattern_root = "<title.*?>.*?</title.*?>"
tagPattern = "<li.*?>.*?</li.*?>"
# print(re.search(tagPattern_root, raw_mhtml, re.IGNORECASE))
#match_results = re.search(tagPattern, kindaClean, re.IGNORECASE)
#extractedText= match_results.group()
#extractedText = re.sub("<.*?>", "", extractedText) # Remove HTML tags

killTheSpans = re.compile("<span.*?></span>")
kindaClean = re.findall(tagPattern, kindaClean, re.IGNORECASE)
for eachEle in kindaClean:
    # print(re.sub("<.*?>","",(re.sub(killTheSpans, "", eachEle))))
    eachEle = (re.sub("<.*?>","",(re.sub(killTheSpans, "", eachEle))))
print(kindaClean)

#print(kindaClean)
#print(extractedText)


#cleanedMhtml = open("Output_Files\cleanedMhtml.html","w") # "w" overwrites the file if it exists, and creates it if it doesn't.
#cleanedMhtml.write(kindaClean)

#input("Hit 'return' to close")