# -*- coding: gbk -*-
import urllib2
import urllib,random,time,sys
reload(sys)
sys.setdefaultencoding('utf-8')

def postdate(strr): 
	#����һ��Ҫ�ύ����������(�ֵ�)
	nstr=strr.strip()
	print nstr
	#open('fff.txt','a').write(nstr)
	#print chardet.detect(nstr)
	nslist=nstr.split('_')
	data = {}
	data['__VIEWSTATE'] = '/wEPDwUKLTYyODEyMzMzMGRkz3sl/sYZLrxrzi9XilnTtY8yGWQ='
	data['txtId'] = nslist[0]
	data['txtOrderNum'] = nslist[1]
	data['Button1'] = 'ȷ��'
	print nslist[0],nslist[1]
	 
	#����post�ĵ�ַ
	url = 'http://www.spzs.com/tools/ptagupdate.aspx'
	post_data = urllib.urlencode(data)
	 
	#�ύ����������
	try:
		req = urllib2.urlopen(url, post_data)
		content = req.read()
		# with open('date','w') as f:
		# 	f.write(content)
		# f.close()
		print 'Suc!',nslist[0]
	except Exception,e:
		print nslist[0],e
	inum = random.choice(range(8,20))
	time.sleep(inum)

f=open('r.txt','r').readlines()
for num in f:
	#print num.strip()
	postdate(num)
