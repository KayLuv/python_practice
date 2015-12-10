import urllib
import os
os.makedirs(r'./1306011')
for xuehao in range(13060110001,13060110050):
	strxue='%d'%xuehao
	url = 'http://my.xidian.edu.cn/ph/'+strxue+'.jpg'  
	print "downloading with urllib"
	urllib.urlretrieve(url, "./1306011/"+strxue+".jpg")