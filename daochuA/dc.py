#!--encode:utf-8--
import lxml.etree as etree
import sys,re,socket,os,time,urllib2,chardet
socket.setdefaulttimeout(3)
reload(sys)
sys.setdefaultencoding('utf-8')

def getdomain(url):
	reg = r'^https?://([a-z0-9-.]+)[/?]?'	
	m = re.match(reg, url)
	uri = m.groups()[0] if m else ''
	link = uri[uri.find('.', 0, uri.rfind('.')) + 1:]
	return uri,link

# def ismake(filename):
# 	if os.path.exists(filename):
# 		os.remove(filename)
# 	else:
# 		print 'file making'

website=open('pages','r').readlines()
print len(website),' urls will check'
#website=['www.19888.tv','www.spzs.com']
#f=open('frendlink.txt','w')
f1=open('res.txt','w')
for index,s in enumerate(website,1):
	ss=s.strip()
	cl,dl=getdomain(ss)
	wl=[]
	try:
		#print ss
		sock = urllib2.urlopen(ss)
	except Exception,e:
		print ss,'website is broken'
		result = '%s is broken' %ss
		f1.write(result+'\n')
		time.sleep(5)
		continue
	html = sock.read()
	sock.close()
	page = etree.HTML(html.lower().decode("utf-8", "ignore"))
	hrefs = page.xpath(u"//a/@href")
	anum = len(hrefs)
	print anum
	cont=0
	wl=0
	for i in hrefs:
		if 'script' not in i:
			cont+=1
		if 'http' in i and dl not in i:
			wl += 1
			#print i
	result = '%s		have %s inlinks and %s outlinks' % (ss,cont,wl)
	f1.write(result+'\n')
	print result
	#print ss,'-end-'
	time.sleep(5)
f1.close()