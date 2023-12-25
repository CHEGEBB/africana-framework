#!/usr/bin/python3

import os
import re
import sys
import time
import random
import requests
import subprocess
from signal import signal, SIGINT

def check_os():
    if os.name == "nt":
        operating_system = "windows"
    if os.name == "posix":
        operating_system = "posix"
    return operating_system

if check_os() == "posix":
    class bcolors:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERL = '\033[4m'
        ENDC = '\033[0m'
        backBlack = '\033[40m'
        backRed = '\033[41m'
        backGREEN = '\033[42m'
        backYellow = '\033[43m'
        backBlue = '\033[44m'
        backMagenta = '\033[45m'
        backCyan = '\033[46m'
        backWhite = '\033[47m'

        def disable(self):
            self.PURPLE = ''
            self.CYAN = ''
            self.BLUE = ''
            self.GREEN = ''
            self.YELLOW = ''
            self.RED = ''
            self.ENDC = ''
            self.BOLD = ''
            self.UNDERL = ''
            self.backBlack = ''
            self.backRed = ''
            self.backGREEN = ''
            self.backYellow = ''
            self.backBlue = ''
            self.backMagenta = ''
            self.backCyan = ''
            self.backWhite = ''
            self.DARKCYAN = ''

else:
    class bcolors:
        PURPLE = ''
        CYAN = ''
        DARKCYAN = ''
        BLUE = ''
        GREEN = ''
        YELLOW = ''
        RED = ''
        BOLD = ''
        UNDERL = ''
        ENDC = ''
        backBlack = ''
        backRed = ''
        backGREEN = ''
        backYellow = ''
        backBlue = ''
        backMagenta = ''
        backCyan = ''
        backWhite = ''

        def disable(self):
            self.PURPLE = ''
            self.CYAN = ''
            self.BLUE = ''
            self.GREEN = ''
            self.YELLOW = ''
            self.RED = ''
            self.ENDC = ''
            self.BOLD = ''
            self.UNDERL = ''
            self.backBlack = ''
            self.backRed = ''
            self.backGREEN = ''
            self.backYellow = ''
            self.backBlue = ''
            self.backMagenta = ''
            self.backCyan = ''
            self.backWhite = ''
            self.DARKCYAN = ''

color_taken = []
def color(*args):
    colors = [bcolors.BLUE, bcolors.PURPLE, bcolors.CYAN, bcolors.DARKCYAN, bcolors.GREEN,
            bcolors.YELLOW, bcolors.RED]
    if args:
        args, = args
        return args
    else:
        if not color_taken: return random.choice(colors)
        else:
            return random.choice(list(set(colors).difference(color_taken)))
check_os()

def sudo():
    if not os.geteuid() == 0:
        sys.exit(color() + "I'm afraid I need some superuser privilages, Start with 'sudo'. Jesus Loves You ¯\(ツ)/¯" + bcolors.ENDC)


def handler(signal_received, frame):
    print(color() + bcolors.BOLD + "\nCTRL-C detected. Exiting.... ")
    exit(0)


if __name__ == '__main__':
    signal(SIGINT, handler)


