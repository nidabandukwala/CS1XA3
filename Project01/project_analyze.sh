
#!/bin/bash
echo please choose a feature between 1 and 3
read input_feature 
if [ "$input_feature" -eq 1 ] ; then
	 ./feature64.sh
elif [ "$input_feature" -eq 2 ] ; then
	./feature65.sh
elif [ "$input_feature" -eq 3 ] ; then
	./feature66.sh
fi

