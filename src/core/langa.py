import re
import os
import sys
import time
import subprocess

from signal import *
from guide.info import *
from urllib.parse import *
from modules.secmon import *
from src.c2.malware import *
from src.core.system import *
from src.core.banner import *
from src.core.bcolors import *
from src.wireles.wifi import *
from scriptures.verses import *
from src.security.anonym import *
from src.phishing.phisher import *
from src.internal.scanner import *
from src.passcrack.cracker import *
from src.webattack.scanner import *

class main_menu(object):
    def __init_(self):
        pass

    def menu_one(self):
        beauty.graphics(), scriptures.verses()
        print(bcolors.BLUE + "\n           -{" + bcolors.ENDC + bcolors.UNDERL + " Select a number from the table below" + bcolors.ENDC + bcolors.BLUE + " }-\n" + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 1.            Install or Update Africana                ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 2.          System Security Configuration               ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 3.           Local Network Attack Vectors               ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 4.          Generate Undetectable Malware               ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 5.               Wifi Attack Vectors                    ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 6.        Crack .Pcap & BruteForce Passwords            ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 7.           Social-Engineering Attacks                 ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 8.              Website Attack Vectors                  ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 9.         Help, Credits, Tricks and About              ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 0.       Exit The Africana Pentest Framework            ] \n" + bcolors.ENDC)

    def menu_two(self):
        beauty.graphics(), scriptures.verses()
        print(bcolors.BLUE + "\n           -{" + bcolors.ENDC + bcolors.UNDERL + " Select a number from the table below" + bcolors.ENDC + bcolors.BLUE + " }-\n" + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 1.           Recon for web wafs detection               ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 2.        Start D.N.S & Subdomain Enumration            ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 3.          Start Web Technology Detection              ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 4.        Launch Nuclei Vulnerbility Scanner            ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 5.           Start Nikto Web Vuln Scanner               ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 6.         Start Host Root File Bruteforcer             ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 7.           Start SQL Injection Detection              ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 8.         Launch BBOT & Uniscan Vuln Scanner           ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 9.            Automate All Tools On Target              ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 0.         Exit Web Scanner & Go To Main Menu           ] \n" + bcolors.ENDC)

    def menu_three(self):
        beauty.graphics(), scriptures.verses()
        print(bcolors.BLUE + "\n           -{" + bcolors.ENDC + bcolors.UNDERL + " Select a number from the table below" + bcolors.ENDC + bcolors.BLUE + " }-\n" + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 1.           Start Network Target Discover              ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 2.        Start Port Discovery On The Target            ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 3.          Start Vuln' Scanning On Target              ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 4.       Start S.M.B Enumration On The Target           ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 5.           Start S.M.B Exploits On Target             ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 6.        Start Internal Packets Sniffer Tools          ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 7.         Start Responder & Capture Hashes             ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 8.       Start Beefxss & Bettercap For (M.I.B)          ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 9.       Launch Wresharck & Sniff All Traffick          ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 0.      Exit Internal Attacks & Go To Main Menu         ] \n" + bcolors.ENDC)
mega_menu = main_menu()

def sudo():
    if not os.geteuid() == 0:
        os.system('clear')
        beauty.graphics(), scriptures.verses()
        sys.exit(1)
sudo ()

class neo_start(object):
    def __init__(self):
        pass
#0
    def user_agree(self):
        while True:
            try:
                os.system('clear')
                beauty.graphics(), scriptures.verses()
                print(bcolors.ENDC  + "\n                      " + bcolors.BLUE + "~[ " + bcolors.ENDC + bcolors.UNDERL + "Endless Intellect" + bcolors.ENDC + bcolors.BLUE + " ]~\n" + bcolors.ENDC)
                print(bcolors.BLUE + "   [   Code samples are provided for " + bcolors.RED + bcolors.UNDERL + "Educational Purposes" + bcolors.ENDC + bcolors.BLUE + "    ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [   Adequate defenses can only be built by researching    ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [    attack techniques available to malicious actors      ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [  Using this code against target systems without prior   ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [      permission is illegal in most jurisdictions        ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ The authors are not liable for any damages from misuse  ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [              of this information or code.               ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ Do you Agree to Use This Code Only for " + bcolors.ENDC + bcolors.UNDERL + "GOOD"+ bcolors.ENDC + bcolors.YELLOW + " & " + bcolors.BLUE + "not " + bcolors.RED + bcolors.UNDERL + "EVIL" + bcolors.ENDC + bcolors.BLUE + "? ] \n" + bcolors.ENDC)
                print(bcolors.ENDC + "                  ~[ " + bcolors.BLUE + "Type: " + bcolors.RED + "1. " + bcolors.BLUE + "Accept " + bcolors.RED + "0. " + bcolors.BLUE+ "Reject " + bcolors.ENDC + " ]~\n" + bcolors.ENDC)
                try:
                    covenant = input(bcolors.GREEN + "(" + bcolors.ENDC + "africana:" + bcolors.DARKCYAN + "framework" + bcolors.GREEN + ")# " + bcolors.ENDC)
                    if covenant == '0':
                        os.system('clear')
                        beauty.graphics(), scriptures.verses()
                        break
                    elif covenant == '1':
                        neo.one()
                        break
                    else:
                        try:
                            print("\n")
                            warn = bcolors.ENDC + "  ~{ " + bcolors.RED + "Poor choice of selection!. Please select int -> " + bcolors.DARKCYAN + "0. or 1. " + bcolors.ENDC + "}~" + bcolors.ENDC
                            for w in warn:
                                sys.stdout.write(w)
                                sys.stdout.flush()
                                time.sleep(0.09)
                            neo.user_agree()
                            break
                        except:
                            neo.user_agree()
                            break
                except:
                    os.system('clear')
                    beauty.graphics(), scriptures.verses()
                    break
            except:
                break

#1
    def install_africana(self):
        while True:
            try:
                return installer.update_system(); neo.one()
            except:
                neo.one()
                break

#2
    def vanish_tor(self):
        while True:
            try:
                os.system('clear')
                beauty.graphics(), scriptures.verses()
                def anonymity():
                    while True:
                        try:
                            print(bcolors.BLUE + "\n            -[" + bcolors.ENDC + bcolors.UNDERL + " Select a number from the table below" + bcolors.ENDC + bcolors.BLUE + " ]-\n" + bcolors.ENDC)
                            print(bcolors.BLUE + "   [ 1.          Install & Setup Tor (start here)            ] " + bcolors.ENDC)
                            print(bcolors.BLUE + "   [ 2.            Start anonymizing through tor             ] " + bcolors.ENDC)
                            print(bcolors.BLUE + "   [ 3.           Stop tor & restore all iptables            ] " + bcolors.ENDC)
                            print(bcolors.BLUE + "   [ 4.   Chains (local => squid => privoxy => tor => net)   ] " + bcolors.ENDC)
                            print(bcolors.BLUE + "   [ 5.                  Check if using tor                  ] " + bcolors.ENDC)
                            print(bcolors.BLUE + "   [ 0.            Exit and go back fo main menu             ] \n" + bcolors.ENDC)
                            choice = input(bcolors.GREEN + "(" + bcolors.ENDC + "africana:" + bcolors.DARKCYAN + "framework" + bcolors.GREEN + ")# " + bcolors.ENDC)
                        except:
                            neo.one()
                            break
                        try:
                            if choice == '0':
                                neo.one()
                                break
                            elif choice == '1':
                                try:
                                    return anonymous.vanish_install(), anonymity()
                                except:
                                    neo.vanish_tor()
                                    break
                            elif choice == '2':
                                try:
                                    return anonymous.vanish_start(), anonymity()
                                except:
                                    neo.vanish_tor()
                                    break
                            elif choice == '3':
                                try:
                                    return anonymous.vanish_stop(), anonymity()
                                except:
                                    neo.vanish_tor()
                                    break
                            elif choice == '4':
                                try:
                                    return anonymous.chains_start(), anonymity()
                                except:
                                    neo.vanish_tor()
                                    break
                            elif choice == '5':
                                try:
                                    return anonymous.checktor_status(), anonymity()
                                except:
                                    neo.vanish_tor()
                                    break
                            else:
                                try:
                                    print("\n")
                                    warn = bcolors.ENDC + "   ~{  " + bcolors.RED + " Poor Choice Of Selection!!!. Please Select " + bcolors.DARKCYAN + " from 0. to 5. " + bcolors.ENDC +  "  }~" + bcolors.ENDC
                                    for w in warn:
                                        sys.stdout.write(w)
                                        sys.stdout.flush()
                                        time.sleep(0.09)
                                    neo.vanish_tor()
                                    break
                                except:
                                    neo.vanish_tor()
                                    break
                        except:
                            os.system('clear')
                            beauty.graphics(), scriptures.verses()
                            break
                anonymity()
                break
            except:
                break

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
                print(bcolors.ENDC + "\n   {" + bcolors.BLUE + " Selet a target from Bettercap's table above to be Attacked! " + bcolors.ENDC + "}\n" + bcolors.ENDC)
                try:
                    host = input(bcolors.GREEN + "(" + bcolors.ENDC + "africana:" + bcolors.DARKCYAN + "framework" + bcolors.GREEN + ")# " + bcolors.ENDC)
                except:
                    neo.one()
                    break
                os.system('clear')
                def neo_attack():
                    while True:
                        try:
                            mega_menu.menu_three()
                            print(bcolors.BLUE + "          -{ " + bcolors.RED + "ready to attack " + bcolors.BLUE + " }" + bcolors.BLUE + " => " + bcolors.BLUE + "{ " + bcolors.YELLOW + "{0}".format(host) + bcolors.BLUE + " }-\n" + bcolors.ENDC)
                            choice = input(bcolors.GREEN + "(" + bcolors.ENDC + "africana:" + bcolors.DARKCYAN + "framework" + bcolors.GREEN + ")# " + bcolors.ENDC)
                        except:
                            neo.one()
                            break
                        try:
                            if choice == '0':
                                neo.one()
                                break
                            elif choice == '1':
                                try:
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
                                    os.system('clear')
                                    return internal_scanner.packets_sniffer(host), attack_internal.neo_attack()
                                except:
                                    attack_internal.neo_attack()
                                    break
                            elif choice == '7':
                                try:
                                    os.system('clear')
                                    return internal_scanner.packets_responder(), attack_internal.neo_attack()
                                except:
                                    attack_internal.neo_attack()
                                    break
                            elif choice == '8':
                                try:
                                    os.system('clear')
                                    return internal_scanner.beefxss_bettercap(host), attack_internal.neo_attack()
                                except:
                                    attack_internal.neo_attack()
                                    break
                            elif choice == '9':
                                try:
                                    os.system('clear')
                                    return internal_scanner.packets_wireshark(), attack_internal.neo_attack()
                                except:
                                    attack_internal.neo_attack()
                                    break
                            else:
                                try:
                                    print("\n")
                                    warn = bcolors.ENDC + "   ~{  " + bcolors.RED + " Poor Choice Of Selection!!!. Please Select " + bcolors.DARKCYAN + " from 0. to 9. " + bcolors.ENDC +  "  }~" + bcolors.ENDC
                                    for w in warn:
                                        sys.stdout.write(w)
                                        sys.stdout.flush()
                                        time.sleep(0.09)
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
                beauty.graphics(), scriptures.verses()
                break

#4
    def rat_kitchen(self):
        while True:
            try:
                os.system('clear')
                beauty.graphics(), scriptures.verses()
                print(bcolors.BLUE + "\n           -[" + bcolors.ENDC + bcolors.UNDERL + " Select a number from the table below" + bcolors.ENDC + bcolors.BLUE + " ]-\n" + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 1.             Shellz (All Distro R.A.T)                ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 2.       Shakamura (Windows Rev Shells)" + bcolors.RED + "(try Me)" + bcolors.BLUE + "         ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 3.          PowerJoker (Windows Rev Shells)             ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 4.         MeterPeter (Windows Powershell C2)           ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 5.  Havoc C2 Default(user: 5pider pass: password1234)   ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 6.               Teardroid (Android Rat)                ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 7.          AndroRAT (Android 4 -> 10 Rat )             ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 8.                       To Add                         ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 9.                       To Add                         ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 0.              Exit & Go To Main Menu                  ] \n" + bcolors.ENDC)
                try:
                    choice = input(bcolors.GREEN + "(" + bcolors.ENDC + "africana:" + bcolors.DARKCYAN + "framework" + bcolors.GREEN + ")# " + bcolors.ENDC)
                except:
                    neo.one()
                    break
                try:
                    if choice == '0':
                        neo.one()
                        break
                    elif choice == '1':
                        try:
                            return rat.shellz(), neo.rat_kitchen()
                        except:
                            neo.rat_kitchen()
                            break
                    elif choice == '2':
                        try:
                            return rat.shakamura(), neo.rat_kitchen()
                        except:
                            neo.rat_kitchen()
                            break
                    elif choice == '3':
                        try:
                            return rat.powerjoker(), neo.rat_kitchen()
                        except:
                            neo.rat_kitchen()
                            break
                    elif choice == '4':
                        try:
                            return rat.meterpeter(), neo.rat_kitchen()
                        except:
                            neo.rat_kitchen()
                            break
                    elif choice == '5':
                        try:
                            return rat.havoc(), neo.rat_kitchen()
                        except:
                            neo.rat_kitchen()
                            break
                    elif choice == '6':
                        try:
                            return rat.teardroid(), neo.rat_kitchen()
                        except:
                            neo.rat_kitchen()
                            break
                    elif choice == '7':
                        try:
                            return rat.androrat(), neo.rat_kitchen()
                        except:
                            neo.rat_kitchen()
                            break
                    else:
                        try:
                            print("\n")
                            warn = bcolors.ENDC + "   ~{  " + bcolors.RED + " Poor Choice Of Selection!!!. Please Select " + bcolors.DARKCYAN + " from 0. to 9. " + bcolors.ENDC + "  }~" + bcolors.ENDC
                            for w in warn:
                                sys.stdout.write(w)
                                sys.stdout.flush()
                                time.sleep(0.09)
                            neo.rat_kitchen()
                            break
                        except:
                            neo.rat_kitchen()
                            break
                except:
                    os.system('clear')
                    beauty.graphics(), scriptures.verses()
                    break
            except:
                break

#5
    def attack_wifi(self):
        while True:
            try:
                os.system('clear')
                beauty.graphics(), scriptures.verses()
                print(bcolors.BLUE + "\n            -[" + bcolors.ENDC + bcolors.UNDERL + " Select a number from the table below" + bcolors.ENDC + bcolors.BLUE + " ]-\n" + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 1.         Wifite (All Wifi Hacks)(Automated)           ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 2.        Bettercap (Few Wifi Hacks)(Automated)         ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 3.      Wifipumpkin3 (Wifi Cred Phish)(Automated)       ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 4.                       To Add                         ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 5.                       To Add                         ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 6.                  Airgeddon (Manual)                  ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 7.        wifiPumpkin3 (Wifi Cred Phish)(Manual)        ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 8.                       To Add                         ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 9.                       To Add                         ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 0.              Exit & Go To Main Menu                  ] \n" + bcolors.ENDC)
                try:
                    choice = input(bcolors.GREEN + "(" + bcolors.ENDC + "africana:" + bcolors.DARKCYAN + "framework" + bcolors.GREEN + ")# " + bcolors.ENDC)
                except:
                    neo.one()
                    break
                try:
                    if choice == '0':
                        neo.one()
                        break
                    elif choice == '1':
                        try:
                            return wifi_killer.wifi_auto_attack_wifite(), neo.attack_wifi()
                        except:
                            neo.attack_wifi()
                            break
                    elif choice == '2':
                        try:
                            return wifi_killer.wifi_auto_attack_bettercap(), neo.attack_wifi()
                        except:
                            neo.attack_wifi()
                            break
                    elif choice == '3':
                        try:
                            return wifi_killer.wifi_auto_attack_wifipumpkin3(), neo.attack_wifi()
                        except:
                            neo.attack_wifi()
                            break
                    elif choice == '4':
                        try:
                            pass
                                #return wifi_killer.wifi_attack_airgeddon(), neo.attack_wifi()
                        except:
                                #neo.attack_wifi()
                                #break
                            pass
                    elif choice == '5':
                        try:
                            pass
                                #return wifi_killer.wifi_attack_airgeddon(), neo.attack_wifi()
                        except:
                                #neo.attack_wifi()
                                #break
                            pass
                    elif choice == '6':
                        try:
                            return wifi_killer.wifi_attack_airgeddon(), neo.attack_wifi()
                        except:
                            neo.attack_wifi()
                            break
                    elif choice == '7':
                        try:
                            return wifi_killer.wifi_attack_wifipumpkin3(), neo.attack_wifi()
                        except:
                            neo.attack_wifi()
                            break
                    elif choice == '8':
                        try:
                            pass
                                #return wifi_killer.wifi_attack_airgeddon(), neo.attack_wifi()
                        except:
                                #neo.attack_wifi()
                                #break
                            pass
                    elif choice == '9':
                        try:
                            pass
                                #return wifi_killer.wifi_attack_airgeddon(), neo.attack_wifi()
                        except:
                                #neo.attack_wifi()
                                #break
                            pass

                    else:
                        try:
                            print("\n")
                            warn = bcolors.ENDC + "   ~{  " + bcolors.RED + " Poor Choice Of Selection!!!. Please Select " + bcolors.DARKCYAN + " from 0. to 9. " + bcolors.ENDC + "  }~" + bcolors.ENDC
                            for w in warn:
                                sys.stdout.write(w)
                                sys.stdout.flush()
                                time.sleep(0.09)
                            neo.attack_wifi()
                            break
                        except:
                            neo.attack_wifi()
                            break
                except:
                    os.system('clear')
                    beauty.graphics(), scriptures.verses()
                    break
            except:
                break

#6
    def crack_passwords(self):
        while True:
            try:
                os.system('clear')
                beauty.graphics(), scriptures.verses()
                print(bcolors.BLUE + "\n            -{" + bcolors.ENDC + bcolors.UNDERL + " Select a number from the table below" + bcolors.ENDC + bcolors.BLUE + " }-\n" + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 1.       Air-Crackng  (All Wifi .Pcap)(Automated)       ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 2.            John (Password)(Automated)                ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 3.                       To Add                         ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 4.                       To Add                         ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 5.                       To Add                         ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 6.                       To Add                         ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 7.                       To Add                         ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 8.                       To Add                         ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 9.                       To Add                         ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 0.              Exit & Go To Main Menu                  ] \n" + bcolors.ENDC)
                try:
                    choice = input(bcolors.GREEN + "(" + bcolors.ENDC + "africana:" + bcolors.DARKCYAN + "framework" + bcolors.GREEN + ")# " + bcolors.ENDC)
                except:
                    neo.one()
                    break
                try:
                    if choice == '0':
                        neo.one()
                        break
                    elif choice == '1':
                        try:
                            return pass_cracker.aircracking_password(), neo.crack_passwords()
                        except:
                            neo.crack_passwords()
                            break
                    elif choice == '2':
                        try:
                            return pass_cracker.john_password(), neo.crack_passwords()
                        except:
                            neo.crack_passwords()
                            break
                    else:
                        try:
                            print("\n")
                            warn = bcolors.ENDC + "   ~{  " + bcolors.RED + " Poor Choice Of Selection!!!. Please Select " + bcolors.DARKCYAN + "from 0. to 9. " + bcolors.ENDC + "}~" + bcolors.ENDC
                            for w in warn:
                                sys.stdout.write(w)
                                sys.stdout.flush()
                                time.sleep(0.09)
                            neo.crack_passwords()
                            break
                        except:
                            neo.crack_passwords()
                            break
                except:
                    os.system('clear')
                    beauty.graphics(), scriptures.verses()
                    break
            except:
                break

#7
    def phish_creds(self):
        while True:
            try:
                os.system('clear')
                beauty.graphics(), scriptures.verses()
                print(bcolors.BLUE + "\n            -{" + bcolors.ENDC + bcolors.UNDERL + " Select a number from the table below" + bcolors.ENDC + bcolors.BLUE + " }-\n" + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 1.         Gophish(Browser Gui)(All Templetes)          ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 2.           Good Ginx (Advanced)(OTP Bypass)           ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 3.                AdvPhishing(OTP Bypass)               ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 4.               Setoolkit(Clones Website)              ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 5.                Anonphisher(OTP Bypass)               ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 6.                       To Add                         ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 7.                       To Add                         ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 8.                       To Add                         ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 9.                       To Add                         ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ 0.              Exit & Go To Main Menu                  ] \n" + bcolors.ENDC)
                try:
                    choice = input(bcolors.GREEN + "(" + bcolors.ENDC + "africana:" + bcolors.DARKCYAN + "framework" + bcolors.GREEN + ")# " + bcolors.ENDC)
                except:
                    neo.one()
                    break
                try:
                    if choice == '0':
                        neo.one()
                        break
                    elif choice == '1':
                        try:
                            return cred_phisher.phish_gophish(), neo.phish_creds()
                        except:
                            neo.phish_creds()
                            break
                    elif choice == '2':
                        try:
                            return cred_phisher.phish_goodginx(), neo.phish_creds()
                        except:
                            neo.phish_creds()
                            break
                    elif choice == '3':
                        try:
                            return cred_phisher.phish_zphisher(), neo.phish_creds()
                        except:
                            neo.phish_creds()
                            break
                    elif choice == '4':
                        try:
                            return cred_phisher.phish_setoolkit(), neo.phish_creds()
                        except:
                            neo.phish_creds()
                            break
                    elif choice == '5':
                        try:
                            return cred_phisher.phish_anonphisher(), neo.phish_creds()
                        except:
                            neo.phish_creds()
                            break
                    else:
                        try:
                            print("\n")
                            warn = bcolors.ENDC + "   ~{  " + bcolors.RED + " Poor Choice Of Selection!!!. Please Select " + bcolors.DARKCYAN + "from 0. to 9. " + bcolors.ENDC + "  }~" + bcolors.ENDC
                            for w in warn:
                                sys.stdout.write(w)
                                sys.stdout.flush()
                                time.sleep(0.09)
                            neo.phish_creds()
                            break
                        except:
                            neo.phish_creds()
                            break
                except:
                    os.system('clear')
                    beauty.graphics(), scriptures.verses()
                    break
            except:
                break

#8
    def attack_websites(self):
        while True:
            try:
                os.system('clear')
                beauty.graphics(), scriptures.verses()
                print(bcolors.ENDC + "\n     {" + bcolors.BLUE + " Enter Your Target (Either HTTP(S)//: HostName OR IP) " + bcolors.ENDC + "}\n" + bcolors.ENDC)
                try:
                    url = input(bcolors.GREEN + "(" + bcolors.ENDC + "africana:" + bcolors.DARKCYAN + "framework" + bcolors.GREEN + ")# " + bcolors.ENDC)
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
                    mega_menu.menu_two()
                    print(bcolors.BLUE + "          -{ " + bcolors.RED + "ready to attack " + bcolors.BLUE + " }" + bcolors.BLUE + " => " + bcolors.BLUE + "{ " + bcolors.YELLOW + "{0}".format(host) + bcolors.BLUE + " }-\n" + bcolors.ENDC)
                    while True:
                        try:
                            choice = input(bcolors.GREEN + "(" + bcolors.ENDC + "africana:" + bcolors.DARKCYAN + "framework" + bcolors.GREEN + ")# " + bcolors.ENDC)
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
                                    print("\n")
                                    warn = bcolors.ENDC + "   ~{  " + bcolors.RED + " Poor Choice Of Selection!!!. Please Select " + bcolors.DARKCYAN + " from 0. to 9. " + bcolors.ENDC + "  }~" + bcolors.ENDC
                                    for w in warn:
                                        sys.stdout.write(w)
                                        sys.stdout.flush()
                                        time.sleep(0.09)
                                    attack_websites.user_nuke(self)
                                    break
                                except:
                                    os.system('clear')
                                    user_nuke(self)
                                    break
                        except:
                            os.system('clear')
                            beauty.graphics(), scriptures.verses()
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

                beauty.graphics(), scriptures.verses()
                print("\n")
                print(bcolors.BLUE + "   [    I am Rojahs Montari. " + bcolors.YELLOW + "A devoted Christian Studied " + bcolors.BLUE + "    ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [       Education In Kenyatta University Kenya. Got       ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [              Passionate In Cybersecurity                ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [ I Then Furthered My Skills By Research, Practice &      ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [                      Experience.                        ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [    I Am Working As A Teacher, Cybersecurity Consoltant  ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [                 & Software Enginear.                    ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [           Contact me at rojahsmontari@gmail.com         ] " + bcolors.ENDC)
                print(bcolors.BLUE + "   [   Youtube Channel" + bcolors.RED + " https://youtube.com/@RojahsMontari" + bcolors.BLUE + "    ] \n" + bcolors.ENDC)
                print(bcolors.ENDC + "     -{ " + bcolors.BLUE + " Click " + bcolors.PURPLE + "Enter" + bcolors.YELLOW + " or " + bcolors.PURPLE + "0. " + bcolors.BLUE + "To Go Back To Main Menu. " + bcolors.PURPLE + "<---'" + bcolors.ENDC + " }- \n" + bcolors.ENDC)
                salvation =  bcolors.ENDC + "  -{ " + bcolors.GREEN + bcolors.UNDERL + "For God so loved the world, that he gave His." + bcolors.ENDC + color() + " [John 3:16] " + bcolors.ENDC + "}- " + bcolors.ENDC
                for s in salvation:
                    sys.stdout.write(s)
                    sys.stdout.flush()
                    time.sleep(0.09)
                print("\n")
            except:
                neo.one()
                break

            try:
                choice = input(bcolors.GREEN + "(" + bcolors.ENDC + "africana:" + bcolors.DARKCYAN + "framework" + bcolors.GREEN + ")# " + bcolors.ENDC)
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
                    choice = input(bcolors.GREEN + "(" + bcolors.ENDC + "africana:" + bcolors.DARKCYAN + "framework" + bcolors.GREEN + ")# " + bcolors.ENDC)
                except:
                    os.system('clear')
                    beauty.graphics(), scriptures.verses()
                    break
                try:
                    if choice == '0':
                        os.system('clear')
                        beauty.graphics(), scriptures.verses()
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
                        try:
                            print("\n")
                            warn = bcolors.ENDC + "  ~{ " + bcolors.RED + "Poor Choice Of Selection. Please Select ->" + bcolors.DARKCYAN + " from 0. to 9. " + bcolors.ENDC + "}~" + bcolors.ENDC
                            for w in warn:
                                sys.stdout.write(w)
                                sys.stdout.flush()
                                time.sleep(0.09)
                        except:
                            neo.one()
                            break
                except:
                    neo.one()
                    break
            except:
                os.system('clear')
                beauty.graphics(), scriptures.verses()
                break

neo = neo_start()
neo.user_agree()
if ' __name__' == '__main__':
        sys.exit(neo())
