#!--encode:utf-8--
import lxml.etree as etree
import sys,re,socket,os,time,urllib2
import useragent
socket.setdefaulttimeout(3)
reload(sys)
sys.setdefaultencoding('utf-8')
def dcnum(url):
    ss=url.strip()
    reg = r'^https?://([a-z0-9-.]+)[/?]?'
    m = re.match(reg, url)
    uri = m.groups()[0] if m else ''
    link = uri[uri.find('.', 0, uri.rfind('.')) + 1:]
    # def ismake(filename):
    # 	if os.path.exists(filename):
    # 		os.remove(filename)
    # 	else:
    # 		print 'file making'
    cl=uri
    dl=link
    wl=[]
    try:
        #print ss
        sock = urllib2.urlopen(ss)
        html = sock.read()
        sock.close()
        page = etree.HTML(html.lower().decode("utf-8", "replace"))
        hrefs = page.xpath(u"//a/@href")
        anum = len(hrefs)
        cont=0
        wl=0
        for i in hrefs:
            if 'script' not in i:
                cont+=1
            if 'http' in i and dl not in i:
                wl += 1
                #print i
        result = 'have %s inlinks and %s outlinks' % (cont,wl)
    except Exception,e:
        result = 'is broken'
    return result
def sitedate(url):
    bru='http://www.link114.cn/get.php?baiduprzz&%s&71842'%url.strip()
    slu='http://www.link114.cn/get.php?baidu&%s&71152'%url.strip()

    headers = { 'Host': 'www.link114.cn',
                'Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': useragent.pcualist(),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'Cookie': 'bdshare_firstime=1488939027441 AlexaToolbar-ALX_NS_PH: AlexaToolbar/alx-4.0'
    }
    data = None
    try:
        request = urllib2.Request(bru,data,headers)
        sock1 = urllib2.urlopen(request)
        brt = sock1.read()
    except Exception,e:
        brt = 'broken'
        #result = 'have %s inlinks and %s outlinks' % (cont,wl)
    try:
        requests = urllib2.Request(slu,data,headers)
        sock1s = urllib2.urlopen(requests)
        slu = sock1s.read()
    except Exception,e:
        slu = 'broken'
        #result = 'have %s inlinks and %s outlinks' % (cont,wl)
    rest = 'br: %s,sl:%s'%(brt,slu)
    return rest