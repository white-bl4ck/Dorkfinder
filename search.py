import os
import time
import sys
import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

try:
    from googlesearch import search
except ImportError:
    try:
        input("No module named 'google' found. press any key to install..")
        install('google')
        install('beautifulsoup4')
    except:
        print('You got error try installing manual [module "google,beautifulsoup4"]')

try:
    from termcolor import colored 
except ImportError:
    try:
        input("No module named 'google' found. press any key to install..")
        install('termcolor')
    except:
        print('You got error try installing manual [module "termcolor"]')

def ALLlinks():
    try:
        query = "site:"+input('domain: ')
        with open('result.txt','w') as f:
            for j in search(query, num=100):
                f.write(j+'\n')
        print("filesaved: "+colored(os.popen('pwd').read().strip()+'/result.txt','green'))
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
        print("filesaved: "+colored(os.popen('pwd').read().strip()+'/result.txt','green'))
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
        print("filesaved: "+colored(os.popen('pwd').read().strip()+'/cut-result.txt','green'))
    except ValueError:
        print('Wrong value;')

def delay_print(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.02)

delay_print('__        _______ ____ \n')
delay_print("\ \      / / ____| __ )\n")
delay_print(" \ \ /\ / /|  _| |  _ \ \n")
delay_print("  \ V  V / | |___| |_) |\n")
delay_print("   \_/\_/  |_____|____/ \n\n")
delay_print("https://white_bl4ck.t.me\n")
print('-----------------------------------------------------------\n\n')


what_to_do = int(input('[1] Detect all links cached on google from this domain \n[2] Custom dork \n[3] Cut domains for custom dork \nWhat to do? '))

if what_to_do == 1:
    ALLlinks()
if what_to_do == 2:
    CUSTOM()
if what_to_do == 3:
    CUTTING_DOMAIN()
