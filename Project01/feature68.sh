#!/bin/bash
echo choose Backup or Restore
read user_input

if [ "$user_input" == Backup ] ; then
	if [ ! -d backup ] ; then
		mkdir backup
	else
		 rm backup/*
	fi
	for i in `find . -type f -name "*.tmp"` ; do
		mv $i ./backup
	done
	echo `pwd`/$i >> ./backup/restore.log
elif [ "$user_input" == Restore ] ; then
	for line in $(cat ./backup/restore.log) ; do
                filename=$(echo $(basename "$line"))
		mv ./backup/$filename $line
		if [ ! -f $line ] ; then
			echo File does not exist
		fi
	done
fi
