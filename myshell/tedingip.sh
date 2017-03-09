#!/bin/bash
cd bd
logdate=(0710 0711 0717 0718)

logip=(79 81 70 71 83 117 72 69 106 111 114 116)
for ld in ${logdate[@]};
do
	bdlog='bd'$ld'.log'
	#logname='www'$ld'.log'
	for li in ${logip[@]};
	do

		savefile='all_'$ld'_'$li'.log'
		awk '$3~/123\.125\.71\.'$li'/' $bdlog>$savefile
		linum=`awk '$3~/123\.125\.71\.'$li'/' $bdlog|wc -l`
		echo 'date:'$ld'	ip:123.125.71.'$li'		num:'$linum
	done
done

