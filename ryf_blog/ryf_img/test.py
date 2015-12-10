import urllib
for num in range(1,50):
	str_num='%d'%num
	url = 'http://www.ruanyifeng.com/images_pub/pub_'+str_num+'.jpg' 
	print "downloading with urllib"
	urllib.urlretrieve(url, "./"+str_num+".jpg")