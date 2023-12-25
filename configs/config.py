import sys
import time
import subprocess
from src.core.bcolors import *

torstring = ['# Created By africana-framework. Delete At Your Own Risk!!', '', 'VirtualAddrNetworkIPv4 10.192.0.0/10', 'AutomapHostsOnResolve 1',
              'TransPort 9040 IsolateClientAddr IsolateClientProtocol IsolateDestAddr IsolateDestPort', 'DNSPort 5353', 'CookieAuthentication 1']

privoxystring = ['# Created By africana-framework. Delete At Your Own Risk!!', '', 'confdir /etc/privoxy', 'logdir /var/log/privoxy', 'logfile logfile', 'debug   4096 ', 'debug   8192', 'user-manual /usr/share/doc/privoxy/user-manual',
              'actionsfile default.action', 'actionsfile user.action', 'filterfile default.filter', 'listen-address  127.0.0.1:8118', 'toggle  1', 'enable-remote-toggle 0',
              'enable-edit-actions 0', 'enable-remote-http-toggle 0', 'buffer-limit 4096', 'forward-socks5t   /               127.0.0.1:9050 .']

squidstring = ['# Created By africana-framework. Delete At Your Own Risk!!', '','acl manager proto cache_object', 'acl localhost src 127.0.0.1/32 ::1', 'acl to_localhost dst 127.0.0.0/8 0.0.0.0/32 ::1', 'acl ftp proto FTP', 'acl localnet src 10.0.0.0/8', 'acl localnet src 172.16.0.0/12',
              'acl localnet src 192.168.0.0/16', 'acl localnet src fc00::/7', 'acl localnet src fe80::/10', 'acl SSL_ports port 443', 'acl Safe_ports port 80 ', 'acl Safe_ports port 21',
              'acl Safe_ports port 443', 'acl Safe_ports port 70', 'acl Safe_ports port 210', 'acl Safe_ports port 1025-65535', 'acl Safe_ports port 280', 'acl Safe_ports port 488', 'acl Safe_ports port 591', 'acl Safe_ports port 777',
              'acl Safe_ports port 3128', 'acl CONNECT method CONNECT', 'http_access allow manager localhost', 'http_access deny manager', 'http_access deny !Safe_ports', 'http_access deny CONNECT !SSL_ports',
              'http_access allow localhost', 'http_access allow all', 'http_port 3128', 'hierarchy_stoplist cgi-bin ?', 'cache_peer 127.0.0.1 parent 8118 7 no-query no-digest', 'coredump_dir /var/spool/squid', 
              'refresh_pattern ^ftp:           1440    20%     10080','refresh_pattern ^gopher:        1440    0%      1440', 'refresh_pattern -i (/cgi-bin/|\?) 0     0%      0', 'refresh_pattern .               0       20%     4320',
              'httpd_suppress_version_string on', 'forwarded_for off', 'always_direct allow ftp', 'never_direct allow all']
dhclientstring = ['# Created By africana-framework. Delete At Your Own Risk!!', '', 'option rfc3442-classless-static-routes code 121 = array of unsigned integer 8;', 'send host-name = gethostname();', 'request subnet-mask, broadcast-address, time-offset, routers,', '	domain-name, domain-name-servers, domain-search, host-name,',
              '	dhcp6.name-servers, dhcp6.domain-search, dhcp6.fqdn, dhcp6.sntp-servers,', '	netbios-name-servers, netbios-scope, interface-mtu,', '	rfc3442-classless-static-routes, ntp-servers;', 'prepend domain-name-servers 127.0.0.1,1.1.1.1, 1.0.0.1, 8.8.8.8, 8.8.4.4;']

changemacstring = ['# Created By africana-framework. Delete At Your Own Risk!!', '', '[Unit]', 'Description=changes mac for %I', 'Wants=network.target', 'Before=network.target', 'BindsTo=sys-subsystem-net-devices-%i.device', 'After=sys-subsystem-net-devices-%i.device', '', '[Service]', 'Type=oneshot', 'ExecStart=/usr/bin/macchanger -r %I', 'RemainAfterExit=yes',
                   '', '[Install]', 'WantedBy=multi-user.target']

