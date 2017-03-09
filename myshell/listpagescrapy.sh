#!/bin/bash
LANG=C
dates=$1
logs='bd/access'$dates'.log'
logname='19888www'$dates'.log'
awk '$12~/www\.19888\.tv/' $logs>$logname
# echo '---log www split,got it---'
# wc -l $logname
allspiders=(Baiduspider sogou 360Spider google YisouSpider Macintosh)
spiders=(Baiduspider sogou 360Spider google)
lists=(listbizinfo showbizinfo listagentinfo showagentinfo listprovideinfo showprovideinfo listproduct ShowProduct ListNews newslist NewsView jiuzsarea)
for sp in ${spiders[@]};
do
	echo '--------------'$sp'蜘蛛栏目抓取情况---------------'
	res=''
	nspn=$sp'_'$logname
	grep -a $sp $logname>$nspn
	for l in ${lists[@]};
	do
		lnum=`awk '$12~/'$l'/' $nspn|wc -l`
		res+=$lnum'	'		
	done
	pronum=`awk '$12~/\/product\//' $nspn|wc -l`
	res+=$pronum
	echo 'listbizinfo showbizinfo listagentinfo showagentinfo listprovideinfo showprovideinfo listproduct ShowProduct ListNews newslist NewsView jiuzsarea product'
	echo $res
	rm $nspn
done
rm $logname