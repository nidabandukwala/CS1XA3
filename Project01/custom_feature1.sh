#!/bin/bash
echo plase enter a file name
read file_name
not_char='/'
if [[ "$file_name" == *"$not_char"* ]] ; then
	echo "Your file name contains an unacceptable character in bash, please remove it"
else
	echo "Your file name is in an acceptable format"
fi