resolvstring = ['# Created By africana-framework. Delete At Your Own Risk!!', 'nameserver 1.1.1.1', 'nameserver 1.0.0.1', 'nameserver 8.8.8.8', 'nameserver 8.8.4.4']

class configure(object):
    def __init__(self):
        pass
    def configure_all(self):

        if os.system("which tor > /dev/null") == 0:
            if not os.path.exists('/etc/tor/torrc'):
                print(
                    f"{color(bcolors.RED)}No torrc file is configured.....{bcolors.ENDC}{color(bcolors.GREEN)}Configuring:)")
                try:
                    f = open('/etc/tor/torrc', 'w+')
                    for elements in torstring:
                        f.write("%s\n" % elements)
                    f.close()
                    print(f"{color(bcolors.CYAN)}Done....{bcolors.ENDC}")
                except Exception as e:
                    print(f"{color(bcolors.RED)}Failed to write the torrc file{bcolors.ENDC} \n {e}")
                    pass
            else:
                print(f"\n{color(bcolors.GREEN)}{bcolors.BOLD}Configuring Torrc {bcolors.ENDC}")
                time.sleep(0.4)

                with open('/etc/tor/torrc') as x:
                    verse = x.read().splitlines()

                subprocess.Popen(["cp", "/etc/tor/torrc", "/etc/tor/torrc.bak_africana"], stdout=subprocess.PIPE).communicate()
                torrc = open('/etc/tor/torrc', 'w')
                for elements in torstring:
                    torrc.write("%s\n" % elements)
                torrc.close()
                print(f"{color(bcolors.RED)}DONE :){bcolors.ENDC}")

        else:
            print(f'''\n{color(bcolors.RED)}tor isn't installed, install it with 'sudo apt install tor'{bcolors.ENDC}''')
            pass

        infile = "/lib/systemd/system/tor@default.service"
        outfile = "/lib/systemd/system/tor@default.service"
        delete_list = ['# Created By africana-framework. Delete At Your Own Risk!!\n', '[Install]\n', 'WantedBy=multi-user.target']
        fin = open(infile)
        os.remove("/lib/systemd/system/tor@default.service")
        fout = open(outfile, "w+")
        for line in fin:
            for word in delete_list:
                line = line.replace(word, '')
            fout.write(line)
        fin.close()
        fout.close()

        os.system('echo -n "\n# Created By africana-framework. Delete At Your Own Risk!!\n" >> "/lib/systemd/system/tor@default.service"')
        infile = "/lib/systemd/system/tor@default.service"
        outfile = "/lib/systemd/system/tor@default.service"
        delete_list = ['# Created By africana-framework. Delete At Your Own Risk!!\n']
        fin = open(infile)
        os.remove("/lib/systemd/system/tor@default.service")
        fout = open(outfile, "w+")
        for line in fin:
            for word in delete_list:
                line = line.replace(word, '# Created By africana-framework. Delete At Your Own Risk!!\n[Install]\nWantedBy=multi-user.target')
            fout.write(line)
        fin.close()
        fout.close()

        if os.system("which privoxy > /dev/null") == 0:
            if not os.path.exists('/etc/privoxy/config'):
                print(
                    f"{color(bcolors.RED)}No privoxy/config file is configured.....{bcolors.ENDC}{color(bcolors.GREEN)}Configuring:)")
                try:
                    f = open('/etc/privoxy/config', 'w+')
                    for elements in privoxytring:
                        f.write("%s\n" % elements)
                    f.close()
                    print(f"{color(bcolors.CYAN)}Done....{bcolors.ENDC}")
                except Exception as e:
                    print(f"{color(bcolors.RED)}Failed to write the privoxy/config file{bcolors.ENDC} \n {e}")
                    pass
            else:
                print(f"\n{color(bcolors.GREEN)}{bcolors.BOLD}Configuring privoxy/config {bcolors.ENDC}")
                time.sleep(0.4)

                with open('/etc/privoxy/config') as x:
                    verse = x.read().splitlines()

                subprocess.Popen(["cp", "/etc/privoxy/config", "/etc/privoxy/config.bak_africana"], stdout=subprocess.PIPE).communicate()
                privoxy = open('/etc/privoxy/config', 'w')
                for elements in privoxystring:
                    privoxy.write("%s\n" % elements)
                privoxy.close()
                print(f"{color(bcolors.RED)}DONE :){bcolors.ENDC}")

        else:
            print(f'''\n{color(bcolors.RED)}privoxy isn't installed, install it with 'sudo apt install privoxy'{bcolors.ENDC}''')
            pass

        if os.system("which squid > /dev/null") == 0:
            if not os.path.exists('/etc/squid/squid.conf'):
                print(
                    f"{color(bcolors.RED)}No squid/config file is configured.....{bcolors.ENDC}{color(bcolors.GREEN)}Configuring:)")
                try:
                    f = open('/etc/squid/squid.conf', 'w+')
                    for elements in squidstring:
                        f.write("%s\n" % elements)
                    f.close()
                    print(f"{color(bcolors.CYAN)}Done....{bcolors.ENDC}")
                except Exception as e:
                    print(f"{color(bcolors.RED)}Failed to write the squid/config file{bcolors.ENDC} \n {e}")
                    pass
            else:
                print(f"\n{color(bcolors.GREEN)}{bcolors.BOLD}Configuring squid/config {bcolors.ENDC}")
                time.sleep(0.4)

                with open('/etc/squid/squid.conf') as x:
                    verse = x.read().splitlines()
                subprocess.Popen(["cp", "/etc/squid/squid.conf", "/etc/squid/config.bak_africana"], stdout=subprocess.PIPE).communicate()
                squid = open('/etc/squid/squid.conf', 'w')
                for elements in squidstring:
                    squid.write("%s\n" % elements)
                squid.close()
                print(f"{color(bcolors.RED)}DONE :){bcolors.ENDC}")

        else:
            print(f'''\n{color(bcolors.RED)}squid isn't installed, install it with 'sudo apt install squid'{bcolors.ENDC}''')
            pass

        if os.system("which dhclient > /dev/null") == 0:
            if not os.path.exists('/etc/dhcp/dhclient.conf'):
                print(
                    f"{color(bcolors.RED)}No dhclient.conf file is configured.....{bcolors.ENDC}{color(bcolors.GREEN)}Configuring:)")
                try:
                    f = open('/etc/dhcp/dhclient.conf', 'w+')
                    for elements in dhclientstring:
                        f.write("%s\n" % elements)
                    f.close()
                    print(f"{color(bcolors.CYAN)}Done....{bcolors.ENDC}")
                except Exception as e:
                    print(f"{color(bcolors.RED)}Failed to write the dhclient.conf file{bcolors.ENDC} \n {e}")
                    pass
            else:
                print(f"\n{color(bcolors.GREEN)}{bcolors.BOLD}Configuring dhclient.conf {bcolors.ENDC}")
                time.sleep(0.4)

                with open('/etc/dhcp/dhclient.conf') as x:
                    verse = x.read().splitlines()

                subprocess.Popen(["cp", "/etc/dhcp/dhclient.conf", "/etc/dhcp/dhclient.bak_africana"], stdout=subprocess.PIPE).communicate()
                dhclient = open('/etc/dhcp/dhclient.conf', 'w')
                for elements in dhclientstring:
                    dhclient.write("%s\n" % elements)
                dhclient.close()
                print(f"{color(bcolors.RED)}DONE :){bcolors.ENDC}")

        else:
            print(f'''\n{color(bcolors.RED)}squid isn't installed, install it with 'sudo apt install isc-dhcp-client'{bcolors.ENDC}''')
            pass

        if os.system("which macchanger > /dev/null") == 0:
            if not os.path.exists('/etc/systemd/system/changemac@.service'):
                print(
                    f"{color(bcolors.RED)}No changemac@.service file is configured.....{bcolors.ENDC}{color(bcolors.GREEN)}Configuring:)")
                try:
                    f = open('/etc/systemd/system/changemac@.service', 'w+')
                    for elements in changemacstring:
                        f.write("%s\n" % elements)
                    f.close()
                    print(f"{color(bcolors.CYAN)}Done....{bcolors.ENDC}")
                except Exception as e:
                    print(f"{color(bcolors.RED)}Failed to write the changemac@.service file{bcolors.ENDC} \n {e}")
                    pass
            else:
                print(f"\n{color(bcolors.GREEN)}{bcolors.BOLD}Configuring changemac@.service {bcolors.ENDC}")
                time.sleep(0.4)

                with open('/etc/systemd/system/changemac@.service') as x:
                    verse = x.read().splitlines()

                subprocess.Popen(["cp", "/etc/systemd/system/changemac@.service", "/etc/systemd/system/changemac@.service.bak_africana"], stdout=subprocess.PIPE).communicate()
                changemac = open('/etc/systemd/system/changemac@.service', 'w')
                for elements in changemacstring:
                    changemac.write("%s\n" % elements)
                changemac.close()
                print(f"{color(bcolors.RED)}DONE :){bcolors.ENDC}")

        else:
            print(f'''\n{color(bcolors.RED)}squid isn't installed, install it with 'sudo apt install macchanger'{bcolors.ENDC}''')
            pass

        if os.system("which dnsmasq > /dev/null") == 0:
            if not os.path.exists('/etc/dnsmasq.conf'):
                print(
                    f"{color(bcolors.RED)}No dnsmasq.conf file is configured.....{bcolors.ENDC}{color(bcolors.GREEN)}Configuring:)")
                try:
                    infile = "/etc/dnsmasq.conf"
                    outfile = "/etc/dnsmasq.conf"
                    delete_list = ['#port=5353']
                    fin = open(infile)
                    os.remove("/etc/dnsmasq.conf")
                    fout = open(outfile, "w+")
                    for line in fin:
                        for word in delete_list:
                            line = line.replace(word, 'port=5353')
                        fout.write(line)
                    fin.close()
                    fout.close()
                    print(f"{color(bcolors.CYAN)}Done....{bcolors.ENDC}")
                except Exception as e:
                    print(f"{color(bcolors.RED)}Failed to write the dnsmasq.conf file{bcolors.ENDC} \n {e}")
                    pass
            else:
                print(f"\n{color(bcolors.GREEN)}{bcolors.BOLD}Configuring dnsmasq.conf {bcolors.ENDC}")
                time.sleep(0.4)
                try:
                    infile = "/etc/dnsmasq.conf"
                    outfile = "/etc/dnsmasq.conf"
                    delete_list = ['#port=5353']
                    fin = open(infile)
                    os.remove("/etc/dnsmasq.conf")
                    fout = open(outfile, "w+")
                    for line in fin:
                        for word in delete_list:
                            line = line.replace(word, 'port=5353')
                        fout.write(line)
                    fin.close()
                    fout.close()
                    print(f"{color(bcolors.CYAN)}Done....{bcolors.ENDC}")
                except Exception as e:
                    print(f"{color(bcolors.RED)}Failed to write the dnsmasq.conf file{bcolors.ENDC} \n {e}")
                    pass
                print(f"{color(bcolors.RED)}DONE :){bcolors.ENDC}")
        else:
            print(f'''\n{color(bcolors.RED)}dnsmasq isn't installed, install it with 'sudo apt install dnsmasq'{bcolors.ENDC}''')
            pass

config = configure()
if ' __name__' == '__main__':
        sys.exit(config())
