#code utf-8
import urllib2
import urllib
def pachong(url):
	http_header = {"User-Agent":"Chrome"}
	values = {
	}
	data = urllib.urlencode(values)
	http_request = urllib2.Request(url,data,http_header)

	http_response = urllib2.urlopen(http_request)

	print http_response.code
	print http_response.info()
	print http_response.read()
if __name__ == "__main__":
	pachong("./pne.html")