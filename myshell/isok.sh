#!/bin/bash
file=bd/$1
cat $file|while read line; do
	#statements
	status=`curl -I -s $line|grep HTTP|awk '{print $2}'`
	echo $line'	'$status
done