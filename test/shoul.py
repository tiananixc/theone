#coding: utf-8

import requests,threading,Queue,random,re,time,pycurl,StringIO,urllib

class CheckStatus(threading.Thread):
    def __init__(self, queue):
        super(CheckStatus, self).__init__()
        self.queue = queue
        self.op_txt=open('no_index.txt','a')
        self.daili_list=[]

    def getUA(self):
        uaList = [
            'Mozilla/4.0+(compatible;+MSIE+6.0;+Windows+NT+5.1;+SV1;+.NET+CLR+1.1.4322;+TencentTraveler)',
            'Mozilla/4.0+(compatible;+MSIE+6.0;+Windows+NT+5.1;+SV1;+.NET+CLR+2.0.50727;+.NET+CLR+3.0.4506.2152;+.NET+CLR+3.5.30729)',
            'Mozilla/5.0+(Windows+NT+5.1)+AppleWebKit/537.1+(KHTML,+like+Gecko)+Chrome/21.0.1180.89+Safari/537.1',
            'Mozilla/4.0+(compatible;+MSIE+6.0;+Windows+NT+5.1;+SV1)',
            'Mozilla/5.0+(Windows+NT+6.1;+rv:11.0)+Gecko/20100101+Firefox/11.0',
            'Mozilla/4.0+(compatible;+MSIE+8.0;+Windows+NT+5.1;+Trident/4.0;+SV1)',
            'Mozilla/4.0+(compatible;+MSIE+8.0;+Windows+NT+5.1;+Trident/4.0;+GTB7.1;+.NET+CLR+2.0.50727)',
            'Mozilla/4.0+(compatible;+MSIE+8.0;+Windows+NT+5.1;+Trident/4.0;+KB974489)',
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
            "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
        ]
        headers = random.choice(uaList)
        return headers
            

    def daili_cookie(self):
        cookie_list = [
            'BIDUPSID=4B0DC2F54860625BA83681F98C507951; BAIDUID=791ED7F86F43AF44A3808AB244404E1A:FG=1; PSTM=1441808712; BDUSS=RINjR4TVFBeHpKLTNIREJ4MkFUT0h3SFdFWlQwdHJIdlZORzc5aW00QWpnQ2hXQVFBQUFBJCQAAAAAAAAAAAEAAAAJkstJv7TXvMTj1NnM-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACPzAFYj8wBWd0; BDSFRCVID=tc4sJeC62wRkfgj40DCH-qjWNeMhJHrTH6aov8OLjxwzgCDAMXfsEG0Pt7lQpYD-MjrsogKK0mOTHUcP; H_BDCLCKID_SF=JJ4O_C-5tCv8fjrzhJbM-J3H-UnLq5btX57Z0lOnMp05jpjDjT823PFTKPKtaxTnW56uXRPyMn3zODO_e6-bDjQ3DaAs-460aK_X3bRVKbk_jR-k-PnVep8qQhbZKxJmMgkeoxJtJK-2SnbVKU5mytKXhq6qWnvN3mn2LIOFfDDbbDtxD5_32JLHqx5Ka43tHD7yWCvd-M75OR5JLn7nDUFdhpDJJpvm3Ibv3xQ73hbAVUnjqt8hXpjyyGCftj_JtnIeVb3HbTrMHJo1btQhq4tehHRJ553eWDTm_Do5LJvtenFmDMOTyKuLMRJwKxr3WebH-pPKKR7-bh7sMR7b24-dQ-QuXP5e3mkjbP-5aUj2oq-zXt6KKP4syP4j2xRnWNT2bIcJ-J8XhI86j5rP; BDRCVFR[ltbVPlNi2ac]=mk3SLVN4HKm; BD_HOME=1; BD_UPN=123253; sug=3; sugstore=1; ORIGIN=0; bdime=0; H_PS_645EC=5894fstaLnB%2Bx%2F1GkrMZWqKZiK7vVRh2YO9qL7vORnC1%2BY%2BbXOz%2BVwgRSuL80CXajur4; WWW_ST=1443000293566; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BD_CK_SAM=1; BDSVRTM=146; H_PS_PSSID=17143_16716_1431_17100_12824_14430_12867_17245_17104_17182_17000_17003_17073_15864_17348_12413_13932_17351_14924_17050',
            'BAIDUID=1F63B9A436CE0DBA3C7D1849367F30CB:FG=1; BIDUPSID=1F63B9A436CE0DBA3C7D1849367F30CB; PSTM=1441517552; BD_UPN=13314452; ispeed_lsm=10; ispeed=1; sug=3; ORIGIN=0; bdime=0; BDUSS=m5TYjhuODBCWHpQcVNYV2FDeS1BLUFzV0t3WTQwcTctUkV2S2x6M1ZBcjZMU2RXQVFBQUFBJCQAAAAAAAAAAAEAAAChsHQiuqPAtjIyOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPqg~1X6oP9Vc; H_PS_645EC=217efvXBesXqzUCKdQMslc2uc5TwenrsDDar8Tir0uHuQfpJAglN689%2BHSNYep8LeRTy; BD_HOME=1; H_PS_PSSID=16230_17326_1447_12657_12824_14432_12867_17246_17105_14952_17001_17004_17072_15713_17347_11798_13932_17352_14554_17051; __bsi=12190823682724921622_00_0_I_R_166_0303_C02F_N_I_I_0; sugstore=1',
            'Cookie: BAIDUID=1F63B9A436CE0DBA3C7D1849367F30CB:FG=1; BIDUPSID=1F63B9A436CE0DBA3C7D1849367F30CB; PSTM=1441517552; BDUSS=m5TYjhuODBCWHpQcVNYV2FDeS1BLUFzV0t3WTQwcTctUkV2S2x6M1ZBcjZMU2RXQVFBQUFBJCQAAAAAAAAAAAEAAAChsHQiuqPAtjIyOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPqg~1X6oP9Vc; H_PS_PSSID=16230_17326_1447_12657_12824_14432_12867_17246_17105_14952_17001_17004_17072_15713_17347_11798_13932_17352_14554_17051; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0'
        ]
        cookie = random.choice(cookie_list)
        return cookie


    def ip(self):
        for x in open('/root/aliyun/seo/daili.txt'):
            x = x.strip()
            self.daili_list.append(x)
        newip = random.choice(self.daili_list)
        return newip


    def getHtml(self,line,headers):
        # print u'开始获取网页源码'
        while 1:
            try:
                url = 'http://www.baidu.com/s?wd=%s' % urllib.quote_plus(line.strip())
                # newip = self.ip()
                # proxies={"http": "http://%s"%newip.strip()}
                # c = requests.post(url=url,headers=headers,proxies=proxies,timeout=30)
                # # c=requests.post(url,headers,timeout=10)
                # html = c.content
                c = pycurl.Curl()
                c.setopt(pycurl.MAXREDIRS,5)
                c.setopt(pycurl.REFERER, url)
                c.setopt(pycurl.FOLLOWLOCATION, True)
                c.setopt(pycurl.CONNECTTIMEOUT, 120)
                c.setopt(pycurl.TIMEOUT,120)
                c.setopt(pycurl.ENCODING,'gzip,deflate')
                #c.setopt(c.PROXY,ip)
                c.fp = StringIO.StringIO()
                c.setopt(pycurl.URL, url)
                c.setopt(pycurl.HTTPHEADER,headers)
                c.setopt(c.WRITEFUNCTION, c.fp.write)
                c.perform()
                code = c.getinfo(c.HTTP_CODE) #返回状态码
                html = c.fp.getvalue()
                if '="http://verify.baidu.com' in html:
                    print u'出验证码，重试'
                    continue
                elif '302 Found' in html or code != 200:
                    print u'代理失效，重试'
                    continue
                else:
                    return html
            except Exception, e:
                print e
                continue


    def run(self):
        while True:
            url = self.queue.get()
            status_index = self.getIndex(url)           


    def getIndex(self, url):
        # headers={
        #     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        #     'Accept-Encoding':'gzip, deflate, sdch',
        #     'Accept-Language':'zh-CN,zh;q=0.8',
        #     'Connection':'keep-alive',
        #     # 'Cookie':'%s'%self.daili_cookie(),
        #     'Host':'www.baidu.com',
        #     'Upgrade-Insecure-Requests':'1',
        #     'User-Agent':'%s' % self.getUA(),
        # }
        headers = [
            "Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding:gzip, deflate, sdch",
            "Accept-Language:zh-CN,zh;q=0.8,en;q=0.6",
            "Cache-Control:max-age=0",
            "Connection:keep-alive",
            #"Cookie:BAIDUID=18BFE1C8A802F8458F26D043CD7CD624:FG=1; BDUSS=lpaNUg2NkloQTBKVVh4aVBsczJNLUc2QjEzN05wMXUzeE50WXZSQVNaRmU3WlZWQVFBQUFBJCQAAAAAAAAAAAEAAAAJkstJv7TXvMTj1NnM-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF5gblVeYG5Vb; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a01833473155; BDSFRCVID=Vy8sJeCCxG3TKh3lHco6WY5CFWPhzzDzLlKH3J; H_BDCLCKID_SF=JbAjoKK5tKvbfP0kh-QJhnQH-UnLq5JIH67Z0lOnMp05ShvdDPv12bTL-q5mhU70LIbEXqbLBnRvOKO_e6t5D5J0jN-s-bbfHDJK0b7aHJOoDDvK2j75y4LdLp7xJh3i2n7QanOOJf3ZMqOD3p3s2RIv24vQBMkeWJQ2QJ8BJD_2hI3P; BIDUPSID=18BFE1C8A802F8458F26D043CD7CD624; PSTM=1433406316; BDRCVFR[ltbVPlNi2ac]=mk3SLVN4HKm; BD_UPN=123253; sug=3; sugstore=1; ORIGIN=0; bdime=0; H_PS_645EC=2002DrwijyvB4e2cepMJ9FuSgzu6vKJjbMOeRrfZjipiNRVem6mc9uqx%2FBzqlM7Z; BD_CK_SAM=1; BDSVRTM=14; H_PS_PSSID=13372_1428_14602_12772_14509_14444_10812_14600_12868_14622_10562_14501_12723_14626_14485_14244_11460_13936_8498
            "Host:www.baidu.com",
            "RA-Sid:7739A016-20140918-030243-3adabf-48f828",
            "RA-Ver:2.10.4",
            "User-Agent:%s" % self.getUA()
        ]   
        html = self.getHtml(url,headers)
        # print html
        if '抱歉，没有找到与' in html or '没有找到该URL' in html:
            
            print u'%s,未收录，写入文档'%url
            self.op_txt.writelines('%s\n'%url)

        else:
            print u'%s,已收录'%url

        self.queue.task_done()



def main():
    queue = Queue.Queue()
    for url in open("allurl.txt"):
        queue.put(url.strip())
    for i in range(10):
        t = CheckStatus(queue)
        t.setDaemon(True)
        t.start()

    queue.join()
    print "done."

if __name__ == '__main__':
    main()