def getUserData():
    
    file = open('user-data.txt')
    pincodes_txt = file.readline()
    mobile = file.readline()

    start = pincodes_txt.index('[')
    end = pincodes_txt.index(']')

    pincodes_txt = pincodes_txt[start+1:end]
    pincodes = pincodes_txt.split(',')

    start = mobile.index('+')
    mobile = mobile[start:]

    userdata = {
        'pincodes' : pincodes,
        'mobile' : mobile
    }

    return userdata