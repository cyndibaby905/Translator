import urllib2
import json
import codecs
import re
import sys

def getPage(words,src,dest):
	url = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20google.translate%20where%20q%3D%22" + words +"%22%20and%20target%3D%22" + dest + "%22%20and%20source%3D%22" + src +"%22%3B&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="
	headers = { 'User-Agent' : 'Mozilla/5.0' }
	req = urllib2.Request(url, None, headers)
	response = urllib2.urlopen(req)
	return response.read()

def parseJsonResult(resultStr):
	result = json.loads(resultStr)
	resultArray = result['query']['results']['json']['json'][0]['json']
	str=""
	if type(resultArray) is dict:
		str+=resultArray['json'][0]
	else:
		for subDict in resultArray:
			str+=subDict['json'][0]	
	return str
	
 
if __name__ == "__main__":
	fileName = "Localizable.strings"
	destLanguage = "zh"
	srcLanguage = "en"
	if len(sys.argv) >= 4:
		fileName = sys.argv[1]
		srcLanguage = sys.argv[2]
		destLanguage = sys.argv[3]
	
	
	
	
	f = codecs.open(fileName, "r", "utf-16")
	for line in f:
		#The translation key
		pattern = re.compile(r'[\"\'].*[\"\']\s*=\s*[\"\'].*[\"\']')
		match = pattern.match(line)
		if match:
			src = line.split("=")[0].strip()
			namesPage = getPage(urllib2.quote(src[1:-1].encode('utf8')),srcLanguage,destLanguage)
			result = json.loads(namesPage)
			print src[1:-1] + ":" + parseJsonResult(namesPage)
			
	f.close()

	srcStr = """There are several ways to present the output of a program; data can be printed in a human-readable form, or written to a file for future use. This chapter will discuss some of the possibilities."""
	namesPage = getPage(urllib2.quote(srcStr.encode('utf8')),srcLanguage,destLanguage)
	result = json.loads(namesPage)
	
	print parseJsonResult(namesPage)
