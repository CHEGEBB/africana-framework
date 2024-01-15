import sys
import subprocess
from configs.config import *
from src.core.banner import *
from src.core.bcolors import *
from scriptures.verses import *

class anonym(object):
    def __init__(self):
        pass

    def vanish_install(self):
        os.system('clear')
        beauty.graphics(), scriptures.verses()
        print(bcolors.BLUE + "\n                 -[" + bcolors.ENDC + bcolors.UNDERL + " Installing & Configuring " + bcolors.ENDC + bcolors.BLUE + " ]-\n" + bcolors.ENDC)
        print(bcolors.BLUE + "   [             Tor (Install tor & set proxies)             ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [        Iptables (Install Iptables for firewalls)        ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [        Squid (Install Squid set through Privoxy)        ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [       Privoxy (Install Privoxy & set through tor)       ] " + bcolors.ENDC)
        print(bcolors.ENDC + "\n         {" + bcolors.RED + bcolors.UNDERL + " apt-get install -y tor squid privoxy iptables." + bcolors.ENDC + "}\n" + bcolors.ENDC)
        africana = bcolors.ENDC + " -{" + bcolors.YELLOW + " Installin iptables, tor, privoxy, squid, dnsmasq & configing " + bcolors.ENDC + "}-\n" + bcolors.ENDC
        for a in africana:
            sys.stdout.write(a)
            sys.stdout.flush()
            time.sleep(0.09)
        print("\n")
        subprocess.Popen('apt-get install -y tor squid privoxy iptables', shell = True).wait(), config.configure_all()
        subprocess.Popen('systemctl daemon-reload; systemctl enable tor@default.service; systemctl enable privoxy.service; systemctl enable squid.service; systemctl restart tor@default.service; systemctl restart privoxy.service; systemctl restart squid.service; systemctl --no-pager status tor@default.service; systemctl --no-pager status privoxy.service; systemctl --no-pager status squid.service; sleep 3', shell = True).wait()

    def vanish_start(self):
        os.system('clear')
        subprocess.Popen(['python3 externals/tor-vanish/vanish.py -m'], shell = True).wait()

    def vanish_stop(self):
        os.system('clear')
        subprocess.Popen('python3 externals/tor-vanish/vanish.py -e', shell = True).wait()

    def checktor_status(self):
        os.system('clear')
        subprocess.Popen('python3 externals/tor-vanish/vanish.py -w', shell = True).wait()

    def chains_start(self):
        os.system('clear')
        subprocess.Popen('bash modules/secmon.py', shell = True).wait()

anonymous = anonym()
if ' __name__' == '__main__':
        sys.exit(anonymous())
