#!--encode:utf-8--
import lxml.etree as etree
import urllib2
import sys,re
import socket,os
socket.setdefaulttimeout(3)
reload(sys)
sys.setdefaultencoding('utf-8')

def getdomain(url):
	reg = r'^https?://([a-z0-9-.]+)[/?]?'	
	m = re.match(reg, url)
	uri = m.groups()[0] if m else ''
	link = uri[uri.find('.', 0, uri.rfind('.')) + 1:]
	return uri,link

def ismake(filename):
	if os.path.exists(filename):
	    os.remove(filename)
	else:
		print 'file making'


website=['www.19888.tv','www.spzs.com']
#f=open('frendlink.txt','w')
for index,s in enumerate(website,1):
	ismake('frendlink'+str(index)+'.txt')
	f=open('frendlink'+str(index)+'.txt','w')
	ss='http://'+s
	cl,dl=getdomain(ss)
	wl=[]
	try:
		sock = urllib2.urlopen(ss)
	except Exception,e:
		print 'website is broken'
		continue 
	html = sock.read()
	sock.close()
	page = etree.HTML(html.lower().decode("utf-8", "replace"))

	hrefs = page.xpath(u"//a/@href")
	for i in hrefs:
		i = i.strip()
		if dl not in i and 'http' in i:
			ii,url=getdomain(i)
			if ii not in wl:
				wl.append(ii)
				f.write(ii+'\n')
				#print ii
	ismake(s+'.txt')
	f1=open(s+'.txt','w')
	for ll in wl:
		global isok
		ll=ll.strip()
		try:
			sock1 = urllib2.urlopen('http://'+ll)
		except Exception,e:
			print ll+'	urlbroken!'
			f1.write(ll+'	urlbroken!'+'\n')
			continue
		html1 = sock1.read()
		sock1.close()
		page1 = etree.HTML(html1.lower().decode("utf-8", "replace"))

		hrefs1 = page1.xpath(u"//a/@href")
		for iii in hrefs1:
			#print '---'+iii+'***'
			iii = iii.strip()
			if s in iii:
				isok ='	Y'
				print ll,isok
				f1.write(ll+isok+'\n')
				break
			else:
				pass
			
	f1.close()
f.close()
