import os
import urllib
import urllib2
import socket
socket.setdefaulttimeout(None)
http_header = {"User-Agent":"Chrome"}
for nianji in range(13,15):
	strnianji='%d'%nianji
	f_dir = strnianji
	os.makedirs(r'./'+f_dir)
	for xueyuan in range(01,18):
		if xueyuan<10:
	 		strxueyuan = '0'+'%d'%xueyuan
	 	else:
	 		strxueyuan='%d'%xueyuan
	 	s_dir = f_dir+strxueyuan
	 	os.makedirs(r'./'+f_dir+'/'+s_dir)
	 	for zhuanye in range(01,10):
	 		if zhuanye<10:
	 			strzhuanye = '0'+'%d'%zhuanye
	 		else:
	 			strzhuanye='%d'%zhuanye
	 		t_dir = s_dir+strzhuanye
	 		os.makedirs(r'./'+f_dir+'/'+s_dir+'/'+t_dir)
	 		for banji in range(1,10):
	 			strbanji='%d'%banji
	 			fu_dir = t_dir+strbanji
	 			os.makedirs(r'./'+f_dir+'/'+s_dir+'/'+t_dir+'/'+fu_dir)
				for idf in (0,8,9):
					stridf = '%d'%idf
					for ids in range(1,120):
						if ids<10:
				 			strids = '00'+'%d'%ids
				 		elif 9<ids<100:
				 			strids ='0'+'%d'%ids
				 		else:
				 			strids = '%d'%ids
				 		url1 = 'http://my.xidian.edu.cn/ph/'+fu_dir+stridf+strids+'.jpg'
						url = urllib2.Request('http://my.xidian.edu.cn/ph/'+fu_dir+stridf+strids+'.jpg')  
						fcode = urllib.urlopen(url1).getcode()
						#print url
						if fcode == 200:
							try:
								print "downloading with pachong"+url1
								#urllib.urlretrieve(url, './'+f_dir+'/'+s_dir+'/'+t_dir+'/'+fu_dir+'/'+fu_dir+stridf+strids+'.jpg')
								f = urllib2.urlopen(url,timeout=10) 
								data = f.read() 
								with open('./'+f_dir+'/'+s_dir+'/'+t_dir+'/'+fu_dir+'/'+fu_dir+stridf+strids+'.jpg', "wb") as code:     
								    code.write(data) 
							except IOError as e:
	    							if e.message=="time out":
	        							continue