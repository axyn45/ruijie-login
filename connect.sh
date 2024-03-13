#! /bin/ash
echo "------$(date)------"

ping -c3 223.5.5.5
pcode=$?
echo $pcode
if [ $pcode -ne 0 ]
then
        python connect.py
else
        echo "Good Connection"

fi
echo "------END------"