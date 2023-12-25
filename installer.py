#! /usr/bin/python3
# coding=utf-8

from src.core.system import *

while True:
    try:
        os.system('clear')
        installer.update_system(); break
    except:
        os.system('clear')
        beauty.squid_banner()
        break
