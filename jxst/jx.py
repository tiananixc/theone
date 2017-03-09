# -*-coding:UTF-8-*- 
import json,urllib2

url="http://act.jiuxian.com/act/selectPricebypids.htm?ids=3,&callback=handleListPrice&handleListPrice=jQuery16203082127552865588_1474970119762&_=1474970120046"
req = urllib2.Request(url)  #
#req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
r = urllib2.urlopen(req)
html1 = r.read() 
html=html1.replace('handleListPrice(\'','').replace('\')','')
print html
hdict=eval(html)
getdata=hdict['data']
#print getdata

for v in getdata.values():
	print v['np']
# encodedjson = json.dumps(html)
# decodejson = json.loads(encodedjson)
# print type(decodejson)

# dict='''{"status":1,"data":{"3":{"mp":1519,"endTimeLenstr":"1505353939000","endTimeLen":30382167,"sp":1099,"np":998},"22":{"mp":1099,"endTimeLenstr":"1504789769000","endTimeLen":29817978,"sp":829,"np":829}}}'''
# b=eval(dict)

# print type(b)