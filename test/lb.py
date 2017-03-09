# -*- coding: utf-8 -*-
import urllib2
import urllib,random,time

def postdate(): 
	#定义一个要提交的数据数组(字典)
	data = {'__VIEWSTATE':'/wEPDwUKMTg0OTA4MDM5Ng9kFgJmD2QWAgIBD2QWAgIBD2QWAgIDDw9kFgIeBVZhbHVlZWQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFHWN0bDAwJE1haW5Db250ZW50JGNieFJlbWVtYmVy+PT8xnnTfEawqVDiAEYGXDvJB04=',
'__EVENTVALIDATION':'/wEWBgKRyKDLDQLwkrODBALil++SAgK5ysLjCwKo36WDDQKRnIq9DwMkbemJvGjpIJD0LGAzxJ6h/DWg',
'ctl00$MainContent$tbxUserName':'tianshuaibing',
'ctl00$MainContent$tbxPassWord':'tianshuaibing123456',
'ctl00$MainContent$txtCode':'gztt'
}
	
	#print nslist[0],nslist[1]
	 
	#定义post的地址
	url = 'https://passport.baidu.com/'
	post_data = urllib.urlencode(data)
	 
	#提交，发送数据
	try:
		req = urllib2.urlopen(url, post_data)
		gcode=req.getcode()
		print gcode
		content = req.read()
		with open('date','w') as f:
			f.write(content)
		f.close()
		print 'Suc!',nstr
	except Exception,e:
		print e
	inum = random.choice(range(8,20))
	time.sleep(inum)

postdate()
