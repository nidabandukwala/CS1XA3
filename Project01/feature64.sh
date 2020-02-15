#!/bin/bash
filelist=$(ls -lS)
echo "$(ls -lS | sort -k 5 -rn |  du -ah | sort -hr )"



