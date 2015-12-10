#coding:utf-8
import requests
URL = 'http://rs.xidian.edu.cn/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'
headers = {"Host":"rs.xidian.edu.cn","Referer":"http://rs.xidian.edu.cn/portal.php","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36"}
data = {
	"username":"jsjhlk@163.com",
	"password":"78dc9c4bf25fdbef6d7339d013fdb49f",
	"quickforward":"yes",
	"handlekey":"ls"
}
