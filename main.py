import os
import time
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
version=red+"\t\t     version 1.1.0 "
notice=""    
def opt():
	print(blue+"\n==> Select Your Option From Below"+end)
	print(cyan+"\n\n\t\t[1]Sms bombing"+end)

def header():
	print(logo)
	print(text)
	print(version)
	print(line)
	print(notice)
#main
print(green+"\t\t[•]Checking For Updates...")
version = open(".version.txt", "r")
mainversion = requests.get("https://raw.githubusercontent.com/error-99/SHREK/main/.version.txt")
time.sleep(0.6)

if(version.read() == mainversion.text):
	print(cyan+"You are using the latest version of SH-BOMB")

else:
	print(' ')
	print(' ')
	print(red+"\t\t[✓]Tool Update Found")

	print(blue+"\t\tUpdating Tool...")

	os.system("cd .. && rm -rf SH-BOMB && git clone https://github.com/error-99/SHREK> /dev/null 2>&1 && cd SHREK && python main.py")

x=1
while x<2:
	os.system("clear")
	header()
	time.sleep(1)
	opt()
	a=str(input(yellow+"\n\n [>] Enter The  Number : "+green))
	if a=="1":
		os.system("python3 sms.py")
		x=3
	else:
		notice=str(red+"\n\t\t[×]Wrong value enter"+end)
