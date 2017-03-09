#encoding=utf-8
import sys,jieba
import jieba.analyse
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')
#数据库连接
conn = MySQLdb.connect (host = "127.0.0.1", user = "root", passwd = "root", db = "test")
cursor = conn.cursor ()
cursor.execute ("SELECT VERSION()")
row = cursor.fetchone ()
print "MySQL server version:", row[0]