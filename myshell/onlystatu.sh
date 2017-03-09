#!/bin/bash
dates=$1; cd bd;_19888log='bd'$dates'.log'
echo '--------------以下为各蜘蛛抓取情况 反馈码汇总---------------';Baidus=`grep Baiduspider $_19888log|wc -l`;_360Spider=`grep 360Spider $_19888log|wc -l`;google=`grep google $_19888log|wc -l`;sogou=`grep sogou $_19888log|wc -l`;Yisou=`grep YisouSpider $_19888log|wc -l`;
echo 'Baiduspider 	sogou 	360Spider 	googlebot 	YisouSpider';
echo $Baidus'	'$sogou'	'$_360Spider'	'$google'	'$Yisou;
echo '--------------日志分析完成！------------';