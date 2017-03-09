#coding:utf-8
 
import requests,re,time,sys,json,datetime
import multiprocessing
from lxml import etree
 
'''  
@@@@ 请依次传入三个参数：@@@
 
1、是否开启多进程（open或close）
2、查询客户端（pc或wap）
3、查询关键词文件路径
###tian.pro
4、可选查询前几页
 
case：python bdrank.py close pc keyword.txt 2
'''
 
progress,client,wordfile,sopage = sys.argv[1:5]

reload(sys)
sys.setdefaultencoding('utf-8')
datetime=time.strftime('%Y%m%d')
current_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
fileex=str(datetime)+client+'baidu_result'
outfilename=fileex+'_all_'+wordfile
resfilename=fileex+'_'+wordfile
outfile = open(outfilename,'w')
resfile = open(resfilename,'w')
def search(req,html):
    text = re.search(req,html)
    if text:
        data = text.group(1)
    else:
        data = 'no'
    return data
 
def number(content):
    text = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，:：。？、~@#￥%……&*（）“”《》]+".decode("utf8"), "".decode("utf8"),content)  #去除中英文标点符号
    text2 = re.sub('<[^>]*?>','',text)  #去除所有标签
    words_number = len(text2)
    return int(words_number)
 
def getHTml(url,client):
    global headers
    host = search('^([^/]*?)/',re.sub(r'(https|http)://','',url))
 
    if client == 'pc':
        headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, sdch",
            "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
            "Cache-Control":"no-cache",
            "Connection":"keep-alive",
            #"Cookie":"__cfduid=df26a7c536a0301ccf36481a14f53b4a81469608715; BIDUPSID=E9B0B6A35D4ABC6ED4891FCC0FD085BD; PSTM=1474352745; lsv=globalTjs_97273d6-wwwTcss_8eba1c3-routejs_6ede3cf-activityControllerjs_b6f8c66-wwwBcss_eabc62a-framejs_902a6d8-globalBjs_2d41ef9-sugjs_97bfd68-wwwjs_8d1160b; MSA_WH=1433_772; BAIDUID=E9B0B6A35D4ABC6ED4891FCC0FD085BD:FG=1; plus_cv=1::m:2a9fb36a; H_WISE_SIDS=107504_106305_100040_100100_109550_104341_107937_108437_109700_109794_107961_108453_109737_109558_109506_110022_107895_107917_109683_109588_110072_107318_107300_107242_100457; BDUSS=XNNMTJlWEdDdzFPdU1nSzVEZ1REYn4tNWNwZk94NVducXpaaThjWjE4bU1TQXRZQVFBQUFBJCQAAAAAAAAAAAEAAADLTBsKYTYzMTM4MTcwMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIy741eMu-NXQ; BDRCVFR[ltbVPlNi2ac]=mk3SLVN4HKm; BDRCVFR[C0p6oIjvx-c]=mbxnW11j9Dfmh7GuZR8mvqV; BDRCVFR[uLXjBGr0i56]=mbxnW11j9Dfmh7GuZR8mvqV; rsv_jmp_slow=1474644236473; sug=3; sugstore=1; ORIGIN=0; bdime=21110; H_PS_645EC=60efFRJ1dM8ial205oBcDuRmtLgH3Q6NaRzxDuIkbMkGVXNSHmXBfW0GZL4l5pnj; BD_UPN=123253; BD_CK_SAM=1; BDSVRTM=110; H_PS_PSSID=17947",
            "Host":host,
            "Pragma":"no-cache",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
        }
 
    elif client == 'wap':
        headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, sdch",
            "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
            "Cache-Control":"no-cache",
            "Connection":"keep-alive",
            #"Cookie":"__cfduid=df26a7c536a0301ccf36481a14f53b4a81469608715; BIDUPSID=E9B0B6A35D4ABC6ED4891FCC0FD085BD; PSTM=1474352745; plus_cv=1::m:2a9fb36a; BDUSS=XNNMTJlWEdDdzFPdU1nSzVEZ1REYn4tNWNwZk94NVducXpaaThjWjE4bU1TQXRZQVFBQUFBJCQAAAAAAAAAAAEAAADLTBsKYTYzMTM4MTcwMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIy741eMu-NXQ; BDRCVFR[ltbVPlNi2ac]=mk3SLVN4HKm; BDRCVFR[C0p6oIjvx-c]=mbxnW11j9Dfmh7GuZR8mvqV; BDRCVFR[uLXjBGr0i56]=mbxnW11j9Dfmh7GuZR8mvqV; lsv=globalTjs_97273d6-wwwTcss_bf2b167-routejs_6ede3cf-activityControllerjs_b6f8c66-wwwBcss_9f22dd4-framejs_38dd0ce-globalBjs_1c30bc8-sugjs_e1176fe-wwwjs_9f21ca8; H_WISE_SIDS=102065_100040_109672_102432_107851_109607_104340_106264_110031_108437_109699_107960_108453_109738_110201_110022_107896_109683_109668_109588_108013_107320_107242; MSA_WH=1433_216; MSA_PBT=92; MSA_ZOOM=1000; BAIDUID=8ADD01F376F3A0D29ED11B9D017537E9:FG=1; wpr=0; BDICON=10123156",
            "Host":host,
            "Pragma":"no-cache",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3",
        }
    else:
        print '查询客户端参数错误！！！！！'   
 
 
  # 代理服务器
    proxyHost = "proxy.abuyun.com"
    proxyPort = "9010"
 
    # 代理隧道验证信息
    proxyUser = "XXXX"
    proxyPass = "XXXX"
 
    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
      "host" : proxyHost,
      "port" : proxyPort,
      "user" : proxyUser,
      "pass" : proxyPass,
    }
 
    proxies = {
        "http"  : proxyMeta,
        "https" : proxyMeta,
    }
 
 
    html = requests.get(url,headers=headers,timeout=30)
    code = html.encoding
    return html.content
 
