#encoding=utf8
import urllib2
import socket,sys,random,time,os
reload(sys)
sys.setdefaultencoding('utf-8')
socket.setdefaulttimeout(3)
#User Agent
def getua():
  USER_AGENT_LIST = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
  ]


  #get proxy ip
  User_Agent =  random.choice(USER_AGENT_LIST)
  # header = {}
  # header['User-Agent'] = User_Agent

  headers = { 'Host':'www.jiuxian.com',
              'Connection':'keep-alive',
              'Cache-Control':'max-age=0',
              'Accept': 'text/html, */*; q=0.01',
              'X-Requested-With': 'XMLHttpRequest',
              'User-Agent': User_Agent,
              'DNT':'1',
              'Referer': 'http://www.baidu.com/',
              'Accept-Encoding': 'gzip, deflate, sdch',
              'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6'
              }
  return headers

url = "http://ip.chinaz.com/getip.aspx"
spurl=['http://www.spzs.com/','http://dw.spzs.com/','http://jk.spzs.com/listbizinfo/2890/','http://www.z.cn/']
if os.path.exists('fr.txt'):
  os.remove('fr.txt')

i=0
while i<20:
  fip=open('res.txt','r')
  ffip=fip.readlines()

  inum = random.choice(range(0,len(ffip)-1))
  proxy = ffip[inum]
  #print proxy
  fip.close()
  proxy_temp = {"http":proxy}

  indexnum = random.choice(range(0,3))
  gurl='http://www.jiuxian.com/'  #spurl[indexnum]
  #print gurl
  try:
    opener = urllib2.build_opener( urllib2.ProxyHandler(proxy_temp) )
    urllib2.install_opener( opener )
    res = urllib2.urlopen(gurl)
    print len(res)
    print type(res)
    tt=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    # print tt
    print 'YY',proxy,gurl
    fres=open('fr.txt','a')
    fres.write(tt+'  '+proxy.strip()+'  '+gurl.strip()+'  '+'\n')
    fres.close()
  except Exception,e:
    print 'NN',proxy,e
  i+=1
  time.sleep(5)



