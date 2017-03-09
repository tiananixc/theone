#encoding=utf-8
import sys,jieba
import jieba.analyse
reload(sys)
sys.setdefaultencoding('utf-8')
jieba.load_userdict('jiukw.txt')
with open('k.txt','r') as f:
    fk=f.readlines()
with open('res01041.csv','w') as f1:
    for x,kw in enumerate(fk,1):
        kw=kw.strip()
        print x,kw
        tags = jieba.analyse.extract_tags(kw, topK=20)
        newtitle=''
        kws='/'.join(tags)
        tn=len(tags)
        for i,tag in enumerate(tags):
            if i>=tn-3 and i<tn-1:
                newtitle+=tag+'|'
            elif i==tn-1:
                newtitle+=tag
            else:
                pass
        res="%s_%s-中华名酒招商网"%(kw,newtitle)
        print "Title:%s"%(res)
        seg_list = jieba.cut(kw,cut_all=True)
        res2="|".join(seg_list)

        f1.write('%s$%s$%s$%s$%s\n'%(str(x),kw,kws,res,res2))



