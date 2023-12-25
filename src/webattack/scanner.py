import sys
import time
import subprocess
from src.core.bcolors import *

class scanners(object):
    def __init__(self, host):
        self.host = host
    def wafw00f(self, host):
        print(bcolors.BLUE + """
+-----------------------------------------------------------------------------+
|         † Wafw00f Scanner Has Began Scanning For Host's Wafs †              |
+-----------------------------------------------------------------------------+""" + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [scanning] > [{0}]
        """.format(host) + bcolors.ENDC)
        process = subprocess.Popen("wafw00f -v -a {0}".format(host), shell = True).wait()
        return process
    def dnsrecon(self, host):
        print(bcolors.BLUE + """
+-----------------------------------------------------------------------------+
|       † Dnsenumration Has Begun Digging for Host's Subdomains †             |
+-----------------------------------------------------------------------------+""" + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [scanning] > [{0}]
        """.format(host) + bcolors.ENDC)
        time.sleep(0.03)
        process = subprocess.Popen("dnsrecon -a -d {0}".format(host), shell = True).wait()
        return process
    def whatweb(self, host):
        print(bcolors.BLUE + """
+-----------------------------------------------------------------------------+
|       † WhatWeb Has Started Discovering Host's Running Technologies †       |
+-----------------------------------------------------------------------------+""" + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [scanning] > [{0}]
        """.format(host) + bcolors.ENDC)
        time.sleep(0.03)
        process = subprocess.Popen("whatweb -a 3 -v {0}".format(host), shell = True).wait()
        return process
    def httpx(self, host):
        print(bcolors.BLUE + """
+-----------------------------------------------------------------------------+
|        † HTTPX Has Started Discovering Host's Title & E.T.C Tech†           |
+-----------------------------------------------------------------------------+""" + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [scanning] > [{0}]
        """.format(host) + bcolors.ENDC)
        time.sleep(0.03)
        process = subprocess.Popen("echo {0}| httpx-toolkit -sc -cl -ct -title -location -status-code -tech-detect -follow-redirects -lc -wc -probe".format(host), shell = True).wait()
        return process
    def param_spider(self, host):
        print(bcolors.BLUE + """
+-----------------------------------------------------------------------------+
|     † Paramspider Scanner Has Began Discovering Host Root Urls †            |
+-----------------------------------------------------------------------------+""" + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [scanning] > [{0}]
        """.format(host) + bcolors.ENDC)
        time.sleep(0.03)
        process = subprocess.Popen("paramspider -s -d {0}".format(host), shell = True).wait()  
        return process
    def ssl_scan(self, host):
        print(bcolors.BLUE + """
+-----------------------------------------------------------------------------+
|            † SslScanner Has Began Discovering Host Root Urls †              |
+-----------------------------------------------------------------------------+""" + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [scanning] > [{0}]
        """.format(host) + bcolors.ENDC)
        time.sleep(0.03)
        process = subprocess.Popen("sslscan --show-certificate --show-sigs --tlsall --verbose {0}".format(host), shell = True).wait()  
        return process
    def dirsearch(self, host):
        print(bcolors.BLUE + """
+-----------------------------------------------------------------------------+
|         † Dirsearch Scanner Has Started Discovering Host Files †            |
+-----------------------------------------------------------------------------+""" + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [scanning] > [{0}]
        """.format(host) + bcolors.ENDC)
        time.sleep(0.03)
        process = subprocess.Popen("dirsearch -q -u {0}".format(host), shell = True).wait()
        return process
    def nuclei(self, host):
        print(bcolors.BLUE + """
+-----------------------------------------------------------------------------+
|         † Nuclei Has Started Discovering Vulnerbilities on The Host †       |
+-----------------------------------------------------------------------------+""" + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [scanning] > [{0}]
        """.format(host) + bcolors.ENDC)
        time.sleep(0.03)
        process = subprocess.Popen("subfinder -silent -d {0}| httpx-toolkit -silent| nuclei -sa -system-resolvers; nuclei -sa -silent -system-resolvers -u {0}".format(host), shell = True).wait()
        return process
    def nikto(self, host):
        print(bcolors.BLUE + """
+-----------------------------------------------------------------------------+
|          † Nikto Scanner Has Started Vulnerbility Scanning †                |
+-----------------------------------------------------------------------------+""" + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [scanning] > [{0}]
        """.format(host) + bcolors.ENDC)
        time.sleep(0.03)
        process = subprocess.Popen("nikto -ask no -Cgidirs all -Display 3 -host {0}".format(host), shell = True).wait()
        return process
    def bbot(self, host):
        print(bcolors.BLUE + """
+-----------------------------------------------------------------------------+
|                † BBOT Scanner Has Began Enumurating Target Host †           |
+-----------------------------------------------------------------------------+""" + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [scanning] > [{0}]
        """.format(host) + bcolors.ENDC)
        time.sleep(0.03)
        process = subprocess.Popen("bbot -y -f subdomain-enum email-enum cloud-enum web-basic -m nmap gowitness nuclei --allow-deadly -t {0}".format(host), shell = True).wait()  
        return process
    def uniscan(self, host):
        print(bcolors.BLUE + """
+-----------------------------------------------------------------------------+
|    † UniScan Scanner Has Began Discovering Host Vulnerbilities †            |
+-----------------------------------------------------------------------------+""" + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [scanning] > [{0}]
        """.format(host) + bcolors.ENDC)
        time.sleep(0.03)
        process = subprocess.Popen("uniscan -qwedsrj -u {0}".format(host), shell = True).wait()  
        return process
    def sqlmap(self, host):
         print(bcolors.BLUE + """
+-----------------------------------------------------------------------------+
|             † Select Targets From Results Above For Sqlmap †                |
+-----------------------------------------------------------------------------+""" + bcolors.ENDC)
         print(bcolors.GREEN + """                   [africana] [scanning] > [{0}]
         """.format(host) + bcolors.ENDC)
         time.sleep(0.03)
         process = subprocess.Popen("sqlmap --tamper=between,luanginx,xforwardedfor --random-agent --threads=10 --level=5 --risk=3 --eta  -wizard", shell = True).wait()
         return process
    def commix(self, host):
        print(bcolors.BLUE + """
+-----------------------------------------------------------------------------+
|            † Select Targets From Results Above For Commix †                 |
+-----------------------------------------------------------------------------+""" + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [scanning] > [{0}]
        """.format(host) + bcolors.ENDC)
        time.sleep(0.03)
        process = subprocess.Popen("commix --wizard", shell = True).wait()
        return process
    def dalfox(self, host):
        print(bcolors.BLUE + """
+-----------------------------------------------------------------------------+
|         † Automating XSS Vuln With Katana, Httpx & Dalfox  Tools. †         |
+-----------------------------------------------------------------------------+""" + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [scanning] > [{0}]
        """.format(host) + bcolors.ENDC)
        time.sleep(0.03)
        process = subprocess.Popen("katana -silent -u {0} -jc -kf all -c 5 -d 3 | httpx-toolkit -silent -follow-redirects -random-agent -status-code -threads 5 | dalfox pipe --only-poc r --ignore-return 302,404,403 --skip-bav".format(host), shell = True).wait()
        return process
    def xsser(self, host):
        print(bcolors.BLUE + """
+-----------------------------------------------------------------------------+
|            † Select Targets From Results Above For Xsser. †                 |
+-----------------------------------------------------------------------------+""" + bcolors.ENDC)
        print(bcolors.GREEN + """                   [africana] [scanning] > [{0}]
        """.format(host) + bcolors.ENDC)
        time.sleep(0.03)
        process = subprocess.Popen("xsser --wizard", shell = True).wait()
        return process

spiders = scanners(host = '')
if ' __name__' == '__main__':
        sys.exit(spiders())
