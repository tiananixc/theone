#!/bin/bash
LANG=C
arr=(220.181.108 123.125.71 180.76.15)
for file in bd/bd*.log;
do
	zzz=0
	cont=`cat $file|wc -l`
	for arrs in ${arr[@]};
	do
		
		spcont=`grep $arrs $file|awk '{print $3}'|wc -l`
		echo $file'-----'$arrs'蜘蛛数量:'$spcont	
		let zzz+=$spcont
	done
	echo $file'-sp总数量：'$cont'--------真实蜘蛛数量:'$zzz
done