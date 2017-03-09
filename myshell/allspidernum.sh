#!/bin/bash
for file in bd/acc*.log
do
	# echo '----------'
	# snum=`grep Sogou $file|wc -l`
	# bnum=`grep Baiduspider $file|wc -l`
	# _3num=`grep 360Spider $file|wc -l`
	# gnum=`grep google $file|wc -l`
	# ynum=`grep Yis $file|wc -l`
	applenum=`grep Macintosh $file|wc -l`
	echo $file':搜狗：'$snum'	百度：'$bnum'	360:'$_3num'	Yisospider：'$ynum'	AppleBot:'$applenum
done
