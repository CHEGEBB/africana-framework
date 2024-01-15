import sys
import time
import subprocess
from src.core.banner import *
from src.core.bcolors import *
from scriptures.verses import *

class update(object):
    def __init__(self):
        pass

    def update_system(self):
        os.system('clear')
        beauty.graphics(), scriptures.verses()
        print(bcolors.BLUE + "\n           -[" + bcolors.ENDC + bcolors.UNDERL + " Select a number from the table below" + bcolors.ENDC + bcolors.BLUE + " ]-\n" + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 1.                    Kali-Linux                        ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 2.                   Ubuntu-Linux                       ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 3.                    Arch-Linux                        ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 4.                Uninstall-Africana                    ] " + bcolors.ENDC)
        print(bcolors.BLUE + "   [ 0.                       Exit                           ] \n" + bcolors.ENDC)
        try:
            choice = input(bcolors.GREEN + "(" + bcolors.ENDC + "africana:" + bcolors.DARKCYAN + "framework" + bcolors.GREEN + ")# " + bcolors.ENDC)
        except:
            pass
        while True:
            try:
                if choice == '0':
                    neo.one()
                    break
                elif choice == '1':
                    os.system('clear')
                    print("\n")
                    print(bcolors.ENDC + "  -{ " + bcolors.GREEN + bcolors.UNDERL + "For God so loved the world, that he gave His." + bcolors.ENDC + color() + " [John 3:16] " + bcolors.ENDC + "}-\n" + bcolors.ENDC)
                    print(bcolors.BLUE + "   [            Installing Africana On Kali-Linux            ] " + bcolors.ENDC)
                    print(bcolors.BLUE + "   [                    Pleas Be Patient                     ] " + bcolors.ENDC)
                    print(bcolors.BLUE + "   [      Installer will copy core files to your system      ] " + bcolors.ENDC)
                    print(bcolors.BLUE + "   [                            &                            ] " + bcolors.ENDC)
                    print(bcolors.BLUE + "   [              All Necessary Foundation Tools             ] \n" + bcolors.ENDC)
                    print(bcolors.ENDC + "       -{" + bcolors.RED + bcolors.UNDERL + " apt-get install -y git zsh python3 python3-pip. " + bcolors.ENDC + "}-\n" + bcolors.ENDC)

                    afric = '/usr/local/opt/africana-framework'
                    if os.path.exists(afric):
                        os.system('clear')
                        print("\n")
                        print(bcolors.ENDC + "  -{ " + bcolors.GREEN + bcolors.UNDERL + "For God so loved the world, that he gave His." + bcolors.ENDC + color() + " [John 3:16] " + bcolors.ENDC + "}-\n" + bcolors.ENDC)
                        print(bcolors.BLUE + "   [              Africana detected in your system           ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [                   Pleas Be Patient as the               ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [                 Installer runs full updates             ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [                            &                            ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [       Upgrades for All Necessary Foundation Tools       ] \n" + bcolors.ENDC)
                        print(bcolors.ENDC + "               {" + bcolors.RED + bcolors.UNDERL + " git pull & apt-get upgrade -y.. " + bcolors.ENDC + "}\n" + bcolors.ENDC)
                        africana = bcolors.ENDC + " -{" + bcolors.YELLOW + " Africana is already installed in your system. Updating It. " + bcolors.ENDC + "}-\n" + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.09)
                        print("\n")
                        os.system('apt-get update -y')
                        print("\n")
                        os.system('cd /usr/local/opt/africana-framework; git pull; cd Teardroid-phprat; git pull; cd ../AdvPhishing; git pull; cd ../ufonet; git pull; cd ../anonphisher; git pull')
                        time.sleep(0.09)

                        os.system('clear')
                        print("\n")
                        print(bcolors.ENDC + "  -{ " + bcolors.GREEN + bcolors.UNDERL + "For God so loved the world, that he gave His." + bcolors.ENDC + color() + " [John 3:16] " + bcolors.ENDC + "}-\n" + bcolors.ENDC)
                        print(bcolors.BLUE + "   [              Setting up project discovery tools         ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [                   Pleas Be Patient as the               ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [                      Installer runs                     ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [                            &                            ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [              Sets up all golang necessary tools         ] \n" + bcolors.ENDC)
                        print(bcolors.ENDC + "          {" + bcolors.RED + bcolors.UNDERL + " cd ~/go/bin; ./pdtm -ia; source ~/.zshrc. " + bcolors.ENDC + "}\n" + bcolors.ENDC)
                        africana = bcolors.ENDC + " -{" + bcolors.YELLOW + " Updating all Project Discovery tools & testing them for you " + bcolors.ENDC + "}-\n" + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.09)
                        afric = '/root/go'
                        if os.path.exists(afric):
                            os.system('cd ~/go/bin; ./pdtm -ia; source ~/.zshrc')
                        else:
                            pass

                        os.system('clear')
                        print("\n")
                        beauty.graphics(), scriptures.verses()
                        print("\n")
                        print(bcolors.BLUE + "   [              All foundation tools installed             ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [                 Anonymous tools installed               ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [               Wifi pentesting tools installed           ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [                 Web pentest tools installed             ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [              Local pentesting tools installed           ] \n" + bcolors.ENDC)
                        africana = bcolors.ENDC + " -{" + bcolors.YELLOW + " Everything is set. Type 'africana' to launch the framework " + bcolors.ENDC + "}-\n" + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.09)
                        break

                    else:
                        os.system('mkdir -p /usr/local/opt; cp -rf ../africana-framework /usr/local/opt/; ln -s /usr/local/opt/africana-framework/modules/kenyan.py /usr/local/bin/africana; chmod +x /usr/local/bin/africana; apt-get update -y; apt-get install zsh git curl -y; mkdir -p /etc/apt/trusted.gpg.d/; cd /etc/apt/trusted.gpg.d/; curl -SL https://playit-cloud.github.io/ppa/key.gpg | gpg --dearmor > playit.gpg; curl -SL -o /etc/apt/sources.list.d/playit-cloud.list https://playit-cloud.github.io/ppa/playit-cloud.list; dpkg --add-architecture i386; apt-get update -y; apt-get install -y tor squid privoxy iptables openssh-client openssh-server ftp ncat rlwrap powershell golang-go docker.io python3 python3-pip build-essential libssl-dev libffi-dev python3-dev python3-venv python3-pycurl python3-geoip python3-whois python3-requests python3-scapy libgeoip1 libgeoip-dev privoxy dnsmasq gophish wifipumpkin3 wifite airgeddon nuclei nikto nmap smbmap dnsrecon metasploit-framework dnsrecon feroxbuster dirsearch uniscan sqlmap commix dnsenum sslscan whatweb wafw00f wordlists wapiti xsser villain set playit wine32:i386')
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
                        print("\n")
                        print(bcolors.ENDC + "  -{ " + bcolors.GREEN + bcolors.UNDERL + "For God so loved the world, that he gave His." + bcolors.ENDC + color() + " [John 3:16] " + bcolors.ENDC + "}-\n" + bcolors.ENDC)
                        print(bcolors.BLUE + "   [           Setting up Go, Python env @ '~/.afric'        ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [                   Pleas Be Patient as the               ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [                        Setup runs                       ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [                            &                            ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [              Source @ ~/.afric/bin/activate             ] \n" + bcolors.ENDC)
                        print(bcolors.ENDC + "          {" + bcolors.RED + bcolors.UNDERL + " cd ~/; pip3 install virtualenv; virtualenv " + bcolors.ENDC + "}\n" + bcolors.ENDC)
                        africana = bcolors.ENDC + " -{" + bcolors.YELLOW + " Creating Go, Python env @ '~/.afric' & activating it for you " + bcolors.ENDC + "}-\n" + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.09)
                        print("\n")
                        os.system('cd ~/; pip3 install virtualenv; virtualenv .afric; echo -n "\n# Created By africana-framework. Delete At Your Own Risk\nsource ~/.afric/bin/activate" >> ~/.zshrc')
                        infile = "/root/.zshrc"
                        outfile = "/root/.zshrc"
                        delete_list = ["# Created By africana-framework. Delete At Your Own Risk\n", "source ~/.afric/bin/activate"]
                        fin = open(infile)
                        os.remove("/root/.zshrc")
                        fout = open(outfile, "w+")
                        for line in fin:
                            for word in delete_list:
                                line = line.replace(word, "")
                            fout.write(line)
                        fin.close()
                        fout.close()

                        git = '/usr/local/opt/africana-framework/externals'
                        if os.path.exists(git):
                            try:
                                os.system('clear')
                                print("\n")
                                print(bcolors.ENDC + "  -{ " + bcolors.GREEN + bcolors.UNDERL + "For God so loved the world, that he gave His." + bcolors.ENDC + color() + " [John 3:16] " + bcolors.ENDC + "}-\n" + bcolors.ENDC)
                                print(bcolors.BLUE + "   [              All foundation tools installed             ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [                 Anonymous tools installed               ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [               Wifi pentesting tools installed           ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [                 Web pentest tools installed             ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [              Local pentesting tools installed           ] \n" + bcolors.ENDC)
                                print(bcolors.ENDC + "     {" + bcolors.RED + bcolors.UNDERL + " git clone. & cd ~/; pip3 install -r requirements.txt " + bcolors.ENDC + "}\n" + bcolors.ENDC)
                                africana = bcolors.ENDC + "   -{" + bcolors.YELLOW + " Installing africana-framework' s Python3 requirements. " + bcolors.ENDC + "}-\n" + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.09)
                                print("\n")
                                os.system('zsh -c "source ~/.zshrc; cd /usr/local/opt/africana-framework; pip3 install -r requirements.txt"')

                                os.system('clear')
                                print("\n")
                                print(bcolors.ENDC + "  -{ " + bcolors.GREEN + bcolors.UNDERL + "For God so loved the world, that he gave His." + bcolors.ENDC + color() + " [John 3:16] " + bcolors.ENDC + "}-\n" + bcolors.ENDC)
                                print(bcolors.BLUE + "   [              All foundation tools installed             ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [                 Anonymous tools installed               ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [               Wifi pentesting tools installed           ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [                 Web pentest tools installed             ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [              Local pentesting tools installed           ] \n" + bcolors.ENDC)
                                print(bcolors.ENDC + "     {" + bcolors.RED + bcolors.UNDERL + " git clone. & cd ~/; pip3 install -r requirements.txt " + bcolors.ENDC + "}\n" + bcolors.ENDC)
                                africana = bcolors.ENDC + "  -{" + bcolors.YELLOW + " Installing and setting up third party tools from github. " + bcolors.ENDC + "}-\n" + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.09)
                                print("\n")
                                os.system('cd /usr/local/opt/africana-framework/externals; git clone https://github.com/ScRiPt1337/Teardroid-phprat; cd ./Teardroid-phprat; pip3 install -r requirements.txt; wget https://github.com/ScRiPt1337/Teardroidv4_api/archive/refs/heads/main.zip; unzip main.zip; cd ..; git clone https://github.com/devanshbatham/paramspider; cd paramspider; pip3 install .; cd ..; git clone https://github.com/Ignitetch/AdvPhishing.git; cd AdvPhishing/; chmod 777 *; ./Linux-Setup.sh; cd ..;git clone https://github.com/TermuxHackz/anonphisher; cd ./anonphisher; chmod 777 *; bash anonphisher.sh; cd ..; git clone https://github.com/epsylon/ufonet')

                                os.system('clear')
                                print("\n")
                                print(bcolors.ENDC + "  -{ " + bcolors.GREEN + bcolors.UNDERL + "For God so loved the world, that he gave His." + bcolors.ENDC + color() + " [John 3:16] " + bcolors.ENDC + "}-\n" + bcolors.ENDC)
                                print(bcolors.BLUE + "   [              Setting up project discovery tools         ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [                   Pleas Be Patient as the               ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [                      Installer runs                     ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [                            &                            ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [              Sets up all golang necessary tools         ] \n" + bcolors.ENDC)
                                print(bcolors.ENDC + "          {" + bcolors.RED + bcolors.UNDERL + " cd ~/go/bin; ./pdtm -ia; source ~/.zshrc. " + bcolors.ENDC + "}\n" + bcolors.ENDC)
                                africana = bcolors.ENDC + " -{" + bcolors.YELLOW + " Updating all Project Discovery tools & testing them for you " + bcolors.ENDC + "}-\n" + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.09)
                                print("\n")
                                os.system('go install github.com/projectdiscovery/pdtm/cmd/pdtm@latest; go install github.com/hahwul/dalfox/v2@latest')
                                afric = '/root/go'
                                if os.path.exists(afric):
                                    os.system('cd ~/go/bin; ./pdtm -ia; source ~/.zshrc; update-grub2')
                                else:
                                    break

                                os.system('clear')
                                print("\n")
                                beauty.graphics(), scriptures.verses()
                                print("\n")
                                print(bcolors.BLUE + "   [              All foundation tools installed             ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [                 Anonymous tools installed               ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [               Wifi pentesting tools installed           ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [                 Web pentest tools installed             ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [              Local pentesting tools installed           ] \n" + bcolors.ENDC)
                                africana = bcolors.ENDC + " -{" + bcolors.YELLOW + " Everything is set. Type 'africana' to launch the framework " + bcolors.ENDC + "}-\n" + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.09)
                                break
                            except:
                                break

