import os
yellow="\033[0;33m"       # Yellow
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
print(yellow+"welcome to ARNOV HACK BAR")
print(red+"This is line")
print("""          _____  _   _  ______      __ 
     /\   |  __ \| \ | |/ __ \ \    / / 
    /  \  | |__) |  \| | |  | \ \  / /  
   / /\ \ |  _  /| . ` | |  | |\ \/ /   
  / ____ \| | \ \| |\  | |__| | \  /    
 /_/   _\_\_|  \_\_|_\_|\____/   \/     
 | |  | |   /\   / ____| |/ /           
 | |__| |  /  \ | |    | ' /            
 |  __  | / /\ \| |    |  <             
 | |  | |/ ____ \ |____| . \            
 |_|__|_/_/    \_\_____|_|\_\           
 |  _ \   /\   |  __ \                  
 | |_) | /  \  | |__) |                 
 |  _ < / /\ \ |  _  /                  
 | |_) / ____ \| | \ \                  
 |____/_/    \_\_|  \_\                 
                                        
                                       """)

print(green+"AHB")	                                  
                                                                      
def FB():
	print("facebook hacking ") 
opt=int(input("[>] username :"))
opt=int(input ("[>]password :"))
	                        
def sms():
	print("BD SMS Bombing ")
		
def kali():
 	print(" install kali")                         
 	
while True:
 os.system("clear")
 print("[>] select your opinion: \n\n\ [1] facebook hacking\n [2] BD SMS bombing\n [3] install kali")
 opt=int(input("[>] enter your number :"))
 if opt==1:
	 	FB()
	 	a=input()
 elif opt==2:
          sms()
          a=input()
 elif opt==3:
           kali()
           a=input()