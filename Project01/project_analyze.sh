#!/bin/bash
echo please choose a feature between 1 and 7
echo 1. File Size List
echo 2. File Type Count
echo 3. Find Tag
echo 4. Check File Name
echo "5. Check for certain characters in files"
echo 6. Switch to Executable
echo 7. Backup and Delete/Restore

read input_feature

if [ "$input_feature" -eq 1 ] ; then
	 ./feature64.sh
elif [ "$input_feature" -eq 2 ] ; then
	./feature65.sh
elif [ "$input_feature" -eq 3 ] ; then
	./feature66.sh
elif [ "$input_feature" -eq 4 ] ; then
	./custom_feature1.sh
elif [ "$input_feature" -eq 5 ] ; then
	./custom_feature2.sh
elif [ "$input_feature" -eq 6 ] ; then
	./feature67.sh
elif [ "$input_feature" -eq 7 ] ; then
	./feature68.sh
fi
