import os
import time
import sys


def install(package):
    os.system('pip3 install '+package)

try:
    import pip
except ImportError:
    try:
        input("No module named 'pip' found. press any key to install..[using sudo for installing it. 'sudo apt update; sudo apt install python3-pip']")
        os.system('sudo apt update; sudo apt install python3-pip')
        print('Run again;')
        exit()
    except:
        print('You got error try installing manual [module "termcolor"]')
        print('Run again;')
        exit()

try:
    from googlesearch import search
except ImportError:
    try:
        input("No module named 'google' found. press any key to install..")
        install('google')
        install('beautifulsoup4')
        print('Run again;')
        exit()
    except:
        print('You got error try installing manual [module "google,beautifulsoup4"]')
        print('Run again;')
        exit()

try:
    from termcolor import colored 
except ImportError:
    try:
        input("No module named 'termcolor' found. press any key to install..")
        install('termcolor')
        print('Run again;')
        exit()
    except:
        print('You got error try installing manual [module "termcolor"]')
        print('Run again;')
        exit()


def ALLlinks():
    try:
        where_i_am = 0
        query = "site:"+input('domain: ')
        with open('result.txt','w') as f:
            for j in search(query,num=20):
                f.write(j+'\n')
                where_i_am += 1
                print('number '+colored(str(where_i_am),'green')+' discovered')
        print("filesaved: "+colored(os.popen('pwd').read().strip()+'/result.txt','green'))
    except ValueError:
        print('Wrong value;')

def CUSTOM():
    try:
        where_i_am = 0
        query = input('Your query: ')
        howmuch = int(input('How much url? [0 for all] '))
        with open('result.txt','w') as f:
            if not howmuch == 0:
                for j in search(query, num=20, stop=howmuch):
                    f.write(j+'\n')
                    where_i_am += 1
                    print('number: '+colored(str(where_i_am),'green')+' discovered from '+colored(str(howmuch),'green'))
            else:
                for j in search(query, num=20):
                    f.write(j+'\n')
                    where_i_am += 1
                    print('number: '+colored(str(where_i_am),'green')+' discovered from '+colored(str(howmuch),'green'))
        print("filesaved: "+colored(os.popen('pwd').read().strip()+'/result.txt','green'))
    except ValueError:
        print('Wrong value;')

def CUTTING_DOMAIN():
    try:
        where_i_am = 0
        query = input('Your query: ')
        howmuch = int(input('How much url? [0 for all] '))
        with open('result.txt','w') as f:
            if not howmuch == 0:
                for j in search(query, num=20, stop=howmuch):
                    f.write(j+'\n')
                    where_i_am += 1
                    print('number: '+colored(str(where_i_am),'green')+' discovered from '+colored(str(howmuch),'green'))
            else:
                for j in search(query, num=20):
                    f.write(j+'\n')
                    where_i_am += 1
                    print('number: '+colored(str(where_i_am),'green')+' discovered from '+colored(str(howmuch),'green'))
        # cutting domains
        os.system("cut -d '/' -f 3 result.txt > cut-result.txt;rm result.txt")
        print("filesaved: "+colored(os.popen('pwd').read().strip()+'/cut-result.txt','green'))
    except ValueError:
        print('Wrong value;')

def banner():
    return '''
            

 █     █░▓█████  ▄▄▄▄      ▄▄▄█████▓▓█████ ▄▄▄       ███▄ ▄███▓
▓█░ █ ░█░▓█   ▀ ▓█████▄    ▓  ██▒ ▓▒▓█   ▀▒████▄    ▓██▒▀█▀ ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██   ▒ ▓██░ ▒░▒███  ▒██  ▀█▄  ▓██    ▓██░
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀     ░ ▓██▓ ░ ▒▓█  ▄░██▄▄▄▄██ ▒██    ▒██ 
░░██▒██▓ ░▒████▒░▓█  ▀█▓     ▒██▒ ░ ░▒████▒▓█   ▓██▒▒██▒   ░██▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒     ▒ ░░   ░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ░  ░
  ▒ ░ ░   ░ ░  ░▒░▒   ░        ░     ░ ░  ░ ▒   ▒▒ ░░  ░      ░
  ░   ░     ░    ░    ░      ░         ░    ░   ▒   ░      ░   
    ░       ░  ░ ░                     ░  ░     ░  ░       ░   
                      ░                                                                   '''
        
def delay_print(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

print(colored(banner(),'red'))
delay_print("https://FedMan.t.me\n")
delay_print('-----------------------------------------------------------\n\n')

delay_print('[1] Detect all links cached on google from this domain)(And subdomains [If cached on google.]) \n[2] Custom dork \n[3] Cut domains for custom dork \nWhat to do? ')
what_to_do = int(input())
if what_to_do == 1:
    ALLlinks()
if what_to_do == 2:
    CUSTOM()
if what_to_do == 3:
    CUTTING_DOMAIN()
