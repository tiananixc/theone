#encoding=utf-8                     
import sys,jieba
import jieba.analyse
reload(sys)
sys.setdefaultencoding('utf-8')

jieba.load_userdict('jiukw.txt')
with open('3211.txt','r') as f:
    fk=f.readline()
    print fk