#UbuntuLinux
                elif choice == '2':
                    os.system('clear')
                    print("\n")
                    print(bcolors.ENDC + "  -{ " + bcolors.GREEN + bcolors.UNDERL + "For God so loved the world, that he gave His." + bcolors.ENDC + color() + " [John 3:16] " + bcolors.ENDC + "}-\n" + bcolors.ENDC)
                    print(bcolors.BLUE + "   [            Installing Africana On Ubuntu-Linux          ] " + bcolors.ENDC)
                    print(bcolors.BLUE + "   [                    Pleas Be Patient                     ] " + bcolors.ENDC)
                    print(bcolors.BLUE + "   [      Installer will copy core files to your system      ] " + bcolors.ENDC)
                    print(bcolors.BLUE + "   [                            &                            ] " + bcolors.ENDC)
                    print(bcolors.BLUE + "   [              All Necessary Foundation Tools             ] \n" + bcolors.ENDC)
                    print(bcolors.ENDC + "       -{" + bcolors.RED + bcolors.UNDERL + " apt-get install -y git zsh python3 python3-pip. " + bcolors.ENDC + "}-\n" + bcolors.ENDC)

                    afric = '/usr/local/opt/africana-framework'
                    if os.path.exists(afric):
                        os.system('clear')
                        print("\n")
                        print(bcolors.ENDC + "  -{ " + bcolors.GREEN + bcolors.UNDERL + "For God so loved the world, that he gave His." + bcolors.ENDC + color() + " [John 3:16] " + bcolors.ENDC + "}-\n" + bcolors.ENDC)
                        print(bcolors.BLUE + "   [              Africana detected in your system           ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [                   Pleas Be Patient as the               ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [                 Installer runs full updates             ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [                            &                            ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [       Upgrades for All Necessary Foundation Tools       ] \n" + bcolors.ENDC)
                        print(bcolors.ENDC + "               {" + bcolors.RED + bcolors.UNDERL + " git pull & apt-get upgrade -y.. " + bcolors.ENDC + "}\n" + bcolors.ENDC)
                        africana = bcolors.ENDC + " -{" + bcolors.YELLOW + " Africana is already installed in your system. Updating It. " + bcolors.ENDC + "}-\n" + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.09)
                        print("\n")
                        os.system('apt-get update -y')
                        print("\n")
                        os.system('cd /usr/local/opt/africana-framework; git pull; cd Teardroid-phprat; git pull; cd ../AdvPhishing; git pull; cd ../ufonet; git pull; cd ../anonphisher; git pull')
                        time.sleep(0.09)

                        os.system('clear')
                        print("\n")
                        print(bcolors.ENDC + "  -{ " + bcolors.GREEN + bcolors.UNDERL + "For God so loved the world, that he gave His." + bcolors.ENDC + color() + " [John 3:16] " + bcolors.ENDC + "}-\n" + bcolors.ENDC)
                        print(bcolors.BLUE + "   [              Setting up project discovery tools         ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [                   Pleas Be Patient as the               ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [                      Installer runs                     ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [                            &                            ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [              Sets up all golang necessary tools         ] \n" + bcolors.ENDC)
                        print(bcolors.ENDC + "          {" + bcolors.RED + bcolors.UNDERL + " cd ~/go/bin; ./pdtm -ia; source ~/.zshrc. " + bcolors.ENDC + "}\n" + bcolors.ENDC)
                        africana = bcolors.ENDC + " -{" + bcolors.YELLOW + " Updating all Project Discovery tools & testing them for you " + bcolors.ENDC + "}-\n" + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.09)
                        afric = '/root/go'
                        if os.path.exists(afric):
                            os.system('cd ~/go/bin; ./pdtm -ia; source ~/.zshrc')
                        else:
                            pass

                        os.system('clear')
                        print("\n")
                        beauty.graphics(), scriptures.verses()
                        print("\n")
                        print(bcolors.BLUE + "   [              All foundation tools installed             ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [                 Anonymous tools installed               ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [               Wifi pentesting tools installed           ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [                 Web pentest tools installed             ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [              Local pentesting tools installed           ] \n" + bcolors.ENDC)
                        africana = bcolors.ENDC + " -{" + bcolors.YELLOW + " Everything is set. Type 'africana' to launch the framework " + bcolors.ENDC + "}-\n" + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.09)
                        break

                    else:
                        os.system('mkdir -p /usr/local/opt; cp -rf ../africana-framework /usr/local/opt/; ln -s /usr/local/opt/africana-framework/modules/kenyan.py /usr/local/bin/africana; chmod +x /usr/local/bin/africana; apt-get update -y; apt-get upgrade -y; apt-get install zsh git curl -y; echo -n "# Kali linux repositories | Added by Africana\ndeb http://http.kali.org/kali kali-rolling main contrib non-free" >> /etc/apt/sources.list; mkdir -p /etc/apt/trusted.gpg.d/; cd /etc/apt/trusted.gpg.d/; apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ED444FF07D8D0BF6; mkdir -p /etc/apt/trusted.gpg.d/; cd /etc/apt/trusted.gpg.d/; curl -SL https://playit-cloud.github.io/ppa/key.gpg | gpg --dearmor > playit.gpg; curl -SL -o /etc/apt/sources.list.d/playit-cloud.list https://playit-cloud.github.io/ppa/playit-cloud.list; dpkg --add-architecture i386; apt-get update -y; apt-get install -y tor squid privoxy iptables openssh-client openssh-server ftp ncat rlwrap powershell golang-go docker.io python3 python3-pip build-essential libssl-dev libffi-dev python3-dev python3-venv python3-pycurl python3-geoip python3-whois python3-requests python3-scapy libgeoip1 libgeoip-dev privoxy dnsmasq gophish wifipumpkin3 wifite airgeddon nuclei nikto nmap smbmap dnsrecon metasploit-framework dnsrecon feroxbuster dirsearch uniscan sqlmap commix dnsenum sslscan whatweb wafw00f wordlists wapiti xsser villain set playit wine32:i386')
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
                        print("\n")
                        print(bcolors.ENDC + "  -{ " + bcolors.GREEN + bcolors.UNDERL + "For God so loved the world, that he gave His." + bcolors.ENDC + color() + " [John 3:16] " + bcolors.ENDC + "}-\n" + bcolors.ENDC)
                        print(bcolors.BLUE + "   [           Setting up Go, Python env @ '~/.afric'        ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [                   Pleas Be Patient as the               ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [                        Setup runs                       ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [                            &                            ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [              Source @ ~/.afric/bin/activate             ] \n" + bcolors.ENDC)
                        print(bcolors.ENDC + "          {" + bcolors.RED + bcolors.UNDERL + " cd ~/; pip3 install virtualenv; virtualenv " + bcolors.ENDC + "}\n" + bcolors.ENDC)
                        africana = bcolors.ENDC + " -{" + bcolors.YELLOW + " Creating Go, Python env @ '~/.afric' & activating it for you " + bcolors.ENDC + "}-\n" + bcolors.ENDC
                        for a in africana:
                            sys.stdout.write(a)
                            sys.stdout.flush()
                            time.sleep(0.09)
                        print("\n")
                        os.system('cd ~/; pip3 install virtualenv; virtualenv .afric; echo -n "\n# Created By africana-framework. Delete At Your Own Risk\nsource ~/.afric/bin/activate" >> ~/.zshrc')
                        infile = "/root/.zshrc"
                        outfile = "/root/.zshrc"
                        delete_list = ["# Created By africana-framework. Delete At Your Own Risk\n", "source ~/.afric/bin/activate"]
                        fin = open(infile)
                        os.remove("/root/.zshrc")
                        fout = open(outfile, "w+")
                        for line in fin:
                            for word in delete_list:
                                line = line.replace(word, "")
                            fout.write(line)
                        fin.close()
                        fout.close()

                        git = '/usr/local/opt/africana-framework/externals'
                        if os.path.exists(git):
                            try:
                                os.system('clear')
                                print("\n")
                                print(bcolors.ENDC + "  -{ " + bcolors.GREEN + bcolors.UNDERL + "For God so loved the world, that he gave His." + bcolors.ENDC + color() + " [John 3:16] " + bcolors.ENDC + "}-\n" + bcolors.ENDC)
                                print(bcolors.BLUE + "   [              All foundation tools installed             ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [                 Anonymous tools installed               ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [               Wifi pentesting tools installed           ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [                 Web pentest tools installed             ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [              Local pentesting tools installed           ] \n" + bcolors.ENDC)
                                print(bcolors.ENDC + "     {" + bcolors.RED + bcolors.UNDERL + " git clone. & cd ~/; pip3 install -r requirements.txt " + bcolors.ENDC + "}\n" + bcolors.ENDC)
                                africana = bcolors.ENDC + "   -{" + bcolors.YELLOW + " Installing africana-framework' s Python3 requirements. " + bcolors.ENDC + "}-\n" + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.09)
                                print("\n")
                                os.system('zsh -c "source ~/.zshrc; cd /usr/local/opt/africana-framework; pip3 install -r requirements.txt"')

                                os.system('clear')
                                print("\n")
                                print(bcolors.ENDC + "  -{ " + bcolors.GREEN + bcolors.UNDERL + "For God so loved the world, that he gave His." + bcolors.ENDC + color() + " [John 3:16] " + bcolors.ENDC + "}-\n" + bcolors.ENDC)
                                print(bcolors.BLUE + "   [              All foundation tools installed             ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [                 Anonymous tools installed               ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [               Wifi pentesting tools installed           ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [                 Web pentest tools installed             ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [              Local pentesting tools installed           ] \n" + bcolors.ENDC)
                                print(bcolors.ENDC + "     {" + bcolors.RED + bcolors.UNDERL + " git clone. & cd ~/; pip3 install -r requirements.txt " + bcolors.ENDC + "}\n" + bcolors.ENDC)
                                africana = bcolors.ENDC + "  -{" + bcolors.YELLOW + " Installing and setting up third party tools from github. " + bcolors.ENDC + "}-\n" + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.09)
                                print("\n")
                                os.system('cd /usr/local/opt/africana-framework/externals; git clone https://github.com/ScRiPt1337/Teardroid-phprat; cd ./Teardroid-phprat; pip3 install -r requirements.txt; wget https://github.com/ScRiPt1337/Teardroidv4_api/archive/refs/heads/main.zip; unzip main.zip; cd ..; git clone https://github.com/devanshbatham/paramspider; cd paramspider; pip3 install .; cd ..; git clone https://github.com/Ignitetch/AdvPhishing.git; cd AdvPhishing/; chmod 777 *; ./Linux-Setup.sh; cd ..;git clone https://github.com/TermuxHackz/anonphisher; cd ./anonphisher; chmod 777 *; bash anonphisher.sh; cd ..; git clone https://github.com/epsylon/ufonet')

                                os.system('clear')
                                print("\n")
                                print(bcolors.ENDC + "  -{ " + bcolors.GREEN + bcolors.UNDERL + "For God so loved the world, that he gave His." + bcolors.ENDC + color() + " [John 3:16] " + bcolors.ENDC + "}-\n" + bcolors.ENDC)
                                print(bcolors.BLUE + "   [              Setting up project discovery tools         ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [                   Pleas Be Patient as the               ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [                      Installer runs                     ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [                            &                            ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [              Sets up all golang necessary tools         ] \n" + bcolors.ENDC)
                                print(bcolors.ENDC + "          {" + bcolors.RED + bcolors.UNDERL + " cd ~/go/bin; ./pdtm -ia; source ~/.zshrc. " + bcolors.ENDC + "}\n" + bcolors.ENDC)
                                africana = bcolors.ENDC + " -{" + bcolors.YELLOW + " Updating all Project Discovery tools & testing them for you " + bcolors.ENDC + "}-\n" + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.09)
                                print("\n")
                                os.system('apt-get update -y')
                                os.system('go install github.com/projectdiscovery/pdtm/cmd/pdtm@latest; go install github.com/hahwul/dalfox/v2@latest')
                                afric = '/root/go'
                                if os.path.exists(afric):
                                    os.system('cd ~/go/bin; ./pdtm -ia; source ~/.zshrc; update-grub2')

                                else:
                                    break

                                os.system('clear')
                                print("\n")
                                beauty.graphics(), scriptures.verses()
                                print("\n")
                                print(bcolors.BLUE + "   [              All foundation tools installed             ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [                 Anonymous tools installed               ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [               Wifi pentesting tools installed           ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [                 Web pentest tools installed             ] " + bcolors.ENDC)
                                print(bcolors.BLUE + "   [              Local pentesting tools installed           ] \n" + bcolors.ENDC)
                                africana = bcolors.ENDC + " -{" + bcolors.YELLOW + " Everything is set. Type 'africana' to launch the framework " + bcolors.ENDC + "}-\n" + bcolors.ENDC
                                for a in africana:
                                    sys.stdout.write(a)
                                    sys.stdout.flush()
                                    time.sleep(0.09)
                                break
                            except:
                                break

