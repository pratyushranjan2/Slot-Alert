#!/bin/bash

echo ""
echo "Installing required packages..."
echo ""
sleep 2s

pip3 install requests
pip3 install twilio

echo ""
echo "The script will check for slot availability every 5 min"
echo "If a slot is found, sms will be sent to the provided mobile number"
echo "Pincodes and mobile number can be changed in user-data.txt"
echo "Quitting this terminal session will stop the process"

valid=true
while [ $valid ]
do
python3 slot.py
sleep 5m # Change to sleep 2m if you wish to check every 2 mins and so on
done