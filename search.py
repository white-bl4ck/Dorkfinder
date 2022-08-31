import os
import time
import sys

try:
    from googlesearch import search
except ImportError:
    input("No module named 'google' found. press any key to install..")
    os.system('pip3 install google')
    os.system('pip3 install google')

def ALLlinks():
    try:
        query = "site:"+input('domain: ')
        with open('result.txt','w') as f:
            for j in search(query, num=100):
                f.write(j+'\n')
    except ValueError:
        print('Wrong value;')

def CUSTOM():
    try:
        query = input('Your query: ')
        howmuch = int(input('How much url? [0 for all] '))
        with open('result.txt','w') as f:
            if not howmuch == 0:
                for j in search(query, num=10, stop=howmuch):
                    f.write(j+'\n')
            else:
                for j in search(query, num=100):
                    f.write(j+'\n')
    except ValueError:
        print('Wrong value;')

def CUTTING_DOMAIN():
    try:
        query = input('Your query: ')
        howmuch = int(input('How much url? [0 for all] '))
        with open('result.txt','w') as f:
            if not howmuch == 0:
                for j in search(query, num=10, stop=howmuch):
                    f.write(j+'\n')
            else:
                for j in search(query, num=100):
                    f.write(j+'\n')
        # cutting domains
        os.system("cut -d '/' -f 3 result.txt > cut-result.txt;rm result.txt")
    except ValueError:
        print('Wrong value;')

def delay_print(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.02)

delay_print('__        ___     _ _             _     _ _  _        _\n')
delay_print("\ \      / / |__ (_) |_ ___      | |__ | | || |   ___| | __\n")
delay_print(" \ \ /\ / /| '_ \| | __/ _ \_____| '_ \| | || |_ / __| |/ /\n")
delay_print("  \ V  V / | | | | | ||  __/_____| |_) | |__   _| (__|   <\n")
delay_print("   \_/\_/  |_| |_|_|\__\___|     |_.__/|_|  |_|  \___|_|\_\ \n")
delay_print("https://white_bl4ck.t.me\n")
print('-----------------------------------------------------------\n\n')


what_to_do = int(input('[1] Detect all links cached on google from this domain \n[2] Custom dork \n[3] Cut domains for custom dork \nWhat to do? '))

if what_to_do == 1:
    ALLlinks()
if what_to_do == 2:
    CUSTOM()
if what_to_do == 3:
    CUTTING_DOMAIN()
