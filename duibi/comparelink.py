#!--encode:utf-8--
import sys
afile=sys.argv[1]
bfile=sys.argv[2]
f1=open(afile,'r')
fr1=f1.readlines()
f2=open(bfile,'r')
fr2=f2.readlines()
f3=open('res.csv','w')
for l1 in fr1:
	for l2 in fr2:
		if l1.strip() == l2.strip():
			# print l1
			# print l2
			# print l1.strip(),'	Y'
			f3.write(l1.strip()+'	Y'+'\n')
			break
		else:
			continue
