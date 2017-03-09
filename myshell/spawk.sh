#!/bin/bash
dates=$1;spname=$2;echo $dates' '$spname' log analytics rasurlt：';newfilename='access'$dates'.log';bdname=$spname'_'$dates'.log';cd bd;grep $spname $newfilename>$bdname;echo 'Logfile Split Success!';echo '--------------反馈码汇总---------------';awk '{print $6}' $bdname|awk -F'/' '{print $2}'|sort|uniq -c|sort -nr;echo '--------------抓取量最大的前30个页面---------------';awk '{print $9}' $bdname|sort|uniq -c|sort -nr|head -30;echo '--------------抓取量最大的前30个二级域名---------------';awk '{print $9}' $bdname|awk -F'/' '{print $3}'|sort|uniq -c|sort -nr|head -30;echo '--------------抓取响应数据最大的前30个页面---------------';awk '{print $9,$7}' $bdname|sort -nrk2|head -30;echo '--------------抓取量最大的前30个目录---------------';awk '{print $9}' $bdname|awk -F'/' '{print $4}'|sort|uniq -c|sort -nr|head -30;echo '--------------抓取量最大的404页面前30个页面---------------';awk '$6~/404/'  $bdname|awk '{print $9}'|sort|uniq -c|sort -nr|head -30;echo '--------------日志分析完成！------------';rm $bdname