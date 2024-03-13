#! /bin/ash
echo "------$(date)------"

ping -c3 223.5.5.5
code=$?
echo $pingcode
if [ $code -ne 0 ]
then
        python /root/autoconnect/connect.py
else
        echo "Good Connection"

fi