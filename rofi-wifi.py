####################################################################################
################################ PARAMETERS ########################################
####################################################################################

#Pick the format (IMPORTANT : SSID is required) [IN-USE / SSID / MODE / CHAN(Chanel) / RATE / SIGNAL / BARS / SECURITY]
tableFormat = ['IN-USE', 'SSID', 'RATE', 'BARS', 'SECURITY']


####################################################################################
################################# FUNCTIONS ########################################
####################################################################################
import os

# Network Manager Info functions
def getRawWifiList():
    return os.popen('nmcli d wifi list').read()

def getWifiList():
    baseList = getRawWifiList()
    list = ''
    for line in str(baseList).splitlines():
        for legend in tableFormat :
            start = str(baseList).splitlines()[0].find(legend)
            i = start + len(str(legend))
            while baseList[i] == ' ' :
                i += 1
            list+=line[start:i]
        list += '\n'
    list = list[:len(str(list))-2]
    return list

def getConnections():
    r = os.popen("nmcli c show").read()
    end = str(r).find('UUID')
    conncetions = []
    for connection in str(r).splitlines():
        conncetions.append(connection[:end].strip(' '))
    return conncetions

#Network Manager conncetion management functions

def activateConnection(connection):
    print(os.popen("nmcli connection up "+connection).read())

def removeConnection(connection):
    print(os.popen('nmcli connection delete '+connection).read())

# rofi dmenu function
def rofi(input):
    return os.popen('echo "'+ input + '"| rofi -dmenu').read()

def textInput(legend):
    return os.popen('echo ""| rofi -dmenu -p "'+legend+'"').read()

#
def getSelectedWifi() :
    wifiList = getWifiList()
    r = rofi(wifiList)
    if(str(r) == (str(wifiList).splitlines()[0]+'\n')):
        r = getSelectedWifi()
    start = str(wifiList).splitlines()[0].find('SSID')
    i = start + len(str('SSID'))
    while wifiList[i] == ' ':
        i += 1
    return str(r)[start:i].strip(' ')

def getPassword():
    return textInput('PASSWORD : ')

def connecterWifi(wifi):
    wifis = getRawWifiList()
    security = str(wifis).find('SECURITY')
    for line in str(wifis).splitlines():
        if line.find(wifi) != -1 :
            if line[security:security+2]=='--':
                print(os.popen('nmcli dev wifi connect'+wifi).read())
            else:
                print(os.popen('nmcli dev wifi connect '+wifi+' password '+getPassword()).read())

def connectionParameter(connection):
    r = rofi("Activate connection\n"
         "Remove connection")
    if(r == 'Activate connection\n'):
        activateConnection(connection)
    elif (r == 'Remove connection\n'):
        removeConnection(selectedWifi)

####################################################################################
################################# SCRIPT ###########################################
####################################################################################

selectedWifi = getSelectedWifi()
if selectedWifi != '' :
    if(selectedWifi in getConnections()):
        connectionParameter(selectedWifi)
    else:
        connecterWifi(selectedWifi)