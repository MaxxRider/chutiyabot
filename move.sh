#!/bin/bash

if [ -n "$1" ]              # Tested variable is quoted.
then
 echo "change folder #1 to $1"  # Need quotes to escape #
 mv robote/started robote/$1
 find ./ -type f -exec sed -i "s/started/$1/gI" {} \;
fi

if [ -n "$2" ]
then
 echo "change folder #2 to $2"
 mv robote/lokal robote/$2
 find ./ -type f -exec sed -i "s/lokal/$2/gI" {} \;
fi

if [ -n "$3" ]
then
 echo "change folder #3 to $3"
 mv robote $3
 find ./ -type f -exec sed -i "s/robote/$3/gI" {} \;
fi

if [ -n "$4" ]
then
 echo "change folder and script alisa to $4"
 find ./ -type f -exec sed -i "s/alisa/$4/gI" {} \;
 find . -type f -name 'download_alisa.py' -exec mv {} $3/$2/'download_'$4'.py' \;
fi

echo "change debug level and session"
find ./ -type f -exec sed -i "s/robote_lokal/$3_$2/gI" {} \;
find ./ -type f -exec sed -i "s/logging.ERROR/logging.ERROR/gI" {} \;
find ./ -type f -exec sed -i "s/logging.ERROR/logging.ERROR/gI" {} \;
