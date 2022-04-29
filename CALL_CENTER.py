import requests
import threading
import time
import pyfiglet
import os,sys
os.system("clear")

a = pyfiglet.figlet_format(" CENTER")
print(f'\033[1;91m{a}')
no = input('\033[1;92m PHONE-NUMBER: \033[1;96m')
m = input('\033[1;92m EMAIL(respond): \033[1;96m')
u = input('\033[1;92m NICK-NAME: \033[1;96m')
u2 = input('\033[1;92m SURNAME: \033[1;96m')
print(' ')

def CALL_1():
	head = {
	    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
	    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "Referer": "https://m.pf.co.th/th/collection/single-house/the-signature?utm_medium=sem&utm_source=cpc&utm_campaign=generic"
	    }
	requests.post("https://api.pf.co.th/v2.1/registers",headers=head,data=f"locale=th&device=mobile&ref_type=collection&ref_id=1&first_name={u}&last_name={u2}&contact={no}&email={m}&avaliable_at=12%3A00+-+14%3A00&location_id=126&tracking%5Butm_medium%5D=sem&tracking%5Butm_source%5D=cpc&tracking%5Butm_campaign%5D=generic&tracking%5Blatitude%5D=&tracking%5Blongitude%5D=")
	print("\033[1;92m CALL_1\033[1;91m | \033[1;92mทำงาน \033[1;91m| \033[1;96m12:00 - 14:00")
	
for i in range(1):
	threading.Thread(target=CALL_1).start()