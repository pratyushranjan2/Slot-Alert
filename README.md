# SLOT-ALERT

## About
The script checks for covid vaccine slot availability at cowin.gov.in every 3 min and alerts the user through an sms if slot/s are found.

## Providing pincodes and mobile number
The user can provide multiple pincodes and a mobile number in the user-data.txt file in the same format as given.

## Requirements
python3 is required.<br/> The user must create a free twilio trial account and replace account_sid, auth_token and service_no in Network.py

## Execution
To facilitate one command processing, a shell script is added.<br/>
Go to the project directory and copy paste the following command on terminal to start the process<br/>
`bash process.sh`<br/>
All the required packages will be installed and the process will start.

## External packages used
Twilio and Requests.<br/>
Both the packages are installed automatically through the shell script.
