#!/bin/bash
echo "please enter the python file you would like to check"
read input_file
echo "please enter what you would like to search the file for"
read char
echo $( cat "$input_file".py | grep $char | wc -w )
