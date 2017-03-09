#!/bin/bash
lynx -dump 'http://www.baidu.com/s?wd=19888'|grep 'http://www.baidu.com/link?url='|xargs curl -s -I