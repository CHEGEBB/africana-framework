import re
import os
import sys
import time
import subprocess
from signal import *
from guide.info import *
from urllib.parse import *
from configs.config import *
from src.core.system import *
from src.core.banner import *
from src.core.bcolors import *
from src.wireles.wifi import *
from src.security.anonym import *
from src.payload.malware import *
from src.phishing.phisher import *
from src.internal.scanner import *
from src.webattack.scanner import *

class main_menu(object):
    def __init_(self):
        pass

    def menu_one(self):
        beauty.dove_banner()
        print(bcolors.BLUE + """
+-----------------------------------------------------------------------------+
|              † What Would You Like To Do From The Table Below ? †           |
+-----------------------------------------------------------------------------+
| 1. Install or Update Africana.      2. System Security Configuration.       |
| 3. Local Network Attack Vectors.    4. Generate Undetectable Malware.       |
| 5. Wifi Attack Vectors.             6. Crack .Pcap & BruteForce Passwords.  |
| 7. Social-Engineering Attacks.      8. Website Attack Vectors.              |
| 9. Help, Credits, Tricks and About. 0. Exit The Africana Pentest Framework. |
+-----------------------------------------------------------------------------+
""" + bcolors.ENDC)

    def menu_two(self):
        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|              † What Would You Like To Do From The Table Below ? †            |
+------------------------------------------------------------------------------+
| 1. Start Web W.A.F Detection.       2. Start D.N.S & Subdomain Enumration.   |
| 3. Start Web Technology Detection.  4. Start Nuclei Vulnerbility Scanner.    |
| 5. Start Nikto Web Vuln Scanner.    6. Start Host Root File Bruteforcer.     |
| 7. Start SQL Injection Detection.   8. Start BBOT & Uniscan Vuln Scanner.    |
| 9. Automate All Tools On Target.    0. Exit Web Scanner & Go To Main Menu.   |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
        
    def menu_three(self):
        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|              † What Would You Like To Do From The Table Below ? †            |
+------------------------------------------------------------------------------+
| 1. Start Network Target Discover.   2. Start Port Discovery On The Target.   |
| 3. Start Vuln' Scanning On Target.  4. Start S.M.B Enumration On The Target. |
| 5. Start S.M.B Exploits On Target.  6. Start Internal Packets Sniffer Tools. |
| 7. Start Responder & Capture Hash.  8. Start Beefxss & Bettercap For M.I.B.  |
| 9. Launch Wresharck & Sniff All.    0. Exit Internal Atta' & Go To Main Menu.|
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
mega_menu = main_menu()

def sudo():
    if not os.geteuid() == 0:
        os.system('clear')
        sys.exit(beauty.sudo_banner())
sudo ()

class neo_start(object):
    def __init__(self):
        pass
#0
    def user_agree(self):
        while True:
            try:
                os.system('clear')
                beauty.duck_banner()
                print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|   † Do you Agree to Use This Tool Only for [GOOD] and not [EVIL] †           |
