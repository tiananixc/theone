#!/bin/bash
date=$1
cd bd
awk '$9~/www\.19888\.tv/' 'bd'$date'.log' |sed 's/:90//g'>bd9www.log
wwwnum=`cat bd9www.log|wc -l`
echo 'www数量：'$wwwnum
echo '抓取量最大的页面：'
awk '{print $9}' bd9www.log|sort|uniq -c|sort -nr |head -30
echo '页面反馈码：'
awk '{print $6}' bd9www.log|awk -F'/' '{print $2}'|sort|uniq -c|sort -nr
echo '抓取目录：'
awk '{print $9}' bd9www.log|awk -F'/' '{print $4}'|sort|uniq -c|sort -nr |head -30
rm bd9www.log

