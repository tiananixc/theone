# -*- coding: utf-8 -*-
import urllib2
import urllib,random,time,requests
import lxml.etree as etree
def postdate(fl): 
	#定义一个要提交的数据数组(字典)
	data = {'formids':'TextField,Submit,Submit_0',
'submitmode':'submit',
'submitname':'',
'TextField':fl,
'Submit':'进入词条'
}
	
	#print nslist[0],nslist[1]
	 
	#定义post的地址
	url = 'http://baike.sogou.com/Search,$FinalBorder.$NewSearchBar.sf.sd'
	post_data = urllib.urlencode(data)
	 
	#提交，发送数据
	try:
		req = urllib2.urlopen(url, post_data)
		gcode=req.getcode()
		r = requests.get(url,allow_redirects=False)
		recode=r.status_code
		print gcode,recode
		content = req.read()
		if 'no_result_wrapper' in content :
			lx='Search page'
		else:
			lx='citiao'
		print lx
		with open('datesg','a') as f:
			f.write(fl+'\n'+lx)
		f.close()
		print 'Suc!'
	except Exception,e:
		print e
	# inum = random.choice(range(8,20))
	# time.sleep(inum)
with open('u360','r') as fs:
	fss = fs.readlines()
for i in fss:
	postdate(i.strip())