+------------------------------------------------------------------------------+
|                    Type 1. For  Yes   &   0. For  No                         |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                try:
                    covenant = input(bcolors.DARKCYAN + bcolors.BOLD + "[africana] > " + bcolors.ENDC)
                    if covenant == '0':
                        beauty.banner_wise()
                        break
                    elif covenant == '1':
                        neo.one()
                        break
                    else:
                        try:
                            os.system('clear')
                            print(bcolors.RED + """
+------------------------------------------------------------------------------+
|           † Poor Choice Of Selection!!. Pleas Select [0 or 1] †              |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                            time.sleep(3)
                            neo.user_agree()
                            break
                        except:
                            neo.user_agree()
                            break
                except:
                    os.system('clear')
                    beauty.moana_banner()
                    break
            except:
                break

#1
    def install_africana(self):
        while True:
            try:
                os.system('clear')
                return installer.update_system(); neo.one()
            except:
                neo.one()
                break

#2
    def vanish_tor(self):
        os.system('clear')
        beauty.ponny_banner()
        def anonymity():
            while True:
                try:
                    print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|        † What Do you Feel Like Doing From The Table Below ? †                |
+------------------------------------------------------------------------------+
| 1. Install & Setup Tor (start here). | 2. Start Anonymizing Through Tor.     |
| 3. Stop Tor & Restore All Iptables.  + 0. Exit And Go Back To Main Menu.     |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                    try:
                        choice = input(bcolors.DARKCYAN + bcolors.BOLD + "[africana] > " + bcolors.ENDC)
                    except:
                        neo.one()
                        break
                    try:
                        if choice == '0':
                            neo.one()
                            break
                        elif choice == '1':
                            try:
                                os.system('clear')
                                return anonymous.vanish_install(), anonymity()
                            except:
                                neo.vanish_tor()
                                break
                        elif choice == '2':
                            try:
                                os.system('clear')
                                return anonymous.vanish_start(), anonymity()
                            except:
                                neo.vanish_tor()
                                break
                        elif choice == '3':
                            try:
                                os.system('clear')
                                return anonymous.vanish_stop(), anonymity()
                            except:
                                neo.vanish_tor()
                                break
                        else:
                            try:
                                os.system('clear')
                                print(bcolors.RED + """
+------------------------------------------------------------------------------+
|          † Poor Choice Of Selection!!. Pleas Select [0-3] †                  |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                                time.sleep(3)
                                os.system('clear')
                                neo.vanish_tor()
                                break
                            except:
                                neo.vanish_tor()
                                break
                    except:
                        neo.vanish_tor()
                        break
                except:
                    os.system('clear')
                    beauty.hacker_banner()
                    break
        anonymity()

#3
    def scann_internal(self):
        while True:
            try:
                return internal_scanner.bettercap_discover()
            except:
                neo.one()
                break

    def attack_internal(self):
        while True:
            try:
                os.system('clear')
                neo.scann_internal()
                print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|       † Selet A Target From Bettercap's Table Above To Be Attacked! †        |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                try:
                    host = input(bcolors.DARKCYAN + bcolors.BOLD + "[africana] > " + bcolors.ENDC)
                except:
                    neo.one()
                    break
                os.system('clear')
                def neo_attack():
                    while True:
                        try:
                            beauty.scatter_banner()
                            mega_menu.menu_three()
                            choice = input(bcolors.DARKCYAN + bcolors.BOLD + "[africana] [target] = [{0}] > ".format(host) + bcolors.ENDC)
                        except:
                            neo.one()
                            break
                        try:
                            os.system('clear')
                            if choice == '0':
                                neo.one()
                                break
                            elif choice == '1':
                                try:
                                    os.system('clear')
                                    return neo.attack_internal()
                                except:
                                    attack_internal.neo_attack()
                                    break
                            elif choice == '2':
                                try:
                                    os.system('clear')
                                    return internal_scanner.nmap_pscanner(host), attack_internal.neo_attack()
                                except:
                                    attack_internal.neo_attack()
                                    break
                            elif choice == '3':
                                try:
                                    os.system('clear')
                                    return internal_scanner.nmap_vulnscanner(host), attack_internal.neo_attack()
                                except:
                                    attack_internal.neo_attack()
                                    break
                            elif choice == '4':
                                try:
                                    os.system('clear')
                                    return internal_scanner.smb_enumuration(host), attack_internal.neo_attack()
                                except:
                                    attack_internal.neo_attack()
                                    break
                            elif choice == '5':
                                try:
                                    os.system('clear')
                                    return internal_scanner.smb_exploit(host), attack_internal.neo_attack()
                                except:
                                    attack_internal.neo_attack()
                                    break
                            elif choice == '6':
                                try:
                                    return internal_scanner.packets_sniffer(host), attack_internal.neo_attack()
                                except:
                                    attack_internal.neo_attack()
                                    break
                            elif choice == '7':
                                try:
                                    return internal_scanner.packets_responder(), attack_internal.neo_attack()
                                except:
                                    attack_internal.neo_attack()
                                    break
                            elif choice == '8':
                                try:
                                    return internal_scanner.beefxss_bettercap(host), attack_internal.neo_attack()
                                except:
                                    attack_internal.neo_attack()
                                    break
                            elif choice == '9':
                                try:
                                    return internal_scanner.packets_wireshark(), attack_internal.neo_attack()
                                except:
                                    attack_internal.neo_attack()
                                    break
                            else:
                                try:
                                    os.system('clear')
                                    print(bcolors.RED + """
+------------------------------------------------------------------------------+
|            † Poor Choice  Of Selection!!. Pleas Select [0-9] †               |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                                    time.sleep(3)
                                    attack_internal.neo_attack()
                                    break
                                except:
                                    os.system('clear')
                                    attack_internal.neo_attack()
                                    break
                        except:
                            neo_attack()
                            break
                neo_attack()
                break
            except:
                os.system('clear')
                beauty.hacker_banner()
                break

#4
    def rat_kitchen(self):
        while True:
            try:
                os.system('clear')
                beauty.scorpion_banner()
                print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|                † Africana Malware Generation Menu †                          |
+------------------------------------------------------------------------------+
|  Type  1. Windows,Linux,Mac Shells  2. Android Attack  0.  Back To Main      |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                try:
                    choice = input(bcolors.DARKCYAN + bcolors.BOLD + "[africana] > " + bcolors.ENDC)
                except:
                    neo.one()
                    break
                try:
                    os.system('clear')
                    if choice == '0':
                        neo.one()
                        break
                    elif choice == '1':
                        beauty.cross_banner()
                        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|                † Africana Malware Generation Menu †                          |
+------------------------------------------------------------------------------+
| Type   1. Launch Hoax 2. Launch Villain  3. Launch Shellz    0. Go To Main   |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                        try:
                            select = input(bcolors.DARKCYAN + bcolors.BOLD + "[africana] > " + bcolors.ENDC)
                        except:
                            neo.rat_kitchen()
                            break
                        if select == '0':
                            neo.rat_kitchen()
                            break
                        elif select == '1':
                            try:
                                return rat.hoaxshell(), neo.rat_kitchen()
                            except:
                                neo.rat_kitchen()
                                break
                        elif select == '2':
                            try:
                                return rat.villain(), neo.rat_kitchen()
                            except:
                                neo.rat_kitchen()
                                break
                        elif select == '3':
                            try:
                                return rat.kitchen(), neo.rat_kitchen()
                            except:
                                neo.rat_kitchen()
                                break
                        else:
                            try:
                                os.system('clear')
                                print(bcolors.RED + """
+------------------------------------------------------------------------------+
|            † Poor Choice Of Selection!!. Pleas Select [0-2] †                |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                                time.sleep(3)
                                os.system('clear')
                                neo.rat_kitchen(self)
                                break
                            except:
                                neo.rat_kitchen()
                                break
                    elif choice == '2':
                        try:
                            return rat.teardroid(), neo.rat_kitchen()
                        except:
                            neo.rat_kitchen()
                            break
                    else:
                        try:
                            os.system('clear')
                            print(bcolors.RED + """
+------------------------------------------------------------------------------+
|           † Poor Choice Of Selection!!. Pleas Select [0-2] †                 |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                            time.sleep(3)
                            os.system('clear')
                            neo.rat_kitchen()
                            break
                        except:
                            neo.rat_kitchen()
                            break
                except:
                    os.system('clear')
                    beauty.wolf_banner()
                    break
            except:
                break

#5
    def attack_wifi(self):
        while True:
            try:
                os.system('clear')
                beauty.wolf_banner()
                print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|                      † Africana wifi Pentesting Menu †                       |
+------------------------------------------------------------------------------+
|  Type  1. For Automated Attack   2. For Manual Attack   0. Back To Main      |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                try:
                    choice = input(bcolors.DARKCYAN + bcolors.BOLD + "[africana] > " + bcolors.ENDC)
                except:
                    neo.one()
                    break
                try:
                    os.system('clear')
                    beauty.bear_banner()
                    if choice == '0':
                        neo.one()
                        break
                    elif choice == '1':
                        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|                    † Africana wifi Pentesting Menu †                         |
+------------------------------------------------------------------------------+
| Type 1. With Bettercap  2. With Wifite  3. With Wifipumpkin  0. Back To Menu |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                        try:
                            select = input(bcolors.DARKCYAN + bcolors.BOLD + "[africana] > " + bcolors.ENDC)
                        except:
                            neo.attack_wifi()
                            break
                        if select == '0':
                            neo.attack_wifi()
                            break
                        elif select == '1':
                            try:
                                os.system('clear')
                                return wifi_killer.wifi_attack_bettercap(), neo.attack_wifi()
                            except:
                                neo.attack_wifi()
                                break
                        elif select == '2':
                            try:
                                os.system('clear')
                                return wifi_killer.wifi_attack_wifite(), neo.attack_wifi()
                            except:
                                neo.attack_wifi()
                                break
                        elif select == '3':
                            try:
                                os.system('clear')
                                return wifi_killer.wifi_auto_attack_wifipumpkin3(), neo.attack_wifi()
                            except:
                                neo.attack_wifi()
                                break
                        else:
                            try:
                                os.system('clear')
                                print(bcolors.RED + """
+------------------------------------------------------------------------------+
|         † Poor Choice  Of Selection!!. Pleas Select [0-2] †                  |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                                time.sleep(3)
                                neo.attack_wifi()
                                break
                            except:
                                neo.attack_wifi()
                                break
                    elif choice == '2':
                        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|                       † Africana wifi Pentesting Menu †                      |
+------------------------------------------------------------------------------+
|   Type   1. With Airgeddon   2. With wifiPumpkin3   0. Back To Main          |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                        try:
                            select = input(bcolors.DARKCYAN + bcolors.BOLD + "[africana] > " + bcolors.ENDC)
                        except:
                            neo.attack_wifi()
                            break
                        if select == '0':
                            neo.attack_wifi()
                            break
                        elif select == '1':
                            try:
                                os.system('clear')
                                return wifi_killer.wifi_attack_airgeddon(), neo.attack_wifi()
                            except:
                                neo.attack_wifi()
                                break
                        elif select == '2':
                            try:
                                os.system('clear')
                                return wifi_killer.wifi_attack_wifipumpkin3(), neo.attack_wifi()
                            except:
                                neo.attack_wifi()
                                break
                        else:
                            try:
                                os.system('clear')
                                print(bcolors.RED + """
+------------------------------------------------------------------------------+
|       † Poor Choice  Of Selection!!. Pleas Select [0-2] †                    |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                                time.sleep(3)
                                neo.attack_wifi()
                                break
                            except:
                                neo.attack_wifi()
                                break
                    else:
                        try:
                            os.system('clear')
                            print(bcolors.RED + """
+------------------------------------------------------------------------------+
|       † Poor Choice  Of Selection!!. Pleas Select [0-2] †                    |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                            time.sleep(3)
                            neo.attack_wifi()
                            break
                        except:
                            neo.attack_wifi()
                            break
                except:
                    os.system('clear')
                    beauty.volture_banner()
                    break
            except:
                break

#6
    def crack_passwords(self):
        while True:
            try:
                os.system('clear')
                beauty.prawn_banner()
                print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|         † Welcome To Password Cracking And Generation Sector †               |
+------------------------------------------------------------------------------+
| Type   1. Crack Using Air-Crackng   2. Use John   0. Back To Main            |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                try:
                    choice = input(bcolors.DARKCYAN + bcolors.BOLD + "[africana] > " + bcolors.ENDC)
                except:
                    neo.one()
                    break
                try:
                    if choice == '0':
                        neo.one()
                        break
                    elif choice == '1':
                        try:
                            return wifi_killer.aircrackng_password(), neo.crack_passwords()
                        except:
                            neo.crack_passwords()
                            break
                    elif choice == '2':
                        try:
                            return wifi_killer.john_password(), neo.crack_passwords()
                        except:
                            neo.crack_passwords()
                            break
                    else:
                        try:
                            os.system('clear')
                            print(bcolors.RED + """
+------------------------------------------------------------------------------+
|           † Poor Choice Of Selection!!. Pleas Select [0-2] †                 |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                            time.sleep(3)
                            neo.crack_passwords()
                            break
                        except:
                            neo.crack_passwords()
                            break
                except:
                    os.system('clear')
                    beauty.scatter_banner()
                    break
            except:
                break

#7
    def phish_creds(self):
        while True:
            try:
                os.system('clear')
                beauty.dog_banner()
                print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|        † What Tool Would You Like To Use From The Table Below ? †            |
+------------------------------------------------------------------------------+
| 1. Gophish                           | 2. Good Ginx       5. Anonphisher     |
| 3. AdvPhishing                       + 4. Setoolkit       0. Go to Main Menu |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                try:
                    choice = input(bcolors.DARKCYAN + bcolors.BOLD + "[africana] > " + bcolors.ENDC)
                except:
                    neo.one()
                    break
                try:
                    if choice == '0':
                        neo.one()
                        break
                    elif choice == '1':
                        os.system('clear')
                        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|                † Launching Go Phish At YOUR IP : 3333 ? †                    |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                        try:
                            return cred_phisher.phish_gophish(), neo.phish_creds()
                        except:
                            neo.phish_creds()
                            break
                    elif choice == '2':
                        os.system('clear')
                        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|                † Launching GoodGinx Work For Good Not Evil ? †               |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                        try:
                            return cred_phisher.phish_goodginx(), neo.phish_creds()
                        except:
                            neo.phish_creds()
                            break
                    elif choice == '3':
                        os.system('clear')
                        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|    † Launching AdvPhishing Tool. Pleas Work For Good Not Evil ? †            |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                        try:
                            return cred_phisher.phish_zphisher(), neo.phish_creds()
                        except:
                            neo.phish_creds()
                            break
                    elif choice == '4':
                        os.system('clear')
                        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|        † Launching Setoolkit Tool. Pleas Work For Good Not Evil ? †          |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                        try:
                            return cred_phisher.phish_setoolkit(), neo.phish_creds()
                        except:
                            neo.phish_creds()
                            break
                    elif choice == '5':
                        os.system('clear')
                        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|        † Launching Anonphisher Tool. Pleas Work For Good Not Evil ? †        |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                        try:
                            return cred_phisher.phish_anonphisher(), neo.phish_creds()
                        except:
                            neo.phish_creds()
                            break
                    else:
                        try:
                            os.system('clear')
                            print(bcolors.RED + """
+------------------------------------------------------------------------------+
|          † Poor Choice Of Selection!!. Pleas Select [0-3] †                  |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                            time.sleep(3)
                            neo.phish_creds()
                            break
                        except:
                            neo.phish_creds()
                            break
                except:
                    os.system('clear')
                    beauty.squid_banner()
                    break
            except:
                break

#8
    def attack_websites(self):
        while True:
            try:
                os.system('clear')
                beauty.be_banner()
                print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|        † Enter Your Target [Either HTTP(S)//: HostName OR IP]. †             |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                try:
                    url = input(bcolors.DARKCYAN + bcolors.BOLD + "[africana] > " + bcolors.ENDC)
                except:
                    neo.one()
                    break
                def url_maker(url):
                    if not re.match(r'http(s?)\:', url):
                        url = 'http://' + url
                    parsed = urlsplit(url)
                    host = parsed.netloc
                    if host.startswith('www.'):
                        host = host[4:]
                    return url
                host = url_maker(url)
                spiders = scanners(host = '')
                os.system('clear')
                def user_nuke(self):
                    beauty.web_banner()
                    mega_menu.menu_two()
                    while True:
                        try:
                            choice = input(bcolors.DARKCYAN + bcolors.BOLD + "[africana] [Target] = [{0}] > ".format(host) + bcolors.ENDC)
                        except:
                            neo.one()
                            break
                        try:
                            if choice == '0':
                                neo.one()
                                break
                            elif choice == '1':
                                try:
                                    os.system('clear')
                                    return spiders.wafw00f(host), attack_websites.user_nuke(self)
                                except:
                                    user_nuke(self)
                                    break
                            elif choice == '2':
                                try:
                                    os.system('clear')
                                    url = host
                                    xhost = url.replace("https://", "").replace("http://", "").replace("www.", "")
                                    return spiders.dnsrecon(xhost), attack_websites.user_nuke(self)
                                except:
                                    user_nuke(self)
                                    break
                            elif choice == '3':
                                try:
                                    os.system('clear')
                                    return spiders.whatweb(host), attack_websites.user_nuke(self)
                                except:
                                    user_nuke(self)
                                    break
                            elif choice == '4':
                                try:
                                    os.system('clear')
                                    url = host
                                    xhost = url.replace("https://", "").replace("http://", "").replace("www.", "")
                                    return spiders.nuclei(xhost), attack_websites.user_nuke(self)
                                except:
                                    user_nuke(self)
                                    break
                            elif choice == '5':
                                try:
                                    os.system('clear')
                                    return spiders.nikto(host), attack_websites.user_nuke(self)
                                except:
                                    user_nuke(self)
                                    break
                            elif choice == '6':
                                try:
                                    os.system('clear')
                                    return spiders.dirsearch(host), attack_websites.user_nuke(self)
                                except:
                                    user_nuke(self)
                                    break
                            elif choice == '7':
                                try:
                                    os.system('clear')
                                    return spiders.sqlmap(host), attack_websites.user_nuke(self)
                                except:
                                    user_nuke(self)
                                    break
                            elif choice == '8':
                                try:
                                    os.system('clear')
                                    return spiders.bbot(host), spiders.uniscan(host), attack_websites.user_nuke(self)
                                except:
                                    user_nuke(self)
                                    break
                            elif choice == '9':
                                try:
                                    os.system('clear')
                                    url = host
                                    xhost = url.replace("https://", "").replace("http://", "").replace("www.", "")
                                    return spiders.wafw00f(host), spiders.dnsrecon(xhost), spiders.whatweb(host), spiders.httpx(host), spiders.param_spider(host), spiders.ssl_scan(host), spiders.dirsearch(host), spiders.nuclei(host), spiders.nikto(host), spiders.dalfox(host), spiders.sqlmap(host), spiders.commix(host), spiders.xsser(host), attack_websites.user_nuke(self)
                                except:
                                    user_nuke(self)
                                    break
                            else:
                                try:
                                    os.system('clear')
                                    print(bcolors.RED + """
+------------------------------------------------------------------------------+
|            † Poor Choice  Of Selection!!. Pleas Select [0-9] †               |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                                    time.sleep(3)
                                    attack_websites.user_nuke(self)
                                    break
                                except:
                                    os.system('clear')
                                    user_nuke(self)
                                    break
                        except:
                            os.system('clear')
                            beauty.ponny_banner()
                            break
                user_nuke(self)
                break
            except:
                break

#9
    def about_me(self):
        while True:
            try:
                os.system('clear')
                guide_info.guide()
                about = bcolors.BLUE + """
+------------------------------------------------------------------------------+
|                         † About The Author †                                 |
+------------------------------------------------------------------------------+
|        I am Rojahs Montari. A devoted Christian Studied Education In         |
|         Kenyatta University Kenya. Got Persionate In Cybersecurity           |
|        I Then Furthered My Skills By Research, Practice & Expirience.        |
|                      Thanks To Ippsec Hack TheBox.                           |
|   I Am Working As A Teacher, Cybersecurity Consoltant, Software Enginear.    |
|                 Contactme at rojahsmontari@gmail.com                         |
|            Youtube Channel https://youtube.com/@RojahsMontari                |
+------------------------------------------------------------------------------+
|                Click Enter or 0).Back To Main Menu. <---'                    |
+------------------------------------------------------------------------------+

""" + bcolors.ENDC
                for a in about:
                    sys.stdout.write(a)
                    sys.stdout.flush()
                    time.sleep(0.03)
            except:
                neo.one()
                break

            try:
                choice = input(bcolors.DARKCYAN + bcolors.BOLD + "[africana] > " + bcolors.ENDC)
                if choice == '0':
                    neo.one()
                    break
                else:
                    neo.one()
                    break
            except:
                neo.one()
                break

# (all)
    def one(self):
        while True:
            try:
                os.system('clear')
                mega_menu.menu_one()
                try:
                    choice = input(bcolors.DARKCYAN + bcolors.BOLD + "[africana] > " + bcolors.ENDC)
                except:
                    os.system('clear')
                    beauty.pill_banner()
                    break
                try:
                    if choice == '0':
                        os.system('clear')
                        beauty.wise_banner()
                        break
                    elif choice == '1':
                        try:
                            return neo.install_africana()
                        except:
                            break
                    elif choice == '2':
                        try:
                            return neo.vanish_tor()
                        except:
                            break
                    elif choice == '3':
                        try:
                            return neo.attack_internal()
                        except:
                            break
                    elif choice == '4':
                        try:
                            return neo.rat_kitchen()
                        except:
                            break
                    elif choice == '5':
                        try:
                            return neo.attack_wifi()
                        except:
                            break
                    elif choice == '6':
                        try:
                            return neo.crack_passwords()
                        except:
                            break
                    elif choice == '7':
                        try:
                            return neo.phish_creds()
                        except:
                            break
                    elif choice == '8':
                        try:
                            return neo.attack_websites()
                        except:
                            break
                    elif choice == '9':
                        try:
                            return neo.about_me()
                        except:
                            break
                    else:
                        os.system('clear')
                        print(bcolors.RED + """
+------------------------------------------------------------------------------+
|           † Poor Choice Of Selection!!. Pleas Select [0-9] †                 |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                        time.sleep(3)
                        try:
                            neo.one()
                            break
                        except:
                            neo.one()
                            break
                except:
                    neo.one()
                    break
            except:
                os.system('clear')
                beauty.block_banner()
                break

neo = neo_start()
neo.user_agree()
if ' __name__' == '__main__':
        sys.exit(neo())
