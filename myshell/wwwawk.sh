#!/bin/bash
mdate=$1
fday=$2
bday=$3
fdate=$1$2
bdate=$1$3
aNumList=$(seq $fdate $bdate);
suzu=$aNumList
cd bd
for arrs in ${suzu[@]};
do
	fn=bd0$arrs.log
	if [ -f "$fn" ]; then
		echo 'date:0'$arrs
		echo '主站抓取：'
		awk '$12~/\/www\.spzs\.com/{print $12}' $fn|awk -F'/' '{print $4}'|sort|uniq -c|sort -nrr|head -30
		echo '整站抓取：'
		awk '$12~/\.spzs\.com/{print $12}' $fn|awk -F'/' '{print $4}'|sort|uniq -c|sort -nrr|head -30
		echo '----------------------'
	fi
done