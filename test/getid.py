# -*- coding: utf-8 -*-
import urllib,random,time
f1=open('bdf.txt','r').readlines()
f2=open('test.txt','r').readlines()
global yn

for r1 in f2:
	r11 = r1.strip()
	n1=r11.split('_')
	n11=n1[0]
	n12=n1[1]
	#print 'name',n12
	for r2 in f1:
		r22 =r2.strip()
		#print r22
		if r22 == n12 :
			yn = 'Y'
			# print r11,' YY ',r22
			
			# print n11,n12,r11
			break
		else:
			yn = 'N'
	#print yn
	#global yn
	if yn=='Y':
		ys = 'Y'
	else:
		ys = 'N'

	open('ffres.txt','a').write(n11+'\t'+n12+'\t'+ys+'\n')

