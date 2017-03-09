#!/bin/bash
cat geturl.txt|while read line; do
	echo $line
	curl -sI $line|grep Loc|sed 's/Location://g'>>trueurl.txt
done