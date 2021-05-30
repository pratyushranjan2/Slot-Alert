from twilio.rest import Client
from data import*

account_sid = 'ACca24bfdc63ddd2791e669661950a0200'
auth_token = '5bf71eb66356234b264d1c15ffed4caf'
service_no = '+18329003565'
client = Client(account_sid, auth_token)
msg_text = 'Vaccination slots available at your provided pincodes.\n\n'


def frameMessage(center):
    
    global msg_text
    text = 'Center name: '+center['center']+'\n'+'Dose 1 slots: '+str(center['dose1'])+'\n'+'Dose 2 slots: '+str(center['dose2'])+'\n'+'Min age limit: '+str(center['minage'])+'\n'+'Date: '+center['date']+'\n\n\n'
    msg_text = msg_text+text

def sendMessage(centersByPincodes):
    
    send_message = False

    for centersByPincode in centersByPincodes:
        if len(centersByPincode) > 0:
            send_message = True
        for center in centersByPincode:
            frameMessage(center)

    if send_message:
        message = client.messages \
        .create(
            body=msg_text,
            from_=service_no,
            to=getUserData()['mobile']
        )