def date(timeStamp):
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime
 
def getContent(word,client,sopage):
    global ysr
    siteurl='19888.tv'
    srpage=str(sopage)+str(0)
    if client == 'pc':
        pcurl = 'http://www.baidu.com/s?q=&tn=json&ct=2097152&si=&ie=utf-8&cl=3&wd=%s&rn=%s' % (word,srpage)
        #print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ start crawl %s @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@' % word
        html = getHTml(pcurl,client)
 
        html_dict = json.loads(html)
        for tag in html_dict['feed']['entry']:
            if tag.has_key('title'):
                global rank
                title = tag['title']
                url = tag['url']
                rank = tag['pn']
                time = date(tag['time'])
                outfile.write('%s,%s,%s,%s,%s\n' % (word,rank,url,title,time))
                #print rank,url
                if siteurl in url:
                    print word,url,rank,time
                    ysr='Y'
                    resfile.write('%s,%s,%s,%s,%s\n' % (word,rank,url,title,time))
                    break
                else:
                    ysr='N'

        if ysr=='N':
            srtn='no field'
            rank='0'
            resfile.write('%s,%s,%s\n' % (word,srtn,srtn))
        return rank
 
    else:
        for sn in range(0,int(sopage)):

            wapurl = 'http://m.baidu.com/s?pn=%s&usm=2&word=%s&sa=np' % (sn,word)
            #print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ start crawl %s @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@' % word
            html = getHTml(wapurl,client)
     
            tree = etree.HTML(html) 
            div = tree.xpath('//*[@id="results"]/div')  # 通过xpath路径提取元素
            for line in div:
                line_html = etree.tostring(line)    #通过etree.tostring方法得到一个html
                #print line_html
     
                title = re.sub('<[^>]*?>','',search(r'<h3 class="c-title[^>]*?>([\s\S]*?)</h3>',line_html))
                rank = search(r'order="(\d+)"',line_html)
                domain = search(r'<div class="c-showurl c-line-clamp1"><span[^>]*?>(.*?)</span>',line_html)
                if domain == 'no':
                    domain = search(r'<div class="c-showurl">(.*?)\s+\d+k</div>',line_html)
                if domain == 'no':
                    domain = search(r'<span class="c-color-url">(.*?)</span>',line_html)
                if domain == 'no':
                    domain = search(r'<div class="c-color-url">(.*?)</div>',line_html)
                if domain == 'no':
                    domain = search('<span class="site">(.*?)</span>',line_html)
                if domain == 'no':
                    domain = search(r'<div class="c-showurl c-line-clamp1">(.*?) \d+k<span',line_html)
                if domain == 'no':
                    domain = '搜索特型'
                #print rank,domain
                outfile.write('%s,%s,%s\n' % (word,rank,domain))
                if siteurl in domain:
                    print word,domain,rank
                    ysr='Y'
                    resfile.write('%s,%s,%s\n' % (word,domain,rank))
                    break
                else:
                    ysr='N'
                #print ysr
            #print ysr,sn
            if ysr == 'Y':
                break
        print word,ysr
        if ysr=='N':
            srtn='no field'
            resfile.write('%s,%s,%s\n' % (word,srtn,srtn))
                    
        return 1
global dqtime
dqtime=time.strftime('%Y-%m-%d',time.localtime(time.time()))
resfiles = open('res.csv','a')
if progress == 'close':
    kwranks=''
    for word in open(wordfile):
        word = word.strip()
        #print word
        kwrank=getContent(word,client,sopage)
        #print kwrank
        kwranks+=str(kwrank)+'\t'
        time.sleep(5)
    print kwranks
    resfiles.write(dqtime+'\t'+kwranks+'\n')
 
elif progress == 'open':
    words = open(wordfile).readlines()
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    for word in words:
        pool.apply_async(getContent, (word,client,sopage))
    pool.close()
    pool.join()
    time.sleep(5)
 
else:
    print 'Error！！！progress 传参错误！！！'

resfiles.close()
outfile.close()
resfile.close()