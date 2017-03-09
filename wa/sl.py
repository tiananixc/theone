#coding=utf-8

import requests
from BeautifulSoup import BeautifulSoup
import re
import useragent

headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, sdch",
    "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
    "Cache-Control":"no-cache",
    "Connection":"keep-alive",
    #"Cookie":"__cfduid=df26a7c536a0301ccf36481a14f53b4a81469608715; BIDUPSID=E9B0B6A35D4ABC6ED4891FCC0FD085BD; PSTM=1474352745; lsv=globalTjs_97273d6-wwwTcss_8eba1c3-routejs_6ede3cf-activityControllerjs_b6f8c66-wwwBcss_eabc62a-framejs_902a6d8-globalBjs_2d41ef9-sugjs_97bfd68-wwwjs_8d1160b; MSA_WH=1433_772; BAIDUID=E9B0B6A35D4ABC6ED4891FCC0FD085BD:FG=1; plus_cv=1::m:2a9fb36a; H_WISE_SIDS=107504_106305_100040_100100_109550_104341_107937_108437_109700_109794_107961_108453_109737_109558_109506_110022_107895_107917_109683_109588_110072_107318_107300_107242_100457; BDUSS=XNNMTJlWEdDdzFPdU1nSzVEZ1REYn4tNWNwZk94NVducXpaaThjWjE4bU1TQXRZQVFBQUFBJCQAAAAAAAAAAAEAAADLTBsKYTYzMTM4MTcwMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIy741eMu-NXQ; BDRCVFR[ltbVPlNi2ac]=mk3SLVN4HKm; BDRCVFR[C0p6oIjvx-c]=mbxnW11j9Dfmh7GuZR8mvqV; BDRCVFR[uLXjBGr0i56]=mbxnW11j9Dfmh7GuZR8mvqV; rsv_jmp_slow=1474644236473; sug=3; sugstore=1; ORIGIN=0; bdime=21110; H_PS_645EC=60efFRJ1dM8ial205oBcDuRmtLgH3Q6NaRzxDuIkbMkGVXNSHmXBfW0GZL4l5pnj; BD_UPN=123253; BD_CK_SAM=1; BDSVRTM=110; H_PS_PSSID=17947",
    "Host":"www.baidu.com",
    "Pragma":"no-cache",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":useragent.pcualist()
}  # 设置UA模拟用户，还可设置多个UA提高搜索成功率

def baidu_url(word): # 构建百度搜索URL；因为是查收录，所以只显示了前10个搜索结果，还可以通过rn参数来调整搜索结果的数量
    '''
    get baidu search url
    '''
    return 'http://www.baidu.com/s?wd=%s' % word


def baidu_cont(url):  # 获取百度搜索结果页内容
    r = requests.get(url, headers=headers)
    return r.content


def serp_links(word):  #获取百度搜索结果的最终URL
    '''
    get baidu serp links with the word
    '''
    b_url = baidu_url(word)
    soup = BeautifulSoup(baidu_cont(b_url))
    b_tags = soup.findAll('h3', {'class': 't'})  # 获取URL的特征值是通过class="t"
    b_links = [tag.a['href'] for tag in b_tags]
    real_links = []
    for link in b_links:  # 使用requests库获取了最终URL，而不是快照URL
        try:
            r = requests.get(link, headers=headers, timeout=120)
        except Exception as e:
            real_links.append('page404')
        else:
            real_links.append(r.url)
    return real_links


def indexer(url):  # 待查URL是否在百度搜索结果的URL列表中，如果在就表示收录，反之未收录
    indexed_links = serp_links(url)
    if url in indexed_links:
        return 'Y'
    else:
        return 'N'