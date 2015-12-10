import urllib
url = './my.xidian.edu.cn/ph/13060110001.jpg'  
print "downloading with urllib"
urllib.urlretrieve(url, "./test.jpg")