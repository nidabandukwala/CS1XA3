#!/bin/bash
echo please enter a file extension
read fileext
count=0
for i in $(echo "$(ls -lS | egrep \.$fileext)"); do
	count=$((count+1))
done
echo $count
