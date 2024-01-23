import sys
import time
import subprocess
from src.core.bcolors import *

class phish_hack(object):
    def __init__(self):
        pass

    def phish_gophish(self):
        os.system('clear')
        process = subprocess.Popen('gophish', shell = True).wait()
        time.sleep(0.03)
        return process

    def phish_goodginx(self):
        os.system('clear')
        process = subprocess.Popen('evilginx2', shell = True).wait()
        time.sleep(0.03)
        return process

    def phish_setoolkit(self):
        os.system('clear')
        process = os.system('python3 externals/set/setoolkit')
        return process

    def phish_anonphisher(self):
        os.system('clear')
        process = subprocess.Popen("cd /usr/local/opt/africana-framework/externals/anonphisher; bash anonphisher.sh", shell = True).wait()
        return process

    def phish_zphisher(self):
        os.system('clear')
        process = subprocess.Popen("cd /usr/local/opt/africana-framework/externals/AdvPhishing; bash AdvPhishing.sh", shell = True).wait()
        time.sleep(0.03)
        return process

cred_phisher = phish_hack()
if ' __name__' == '__main__':
        sys.exit(cred_phisher())
