#coding:utf-8

import requests,re,time,sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

current_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
#print os.getcwd()
def search(req,html):
    text = re.search(req,html)
    if text:
        data = text.group(1)
    else:
        data = 'no'
    return data

def getHTml(url):

    host = search('^([^/]*?)/',re.sub(r'(https|http)://','',url))

    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, sdch",
        "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
        "Cache-Control":"no-cache",
        "Connection":"keep-alive",
        #"Cookie":"test_cookie_enable=null; __guid=9114931.3328104939189724000.1470120907720.1077; __huid=10b%2FlAllne5BlNqgNnq%2FeKB3A31jZx%2B7s3q05fZJUWb7M%3D; WDTKID=1736ed9baf299da6; test_cookie_enable=null; count=5; search_last_sid=ff6f4570334e52cf4d0b66709f98e6bc; search_last_kw=%u836F%u9152",
        "Host":host,
        "Pragma":"no-cache",
        #"Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
        }

    # 代理服务器
    proxyHost = "proxy.XXX.com"
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


    html = requests.get(url,headers=headers)
    html.encoding = "utf-8"
    return html.text


#con = mdb.connect(host="127.0.0.1",user="root",passwd="",db="heichan",charset='utf8');
#cur = con.cursor(mdb.cursors.DictCursor)

# '''抓取新闻详情页，获取详情页链接'''
j=0
for word in open('gonews/word').readlines():
    j+=1
    word = word.strip()
    svfile='gonews/'+str(j)+'.url'
    url = 'http://news.baidu.com/ns?ct=1&rn=50&ie=utf-8&rsv_bp=1&sr=0&cl=2&f=8&prevct=no&tn=newstitle&word=%s&pn=0' % word
    content=getHTml(url).encode('utf8')
    num = int(re.sub('约|,','',search(r'找到相关新闻(.*?)篇',content)))

    if num == 0:
        continue

    # 最多只抓前10页
    max_num = (num/50+1)*50
    if max_num > 1050:
        max_num = 1050
    geturlcontent=''
    for id in range(0,max_num,50):
        url = 'http://news.baidu.com/ns?ct=1&rn=50&ie=utf-8&rsv_bp=1&sr=0&cl=2&f=8&prevct=no&tn=newstitle&word=%s&pn=%s' % (word,id)
        print '@@@@@@@@@@@@@@@@@@@@@ >>>>>>> 当前抓取：%s' % url

        html = getHTml(url)
        for tag in re.findall(r'<div class="result title" id="\d+">([\s\S]*?)</div>',html):
            detail_url = search(r'<h3 class="c-title"><a href="(.*?)"',tag)

            #sql = '''INSERT INTO newbaidu_detail_url VALUES ('%s','%s','%s')''' % (word,detail_url,current_date)
            urlcontent=detail_url+'\n'
            geturlcontent+=urlcontent

        try:
            with open(svfile,'w') as f1:
                f1.write(geturlcontent)
            print '>>> sql执行成功 %s' % detail_url
        except Exception,e:
            print '>>> sql执行失败:%s' % e

            time.sleep(7)