import csv
import HTMLParser
import re

inFile = open('vw_ContentAggregation_ASSHWebIndex_ClinicalArticles.csv', "rb")
reader = csv.DictReader(inFile)
outFile = open('sample_out3.csv', "wb")
writer = csv.writer(outFile)

htmlParser = HTMLParser.HTMLParser()

#text = ""

for i, row in enumerate(reader):
    content = row["\xef\xbb\xbfcontent"]
    metaKeywords = row["metaKeywords"]
    if type(metaKeywords) is str and len(metaKeywords) > 4:
        #if metaKeywords != "NULL":
            print i, metaKeywords
            #metaKeywords = metaKeywords.split('~|~')
                    
            parsedContent = htmlParser.unescape(content)
            parsedContent = re.sub(r'<([^>]+)>', "", parsedContent)
            parsedContent = re.sub(r'&([^;]+);', "", parsedContent)
            
            result = [parsedContent, metaKeywords]
            writer.writerow(result)


inFile.close()
outFile.close()

