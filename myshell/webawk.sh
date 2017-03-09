#!/bin/bash
site=(www.spzs.com spzs.com www.19888.tv 19888.tv)
for s in ${site[@]};
do
	echo $s' 网站基本数据：';sitecode='http://www.baidu.com/s?wd=site:'$s;www=`curl -i -s $sitecode>sitehahait.txt`;sitev=`cat sitehahait.txt|grep -o -E '<b style="color:#333">.+</b>'|sed 's/<b.*">//g'|sed 's/<\/b>//g'`;echo '收录为：'$sitev;suoyin=`cat sitehahait.txt|grep -o -E 'searchTool-spanner c-icon-setting.+</div>' | head -1|grep -o -P '\d+'`;echo '索引为：'$suoyin;echo '-----------------------------';rm sitehahait.txt;chinazurl='http://seo.chinaz.com/?host='$s;chinaz=`curl -s $chinazurl>chinaz.txt`;kwnum=`cat chinaz.txt|grep '<div class="Ma01LiRow w10-7">'|grep -o -P '">\d+<'|head -1|grep -o -P '\d+'`;echo '预估流量为：'$kwnum;ipnum=`cat chinaz.txt|grep -n '<div class="Ma01LiRow w10-7">'|grep -o -P '">\d+<'|tail -1|grep -o -P '\d+'`;echo '关键词数为：'$ipnum;rm chinaz.txt;echo '-----网站基本数据查询完成------'
done
