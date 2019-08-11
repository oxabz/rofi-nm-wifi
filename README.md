```
██████╗  ██████╗ ███████╗██╗
██╔══██╗██╔═══██╗██╔════╝██║
██████╔╝██║   ██║█████╗  ██║
██╔══██╗██║   ██║██╔══╝  ██║
██║  ██║╚██████╔╝██║     ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝
                            
███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗
████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝
██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ 
██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██╔═██╗ 
██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗
╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
                                                              
███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
```
        

# Description

Rofi network manager is a python base script for rofi that allows you to
manage your wifi connexion


# Install

1) Veriffy that NetworkManager is installed if not install it (see on your distro wiki)
2) Install rofi 
3) Install python 3.7 (should work on other python 3 version but the script has been created and tested on python 3.7)
4) Clone the repository `git clone`
(optional) 5) Edit the script (vim, vi, nano, atom...) and change the array table format to your liking (WARNING the field SSID is REQUIRED)
```
#Pick the format (IMPORTANT : SSID is required) [IN-USE / SSID / MODE / CHAN(Chanel) / RATE / SIGNAL / BARS / SECURITY]
tableFormat = ['IN-USE', 'SSID', 'RATE', 'BARS', 'SECURITY']
```
6)you're good to go the script can be launched with the command `python3 <path to the script>`


# Other info 

This script is my first "program" to be put online with the intent of being used by other than me so all constructive criticism would be greatly apreciated
