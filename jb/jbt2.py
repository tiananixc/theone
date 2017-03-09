#encoding=utf-8
import sys,jieba,MySQLdb,chardet
import jieba.analyse
reload(sys)
sys.setdefaultencoding('utf-8')
#数据库连接
conn = MySQLdb.connect (host = "127.0.0.1", user = "root", passwd = "root", db = "test")
cursor = conn.cursor ()

jieba.load_userdict('jiukw.txt')
with open('k.txt','r') as f:
    fk=f.readlines()
with open('res.csv','w') as f1:
    for x,kw in enumerate(fk,1):
        if x>20:
            break
        else:
            kw=kw.strip()
            print x,kw
            tags = jieba.analyse.extract_tags(kw, topK=20,withWeight=True)
            kws=''
            score=''
            total=0
            for tag, weight in tags:
                kws+=tag+'/'
                tag1=tag.encode('utf-8')
                #kws='/'.join(tags)
                cursor.execute ("select score from weight where word like '%s'"% tag1)
                row = cursor.fetchone ()
                print row[0]
                if row :
                    score += str(row[0])+'|'
                    total += float(row[0])
                    print tag,total,'321'
                else :
                    print tag,' no index'
            print '%s$%s$%s$%s\n'%(kw,kws,score,total)

        #            seg_list = jieba.cut(kw,cut_all=True)
        #            res="|".join(seg_list)
        #f1.write('%s$%s$%s$%s\n'%(str(x),kw,kws,res))


#weight权重表词不完善，等完善后再进行匹配赋值  12.31



