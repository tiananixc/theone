# -*-coding:UTF-8-*- 
import urllib,urllib2,random,sys
import lxml.etree as etree
reload(sys)
sys.setdefaultencoding('utf-8')
def postdate(strr): 
	#定义一个要提交的数据数组(字典)
	#nstr=strr.strip()
	#nslist=nstr.split('_')
	data = {}
	data['proId'] = strr
	data['pageNum'] = '1'
	data['onlyImg'] = 'true'
	#data['Button1'] = '确定'
	#print nslist[0],nslist[1]
	 
	#定义post的地址
	url = 'http://www.jiuxian.com/pro/selectProEvaluate.htm'
	post_data = urllib.urlencode(data)
	 
	#提交，发送数据
	try:
		req = urllib2.urlopen(url, post_data)
		html = req.read()
		
		print 'Suc!'
		page = etree.HTML(html.lower().decode("utf-8", "replace"))

		ll = page.xpath(u'//li[@class="clearfix "]')
		print len(ll)
		pl=random.sample(ll, 3)
		for plitem in pl:
			lname = plitem.xpath(u'.//p[@class="name"]/text()')[0]
			lpc=lname.strip()+'评价：'
			pj = plitem.xpath(u'.//div[@class="reviews clearfix"]/p/text()')[0]
			lpc+=pj.strip()+'\n'
			with open('date1','a') as f:
				f.write(lpc)
			f.close()
	except Exception,e:
		print strr,e
	# inum = random.choice(range(8,20))
	# time.sleep(inum)

postdate(17669)