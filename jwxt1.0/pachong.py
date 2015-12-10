import urllib
for nianji in range(13,15):
	strnianji='%d'%nianji
	for xueyuan in range(01,18):
		strxueyuan = '%d'%xueyuan
		for zhuanye in range(01,10):
			strzhuanye = '%d'%zhuanye
			for idf in (0,8,9):
				stridf = '%d'%idf
				for ids in range(0,120):
					strids = '%d'%idf
					url = 'http://my.xidian.edu.cn/ph/'+nianji+strxue+'.jpg'  
					print "downloading with urllib"
					urllib.urlretrieve(url, "./1314022/"+strxue+".jpg")