def logo(*args):

    global color_taken

    logo = r'''
                              [africana]

                ███████▓█████▓▓╬╬╬╬╬╬╬╬▓███▓╬╬╬╬╬╬╬▓╬╬▓█
                ████▓▓▓▓╬╬▓█████╬╬╬╬╬╬███▓╬╬╬╬╬╬╬╬╬╬╬╬╬█
                ███▓▓▓▓╬╬╬╬╬╬▓██╬╬╬╬╬╬▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
                ████▓▓▓╬╬╬╬╬╬╬▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
                ███▓█▓███████▓▓███▓╬╬╬╬╬╬▓███████▓╬╬╬╬▓█
                ████████████████▓█▓╬╬╬╬╬▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬█
                ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
                ████▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
                ███▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
                █████▓▓▓▓▓▓▓▓█▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
                █████▓▓▓▓▓▓▓██▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
                █████▓▓▓▓▓████▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
                ████▓█▓▓▓▓██▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
                ████▓▓███▓▓▓▓▓▓▓██▓╬╬╬╬╬╬╬╬╬╬╬╬█▓╬▓╬╬▓██
                █████▓███▓▓▓▓▓▓▓▓████▓▓╬╬╬╬╬╬╬█▓╬╬╬╬╬▓██
                █████▓▓█▓███▓▓▓████╬▓█▓▓╬╬╬▓▓█▓╬╬╬╬╬╬███
                ██████▓██▓███████▓╬╬╬▓▓╬▓▓██▓╬╬╬╬╬╬╬▓███
                ███████▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬████
                ███████▓▓██▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓████
                ████████▓▓▓█████▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█████
                █████████▓▓▓█▓▓▓▓▓███▓╬╬╬╬╬╬╬╬╬╬╬▓██████
                ██████████▓▓▓█▓▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬▓███████
                ███████████▓▓█▓▓▓▓███▓╬╬╬╬╬╬╬╬╬▓████████
                ██████████████▓▓▓███▓▓╬╬╬╬╬╬╬╬██████████
                ███████████████▓▓▓██▓▓╬╬╬╬╬╬▓███████████

                            [codename:humble]
'''

    verse = ["""{}I will walk among you, and will be your God [Lev.26:12] {}(ღ˘⌣˘)❛ั◡❛ัღ)""", """{}The LORD is longsuffering, and of great mercy [Num.14:18]{} 〆(・∀・＠ )""",
                  """{}Thou shalt love the LORD thy God with all thine heart [Deut.6:5]{} ✿(੭*ˊᵕˋ)੭*""",

                  """{}Thou shalt rejoice before the LORD thy God [Deut.12:18]{} っ◕‿◕)っ ♥""", """{}Only be thou strong and very courageous [Josh.1:7]{} (´･ᴗ･`)♡""",
                  """{}The LORD your God, He it is that fighteth for you [Josh.23:10]{} ʕ•̬͡•ʔ""", """{}I will never break my covenant with you [Judg.2:1]{} (′◕ᴗ◕‵)""",
                  """{}Yet he hath made with me an everlasting covenant [2 Sam.23:5]{} ( ◠‿◠✿)""", """{}Give therefore thy servant an understanding heart [1 Kin.3:9]{} ٩(˘◡˘)۶""",
                  """{}The LORD your God ye shall fear; and he shall deliver you [2 Kin.17:39]{} ʕ•̬͡•ʔ""", """{}They that seek the LORD shall not want any good thing [Ps.34:10]{} ᕦʕ•̀ᴥ•́ʔᕤ""",
                  """{}Call upon me in the day of trouble: I will deliver thee [Ps.50:15]{} ໒( ♥ ◡ ♥ )७"""
                  ]

    quats = random.choice(verse)
    color_taken.append(color())
    color_taken.append(color())
    
    print(f"{color_taken[0]}{logo}{bcolors.ENDC}", end = '\n', flush=True)
    print(quats.strip("\n").format(color_taken[1], color()) + bcolors.ENDC, sep = bcolors.BOLD, flush=True)
    if args: time.sleep(0.8)


def mask():
    try:
        mask0 = requests.get('https://icanhazip.com/').text
    except requests.exceptions.RequestException:
        try:
            mask1 = requests.get('https://ipinfo.io/ip').text
            return mask1
        except requests.exceptions.RequestException as e:
            print(f'\n{e}')
            sys.exit(color() + """\n            Sorry, can't fetch the Details.
Either the site's down or something's up with your internet-config.

            You may find solution here :)
https://github.com/Feliz-SZK/Linux-Decoded/blob/master/Fix%20temporary%20failure%20in%20name%20resolution.md""" + bcolors.ENDC)


    return mask0


