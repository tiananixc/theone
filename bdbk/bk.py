# -*- coding: utf-8 -*- 
import urllib2
import socket,sys,random,time,os,re
import lxml.etree as etree
from useragent import pcualist
reload(sys)
sys.setdefaultencoding('utf-8')
#User Agent
def getua():

  User_Agent = pcualist()

  headers = { 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'freshGuide=1; BIDUPSID=7AD6B1F0076AD0D5E2810FF36119FB56; __cfduid=dbd033b635bd1268fdaefa87e2d34c1261470191700; PSTM=1472281639; BAIDUID=F44B09D83A8074889DE20E167B6F4EBB:FG=1; MCITY=-153%3A268%3A; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a02234882544; H_PS_PSSID=1468_20792_18240_21125_17001_20856_20733_20837_20885',
'Host':'baike.baidu.com',
'Referer':'http://baike.baidu.com/',
'Upgrade-Insecure-Requests':'1',
'User-Agent':User_Agent
              }
  return headers
def convert(ch):
    length = len('柯') #测试汉字占用字节数，utf-8，汉字占用3字节.bg2312，汉字占用2字节
    intord = ord(ch[0:1])
    if (intord >= 48 and intord <= 57):
        return ch[0:1]
    if (intord >= 65 and intord <=90 ) or (intord >= 97 and intord <=122):
        return ch[0:1].lower()
    ch = ch[0:length] #多个汉字只获取第一个
    with open(r'convert-utf-8.txt') as f:
        for line in f:
            if ch in line:
                return line[length:len(line)-2]
#去掉html
def gotdes(html):
  link = re.compile("<.*?>")
  info2 = re.sub(link,'',info)
  return info2

# f1=open('u.txt','r')
# gurls=f1.readlines()
# f1.close()
logsfile = 'logs'
nowday=time.strftime('%Y%m%d')
savefile = 'des'+nowday+'.csv'
if os.path.exists(savefile):
  os.remove(savefile)

with open('i.txt','r') as us:
  fs=us.readlines()

for x,gurl in enumerate(fs,1) :
  ur = gurl.strip()
  try:
    req = urllib2.Request(ur,headers=getua())  #
    #req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
    r = urllib2.urlopen(req)
    html = r.read() 
    print req.get_header('User-agent')    
    
    print 'YY',x,ur
    flog=open(logsfile,'a')
    flog.write(str(x)+'\t ###  \t'+ur+'\t ###  \tYY\n')
    flog.close()
    inum1 = random.choice(range(2,5))
    #print inum1
    time.sleep(inum1)
  except Exception,e:
    flog=open(logsfile,'a')
    flog.write(str(x)+'\t ###  \t'+ur+'\t ###  \tNN\n')
    flog.close()
    print 'NN',x,ur,e
    continue
  content = ''
  page = etree.HTML(html.lower())
  t=page.xpath('//h1/text()')
  #print len(t),'title'
  if len(t) == 0 :
    #pass
    continue
  tit= t[0]
  content+=tit.strip()+'#'

  des11=page.xpath('//div[@class="lemma-summary"]')
  if len(des11) == 0 :
    print 'n'
    continue

  #dessss=gotdes(info)
  des1=des11[0].xpath('string(.)')
  content+=des1.strip()+'#'
  content+=ur
  fres2=open(savefile,'a')
  fres2.write(content+'\n')
  fres2.close()
  inum = random.choice(range(3,9))
  time.sleep(inum)