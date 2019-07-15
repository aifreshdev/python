import os
import urllib.request as urllib2 
import re
import string
from flask import Flask

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def queryInfoUrl():
	header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    }

	url = urllib2.Request('https://m.hkgolden.com/topics.aspx?type=CA', headers = header)
	connect = urllib2.urlopen(url)
	html = connect.read().decode('utf-8', 'ignore')
	pattern = re.compile('<div class="topic-title">(.*?)</div>', re.S)
	items = re.findall(pattern, html)
	# str = ''.join(items)
	return html

if __name__ == "__main__":
	app.run(host = '0.0.0.0', port = 5001, debug = True)