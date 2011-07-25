#!/bin/bash
mypath="$1"
FROM=iso-8859-1
TO=UTF-8
ICONV="iconv -f $FROM -t $TO"
# Convert
find "$mypath" -type f -name "*" | while read fn; do
cp ${fn} ${fn}.bak
$ICONV < ${fn}.bak > ${fn}
rm ${fn}.bak
done
