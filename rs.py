#coding:utf-8
import requests
import re
url = 'http://rs.xidian.edu.cn/portal.php'
html = requests.get(url).text
title = re.findall('target="_blank">(.*?)</a>',html,re.S) 
for each in title:
	print each