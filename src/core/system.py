import sys
import time
import subprocess
from src.core.banner import *
from src.core.bcolors import *

class update(object):
    def __init__(self):
        pass

    def update_system(self):
        beauty.cross_banner()
        print(bcolors.BLUE + """
+------------------------------------------------------------------------------+
|    † Select The System You Want To Install Or Update Africana Frame-Work †   |
+------------------------------------------------------------------------------+
|    Type 1. KaliLinux  2. UbuntuLinux  3. ArchLinux  4. Uninstall  0. Exit    |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
        try:
            choice = input(bcolors.DARKCYAN + bcolors.BOLD + "[africana] > " + bcolors.ENDC)
        except:
            pass
        while True:
            try:
                if choice == '0':
                    neo.one()
                    break
                elif choice == '1':
                    os.system('clear')
                    beauty.bear_a_banner()
                    africana = bcolors.GREEN + '    Choice One Selected. Installing Africana On KaliLinux. Pleas Be Patient.    ' + bcolors.ENDC
                    for a in africana:
                        sys.stdout.write(a)
                        sys.stdout.flush()
                        time.sleep(0.03)
                    print('\n')

                    afric = '/usr/local/opt/africana-framework'
                    if os.path.exists(afric):
                        os.system('clear')
                        beauty.block_banner()
                        africana = bcolors.GREEN + '    Africana Is Already Installed In Your System. Updating It For You.    ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        print('\n')
                        time.sleep(3)

                        os.system('cd /usr/local/opt/africana-framework; git pull;cd afric/hoaxshell; git pull;cd ../Villain; git pull; cd ../shells; git pull; cd ../Teardroid-phprat; git pull; cd ../AdvPhishing; git pull; cd ../ufonet; git pull; cd ../anonphisher; git pull')
                        africana = bcolors.GREEN + '    All Third Party Tools From Github Have Been Set Succesfully.   ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        time.sleep(3)

                        os.system('clear')
                        beauty.web_banner()
                        africana = bcolors.GREEN + '     Updating All Project Discovery Tools & Testing Them.    ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        print('\n')
                        time.sleep(3)

                        afric = '/root/go'
                        if os.path.exists(afric):
                            os.system('cd ~/; mv go .go; cd .go/bin; ./pdtm -ia -bp ~/.go/bin')
                        afric = '/root/.go'
                        if os.path.exists(afric):
                            os.system('cd ~/; cd .go/bin; ./pdtm -ia -bp ~/.go/bin')
                        else:
                            pass

                        os.system('clear')
                        beauty.volture_banner()
                        africana = bcolors.GREEN + '    Everything is Uptodate & Ready. Type "africana" To Launch Your Framework.   ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        break

                    else:
                        os.system('mkdir -p /usr/local/opt; cp -rf ../africana-framework /usr/local/opt/; ln -s /usr/local/opt/africana-framework/modules/kenyan.py /usr/local/bin/africana; chmod +x /usr/local/bin/africana; mkdir -p /etc/apt/trusted.gpg.d/; cd /etc/apt/trusted.gpg.d/; curl -SL https://playit-cloud.github.io/ppa/key.gpg | gpg --dearmor > playit.gpg; curl -SsL -o /etc/apt/sources.list.d/playit-cloud.list https://playit-cloud.github.io/ppa/playit-cloud.list; dpkg --add-architecture i386; apt-get update -y; apt-get install -y tor squid privoxy iptables  zsh git openssh-client openssh-server ftp ncat rlwrap powershell golang-go docker.io python3 python3-pip build-essential libssl-dev libffi-dev python3-dev python3-venv python3-pycurl python3-geoip python3-whois python3-requests python3-scapy libgeoip1 libgeoip-dev privoxy dnsmasq gophish wifipumpkin3 wifite airgeddon nuclei nikto nmap smbmap dnsrecon metasploit-framework dnsrecon feroxbuster dirsearch uniscan sqlmap commix dnsenum sslscan whatweb wafw00f wordlists wapiti xsser set playit wine32:i386')

                        africana = bcolors.GREEN + '    All Foundation Tools Have Been Copied & Installed To Your system..    ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        time.sleep(3)

                        os.system('clear')
                        beauty.bear_banner()
                        africana = bcolors.GREEN + '    Africana Is Installing Esential Golang, System Tools. Pleas Be Patient.     ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        print('\n')

                        os.system('go install -v github.com/projectdiscovery/pdtm/cmd/pdtm@latest; go install github.com/hahwul/dalfox/v2@latest; sleep 3')
                        africana = bcolors.GREEN + '    All Esential Golang Tools Have Been Installed Into To Your system..    ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        time.sleep(3)

                        infile = "/root/.zshrc"
                        outfile = "/root/.zshrc"
                        delete_list = ["# Created By africana-framework. Delete At Your Own Risk\n", "export GOROOT=~/.go\n", "export GOPATH=~/.go\n", "source ~/.afric/bin/activate", "export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games:~/.go/bin"]
                        fin = open(infile)
                        os.remove("/root/.zshrc")
                        fout = open(outfile, "w+")
                        for line in fin:
                            for word in delete_list:
                                line = line.replace(word, "")
                            fout.write(line)
                        fin.close()
                        fout.close()

                        infile = "/etc/sysctl.conf"
                        outfile = "/etc/sysctl.conf"
                        delete_list = ["#net.ipv4.ip_forward=1"]
                        fin = open(infile)
                        os.remove("/etc/sysctl.conf")
                        fout = open(outfile, "w+")
                        for line in fin:
                            for word in delete_list:
                                line = line.replace(word, "net.ipv4.ip_forward=1")
                            fout.write(line)
                        fin.close()
                        fout.close()

                        infile = "/etc/default/grub"
                        outfile = "/etc/default/grub"
                        delete_list = ['GRUB_CMDLINE_LINUX_DEFAULT="quiet"']
                        fin = open(infile)
                        os.remove("/etc/default/grub")
                        fout = open(outfile, "w+")
                        for line in fin:
                            for word in delete_list:
                                line = line.replace(word, 'GRUB_CMDLINE_LINUX_DEFAULT=""')
                            fout.write(line)
                        fin.close()
                        fout.close()

                        infile = "/etc/default/grub.d/kali-themes.cfg"
                        outfile = "/etc/default/grub.d/kali-themes.cfg"
                        delete_list = ['if ! echo "$GRUB_CMDLINE_LINUX_DEFAULT" | grep -q splash; then']
                        delete_list1 = ['    GRUB_CMDLINE_LINUX_DEFAULT="$GRUB_CMDLINE_LINUX_DEFAULT splash"']
                        delete_list2 = ['fi']
                        fin = open(infile)
                        os.remove("/etc/default/grub.d/kali-themes.cfg")
                        fout = open(outfile, "w+")
                        for line in fin:
                            for word in delete_list:
                                line = line.replace(word, '#if ! echo "$GRUB_CMDLINE_LINUX_DEFAULT" | grep -q splash; then')
                            for word in delete_list1:
                                line = line.replace(word, '#    GRUB_CMDLINE_LINUX_DEFAULT="$GRUB_CMDLINE_LINUX_DEFAULT splash"')
                            for word in delete_list2:
                                line = line.replace(word, '#fi')
                            fout.write(line)
                        fin.close()
                        fout.close()

                        os.system('clear')
                        beauty.web_banner()
                        africana = bcolors.GREEN + '    Creating Go, Python Environment @ "~/.afric" And Activating Env For You.    ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        print('\n')
                        os.system('cd ~/; pip3 install virtualenv; virtualenv .afric; echo -n "\n# Created By africana-framework. Delete At Your Own Risk\nexport GOROOT=~/.go\nexport GOPATH=~/.go\nsource ~/.afric/bin/activate\nexport PATH=$PATH:~/.go/bin\n" >> ~/.zshrc')

                        africana = bcolors.GREEN + '    Created Go & Python3 Environment at "~/.afric". Already Activated It For You.    ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        time.sleep(3)

                        rc = '/usr/share/wordlists/rockyou.txt.gz'
                        if os.path.exists(rc):
                            os.system('gunzip /usr/share/wordlists/rockyou.txt.gz')
                        else:
                            pass

                        git = '/usr/local/opt/africana-framework/afric'
                        if os.path.exists(git):
                            try:
                                os.system('cd /usr/local/opt/africana-framework/afric/; cd hoaxshell; git pull;cd ../Villain; git pull; cd ../shells; git pull; cd ../Teardroid-phprat; git pull; cd ../AdvPhishing; git pull; cd ../ufonet; git pull; cd ../anonphisher; git pull')
                                print('\n')
                                africana = bcolors.GREEN + '    Updating all Installed Project Discovery Tools With "Pdtm" Tool.    ' + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)

                                afric = '/root/go'
                                if os.path.exists(afric):
                                    os.system('cd ~/; mv go .go; cd .go/bin; ./pdtm -ia -bp ~/.go/bin')
                                afric = '/root/.go'
                                if os.path.exists(afric):
                                    os.system('cd ~/; cd .go/bin; ./pdtm -ia -bp ~/.go/bin')
                                else:
                                    pass
                                beauty.ponny_banner()
                                africana = bcolors.GREEN + '    Everything is Set & Ready. Type "africana" To Launch Your Framework.    '  + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                            except:
                                break

                        else:
                            try:
                                os.system('clear')
                                beauty.prawn_banner()
                                africana = bcolors.GREEN + '     Installing Third Party Esesntial africana-framework Requirements Tools.      ' + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)

                                print('\n')
                                os.system('zsh -c "source ~/.zshrc; cd /usr/local/opt/africana-framework; pip3 install -r requirements.txt"')
                                africana = bcolors.GREEN + '     All Third Party africana-framework Requirements Installed.   ' + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                                time.sleep(3)

                                os.system('clear')
                                beauty.scorpion_banner()
                                africana = bcolors.GREEN + '     Installing Third Party Tools From Github & Requirements..     ' + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                                print('\n')

                                os.system('mkdir -p /usr/local/opt/africana-framework/afric; cd /usr/local/opt/africana-framework/afric; git clone https://github.com/t3l3machus/Villain; cd ./Villain; pip3 install -r requirements.txt; cd ..;git clone https://github.com/t3l3machus/hoaxshell; cd ./hoaxshell; pip3 install -r requirements.txt; chmod +x hoaxshell.py; cd ..; git clone https://github.com/4ndr34z/shells; cd ./shells; ./install.sh; cd ..; git clone https://github.com/ScRiPt1337/Teardroid-phprat; cd ./Teardroid-phprat; pip3 install -r requirements.txt; wget https://github.com/ScRiPt1337/Teardroidv4_api/archive/refs/heads/main.zip; unzip main.zip; cd ..; git clone https://github.com/devanshbatham/paramspider; cd paramspider; pip3 install .; cd ..; git clone https://github.com/Ignitetch/AdvPhishing.git; cd AdvPhishing/; chmod 777 *; ./Linux-Setup.sh; cd ..;git clone https://github.com/TermuxHackz/anonphisher; cd ./anonphisher; chmod 777 *; bash anonphisher.sh; cd ..; git clone https://github.com/epsylon/ufonet')
                                africana = bcolors.GREEN + '    Succesfully Installed Third Party Tools From Github. Going To The Last Face Of Installation..    ' + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                                time.sleep(3)

                                os.system('clear')
                                beauty.cat_banner()
                                africana = bcolors.GREEN + '    Installing Project Discovery Tools & Testing Them For You.    ' + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                                print('\n')
                                time.sleep(3)

                                afric = '/root/go'
                                if os.path.exists(afric):
                                    os.system('cd ~/; mv go .go; cd .go/bin; ./pdtm -ia -bp ~/.go/bin; update-grub2')
                                afric = '/root/.go'
                                if os.path.exists(afric):
                                    os.system('cd ~/; cd .go/bin; ./pdtm -ia -bp ~/.go/bin; update-grub2')
                                else:
                                    pass
                                africana = bcolors.GREEN + '    All Project Discovery Tools Installed & Tested Successfully.    ' + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                                time.sleep(3)

                                os.system('clear')
                                beauty.volture_banner()
                                africana = bcolors.GREEN + '    Everything is Set And Ready. Type "africana" To Launch Your Af.Framework.   '  + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                                print('\n')
                                break
                            except:
                                break
#UbuntuLinux

                elif choice == '2':
                    os.system('clear')
                    beauty.bear_a_banner()
                    africana = bcolors.GREEN + '    Choice One Selected. Installing Africana On UbuntuLinux. Pleas Be Patient.    ' + bcolors.ENDC
                    for a in africana:
                        sys.stdout.write(a)
                        sys.stdout.flush()
                        time.sleep(0.03)
                    print('\n')

                    afric = '/usr/local/opt/africana-framework'
                    if os.path.exists(afric):
                        os.system('clear')
                        beauty.block_banner()
                        africana = bcolors.GREEN + '    Africana Is Already Installed In Your System. Updating It For You.    ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        print('\n')
                        time.sleep(3)

                        os.system('cd /usr/local/opt/africana-framework; git pull;cd afric/hoaxshell; git pull;cd ../Villain; git pull; cd ../shells; git pull; cd ../Teardroid-phprat; git pull; cd ../AdvPhishing; git pull; cd ../ufonet; git pull; cd ../anonphisher; git pull')
                        africana = bcolors.GREEN + '    All Third Party Tools From Github Have Been Set Succesfully.   ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        time.sleep(3)

                        os.system('clear')
                        beauty.web_banner()
                        africana = bcolors.GREEN + '     Updating All Project Discovery Tools & Testing Them.    ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        print('\n')
                        time.sleep(3)

                        afric = '/root/go'
                        if os.path.exists(afric):
                            os.system('cd ~/; mv go .go; cd .go/bin; ./pdtm -ia -bp ~/.go/bin')
                        afric = '/root/.go'
                        if os.path.exists(afric):
                            os.system('cd ~/; cd .go/bin; ./pdtm -ia -bp ~/.go/bin')
                        else:
                            pass

                        os.system('clear')
                        beauty.volture_banner()
                        africana = bcolors.GREEN + '    Everything is Uptodate & Ready. Type "africana" To Launch Your Framework.   ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        break

                    else:
                        os.system('echo -n "# Kali linux repositories | Added by Africana\ndeb http://http.kali.org/kali kali-rolling main contrib non-free" >> /etc/apt/sources.list; mkdir -p /etc/apt/trusted.gpg.d/; cd /etc/apt/trusted.gpg.d/; apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ED444FF07D8D0BF6; mkdir -p /usr/local/opt; cp -rf ../africana-framework /usr/local/opt/; ln -s /usr/local/opt/africana-framework/modules/kenyan.py /usr/local/bin/africana; chmod +x /usr/local/bin/africana; mkdir -p /etc/apt/trusted.gpg.d/; cd /etc/apt/trusted.gpg.d/; curl -SL https://playit-cloud.github.io/ppa/key.gpg | gpg --dearmor > playit.gpg; curl -SsL -o /etc/apt/sources.list.d/playit-cloud.list https://playit-cloud.github.io/ppa/playit-cloud.list; dpkg --add-architecture i386; apt-get update -y; apt-get install -y tor squid privoxy iptables  zsh git openssh-client openssh-server ftp ncat rlwrap powershell golang-go docker.io python3 python3-pip build-essential libssl-dev libffi-dev python3-dev python3-venv python3-pycurl python3-geoip python3-whois python3-requests python3-scapy libgeoip1 libgeoip-dev privoxy dnsmasq gophish wifipumpkin3 wifite airgeddon nuclei nikto nmap smbmap dnsrecon metasploit-framework dnsrecon feroxbuster dirsearch uniscan sqlmap commix dnsenum sslscan whatweb wafw00f wordlists wapiti xsser set playit wine32:i386')

                        africana = bcolors.GREEN + '    All Foundation Tools Have Been Copied & Installed To Your system..    ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        time.sleep(3)

                        os.system('clear')
                        beauty.bear_banner()
                        africana = bcolors.GREEN + '    Africana Is Installing Esential Golang, System Tools. Pleas Be Patient.     ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        print('\n')

                        os.system('go install -v github.com/projectdiscovery/pdtm/cmd/pdtm@latest; go install github.com/hahwul/dalfox/v2@latest; sleep 3')
                        africana = bcolors.GREEN + '    All Esential Golang Tools Have Been Installed Into To Your system..    ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        time.sleep(3)

                        infile = "/root/.zshrc"
                        outfile = "/root/.zshrc"
                        delete_list = ["# Created By africana-framework. Delete At Your Own Risk\n", "export GOROOT=~/.go\n", "export GOPATH=~/.go\n", "source ~/.afric/bin/activate", "export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games:~/.go/bin"]
                        fin = open(infile)
                        os.remove("/root/.zshrc")
                        fout = open(outfile, "w+")
                        for line in fin:
                            for word in delete_list:
                                line = line.replace(word, "")
                            fout.write(line)
                        fin.close()
                        fout.close()

                        infile = "/etc/sysctl.conf"
                        outfile = "/etc/sysctl.conf"
                        delete_list = ["#net.ipv4.ip_forward=1"]
                        fin = open(infile)
                        os.remove("/etc/sysctl.conf")
                        fout = open(outfile, "w+")
                        for line in fin:
                            for word in delete_list:
                                line = line.replace(word, "net.ipv4.ip_forward=1")
                            fout.write(line)
                        fin.close()
                        fout.close()

                        infile = "/etc/default/grub"
                        outfile = "/etc/default/grub"
                        delete_list = ['GRUB_CMDLINE_LINUX_DEFAULT="quiet"']
                        fin = open(infile)
                        os.remove("/etc/default/grub")
                        fout = open(outfile, "w+")
                        for line in fin:
                            for word in delete_list:
                                line = line.replace(word, 'GRUB_CMDLINE_LINUX_DEFAULT=""')
                            fout.write(line)
                        fin.close()
                        fout.close()

                        os.system('clear')
                        beauty.web_banner()
                        africana = bcolors.GREEN + '    Creating Go, Python Environment @ "~/.afric" And Activating Env For You.    ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        print('\n')
                        os.system('cd ~/; pip3 install virtualenv; virtualenv .afric; echo -n "\n# Created By africana-framework. Delete At Your Own Risk\nexport GOROOT=~/.go\nexport GOPATH=~/.go\nsource ~/.afric/bin/activate\nexport PATH=$PATH:~/.go/bin\n" >> ~/.zshrc')

                        africana = bcolors.GREEN + '    Created Go & Python3 Environment at "~/.afric". Already Activated It For You.    ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        time.sleep(3)

                        rc = '/usr/share/wordlists/rockyou.txt.gz'
                        if os.path.exists(rc):
                            os.system('gunzip /usr/share/wordlists/rockyou.txt.gz')
                        else:
                            pass

                        git = '/usr/local/opt/africana-framework/afric'
                        if os.path.exists(git):
                            try:
                                os.system('cd /usr/local/opt/africana-framework/afric/; cd hoaxshell; git pull;cd ../Villain; git pull; cd ../shells; git pull; cd ../Teardroid-phprat; git pull; cd ../AdvPhishing; git pull; cd ../ufonet; git pull; cd ../anonphisher; git pull')
                                print('\n')
                                africana = bcolors.GREEN + '    Updating all Installed Project Discovery Tools With "Pdtm" Tool.    ' + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)

                                afric = '/root/go'
                                if os.path.exists(afric):
                                    os.system('cd ~/; mv go .go; cd .go/bin; ./pdtm -ia -bp ~/.go/bin')
                                afric = '/root/.go'
                                if os.path.exists(afric):
                                    os.system('cd ~/; cd .go/bin; ./pdtm -ia -bp ~/.go/bin')
                                else:
                                    pass
                                beauty.ponny_banner()
                                africana = bcolors.GREEN + '    Everything is Set & Ready. Type "africana" To Launch Your Framework.    '  + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                            except:
                                break

                        else:
                            try:
                                os.system('clear')
                                beauty.prawn_banner()
                                africana = bcolors.GREEN + '     Installing Third Party Esesntial africana-framework Requirements Tools.      ' + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)

                                print('\n')
                                os.system('zsh -c "source ~/.zshrc; cd /usr/local/opt/africana-framework; pip3 install -r requirements.txt"')
                                africana = bcolors.GREEN + '     All Third Party africana-framework Requirements Installed.   ' + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                                time.sleep(3)

                                os.system('clear')
                                beauty.scorpion_banner()
                                africana = bcolors.GREEN + '     Installing Third Party Tools From Github & Requirements..     ' + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                                print('\n')

                                os.system('mkdir -p /usr/local/opt/africana-framework/afric; cd /usr/local/opt/africana-framework/afric; git clone https://github.com/t3l3machus/Villain; cd ./Villain; pip3 install -r requirements.txt; cd ..;git clone https://github.com/t3l3machus/hoaxshell; cd ./hoaxshell; pip3 install -r requirements.txt; chmod +x hoaxshell.py; cd ..; git clone https://github.com/4ndr34z/shells; cd ./shells; ./install.sh; cd ..; git clone https://github.com/ScRiPt1337/Teardroid-phprat; cd ./Teardroid-phprat; pip3 install -r requirements.txt; wget https://github.com/ScRiPt1337/Teardroidv4_api/archive/refs/heads/main.zip; unzip main.zip; cd ..; git clone https://github.com/devanshbatham/paramspider; cd paramspider; pip3 install .; cd ..; git clone https://github.com/Ignitetch/AdvPhishing.git; cd AdvPhishing/; chmod 777 *; ./Linux-Setup.sh; cd ..;git clone https://github.com/TermuxHackz/anonphisher; cd ./anonphisher; chmod 777 *; bash anonphisher.sh; cd ..; git clone https://github.com/epsylon/ufonet')
                                africana = bcolors.GREEN + '    Succesfully Installed Third Party Tools From Github. Going To The Last Face Of Installation..    ' + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                                time.sleep(3)

                                os.system('clear')
                                beauty.cat_banner()
                                africana = bcolors.GREEN + '    Installing Project Discovery Tools & Testing Them For You.    ' + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                                print('\n')
                                time.sleep(3)

                                afric = '/root/go'
                                if os.path.exists(afric):
                                    os.system('cd ~/; mv go .go; cd .go/bin; ./pdtm -ia -bp ~/.go/bin; update-grub2')
                                afric = '/root/.go'
                                if os.path.exists(afric):
                                    os.system('cd ~/; cd .go/bin; ./pdtm -ia -bp ~/.go/bin; update-grub2')
                                else:
                                    pass
                                africana = bcolors.GREEN + '    All Project Discovery Tools Installed & Tested Successfully.    ' + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                                time.sleep(3)

                                os.system('clear')
                                beauty.ghecko_banner()
                                africana = bcolors.GREEN + '    Delleting All KaliLinux Repos Added In 2 Your SourceList And Updating Apt      ' + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                                infile = "/etc/apt/sources.list"
                                outfile = "/etc/apt/sources.list"
                                delete_list = ["# Kali linux repositories | Added by Africana\n", "deb http://http.kali.org/kali kali-rolling main contrib non-free"]
                                fin = open(infile)
                                os.remove("/etc/apt/sources.list")
                                fout = open(outfile, "w+")
                                for line in fin:
                                    for word in delete_list:
                                        line = line.replace(word, "")
                                    fout.write(line)
                                fin.close()
                                fout.close()
                                os.system('apt-get update -y')

                                os.system('clear')
                                beauty.volture_banner()
                                africana = bcolors.GREEN + '    Everything is Set And Ready. Type "africana" To Launch Your Af.Framework.   '  + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                                print('\n')
                                break
                            except:
                                break

#ArchLinux Installer
                elif choice == '3':
                    os.system('clear')
                    beauty.bear_a_banner()
                    africana = bcolors.GREEN + '    Choice One Selected. Installing Africana On ArchLinux. Pleas Be Patient.    ' + bcolors.ENDC
                    for a in africana:
                        sys.stdout.write(a)
                        sys.stdout.flush()
                        time.sleep(0.03)
                    print('\n')

                    afric = '/usr/local/opt/africana-framework'
                    if os.path.exists(afric):
                        os.system('clear')
                        beauty.block_banner()
                        africana = bcolors.GREEN + '    Africana Is Already Installed In Your System. Updating It For You.    ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        print('\n')
                        time.sleep(3)

                        os.system('cd /usr/local/opt/africana-framework; git pull;cd afric/hoaxshell; git pull;cd ../Villain; git pull; cd ../shells; git pull; cd ../Teardroid-phprat; git pull; cd ../AdvPhishing; git pull; cd ../ufonet; git pull; cd ../anonphisher; git pull')
                        africana = bcolors.GREEN + '    All Third Party Tools From Github Have Been Set Succesfully.   ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        time.sleep(3)

                        os.system('clear')
                        beauty.web_banner()
                        africana = bcolors.GREEN + '     Updating All Project Discovery Tools & Testing Them.    ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        print('\n')
                        time.sleep(3)

                        afric = '/root/go'
                        if os.path.exists(afric):
                            os.system('cd ~/; mv go .go; cd .go/bin; ./pdtm -ia -bp ~/.go/bin')
                        afric = '/root/.go'
                        if os.path.exists(afric):
                            os.system('cd ~/; cd .go/bin; ./pdtm -ia -bp ~/.go/bin')
                        else:
                            pass

                        os.system('clear')
                        beauty.volture_banner()
                        africana = bcolors.GREEN + '    Everything is Uptodate & Ready. Type "africana" To Launch Your Framework.   ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        break

                    else:
                        os.system('mkdir -p /usr/local/opt; cp -rf ../africana-framework /usr/local/opt/; ln -s /usr/local/opt/africana-framework/modules/kenyan.py /usr/local/bin/africana; chmod +x /usr/local/bin/africana; dpkg --add-architecture i386; pacman -Syu ; pacman -Sy tor squid privoxy iptables  zsh git openssh-client openssh-server ftp ncat rlwrap powershell golang-go docker.io python3 python3-pip build-essential libssl-dev libffi-dev python3-dev python3-venv python3-pycurl python3-geoip python3-whois python3-requests python3-scapy libgeoip1 libgeoip-dev privoxy dnsmasq gophish wifipumpkin3 wifite airgeddon nuclei nikto nmap smbmap dnsrecon metasploit-framework dnsrecon feroxbuster dirsearch uniscan sqlmap commix dnsenum sslscan whatweb wafw00f wordlists wapiti xsser set playit wine32:i386')

                        africana = bcolors.GREEN + '    All Foundation Tools Have Been Copied & Installed To Your system..    ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        time.sleep(3)

                        os.system('clear')
                        beauty.bear_banner()
                        africana = bcolors.GREEN + '    Africana Is Installing Esential Golang, System Tools. Pleas Be Patient.     ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        print('\n')

                        os.system('go install -v github.com/projectdiscovery/pdtm/cmd/pdtm@latest; go install github.com/hahwul/dalfox/v2@latest; sleep 3')
                        africana = bcolors.GREEN + '    All Esential Golang Tools Have Been Installed Into To Your system..    ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        time.sleep(3)

                        infile = "/root/.zshrc"
                        outfile = "/root/.zshrc"
                        delete_list = ["# Created By africana-framework. Delete At Your Own Risk\n", "export GOROOT=~/.go\n", "export GOPATH=~/.go\n", "source ~/.afric/bin/activate", "export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games:~/.go/bin"]
                        fin = open(infile)
                        os.remove("/root/.zshrc")
                        fout = open(outfile, "w+")
                        for line in fin:
                            for word in delete_list:
                                line = line.replace(word, "")
                            fout.write(line)
                        fin.close()
                        fout.close()

                        infile = "/etc/sysctl.conf"
                        outfile = "/etc/sysctl.conf"
                        delete_list = ["#net.ipv4.ip_forward=1"]
                        fin = open(infile)
                        os.remove("/etc/sysctl.conf")
                        fout = open(outfile, "w+")
                        for line in fin:
                            for word in delete_list:
                                line = line.replace(word, "net.ipv4.ip_forward=1")
                            fout.write(line)
                        fin.close()
                        fout.close()

                        infile = "/etc/default/grub"
                        outfile = "/etc/default/grub"
                        delete_list = ['GRUB_CMDLINE_LINUX_DEFAULT="quiet"']
                        fin = open(infile)
                        os.remove("/etc/default/grub")
                        fout = open(outfile, "w+")
                        for line in fin:
                            for word in delete_list:
                                line = line.replace(word, 'GRUB_CMDLINE_LINUX_DEFAULT=""')
                            fout.write(line)
                        fin.close()
                        fout.close()

                        os.system('clear')
                        beauty.web_banner()
                        africana = bcolors.GREEN + '    Creating Go, Python Environment @ "~/.afric" And Activating Env For You.    ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        print('\n')
                        os.system('cd ~/; pip3 install virtualenv; virtualenv .afric; echo -n "\n# Created By africana-framework. Delete At Your Own Risk\nexport GOROOT=~/.go\nexport GOPATH=~/.go\nsource ~/.afric/bin/activate\nexport PATH=$PATH:~/.go/bin\n" >> ~/.zshrc')

                        africana = bcolors.GREEN + '    Created Go & Python3 Environment at "~/.afric". Already Activated It For You.    ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        time.sleep(3)

                        rc = '/usr/share/wordlists/rockyou.txt.gz'
                        if os.path.exists(rc):
                            os.system('gunzip /usr/share/wordlists/rockyou.txt.gz')
                        else:
                            pass

                        git = '/usr/local/opt/africana-framework/afric'
                        if os.path.exists(git):
                            try:
                                os.system('cd /usr/local/opt/africana-framework/afric/; cd hoaxshell; git pull;cd ../Villain; git pull; cd ../shells; git pull; cd ../Teardroid-phprat; git pull; cd ../AdvPhishing; git pull; cd ../ufonet; git pull; cd ../anonphisher; git pull')
                                print('\n')
                                africana = bcolors.GREEN + '    Updating all Installed Project Discovery Tools With "Pdtm" Tool.    ' + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)

                                afric = '/root/go'
                                if os.path.exists(afric):
                                    os.system('cd ~/; mv go .go; cd .go/bin; ./pdtm -ia -bp ~/.go/bin')
                                afric = '/root/.go'
                                if os.path.exists(afric):
                                    os.system('cd ~/; cd .go/bin; ./pdtm -ia -bp ~/.go/bin')
                                else:
                                    pass
                                beauty.ponny_banner()
                                africana = bcolors.GREEN + '    Everything is Set & Ready. Type "africana" To Launch Your Framework.    '  + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                            except:
                                break

                        else:
                            try:
                                os.system('clear')
                                beauty.prawn_banner()
                                africana = bcolors.GREEN + '     Installing Third Party Esesntial africana-framework Requirements Tools.      ' + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)

                                print('\n')
                                os.system('zsh -c "source ~/.zshrc; cd /usr/local/opt/africana-framework; pip3 install -r requirements.txt"')
                                africana = bcolors.GREEN + '     All Third Party africana-framework Requirements Installed.   ' + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                                time.sleep(3)

                                os.system('clear')
                                beauty.scorpion_banner()
                                africana = bcolors.GREEN + '     Installing Third Party Tools From Github & Requirements..     ' + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                                print('\n')

                                os.system('mkdir -p /usr/local/opt/africana-framework/afric; cd /usr/local/opt/africana-framework/afric; git clone https://github.com/t3l3machus/Villain; cd ./Villain; pip3 install -r requirements.txt; cd ..;git clone https://github.com/t3l3machus/hoaxshell; cd ./hoaxshell; pip3 install -r requirements.txt; chmod +x hoaxshell.py; cd ..; git clone https://github.com/4ndr34z/shells; cd ./shells; ./install.sh; cd ..; git clone https://github.com/ScRiPt1337/Teardroid-phprat; cd ./Teardroid-phprat; pip3 install -r requirements.txt; wget https://github.com/ScRiPt1337/Teardroidv4_api/archive/refs/heads/main.zip; unzip main.zip; cd ..; git clone https://github.com/devanshbatham/paramspider; cd paramspider; pip3 install .; cd ..; git clone https://github.com/Ignitetch/AdvPhishing.git; cd AdvPhishing/; chmod 777 *; ./Linux-Setup.sh; cd ..;git clone https://github.com/TermuxHackz/anonphisher; cd ./anonphisher; chmod 777 *; bash anonphisher.sh; cd ..; git clone https://github.com/epsylon/ufonet')
                                africana = bcolors.GREEN + '    Succesfully Installed Third Party Tools From Github. Going To The Last Face Of Installation..    ' + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                                time.sleep(3)

                                os.system('clear')
                                beauty.cat_banner()
                                africana = bcolors.GREEN + '    Installing Project Discovery Tools & Testing Them For You.    ' + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                                print('\n')
                                time.sleep(3)

                                afric = '/root/go'
                                if os.path.exists(afric):
                                    os.system('cd ~/; mv go .go; cd .go/bin; ./pdtm -ia -bp ~/.go/bin; update-grub2')
                                afric = '/root/.go'
                                if os.path.exists(afric):
                                    os.system('cd ~/; cd .go/bin; ./pdtm -ia -bp ~/.go/bin; update-grub2')
                                else:
                                    pass
                                africana = bcolors.GREEN + '    All Project Discovery Tools Installed & Tested Successfully.    ' + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                                time.sleep(3)

                                os.system('clear')
                                beauty.volture_banner()
                                africana = bcolors.GREEN + '    Everything is Set And Ready. Type "africana" To Launch Your Af.Framework.   '  + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.03)
                                print('\n')
                                break
                            except:
                                break

## Uninstaller
                elif choice == '4':
                    try:
                        os.system('clear')
                        beauty.block_banner()
                        africana = bcolors.GREEN + '    The Uninstaller Is About To Delete africana-framework And All Its Files.    ' + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        print(bcolors.RED + """
|           Incase Of Any Bug Email Me at: rojahsmontari@gmail.com             |
+------------------------------------------------------------------------------+
| Are You Sure You Want To Uninstall ? : [ 1 ] For Yes  [ 0 ] For No & Go Back |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                        choice = input(bcolors.DARKCYAN + bcolors.BOLD + "[africana] > " + bcolors.ENDC)
                        if choice == '1':
                            afric = '/root/go'
                            if os.path.exists(afric):
                                os.system('rm -rf /usr/local/opt/africana-framework; rm -rf /usr/local/bin/africana; rm -rf /usr/local/bin/vanish; rm -rf ~/.go')
                            afric = '/root/.go'
                            if os.path.exists(afric):
                                    os.system('rm -rf /usr/local/opt/africana-framework; rm -rf /usr/local/bin/africana; rm -rf /usr/local/bin/vanish; rm -rf ~/.go')
                            else:
                                os.system('rm -rf /usr/local/opt/africana-framework; rm -rf /usr/local/bin/africana; rm -rf /usr/local/bin/vanish; rm -rf ~/.go')
                                pass
                            os.system('clear')

                            infile = "/root/.zshrc"
                            outfile = "/root/.zshrc"
                            delete_list = ["# Created By africana-framework. Delete At Your Own Risk\n", "export GOROOT=~/.go\n", "export GOPATH=~/.go\n", "source ~/.afric/bin/activate", "export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games:~/.go/bin"]
                            fin = open(infile)
                            os.remove("/root/.zshrc")
                            fout = open(outfile, "w+")
                            for line in fin:
                                for word in delete_list:
                                    line = line.replace(word, "")
                                fout.write(line)
                            fin.close()
                            fout.close()

                            beauty.volture_banner()
                            africana = bcolors.GREEN + '    [+] The Uninstaller Has Deleted africana-framework And All Its Files. [+]\n\n' + bcolors.ENDC
                            for a in africana:
                                sys.stdout.write(a)
                                sys.stdout.flush()
                                time.sleep(0.03)
                            break
                        else:
                            os.system('clear')
                            installer.update_system()
                            break
                    except:
                        neo.one()
                        break
                else:
                    try:
                        os.system('clear')
                        print(bcolors.RED + """
                                                                                
+------------------------------------------------------------------------------+
|            † Poor Choice  Of Selection!!. Pleas Select [0-3] †               |
+------------------------------------------------------------------------------+
""" + bcolors.ENDC)
                        time.sleep(3)
                        os.system('clear')
                        update_system()
                        break
                    except:
                        os.system('clear')
                        installer.update_system()
                        break
            except:
                neo.one()
                break

installer = update()
if ' __name__' == '__main__':
        sys.exit(installer())
