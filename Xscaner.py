#!/usr/bin/env python3 
import os
from  logo import Logo, bay
from colorama import init, Fore, Style, Back
init()
created=Fore.WHITE+Style.BRIGHT+Back.RED+"""
       
=============================
| Created by: 1LugarParaProgramar  |
|                                                              |
| Created :    H. Saldias                        |
|                                                              |
| Date  :    Domingo 20  de Agosto     |
|                                                              |
| Script :    Vulnerability Scanner         |
|                                                              |
====  1LugarParaProgramar ======


\n\n"""
    
    
def download(name, commands):
    print('\n###### Installing {}'.format(name))
    os.system('apt update && apt upgrade')
    for command in commands:
        os.system(command)
    print('###### Done 100%')
   
while  True:
    Logo()
    print(created)
    print("\n < 1 >  Nmap\n","< 2 > AndroZenmap\n","< 3 > AstraNmap\n","< 4 > Easymap\n","< 5 > Red Hawk\n","< 6 > D-Tect\n","< 7 > Damn Small SQLi Scanner\n","< 8 > SQLiv\n","< 9 > sqlmap\n","< 10 > sqlscan\n",
			 "< 11 > Wordpresscan\n","< 12 > WPScan\n","< 13 > sqlmate\n","< 14 > wordpresscan\n","< 15 > WTF\n",
			 "< 16 > Rang3r\n","< 17 > Striker\n","< 18 > Routersploit\n","< 19 > Xshell\n","< 20 > SH33LL\n",
			 "< 21 > BlackBox\n","< 22 > XAttacker\n","< 23 > OWScan\n","< 0 > Exit\n")
    vulnscan = input("Xscanner > ")
    if vulnscan == "01" or vulnscan == "1":
	    download("Nmap", ('apt install nmap'))
    elif vulnscan == "02" or vulnscan == "2":
		    download("AndroZenmap",('apt install nmap curl','curl -O http://override.waper.co/files/androzenmap.txt','mkdir ~/AndroZenmap','mv androzenmap.txt ~/AndroZenmap/androzenmap.sh'))		
    elif vulnscan == "03" or vulnscan == "3":
	    download("AstraNmap",('apt install git nmap','git clone https://github.com/Gameye98/AstraNmap','mv AstraNmap ~'))
    elif vulnscan == "04" or vulnscan == "4":
	    download("Easymap",('apt install php git','git clone https://github.com/Cvar1984/Easymap','mv Easymap ~','cd ~/Easymap && sh install.sh'))			
    elif vulnscan == "05" or vulnscan == "5":
	    download("RED HAWK", ('apt install git php','git clone https://github.com/Tuhinshubhra/RED_HAWK', 'mv RED_HAWK ~'))
    elif vulnscan == "06" or vulnscan == "6":
        download("D-Tect",('apt install python2 git','git clone https://github.com/shawarkhanethicalhacker/D-TECT', 'mv D-TECT ~'))
    elif vulnscan == "07" or vulnscan == "7":
	    download("DSSS",('apt install python2 git','git clone https://github.com/stamparm/DSSS','mv DSSS ~'))
    elif vulnscan == "08" or vulnscan == "8":
        download('SQLiv',('apt install python2 git','git clone https://github.com/Hadesy2k/sqliv','mv sqliv ~'))
    elif vulnscan == "09" or vulnscan == "9":
	    download("sqlmap",('apt install git python2','git clone https://github.com/sqlmapproject/sqlmap','mv sqlmap ~'))
    elif vulnscan == "10":
	    download("sqlscan",('apt install git php','git clone http://www.github.com/Cvar1984/sqlscan','mv sqlscan ~'))
    elif vulnscan == "11":
	    download("Wordpresscan",('apt install python2 python2-dev clang libxml2-dev libxml2-utils libxslt-dev','git clone https://github.com/swisskyrepo/Wordpresscan','mv Wordpresscan ~','cd ~/Wordpresscan && pip2 install -r requirements.txt'))
    elif vulnscan == "12":
	    download("WPScan",('apt install git ruby curl','git clone https://github.com/wpscanteam/wpscan','mv wpscan ~ && cd ~/wpscan','gem install bundle && bundle config build.nokogiri --use-system-libraries && bundle install && ruby wpscan.rb --update'))
    elif vulnscan == "13":
    	download("sqlmate",('apt install python2 git','pip2 install mechanize bs4 HTMLparser argparse requests urlparse2','git clone https://github.com/UltimateHackers/sqlmate','mv sqlmate ~'))
    elif vulnscan == "14":
	    download("wordpresscan(2)",('apt install nmap figlet git','git clone https://github.com/silverhat007/termux-wordpresscan','cd termux-wordpresscan && chmod +x * && sh install.sh','mv termux-wordpresscan ~'))
    elif vulnscan == "15":
	    download("WTF",('apt install git python2','pip2 bs4 requests HTMLParser urlparse mechanize argparse','git clone https://github.com/Xi4u7/wtf','mv wtf ~'))
    elif vulnscan == "16":
	    download("Rang3r",("apt install git python2 && pip2 install optparse termcolor","git clone https://github.com/floriankunushevci/rang3r","mv rang3r ~"))
    elif vulnscan == "17":
	    download("Striker",('apt install git python2','git clone https://github.com/UltimateHackers/Striker','mv Striker ~','cd ~/Striker && pip2 install -r requirements.txt'))
    elif vulnscan == "18":
	    download("Routersploit",('apt install python2 git','pip2 install requests','git clone https://github.com/reverse-shell/routersploit','mv routersploit ~;cd ~/routersploit;pip2 install -r requirements.txt;termux-fix-shebang rsf.py'))
    elif vulnscan == "19":
	    download("Xshell",("apt install lynx python2 figlet ruby php nano w3m","git clone https://github.com/Ubaii/Xshell","mv Xshell ~"))
    elif vulnscan == "20":
	    download("SH33LL",("apt install git python2","git clone https://github.com/LOoLzeC/SH33LL","mv SH33LL ~"))
    elif vulnscan == "21":
	    download("BlackBox",('apt install python2 git && pip2 install optparse passlib','git clone https://github.com/jothatron/blackbox','mv blackbox ~'))
    elif vulnscan == "22":
    	download("XAttacker",('apt install git perl','cpnm install HTTP::Request','cpnm install LWP::Useragent','git clone https://github.com/Moham3dRiahi/XAttacker','mv XAttacker ~'))
    elif vulnscan == "23":
	    download("OWScan",('apt install git php','git clone https://github.com/Gameye98/OWScan','mv OWScan ~'))
    elif vulnscan == "00" or vulnscan == "0":
        bay()
        os.system("exit")
        break