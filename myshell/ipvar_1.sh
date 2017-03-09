#!/bin/bash
datevar=$1;
ys=$(date -d last-day +%m%d);
if [ -n "$datevar" ];then
	filedir=$datevar
else
	filedir=*
fi
dates=$filedir
LANG=C
arr=(220.181.108 123.125.71 180.76.15)
for file in bd/bd$dates.log;
do
	zzz=0
	cont=`cat $file|wc -l`
	for arrs in ${arr[@]};
	do
		
		spcont=`grep -a $arrs $file|awk '{print $3}'|wc -l`
		echo $file'-----'$arrs'.*蜘蛛数量:'$spcont	
		let zzz+=$spcont
		grep $arrs $file|awk '{print $3}'|sed 's/,.*//g'|sort|uniq -c|sort -nr|awk 'BEGIN{OFS="的数量是:";}{print $2,$1}'
	done
	echo $file'-sp总数量：'$cont'--------真实蜘蛛数量:'$zzz
done