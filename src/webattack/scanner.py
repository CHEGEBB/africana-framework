import sys
import time
import subprocess
from src.core.bcolors import *

class scanners(object):
    def __init__(self, host):
        self.host = host

    def wafw00f(self, host):
        print("\n")
        print(bcolors.BLUE + "   -{ " + bcolors.RED + "trying waf tech detection" + bcolors.BLUE + " }" + bcolors.BLUE + " => " + bcolors.BLUE + "{ " + bcolors.YELLOW + "{0}".format(host) + bcolors.BLUE + " }-\n" + bcolors.ENDC)
        process = subprocess.Popen("wafw00f -v -a {0}".format(host), shell = True).wait()
        return process

    def dnsrecon(self, host):
        print("\n")
        print(bcolors.BLUE + "   -{ " + bcolors.RED + "running dns reconing on" + bcolors.BLUE + " }" + bcolors.BLUE + " => " + bcolors.BLUE + "{ " + bcolors.YELLOW + "{0}".format(host) + bcolors.BLUE + " }-\n" + bcolors.ENDC)
        process = subprocess.Popen("dnsrecon -a -d {0}".format(host), shell = True).wait()
        return process

    def whatweb(self, host):
        print("\n")
        print(bcolors.BLUE + "   -{ " + bcolors.RED + "reconning target for host tech" + bcolors.BLUE + " }" + bcolors.BLUE + " => " + bcolors.BLUE + "{ " + bcolors.YELLOW + "{0}".format(host) + bcolors.BLUE + " }-\n" + bcolors.ENDC)
        process = subprocess.Popen("whatweb -a 3 -v {0}".format(host), shell = True).wait()
        return process

    def httpx(self, host):
        print("\n")
        print(bcolors.BLUE + "   -{ " + bcolors.RED + "grubbibg web http & https headers" + bcolors.BLUE + " }" + bcolors.BLUE + " => " + bcolors.BLUE + "{ " + bcolors.YELLOW + "{0}".format(host) + bcolors.BLUE + " }-\n" + bcolors.ENDC)
        process = subprocess.Popen("echo {0}| httpx-toolkit -sc -cl -ct -title -location -status-code -tech-detect -follow-redirects -lc -wc -probe".format(host), shell = True).wait()
        return process

    def param_spider(self, host):
        print("\n")
        print(bcolors.BLUE + "   -{ " + bcolors.RED + "mining host's root urls" + bcolors.BLUE + " }" + bcolors.BLUE + " => " + bcolors.BLUE + "{ " + bcolors.YELLOW + "{0}".format(host) + bcolors.BLUE + " }-\n" + bcolors.ENDC)
        process = subprocess.Popen("paramspider -s -d {0}".format(host), shell = True).wait()  
        return process

    def ssl_scan(self, host):
        print("\n")
        print(bcolors.BLUE + "   -{ " + bcolors.RED + "scanning for vuln ssl certs" + bcolors.BLUE + " }" + bcolors.BLUE + " => " + bcolors.BLUE + "{ " + bcolors.YELLOW + "{0}".format(host) + bcolors.BLUE + " }-\n" + bcolors.ENDC)
        process = subprocess.Popen("sslscan --show-certificate --show-sigs --tlsall --verbose {0}".format(host), shell = True).wait()  
        return process

    def dirsearch(self, host):
        print("\n")
        print(bcolors.BLUE + "   -{ " + bcolors.RED + "mining host's root files" + bcolors.BLUE + " }" + bcolors.BLUE + " => " + bcolors.BLUE + "{ " + bcolors.YELLOW + "{0}".format(host) + bcolors.BLUE + " }-\n" + bcolors.ENDC)
        process = subprocess.Popen("dirsearch -q -u {0}".format(host), shell = True).wait()
        return process

    def nuclei(self, host):
        print("\n")
        print(bcolors.BLUE + "   -{ " + bcolors.RED + "scanning the host for known vulns" + bcolors.BLUE + " }" + bcolors.BLUE + " => " + bcolors.BLUE + "{ " + bcolors.YELLOW + "{0}".format(host) + bcolors.BLUE + " }-\n" + bcolors.ENDC)
        process = subprocess.Popen("subfinder -silent -d {0}| httpx-toolkit -silent| nuclei -sa -system-resolvers; nuclei -sa -silent -system-resolvers -u {0}".format(host), shell = True).wait()
        return process

    def nikto(self, host):
        print("\n")
        print(bcolors.BLUE + "   -{ " + bcolors.RED + "further scanning host for know vulns" + bcolors.BLUE + " }" + bcolors.BLUE + " => " + bcolors.BLUE + "{ " + bcolors.YELLOW + "{0}".format(host) + bcolors.BLUE + " }-\n" + bcolors.ENDC)
        process = subprocess.Popen("nikto -ask no -Cgidirs all -Display 3 -host {0}".format(host), shell = True).wait()
        return process

    def bbot(self, host):
        print("\n")
        print(bcolors.BLUE + "   -{ " + bcolors.RED + "full reconning the host from dns to vulns " + bcolors.BLUE + " }" + bcolors.BLUE + " => " + bcolors.BLUE + "{ " + bcolors.YELLOW + "{0}".format(host) + bcolors.BLUE + " }-\n" + bcolors.ENDC)
        process = subprocess.Popen("bbot -y -f subdomain-enum email-enum cloud-enum web-basic -m nmap gowitness nuclei --allow-deadly -t {0}".format(host), shell = True).wait()  
        return process

    def uniscan(self, host):
        print("\n")
        print(bcolors.BLUE + "   -{ " + bcolors.RED + "heavy vuln reconning the host" + bcolors.BLUE + " }" + bcolors.BLUE + " => " + bcolors.BLUE + "{ " + bcolors.YELLOW + "{0}".format(host) + bcolors.BLUE + " }-\n" + bcolors.ENDC)
        process = subprocess.Popen("uniscan -qwedsrj -u {0}".format(host), shell = True).wait()  
        return process

    def sqlmap(self, host):
         print("\n")
         print(bcolors.BLUE + "   -{ " + bcolors.RED + "sql injection attacks. use above scans" + bcolors.BLUE + " }" + bcolors.BLUE + " => " + bcolors.BLUE + "{ " + bcolors.YELLOW + "{0}".format(host) + bcolors.BLUE + " }-\n" + bcolors.ENDC)
         process = subprocess.Popen("sqlmap --tamper=between,luanginx,xforwardedfor --random-agent --threads=10 --level=5 --risk=3 --eta  -wizard", shell = True).wait()
         return process

    def commix(self, host):
        print("\n")
        print(bcolors.BLUE + "   -{ " + bcolors.RED + "command injection attacks. use above scans" + bcolors.BLUE + " }" + bcolors.BLUE + " => " + bcolors.BLUE + "{ " + bcolors.YELLOW + "{0}".format(host) + bcolors.BLUE + " }-\n" + bcolors.ENDC)
        process = subprocess.Popen("commix --wizard", shell = True).wait()
        return process

    def dalfox(self, host):
        print("\n")
        print(bcolors.BLUE + "   -{ " + bcolors.RED + "heavy xss injection attacks launched " + bcolors.BLUE + " }" + bcolors.BLUE + " => " + bcolors.BLUE + "{ " + bcolors.YELLOW + "{0}".format(host) + bcolors.BLUE + " }-\n" + bcolors.ENDC)
        process = subprocess.Popen("katana -silent -u {0} -jc -kf all -c 5 -d 3 | httpx-toolkit -silent -follow-redirects -random-agent -status-code -threads 5 | dalfox pipe --only-poc r --ignore-return 302,404,403 --skip-bav".format(host), shell = True).wait()
        return process

    def xsser(self, host):
        print("\n")
        print(bcolors.BLUE + "   -{ " + bcolors.RED + "xss injection attacks. use above scans" + bcolors.BLUE + " }" + bcolors.BLUE + " => " + bcolors.BLUE + "{ " + bcolors.YELLOW + "{0}".format(host) + bcolors.BLUE + " }-\n" + bcolors.ENDC)
        process = subprocess.Popen("xsser --wizard", shell = True).wait()
        return process

spiders = scanners(host = '')
if ' __name__' == '__main__':
        sys.exit(spiders())