def frag():
    fragment = subprocess.Popen("iptables -t nat -L -n", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
    frag, defrag = fragment
    if defrag: print(f"\n{bcolors.RED}encounterd some problems while checking the iptables-details{bcolors.ENDC}")
    return frag.decode("utf-8")

def finesse(langa, resolv_switch):

    if langa > 5:
        sys.exit(
            f"\n{color(bcolors.RED)}excceeded no of retries, terminating to prevent memory corruption.{bcolors.ENDC}")

    if not os.path.exists('/etc/resolv.conf'):
        print(f"\n{color(bcolors.BLUE)}resolv.conf file is missing,", end=" ")
        askin = str(input(
            f"{color(bcolors.BLUE)}you want me to manually create it for you! {bcolors.GREEN}Y/N: {bcolors.ENDC}")).lower().strip()

        if askin == 'y':
            try:
                with open("/etc/resolv.conf", "w") as f:
                    f.write("nameserver 127.0.0.1")
                resolv_switch += 1
                print(f"{color()}Done, saved with local dns.{bcolors.ENDC}")
            except Exception as e:
                print(
                    f"{color(bcolors.RED)}something's wrong, can't write the file.{bcolors.ENDC}\n{e}")
        elif askin == "n":
            sys.exit(f"{color(bcolors.GREEN)}Roger that, terminating....{bcolors.ENDC}")
        else:
            langa += 1
            return finesse(langa, resolv_switch)
    return resolv_switch


torrstring = ['# Created By africana-framework. Delete At Your Own Risk!!', '', 'VirtualAddrNetworkIPv4 10.192.0.0/10', 'AutomapHostsOnResolve 1',
              'TransPort 9040 IsolateClientAddr IsolateClientProtocol IsolateDestAddr IsolateDestPort', 'DNSPort 5353', 'CookieAuthentication 1']


resolvstring = '# Created By africana-framework. Delete At Your Own Risk!!\n\nnameserver 127.0.0.1'


def resolv_config(r_switch):
    if r_switch == 0:
        with open('/etc/resolv.conf') as f:
            lines = f.read().splitlines()

        if resolvstring not in lines:
            print(bcolors.GREEN + bcolors.BOLD + "Configuring resolv.conf" + bcolors.ENDC)
            time.sleep(0.4)
            os.system(
                    "cp /etc/resolv.conf /etc/resolv.conf.backup_vanish")
            with open('/etc/resolv.conf', 'w') as rconf:
                rconf.write("%s\n" % resolvstring)
            print(color(bcolors.RED) + "DONE :)" + bcolors.ENDC)
        else:
            if resolvstring in list(filter(lambda rc: 'nameserver' in rc, lines))[0]:
                print(bcolors.GREEN + bcolors.BOLD + "Configuring Resolv.config" + bcolors.ENDC)
                time.sleep(0.4)
                print(color() + bcolors.BOLD + """ :) Already Configured""" + bcolors.ENDC)
                time.sleep(0.5)
            else:
                print(bcolors.GREEN + bcolors.BOLD + "Configuring resolv.conf" + bcolors.ENDC)
                os.system(
                    "cp /etc/resolv.conf /etc/resolv.conf.backup_vanish")
                with open('/etc/resolv.conf', 'w') as rconf:
                    rconf.write("%s\n" % resolvstring)
                print(color(bcolors.RED) + "Done...." + bcolors.ENDC)
    else:
        print(bcolors.GREEN + bcolors.BOLD + "Configuring Resolv.config" + bcolors.ENDC)
        time.sleep(0.4)
        print(color() + " :) Already Configured" + bcolors.ENDC)

    return 0

def configure():

    if "vanish" in frag(): sys.exit(f"\n{bcolors.BLUE}vanish is already running....{bcolors.ENDC}")

    r_switch = finesse(0, 0)

    if os.system("which tor > /dev/null") == 0:
    
        if not os.path.exists('/etc/tor/torrc'):
            print(
                f"{color(bcolors.RED)}No torrc file is configured.....{bcolors.ENDC}{color(bcolors.GREEN)}Configuring:)")
            try:
                f = open('/etc/tor/torrc', 'w+')
                for elements in torrstring:
                    f.write("%s\n" % elements)
                f.close()
                print(f"{color(bcolors.CYAN)}Done....{bcolors.ENDC}")
            except Exception as e:
                print(f"{color(bcolors.RED)}Failed to write the torrc file{bcolors.ENDC} \n {e}")
                sys.exit()
        else:
            print(f"\n{color(bcolors.GREEN)}{bcolors.BOLD}Configuring Torrc {bcolors.ENDC}")
            time.sleep(0.4)

            with open('/etc/tor/torrc') as x:
                verse = x.read().splitlines()


            subprocess.Popen(["cp", "/etc/tor/torrc", "/etc/tor/torrc.bak_vanish"], stdout=subprocess.PIPE).communicate()
            torrc = open('/etc/tor/torrc', 'w')
            for elements in torrstring:
                torrc.write("%s\n" % elements)
            torrc.close()
            print(f"{color(bcolors.RED)}DONE :){bcolors.ENDC}")


    else:
        print(f'''\n{color(bcolors.RED)}tor isn't installed, install it with 'sudo apt install tor'{bcolors.ENDC}''')
        sys.exit()

    subprocess.Popen(['service', 'tor', 'restart'])

    resolv_config(r_switch)



def terminate():

    trigger = 0
    if os.path.exists('/etc/resolv.conf.backup_vanish'):
        trigger += 1
        restore = "yes | mv /etc/resolv.conf.backup_vanish /etc/resolv.conf"
        process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE,
                                   stdout=open(os.devnull, 'wb'), stderr=subprocess.PIPE)
        print(f"\n{bcolors.GREEN}{bcolors.BOLD}reverting to default resolv.conf{bcolors.ENDC}")
        out, err = process.communicate(restore.encode('utf-8'))

        if err:
            print('\n' + err.decode('utf8').replace("\n", '\n'))
            print(bcolors.RED + r'''\n      I guess you're messing around,
else your system has some serious issues; deleting backups itself.''' + bcolors.ENDC)
            sys.exit()
        time.sleep(0.5)
        print(f"{bcolors.CYAN}{bcolors.BOLD}[Complete]{bcolors.ENDC}")
    
    if os.path.exists('/etc/tor/torrc.bak_vanish'):
        trigger += 1
        torrc_restore = "mv /etc/tor/torrc.bak_vanish /etc/tor/torrc"
        process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE,
                                   stdout=open(os.devnull, 'wb'), stderr=subprocess.PIPE)
        print(f"{bcolors.GREEN}{bcolors.BOLD}dropping of torrc file{bcolors.ENDC}")
        out, err = process.communicate(torrc_restore.encode('utf-8'))

        if err:
            print('\n' + err.decode('utf8').replace("\n", '\n'))
            print(" ")
            print(bcolors.GREEN + r'''I guess you're messing around, 
else your system has some serious issues(deleting backups itself)''' + bcolors.ENDC)
            sys.exit()
        time.sleep(0.5)
        print(f"{bcolors.CYAN}{bcolors.BOLD}[Done]{bcolors.ENDC}")
    if "vanish" in frag():
        trigger += 1
        print(bcolors.GREEN + bcolors.BOLD + 'Restoring Iptables rules..' + bcolors.ENDC)
        if os.path.exists("/etc/iptables_rules_vanish.bak"):
            one, afric = subprocess.Popen('iptables-restore < /etc/iptables_rules_vanish.bak', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
            os.remove('/etc/iptables_rules_vanish.bak')
            if afric and b"Warning" not in afric:
                print(f"{bcolors.RED} can't restore previous rules, seems the file's being tampered with\n{bcolors.RED} {afric.decode('utf-8').strip()}{bcolors.ENDC}")
                print(f"{bcolors.GREEN}{bcolors.BOLD}Defaulting..{bcolors.ENDC}")
                reset_to_default(overide_pass=True)
        else: 
            reset_to_default(overide_pass=True, reset_as_child_func=True)
        time.sleep(1)

    if trigger == 0:
        print('\n' + bcolors.RED + bcolors.BOLD + "No instances of vanish has been executed")
        print(bcolors.GREEN + bcolors.BOLD + '[Exiting...]' + bcolors.ENDC)
        sys.exit()
    else: print(color() + bcolors.BOLD + 'Cleaning up complete :)' + bcolors.ENDC)


def torcircuit():

    if not "vanish" in frag():
        print('\n' + color() + 'You must start vanish first' + bcolors.ENDC)
        sys.exit()
    else:
        subprocess.Popen(["service", "tor", "reload"])
        print(bcolors.GREEN + "\nSrambling Tor Nodes" + bcolors.ENDC)
        time.sleep(0.4)
        print(color() + bcolors.BOLD + "DONE :)" + bcolors.ENDC)
        time.sleep(0.4)
        print(bcolors.GREEN + "Your new ip appears to be: " +
              bcolors.ENDC + color() + bcolors.BOLD + str(mask()) + bcolors.ENDC)


def tor_stat(e_langa):

    try:
        resp = requests.get("https://check.torproject.org")
    except Exception as e:
        e_langa += 1
        if e_langa > 2:
            sys.exit(color() + f"""\nUnable to get the network-details, try with -w once.
if this persists, please raise an issue on github.\n\n{color(bcolors.RED)}{e}""" + bcolors.ENDC)
        print(f"{color(bcolors.GREEN)}\nhaving trouble fetching exit-node details, {color(bcolors.CYAN)}retrying....{color()}{e_langa}{bcolors.ENDC}")
        time.sleep(1.2)
        return tor_stat(e_langa)

    status = re.search(r'<title[^>]*>([^<]+)</title>', resp.text).group(1)
    mask = re.search( r'[0-9]+(?:\.[0-9]+){3}', resp.text ).group(0)
        
    print("\nYour Ip address is: " + color() + bcolors.BOLD + mask + bcolors.ENDC)
    print(f"{color()}Congratulations, you're using tor :){bcolors.ENDC}") if "Congratulations" in status.strip() else print(f"{color()}{status.strip()}{bcolors.ENDC}")
    return 0


def check_default_rules(shell:bool = True):
    return subprocess.Popen(r"iptables-save | grep '^\-' | wc -l", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=shell).communicate()


def firewall():

    print(f"{bcolors.GREEN}Backing up Iptables..{bcolors.ENDC}")
    firewall_green, firewall_red = check_default_rules()
    if firewall_red:
        print(f"{bcolors.RED}\nCan't execute {bcolors.BLUE}iptables-save{bcolors.ENDC}. see the reson below.\n{bcolors.RED}{bcolors.BOLD}{firewall_red.decode('utf-8')}{bcolors.ENDC}")
        sys.exit()
    if firewall_green.strip() == b'0':
        print(f" {bcolors.BLUE}default rules are configured, skipping..")
    else:
        proc = subprocess.Popen('iptables-save > /etc/iptables_rules_vanish.bak', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        outp, error = proc.communicate()
        if error and b'Warning:' not in error: 
            print(f"{bcolors.RED}\nCan't seem to save the iptables_bakup file in /etc.\n{error.decode('utf-8')}")
            sys.exit()
        print(f"{bcolors.RED}Done :) {bcolors.BLUE}location: {bcolors.RED}/etc/iptables_rules_vanish.bak{bcolors.ENDC}", end='\n') 


    inn_out_rules = '''

### Set variables
# The UID that Tor runs as (varies from system to system)

_tor_uid=`id -u debian-tor` #Debian/Ubuntu

# Tor's TransPort
_trans_port="9040"

# Tor's DNSPort
_dns_port="5353"

# Tor's VirtualAddrNetworkIPv4
_virt_addr="10.192.0.0/10"


# LAN destinations that shouldn't be routed through Tor
_non_tor="127.0.0.0/8 10.0.0.0/8 172.16.0.0/12 192.168.0.0/16"

# Other IANA reserved blocks (These are not processed by tor and dropped by default)
_resv_iana="0.0.0.0/8 100.64.0.0/10 169.254.0.0/16 192.0.0.0/24 192.0.2.0/24 192.88.99.0/24 198.18.0.0/15 198.51.100.0/24 203.0.113.0/24 224.0.0.0/4 240.0.0.0/4 255.255.255.255/32"

# Flushing existing Iptables Chains/Firewall rules #
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT

iptables -F
iptables -X
iptables -Z 

iptables -t nat -F
iptables -t nat -X
iptables -t mangle -F
iptables -t mangle -X
iptables -t raw -F
iptables -t raw -X

### *nat OUTPUT (For local redirection)
# nat .onion addresses
iptables -t nat -A OUTPUT -d $_virt_addr -p tcp -m tcp --tcp-flags FIN,SYN,RST,ACK SYN -j REDIRECT --to-ports $_trans_port

# nat dns requests to Tor
iptables -t nat -A OUTPUT -d 127.0.0.1/32 -p udp -m udp --dport 53 -j REDIRECT --to-ports $_dns_port -m comment --comment "vanish_triggered"

# Don't nat the Tor process, the loopback, or the local network
iptables -t nat -A OUTPUT -m owner --uid-owner $_tor_uid -j RETURN
iptables -t nat -A OUTPUT -o lo -j RETURN

# Allow lan access for hosts in $_non_tor and $_resv_ina
# This is to make sure that this local addresses don't get dropped.
for _lan in $_non_tor; do
  iptables -t nat -A OUTPUT -d $_lan -j RETURN
done

for _iana in $_resv_iana; do
  iptables -t nat -A OUTPUT -d $_iana -j RETURN
done

# Redirect all other pre-routing and output to Tor's TransPort
iptables -t nat -A OUTPUT -p tcp -m tcp --tcp-flags FIN,SYN,RST,ACK SYN -j REDIRECT --to-ports $_trans_port

### *filter INPUT
iptables -A INPUT -m state --state ESTABLISHED -j ACCEPT
iptables -A INPUT -i lo -j ACCEPT

# Log & Drop everything else. Uncomment to enable logging
#iptables -A INPUT -j LOG --log-prefix "Dropped INPUT packet: " --log-level 7 --log-uid
iptables -A INPUT -j DROP

### *filter FORWARD
iptables -A FORWARD -j DROP

### Fix for possible kernel packet-leak as discussed in, 
### https://lists.torproject.org/pipermail/tor-talk/2014-March/032507.html
### uncomment below lines to log dropped packets

iptables -A OUTPUT -m conntrack --ctstate INVALID -j DROP
# iptables -A OUTPUT -m state --state INVALID -j LOG --log-prefix "Transproxy state leak blocked: " --log-uid
iptables -A OUTPUT -m state --state INVALID -j DROP

### *filter OUTPUT
iptables -A OUTPUT -m state --state ESTABLISHED -j ACCEPT

# Allow Tor process output
iptables -A OUTPUT -m owner --uid-owner $_tor_uid -p tcp -m tcp --tcp-flags FIN,SYN,RST,ACK SYN -m state --state NEW -j ACCEPT

# Allow loopback output
iptables -A OUTPUT -d 127.0.0.1/32 -o lo -j ACCEPT

# Tor transproxy magic
iptables -A OUTPUT -d 127.0.0.1/32 -p tcp -m tcp --dport $_trans_port --tcp-flags FIN,SYN,RST,ACK SYN -j ACCEPT


# Drop everything else.
iptables -A OUTPUT -j DROP

### Set default policies to DROP
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT DROP

    '''
    print(f"{bcolors.GREEN}Setting up firewall rules{bcolors.ENDC}")
    process5 = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE,
                                stdout=open(os.devnull, 'wb'), stderr=subprocess.PIPE)
    out5, err5 = process5.communicate(inn_out_rules.encode('utf-8'))


    if err5:
        print('\n' + color() + err5.decode('utf8').strip() + bcolors.ENDC)
        print("""There's something strange with your system
It doesn't let me change the iptable rules""")
        sys.exit()
    time.sleep(1.2)
    print(color(bcolors.RED) + "DONE :)" + bcolors.ENDC)


def reset_to_default(reset_trigger: int= 0, overide_pass: bool= False, reset_as_child_func:bool = False, nuke_sanity:bool = False):

    if not overide_pass:
        if reset_trigger >7: sys.exit(f"{bcolors.RED}exiting to prevent memory corruption.{bcolors.ENDC}")
        reset_consent = input(f"{color()}\nThis will overwrite all of your existing rules {bcolors.GREEN}Y(do it){bcolors.ENDC}/{bcolors.RED}N(exit){bcolors.ENDC}: ").lower()
        if reset_consent == 'y': pass
        elif reset_consent == 'n': sys.exit(f"{bcolors.RED}Copy that..\n{bcolors.ENDC}")
        else:
            reset_trigger += 1
            return reset_to_default(reset_trigger=reset_trigger)
        
        time.sleep(1)
        print(f'{PURPLE}Backing up current rules, just in case..{bcolors.ENDC}')
        
        default_check_green, default_check_red = check_default_rules()
        if default_check_red:
            print(f"{bcolors.RED}Error while checking existing rules; {orange}exiting..\n{yellow}Error message: {color()}{default_check_red.decode('utf-8')}{bcolors.ENDC}")
            sys.exit()
        if default_check_green.strip() != b'0': 
            file_name_id = time.strftime("%m_%d_%Y-%H:%M:%S", time.localtime())
            proc = subprocess.Popen(f'sudo iptables-save > /tmp/iptables_{file_name_id}.rules', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            outp, error = proc.communicate()
            if error and b'Warning:' not in error: 
                print(f"{bcolors.RED}\nCan't seem to save the iptables_bakup file in /tmp directory.\n{error.decode('utf-8')}")
                sys.exit()
            print(f"{bcolors.CYAN}Saved in {bcolors.BLUE}/tmp{bcolors.ENDC} as {bcolors.RED}iptables_{file_name_id}.rules{bcolors.ENDC}", end='\n\n') 
        else:
            print(f"{bcolors.CYAN} Default rules are set, backup not required :){bcolors.ENDC}", end= "\n")
            nuke_sanity = True
            
        print(bcolors.GREEN + bcolors.BOLD + 'Reseting Iptables' + bcolors.ENDC) if not nuke_sanity else print(f"{bcolors.CYAN}{bcolors.BOLD}I'm nuking everything just for sanity{bcolors.ENDC}")
    iptables_rules = '''

# Accepting all traffic first#
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
 
# Flushing All Iptables Chains/Firewall rules #
iptables -F
 
# Deleting all Iptables Chains #
iptables -X
 
# Flushing all counters too #
iptables -Z 
# Flush and delete all nat and  mangle #
iptables -t nat -F
iptables -t nat -X
iptables -t mangle -F
iptables -t mangle -X
iptables -t raw -F
iptables -t raw -X
    '''
    process = subprocess.Popen(
        '/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate(iptables_rules.encode('utf-8'))

    time.sleep(0.5)
    if err:
        print(color() + "Can't reset Iptables")
        print(color() + '\n' + err.decode('utf8').strip() + bcolors.ENDC)
        sys.exit()
    if reset_as_child_func:
        pass
    else:
        print(f"{bcolors.BLUE} Successfully reset Iptables to default :)")

    return 0


def usage():
    print(color() + """

⠀⠀⠀⠀⠀⠀⠀⡏⠉⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⠉⠉⠀⠀⠉⠉⢹⠀⠀⠀⠀
⠀⠀⠀⠀⠘⠒⠒⡆⠀⡖⠒⠃⠀⠀⠀⠀
⠀⡿⡀⠀⠀⠀⠀⡇⠀⡇⠀⠀⠀⠀⡜⡇
⠀⡇⡇⠀⠀⠀⠀⡇⠀⡇⠀⠀⠀⢀⠇⡇
⠀⢧⠘⢴⠲⣄⠈⠉⠉⠀⢀⡴⢲⠞⢰⠀
⠀⠈⠳⡄⠳⠌⠳⡀⠀⡴⠋⠴⢁⡴⠁⠀
⠀⠀⠀⢸⠀⠀⠀⡱⢸⠁⠀⠀⢸⠀⠀⠀
⠀⠀⠀⡞⠀⠀⠀⡇⠀⡇⠀⠀⠸⠀

   Jesus love's u.""" + bcolors.ENDC)
    banner = """
+------------------------------------------------------------------+
|                                                                  |
| -h, --help               show this help message and exit         |
| -m, --mask               start anonymizing                       |
| -e, --expose             get back to surface-web                 |
| -i, --ip                 check current IP address                |
| -s, --shuffle            connect to a different exit-node        |
| -w, --who am I           check if using tor                      |
| -n, --nuke               backs up & resets Iptables to default.  |
+------------------------------------------------------------------+
                                                 [codename:Holyness]
"""
    print(color() + banner + bcolors.ENDC)
    print(color() + 'Let us search & try our ways, and turn again to the Good LORD. [Lam.3:40](′◕ᴗ◕‵)' + bcolors.ENDC)

arg = sys.argv[1:]
args = {"proxy": ["--mask", "-m"], "surface":["--expose", "-e"], "identity":["--ip", "-i"], 
        "scramble": ["--shuffle", "-s"], "cover": ['--whatami', '-w'], "revert_tables": ['--nuke', '-n'], "help": ["-h", "--help"]}


if len(arg) != 1:
    print(f"{color()}I need one argument: like -m or -e\nplease, use -h/--help for more usage :)\n{bcolors.ENDC}")
elif sys.argv[1].lower() in args['proxy']:
    sudo()
    logo("sleep")
    configure()
    firewall()
    tor_stat(0)
elif sys.argv[1].lower() in args['surface']:
    sudo()
    logo("sleep")
    terminate()
elif sys.argv[1].lower() in args['identity']:
    logo()
    print('\n' + bcolors.GREEN + 'your ip is: ' + bcolors.ENDC + color() + mask() + bcolors.ENDC)
elif sys.argv[1].lower() in args['scramble']:
    sudo()
    logo("sleep")
    torcircuit()
elif sys.argv[1].lower() in args['cover']:
    logo()
    tor_stat(0)
elif sys.argv[1].lower() in args['revert_tables']:
    sudo()
    logo("sleep")
    reset_to_default()
elif sys.argv[1].lower() in args['help']:
    usage()
else:
    print(
        f"{color(bcolors.GREEN)} {sys.argv[1]}! {color(bcolors.BLUE)}ain't a valid trigger. {bcolors.ENDC}")
    usage()
