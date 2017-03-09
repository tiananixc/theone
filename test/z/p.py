# -*-coding:UTF-8-*- 
import time
with open('f.txt','r') as f:
	fr = f.readlines()
with open('jx.txt','r') as f2:
	fr2 = f2.readlines()

for x,fl in enumerate(fr,1):
	fl = fl.strip()
	for i,fl2 in enumerate(fr2,1):
		fxl = fl2.split('#')[0]
		de = fl2.split('#')[1]
		print x,i
		if fl in fxl:
			print 's'
			with open('res.txt','a') as f3:
				f3.write(fl+'#'+fxl+'#'+de)

		#time.sleep(3)