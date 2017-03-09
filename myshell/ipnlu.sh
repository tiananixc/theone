#!/bin/bash
cat ip.txt | while read line; do
	res=`nslookup $line|grep -oa -e baidus.*com`
	if [ ! $res ];
		then
		r='the ip is not baiduspider!'
	else
		r=$res
	fi
	echo $line':'$r
done