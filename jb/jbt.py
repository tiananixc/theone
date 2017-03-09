#encoding=utf-8
import sys,jieba
import jieba.analyse
reload(sys)
sys.setdefaultencoding('utf-8')
jieba.load_userdict('jiukw.txt')
with open('k.txt','r') as f:
    fk=f.readlines()
with open('res0104.csv','w') as f1:
    for x,kw in enumerate(fk,1):
        kw=kw.strip()
        tags = jieba.analyse.extract_tags(kw, topK=20)
        ks=''
        for i,tt in enumerate(tags):
            if i<2:
                ks+=tt+'|'
            elif i==2:
                ks+=tt

        kws='|'.join(tags)
        print x,kw+'_'+ks
        seg_list = jieba.cut(kw,cut_all=True)
        res="/".join(seg_list)
        f1.write('%s$%s$%s\n'%(str(x),kw,kws))



