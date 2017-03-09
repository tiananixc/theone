#!/usr/bin/python
# -*- coding: utf-8 -*-

import sl,getdc,time

f1=open('link.txt','r')
for l in f1.readlines():
    ls=l.strip()
    sll=sl.indexer(ls)
    #sdn=getdc.sitedate(ls)
    sdc=getdc.dcnum(ls)
    print ls,sll,sdc
    time.sleep(5)