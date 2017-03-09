#!/bin/bash
cat newsurl.txt | while read line; do
	curl $line -o savefile
	awk -F'class="liebiao"'