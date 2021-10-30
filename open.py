
#import_main
import os

try:
	import requests
except:
		os.system("pip install requests")
		import requests

import time
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
notice=""    
def header():
	print(logo)
	print(text)
	print(line)
	print(notice)
	

#check 
check=requests.get("https://pastebin.com/raw/EmsF9YFP").text

if check=="off":
	os.system("python3 rest.py")
elif check=="on":
	os.system("clear")
	header()
	print(green+"\t\tChecking for update"+end)


update=requests.get("https://pastebin.com/raw/6vbRifgm").text
#print(update)
if update=="1.1.0":
	print(green+"\n\t\t[•]No update found"+end)
elif update=="1.1.1":
	os.system("clear")
	header()
	print(red+"\n\t\t [*]Updating tools...wait"+end)
	
os.system("rm -rf SHREK &&git clone https://github.com/error-99/SHREK ; cd SHREK ; python3 main.py")

		