## Uninstaller
                elif choice == '4':
                    try:
                        os.system('clear')
                        beauty.graphics(), scriptures.verses()
                        print("\n")
                        print(bcolors.BLUE + "   [  Incase Of Any Bug Email Me at: " + bcolors.YELLOW + "rojahsmontari@gmail.com " + bcolors.BLUE + "    ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [  Are You Sure You Want To Completely Uninstall Africana?    ] " + bcolors.ENDC)
                        print(bcolors.BLUE + "   [          Select  " + bcolors.YELLOW + "1. " + bcolors.RED + "Yes " + bcolors.YELLOW + " 0. " + bcolors.RED + "No " + bcolors.BLUE + "& Go Back To Menu."  + bcolors.BLUE + "           ] \n" + bcolors.ENDC)

                        choice = input(bcolors.GREEN + "(" + bcolors.ENDC + "africana:" + bcolors.DARKCYAN + "framework" + bcolors.GREEN + ")# " + bcolors.ENDC)
                        if choice == '1':
                            afric = '/usr/local/opt/africana-framework'
                            if os.path.exists(afric):
                                os.system('rm -rf /usr/local/opt/africana-framework')
                            else:
                                os.system('rm -rf /usr/local/opt/africana-framework')
                                pass
                            os.system('clear')

                            infile = "/root/.zshrc"
                            outfile = "/root/.zshrc"
                            delete_list = ["# Created By africana-framework. Delete At Your Own Risk\n", "source ~/.afric/bin/activate"]
                            fin = open(infile)
                            os.remove("/root/.zshrc")
                            fout = open(outfile, "w+")
                            for line in fin:
                                for word in delete_list:
                                    line = line.replace(word, "")
                                fout.write(line)
                            fin.close()
                            fout.close()

                            beauty.graphics(), scriptures.verses()
                            africana = bcolors.ENDC + "   ~{ " + bcolors.RED + "The Uninstaller Has Deleted africana-framework And All Its Files. " + bcolors.DARKCYAN + "0. or 1. " + bcolors.ENDC +  "}~" + bcolors.ENDC
                            for a in africana:
                                sys.stdout.write(a)
                                sys.stdout.flush()
                                time.sleep(0.03)
                            break
                        elif choice == '0':
                            installer.update_system()
                            break
                        else:
                            print("\n")
                            warn = bcolors.ENDC + "   ~{ " + bcolors.RED + "Poor Choice Of Selection!!!. Please Select " + bcolors.DARKCYAN + "0. or 1. " + bcolors.ENDC +  "}~" + bcolors.ENDC
                            for w in warn:
                                sys.stdout.write(w)
                                sys.stdout.flush()
                                time.sleep(0.09)
                            installer.update_system()
                            break
                    except:
                        neo.one()
                        break
                else:
                    try:
                        print("\n")
                        warn = bcolors.ENDC + "   ~{ " + bcolors.RED + "Poor Choice Of Selection!!!. Please Select " + bcolors.DARKCYAN + "0. or 1. " + bcolors.ENDC +  "}~" + bcolors.ENDC
                        for w in warn:
                            sys.stdout.write(w)
                            sys.stdout.flush()
                            time.sleep(0.09)
                        update_system()
                        pass
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
