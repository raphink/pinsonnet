#!/bin/bash

FILE=$1
SPECIES=${FILE%%.txt}

echo "<html><body>"
cat $FILE | while read i; do
  echo "$i"
	echo "<img src='$i' /><br />"
done
echo "</body></html>"
