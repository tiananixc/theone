#!/bin/bash
LANG=C
dates=$1
logname='bd/access'$dates'.log'
arr=(Baiduspider sogou 360Spider google YisouSpider Macintosh)
for arrs in ${arr[@]};
do
	echo '--------------'$arrs'蜘蛛反馈码汇总---------------'
	grep -a $arrs $logname|awk '{print $6}'|awk -F'/' '{print $2}'|sort|uniq -c|sort -nr
done