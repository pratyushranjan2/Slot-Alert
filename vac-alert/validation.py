def isDigitOnly(str):
    for digit in str:
        if not(digit>='0' and digit<='9'):
            return False
    return True


def isValidPinCodes(pincodes):
    for pincode in pincodes:
        if not(len(pincode)==6 and pincode[0]!='0' and (pincode[0]>='1' and pincode[0]<='9') and isDigitOnly(pincode)):
            return False
    return True

def isValidMobile(mobile):
    if not(len(mobile)==13 and mobile[0:3]=='+91' and (mobile[3] in ['6','7','8','9']) and isDigitOnly(mobile[3:])):
        return False
    return True