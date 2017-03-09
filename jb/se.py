#encoding=utf-8
import sys,jieba,chardet
import jieba.analyse
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')
#数据库连接
conn = MySQLdb.connect (host = "127.0.0.1", user = "root", passwd = "root", db = "test")
cursor = conn.cursor ()

jieba.load_userdict('jiukw.txt')
f1=open('324.csv','w')
with open('12456.txt','r') as f:
    fk=f.readline()
    kw=fk.strip()
    tags = jieba.analyse.extract_tags(kw, topK=5000,withWeight=True)
    for tag, weight in tags:
        print "%s的权重值是：%s \n" %(tag, weight)
        f1.write("%s$%s\n" %(tag, weight))
        #tag1=tag.encode('utf-8')
        #print chardet.detect(tag1)
        #cursor.execute (" INSERT INTO weight(word,score) value ('%s','%s')"% (tag1,weight))


f1.close()
cursor.close ()
conn.close ()


#12.31 注：weight权重表的建立，是通过本页面生成200个词然后导入weight表中，200个词远远不够，1月4日导入5000条。