#coding:utf-8
import requests
import re
for num in range(1,50):
	str_num='%d'%num
	url = 'http://www.ruanyifeng.com/images_pub/pub_'+str_num+'.jpg'
	html = requests.get(url).text
	with open("./"+str_num+".jpg", "wb") as code:
		code.write(html)
	print str_num+'.jpg downloaded'
	# title = re.findall('target="_blank">(.*?)</a>',html,re.S) 
	# for each in title:
	# 	print each