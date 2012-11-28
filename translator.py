import urllib2
import json

def getPage(words,src,dest):
	url = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20google.translate%20where%20q%3D%22" + words +"%22%20and%20target%3D%22" + dest + "%22%20and%20source%3D%22" + src +"%22%3B&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="
	headers = { 'User-Agent' : 'Mozilla/5.0' }
	req = urllib2.Request(url, None, headers)
	response = urllib2.urlopen(req)
	return response.read()
 
if __name__ == "__main__":
	namesPage = getPage(urllib2.quote("""Python is a programming language that lets you work more quickly and integrate your systems more effectively. You can learn to use Python and see almost immediate gains in productivity and lower maintenance costs.""".encode('utf8')),'en','zh')
	result = json.loads(namesPage)
	resultArray = result['query']['results']['json']['json'][0]['json']
	str=""
	if type(resultArray) is dict:
		str+=resultArray['json'][0]
	else:
		for subDict in resultArray:
			str+=subDict['json'][0]	
	print str
