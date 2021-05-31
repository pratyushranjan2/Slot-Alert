from validation import*
from data import*
from Network import*

import requests
import json
import datetime

def today():
    date = datetime.datetime.today()
    return date.strftime('%d')+'-'+date.strftime('%m')+'-'+date.strftime('%Y')

def tomorrow():
    date = datetime.datetime.today()+datetime.timedelta(days=1)
    return date.strftime('%d')+'-'+date.strftime('%m')+'-'+date.strftime('%Y')

def checkSlotAvailability(pincode):
    obj = []
    response_today = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode="+pincode+"&date="+today())
    if response_today.status_code is 200:
        sessions = response_today.json()['sessions']
        for session in sessions:
            if (int(session['available_capacity']) > 0):
                obj.append({
                    'center' : session['name'],
                    'dose1' : session['available_capacity_dose1'],
                    'dose2' : session['available_capacity_dose2'],
                    'minage' : session['min_age_limit'],
                    'date' : session['date']
                })
    response_tomorrow = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode="+pincode+"&date="+tomorrow())
    if response_tomorrow.status_code is 200:
        sessions = response_tomorrow.json()['sessions']
        for session in sessions:
            if (int(session['available_capacity']) > 0):
                obj.append({
                    'center' : session['name'],
                    'dose1' : session['available_capacity_dose1'],
                    'dose2' : session['available_capacity_dose2'],
                    'minage' : session['min_age_limit'],
                    'date' : session['date']
                })
    return obj

userdata = getUserData()

if isValidPinCodes(userdata['pincodes']) and isValidMobile(userdata['mobile']):
    centers = []
    for pincode in userdata['pincodes']:
        centers.append(checkSlotAvailability(pincode))
    sendMessage(centers)
else:
    print('\nPincode or mobile number invalid.\nEnter valid details and restart the process\n')
