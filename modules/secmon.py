#!/bin/bash

export BLUE='\033[1;94m'
export GREEN='\033[1;92m'
export RED='\033[1;91m'
export RESETCOLOR='\033[1;00m'

echo -e "\n$RED                    Part of africana-framework."
echo -e "$RED                YOUR INTERNET PROXY CONNECTIONS ROUTES.\n"
echo -e "$BLUE Copy & Paste  -> [tail -f /var/log/privoxy/logfile] To see Your Logs]"
echo -e "$BLUE Launch An Attack Using Port 8888 ex. [sqlmap --proxy=http://127.0.0.1:8888]\n"
echo -e "$BLUE         To Use Launch With [proxmon] comand in your shell"
echo -e "$BLUE        Pproxy [8888] -> Squid [3218] -> Privoxy [8118] -> Tor $GREEN [9050]\n"
pproxy -r http://localhost:3128 -l http://localhost:8888 -vvv "$@"
