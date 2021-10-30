import os
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
def opt():
	print(blue+"\n==> Select Your Option From Below"+end)
	print(cyan+"\n\n\t\t[1]Sms bombing"+end)

def header():
	print(logo)
	print(text)
	print(line)
	print(notice)
#main
x=1
while x<2:
	os.system("clear")
	header()
	opt()
	a=str(input(yellow+"\n\n [>] Enter The  Number : "+green))
	if a=="1":
		os.system("python3 sms_select.py")
		x=3
	else:
		notice=str(red+"\n\t\t[×]Wrong value enter"+end)
