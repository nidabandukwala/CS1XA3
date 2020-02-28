#!/bin/bash
count=0

echo choose Change or Restore
read user_input

if [ "$user_input" == Change ] ; then
	if [ -f permissions.log ] ; then
        	rm permissions.log
	fi
	for i in `find . -type f -name "*.sh"` ; do
		var=$( ls -l $i )
		var2="$( ls -l $i )"
		if [ -w "$i" ] ; then
			new=$( echo $var2 | cut -c3 )
			new1=$( echo $var2 | cut -c6 )
			new2=$( echo $var2 | cut -c8 )
			if [ $new = w ] ; then
				chmod u+x $i
			fi
			if [ $new1 = w ] ; then
				chmod g+x $i
			fi
			if [ $new2 = w ] ; then
				chmod o+x $i
			fi
			echo "$var" >> permissions.log
		fi
	done
elif [ "$user_input" = Restore ] ; then
	x=$( egrep '^-' permissions.log)
	v=$( egrep '.sh$' permissions.log)
	echo $x
	y=$(echo ${x:1:10})
	u1=$(echo ${y:1:3})
	#chmod u+$u1 $v
fi

