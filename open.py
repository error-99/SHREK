import os
import time
import requests
from requests.structures import CaseInsensitiveDict
#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
line=green+"▬"*100
space=" "
logo=red+str("""        ███████╗██╗  ██╗██████╗ ███████╗██╗  ██╗    
        ██╔════╝██║  ██║██╔══██╗██╔════╝██║ ██╔╝ \33[93m   
        ███████╗███████║██████╔╝█████╗  █████╔╝     
        ╚════██║██╔══██║██╔══██╗██╔══╝  ██╔═██╗     
  \33[1;32m      ███████║██║  ██║██║  ██║███████╗██║  ██╗    
        ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    
                                                    """+end)

      
 #HEADER                
text="\t\t"+cyan+"Developed By:Shabbir Rahman\n" 
version="1.1.0"
notice=""    
def opt():
	print(blue+"\n==> Select Your Option From Below"+end)
	print(cyan+"\n\n\t\t[1]Sms bombing\n\t\t[2]E-mail bombing"+end)

def header():
	print(logo)
	print(text)
	print(line)
	print(notice)
#main
os.system("clear")
header()
print(green+"\n\t\t[•]Checking For Updates...")
time.sleep(0)
r=requests.get("https://pastebin.com/raw/SEA7vpH3")
time.sleep(0.6)

upchck=r.text
if upchck==version:
	pass
else:
	os.system("clear")
	time.sleep(2)
	header()
	print(red+"\t\t[✓] Update Found")
	time.sleep(3)
	os.system("clear")
	header()
	print(blue+"\n\t\tUpdating Tool...")
	os.system("cd.. && rm -rf SHREK && git clone https://github.com/error-99/SHREK && cd SHREK && python main.py")
#main

x=1
while x<2:
	os.system("clear")
	header()
	print(green+ "\t\t [√]No update found ")
	time.sleep(1)
	opt()
	a=str(input(yellow+"\n\n [>] Enter The  Number : "+green))
	if a=="1":
		os.system("python3 sms_select.py")
		x=3
	elif a=="2":
		os.system("python3 e-mail.py")
	else:
		notice=str(red+"\n\t\t[×]Wrong value enter"+end)
