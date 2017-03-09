#!--encode:utf-8--
import lxml.etree as etree
import urllib2
import sys,re,time
import socket,os
import httplib
socket.setdefaulttimeout(5)
reload(sys)
sys.setdefaultencoding('utf-8')
#baiduzz tuisong function
def tuisong():
    filecontents = open( "urls.txt", "r" ).read() 
    #print filecontents
    url = "/urls?site=www.19888.tv&token=Mt71rjB84lpiXmJX"
    conn = httplib.HTTPConnection('data.zz.baidu.com')
    conn.request(method="POST", url=url, body=filecontents)
    response = conn.getresponse()
    baiduresult = response.read()
    conn.close()
    return baiduresult
def getnum(rq):
	lists=re.findall(r"\d+\.?\d*",rq)
	ll=''
	for num in lists:
		ll+=str(num)
	return ll 

f1=open('date','r')
date=f1.read()
f1.close()
oldtimenum= getnum(date)
#print oldtimenum
f2=open('rooturl.txt','r')
urls=f2.readlines()
f2.close()
if os.path.exists('urls.txt'):
	os.remove('urls.txt')
f3=open('urls.txt','w')
j=0
yss=0
for ix,url in enumerate(urls) :
	if yss==1:
		break
	ss = url.strip()
	# if ix == 0:
	# 	global ix
	# 	wrurl=url
	print ss
	try:
		sock = urllib2.urlopen(ss)
		j+=1
	except Exception,e:
		print 'website is broken',e
		continue 
	html = sock.read()
	sock.close()
	page = etree.HTML(html.lower().decode("utf-8", "replace"))

	hrefs = page.xpath(u'//div[@class="tit"]')
	global firsthref
	
	if ix == 0:
		firsthref=hrefs[0].xpath(u'./a/@href')[0]
	for titclass in hrefs:
		# tittime=titclass.xpath(u'./span[@class="rq"]')
		# for ttt in tittime:
		# 	timenum = getnum(ttt.text)
		# 	#print timenum
		# if oldtimenum in timenum:
		# 	print 'findall'
		# 	break
		tita=titclass.xpath(u'./a/@href')
		titurl=tita[0]

		if oldtimenum in titurl:
			print 'findall'
			yss=1
			break
		newh='http://www.19888.tv'+titurl
		print newh
		f3.write(newh+'\n')
	time.sleep(5)
f3.close()
print str(j)+'	page get'
if j!=0:

	print tuisong()
	nowday=time.strftime('%Y%m%d')
	f4=open('date','w')
	f4.write(firsthref)
	f4.close()