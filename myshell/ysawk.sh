#!/bin/bash
echo '网站基本数据：'
dates=$(date -d last-day +%m%d);ysfilename='C:\Users\Administrator\Documents\spzs.com_2016'$dates'\usr\local\squid-3.4.14\var\logs\access.log.0';newfilename='bd/access'$dates'log';mv $ysfilename $newfilename;cd bd;