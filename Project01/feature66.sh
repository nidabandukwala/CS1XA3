#!/bin/bash
echo please enter any word
read wordtag
if [ ! -f "$wordtag".log ] ; then
	touch "$wordtag".log
else
	rm "$wordtag".log
	touch "$wordtag".log
fi

pythonfile=`find . -type f -name "*.py" | wc -w`

if [ "$pythonfile" -gt 0 ] ; then
	cat *.py | grep ^# | grep "$wordtag" >> "$wordtag".log
fi
