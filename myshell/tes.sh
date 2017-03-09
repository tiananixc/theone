#!/bin/bash
datevar=$1;
ys=$(date -d last-day +%m%d);
if [ -n "$datevar" ];then
	filedir=$datevar
else
	filedir=$ys
fi
echo $filedir;