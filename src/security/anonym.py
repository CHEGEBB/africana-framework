import sys
import subprocess
from src.core.banner import *
from src.core.bcolors import *

class anonym(object):
    def __init__(self):
        pass

    def vanish_install(self):
        beauty.vanish_banner()
        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|    † Installing & Configuring Tor, Iptables & Vanish Into Your System. †     |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
        subprocess.Popen('apt-get install -y tor squid privoxy iptables; rm -rf /usr/local/bin/vanish; rm -rf /usr/local/bin/secmon; cp -rv ./modules/vanish.py /usr/local/bin/vanish; cp -rv ./modules/secmon.py /usr/local/bin/proxmon; chmod +x /usr/local/bin/vanish; chmod +x /usr/local/bin/proxmon', shell = True).wait(), config.configure_all()
        subprocess.Popen('systemctl daemon-reload; systemctl enable tor@default.service; systemctl enable privoxy.service; systemctl enable squid.service; systemctl restart tor@default.service; systemctl restart privoxy.service; systemctl restart squid.service; systemctl --no-pager status tor@default.service; systemctl --no-pager status privoxy.service; systemctl --no-pager status squid.service; sleep 3', shell = True).wait()

    def vanish_start(self):
        subprocess.Popen(['vanish -m'], shell = True).wait()

    def vanish_stop(self):
        subprocess.Popen('vanish -e', shell = True).wait()

anonymous = anonym()
if ' __name__' == '__main__':
        sys.exit(anonymous())
