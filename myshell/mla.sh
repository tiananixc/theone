#!/bin/bash
date=$1
topsite='www.'$2
bdfile='bd'$date'.log'
savefile='bdspzs.log'
cd bd
awk '$9~/\.'$2'\./{print $9}' $bdfile>$savefile
echo $date'日主站目录抓取情况：'
grep -a $topsite $savefile|awk -F'/' '{print $4}'|sort|uniq -c|sort -nr|head -30
echo $date'日二级域名目录抓取情况：'
grep -va $topsite $savefile|awk -F'/' '{print $4}'|sort|uniq -c|sort -nr|head -30
rm $savefile