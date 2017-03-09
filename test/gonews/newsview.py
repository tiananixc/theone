#coding:utf-8

import requests,re,time,sys
#from multiprocessing.dummy import Pool as ThreadPool
#import multiprocessing
#import MySQLdb as mdb
from readability.readability import Document


reload(sys)
sys.setdefaultencoding('utf-8')

current_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))

def search(req,html):
    text = re.search(req,html)
    if text:
        data = text.group(1)
    else:
        data = ''
    return data

def number(content):
    text = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，:：。？、~@#￥%……&*（）“”《》]+".decode("utf8"), "".decode("utf8"),content)  #去除中英文标点符号
    text2 = re.sub('<[^>]*?>','',text)  #去除所有标签
    words_number = len(text2)
    return int(words_number)


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


    html = requests.get(url,headers=headers,timeout=30)
    code = html.encoding

    return html.content


def getContent(url):

    print '@@ start crawl %s @@@' % url

    html = getHTml(url)

    '''readability介入分析'''
    readable_article = Document(html).summary()
    readable_title = Document(html).short_title()

    a = re.sub(r'<script[\s\S]*?</script>|&#13;','',readable_article).strip()
    b = re.sub(r'<(?!p|img|/p|br|iframe)[^<>]*?>','',a).strip()
    c = re.sub(r'<p[^>]*?>','<p>',b).strip().replace('\n','')
    d = re.sub(r'<p>\s+<p>','',c)

    # 统计中文字数
    num = number(b)

    if num > 100:

        #sql = '''INSERT INTO newbaidu_detail_contont VALUES ('%s','%s','%s','%s')''' % (url,readable_title,d,current_date)
        getc=url+'\n'+readable_title+'\n'+d+'\n'+current_date+'\n'

        try:
           with open('news/'+readable_title+'.txt','w') as f2:
               f2.write(getc)
           print '执行成功'
        except Exception,e:
            print '执行失败,%s' % e

        return '成功'
    else:
        print url,num
        return '失败'

urls = []
with open('1.url','r') as f3:
    rows =f3.readlines()
    for row in rows:
        url = row.strip()
        urls.append(url)


for url in urls:
    getContent(url)
