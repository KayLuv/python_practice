import os
#os.makedirs(r'./1306011')
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
	 		# for idf in (0,8,9):
	 		# 	stridf = '%d'%idf
	 		# 	for ids in range(0,120):
	 		# 		strids = '%d'%idf
					