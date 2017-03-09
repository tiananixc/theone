# -*-encoding:utf8-*-
#python版本：2.7
#作用：采集2次百度百科初始网址右侧相关信息
#lemmaId中的ID 自己从抓包数据里找



import requests
import json

# 初始url随便改


links = set()
new_link = set()

def request(x,next_set=None):
    req = requests.get(x).text
    rez = json.loads(req)
    if rez:
        for a in range(0, len(rez)):
            for x in rez[a]['data']:
                if next_set == 0:
                    print x['title'], x['url'], 'id=' + x['lemmaId']  # 解析打印json数据
                    links.add('http://baike.baidu.com/wikiui/api/zhixinmap?lemmaId=' + x['lemmaId'])

                else:
                    print x['title'], x['url'], 'id=' + x['lemmaId']  # 解析打印json数据
                    new_link.add('http://baike.baidu.com/wikiui/api/zhixinmap?lemmaId=' + x['lemmaId'])
        return [links,new_link]
    else:
        pass


def start_url(url):
    if type(url) == set:
        for x in url:
            request(x,next_set=1)
    else:
        get_id = request(url,next_set=0)[0]
        start_url(get_id)


if __name__ == '__main__':
    start_url('http://baike.baidu.com/wikiui/api/zhixinmap?lemmaId=4608035')
