#coding: utf-8
import urllib2
import urllib
import time
def pachong(url):
	http_header = {
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Encoding":"gzip, deflate",
		"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
		"Cache-Control":"max-age=0",
		"Connection":"keep-alive",
		"Content-Length":"262",
		"Content-Type":"application/x-www-form-urlencoded",
		"Cookie":"RK=vVNHbDDcVX; pgv_pvi=4013387776; o_cookie=925334473; ptwebqq=71baf5b532e2288397b40bab78d688a228104a87143f66770452744e728194bd; zzpaneluin=; zzpanelkey=; qzspeedup=sdch; pt_clientip=68b3718c1d0c0b3b; pt_serverip=c25c0aab3d472544; ptui_loginuin=645297147; pt2gguin=o0645297147; uin=o0645297147; skey=@GaUMnv56k; ptisp=ctc; ptcz=cb52bb6507cac08fb80991db925e6c1ec331ace612c2c035c15ec281a8707f44; p_skey=Gpzw5Gc81sOPZXxGBr9hbjJfPrCojhC3-qsrRsrdSTw_; pt4_token=H5e3z1hW-Wnp0WfiJDbXGg__; __Q_w_s__appDataSeed=1; verifysession=h01bc305304cb9b1ffe12f3d780f90283aca568bf8d90de51ee2a02355dfb117c6278d6bab5e63418cd; __Q_w_s_hat_seed=1; __Q_w_s__QZN_TodoMsgCnt=1; pgv_info=ssid=s1239484468; pgv_pvid=9868165900; Loading=Yes; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=10; rv2=8098C517CE77534F164514605537B38BEE0C13983FE4161375; property20=559A3A71E46A9BB5A1344B1C20864040C6B922BCBBAB5B539894FCE9010E66070FBCEA8189D7D0E9; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; qzmusicplayer=qzone_player_1049562126_1432702739838; blabla=dynamic",
		"Host":"m.qzone.qq.com",
		"Origin":"http://ctc.qzs.qq.com",
		"RA-Sid":"7B8A4F09-20150427-140137-8903cc-356c3b",
		"RA-Ver":"2.10.4",
		"Referer":"http://ctc.qzs.qq.com/qzone/msgboard/msgbcanvas.html",
		"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36"
	}
	values = {
		"qzreferrer":"http://ctc.qzs.qq.com/qzone/msgboard/msgbcanvas.html#page=1",
		"content":"大神,带我飞",
		"hostUin":"1049562126",
		"uin":645297147,
		"format":"fs",
		"inCharset":"utf-8",
		"outCharset":"utf-8",
		"iNotice":1,
		"ref":"qzone",
		"json":1,
		"g_tk":1451405705
	}
	data = urllib.urlencode(values)
	http_request = urllib2.Request(url,data,http_header)

	http_response = urllib2.urlopen(http_request)

	print http_response.code
	print http_response.info()
	print http_response.read()
if __name__ == "__main__":
	while(1):
		pachong("http://m.qzone.qq.com/cgi-bin/new/add_msgb?g_tk=1451405705")
		time.sleep(1)