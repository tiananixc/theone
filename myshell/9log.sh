#!/bin/bash
LANG=C
datevar=$1;
ys=$(date -d last-day +%m%d);
if [ -n "$datevar" ];then
	filedir=$datevar
else
	filedir=$ys
fi
dates=$filedir
alllog='access'$dates'.log'
_quan19888log='19888log_'$dates'.log'
_19888log='www19888log_'$dates'.log'
cd bd
awk '$12~/\.19888\.tv/' $alllog|sed 's/:90//g'>$_19888log
echo $dates' log analytics rasurlt：';bdname='19888bd'$dates'.log';grep -a Baiduspider $_19888log>$bdname;echo 'Logfile Split Success!';echo '--------------抓取量最大的前30个页面---------------';awk '{print $12}' $bdname|sort|uniq -c|sort -nr|head -30;echo '--------------抓取响应数据最大的前30个页面---------------';awk '{print $12,$7}' $bdname|sort -nrk2|head -30;echo '--------------抓取量最大的前30个二级域名---------------';awk '{print $12}' $bdname|awk -F'/' '{print $3}'|sort|uniq -c|sort -nr|head -30;echo '--------------抓取量最大的前30个目录---------------';awk '{print $12}' $bdname|awk -F'/' '{print $4}'|sort|uniq -c|sort -nr|head -30;echo '--------------抓取量最大的404页面前30个页面---------------';awk '$6~/404/'  $bdname|awk '{print $12}'|sort|uniq -c|sort -nr|head -30;echo '--------------抓取的403页面的IP，url---------------';awk '$6~/403/' $bdname|awk '{print $3,$12}';echo '--------------以下为各蜘蛛抓取情况 反馈码汇总---------------';Baidus=`grep -a Baiduspider $_19888log|wc -l`;echo 'Baiduspider:'$Baidus;_360Spider=`grep 360Spider $_19888log|wc -l`;echo '360Spider:'$_360Spider;google=`grep google $_19888log|wc -l`;echo 'google:'$google;sogou=`grep sogou $_19888log|wc -l`;echo 'sogou:'$sogou;Yisou=`grep YisouSpider $_19888log|wc -l`;echo 'YisouSpider:'$Yisou;applenum=`grep Macintosh $_19888log|wc -l`;echo 'AppleBot:'$applenum;echo '--------------日志分析完成！------------';
arr=(Baiduspider sogou 360Spider google YisouSpider Macintosh)
for arrs in ${arr[@]};
do
	echo '--------------'$arrs'蜘蛛反馈码汇总---------------'
	grep -a $arrs $_19888log|awk '{print $6}'|awk -F'/' '{print $2}'|sort|uniq -c|sort -nr
done
awk '$12~/\/www\.19888\.tv\/listagentinfo\/type/{print $12}' $bdname|grep -v %
lai=`awk '$12~/\/www\.19888\.tv\/listagentinfo\/type/' $bdname|grep -v %|wc -l`
echo 'listagentinfo/type_*.html 代理抓取数量:'$lai;
rm $_19888log;rm $bdname;
cd ../
sh listpagescrapy.sh $dates

