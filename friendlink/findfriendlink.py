#!--encode:utf-8--
#查找友情链接
import lxml.etree as etree
import urllib2
import sys,re,time
import socket
socket.setdefaulttimeout(3)
reload(sys)
sys.setdefaultencoding('utf-8')

def getdomain(url):
	reg = r'^https?://([a-z0-9-.]+)[/?]?'	
	m = re.match(reg, url)
	uri = m.groups()[0] if m else ''
	link = uri[uri.find('.', 0, uri.rfind('.')) + 1:]
	return uri,link
def getbr(s):
	end1=s.rfind('.')
	end2=s.rfind('/')
	return s[end2+1:end1]
def getnum(s):
	reg = r'(\w*[0-9]+)\w*'	
	m = re.search(reg, s)
	i = m.groups()[0] if m else ''
	return i
def getbd(url):
	global sock
	allurl='http://check.links.cn/getbaidurank_ajax.asp?queryurl=http://'+url
	req = urllib2.Request(allurl)
	req.add_header('Referer', 'http://check.links.cn/')
	req.add_header('User-Agent',"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36")
	try:
		sock = urllib2.urlopen(req)
		#print '123'
	except Exception,e:
		print 'the website is broken',e
		return 'null','null'
	html = sock.read()
	sock.close()
	page = etree.HTML(html.lower().decode("utf-8", "replace"))

	ll = page.xpath(u"//a/text()")[0]
	br = page.xpath(u"//img/@src")[0]
	lll=getnum(ll)
	brs=getbr(br)
	return lll,brs

f=open('url.txt','r')
f1=f.readlines()
global f2

f2=open('ews.txt','w')
f2.write('site 	'+'friendlink 	'+'traffic 	'+'baidurank 	'+'\n')
def botreapet(arr):
	global wl
	wl = []
	for x,url in enumerate(arr):
		#print '<'+str(x)+'>'
		url = url.strip()
		print url
		print 
		link ='http://'+url
		xx,xxx=getdomain(link)
		#print link
		try:
			sock = urllib2.urlopen(link)
		except Exception,e:
			print 'the website is broken'
			continue 
		html = sock.read()
		sock.close()
		page = etree.HTML(html.lower().decode("utf-8", "replace"))

		hrefs = page.xpath(u"//a/@href")
		for i in hrefs:
			i = i.strip()
			if xxx not in i and 'http' in i:
				#print i
				ii,iii=getdomain(i)
				if ii not in wl:
					wl.append(ii)
					lls,brs=getbd(ii)
					f2.write(url+'	'+ii+'	'+lls+'	'+brs+'\n')
					print url,ii,lls,brs
					time.sleep(3)
	return wl

def gogogo(arr,n):
	j = 0
	while j <= n:
		#print str(j)+'--'*10
		j+=1
		#print len(arr)
		arr=botreapet(arr)
        time.sleep(5)		
		# print '---'
		# print len(arr)
		# print '****'
gogogo(f1,3)		
f2.close()
f.close()
