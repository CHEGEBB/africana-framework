import time
import random
from src.core.bcolors import *

class banners(object):
    def __init__(self):
        pass
    def graphics(self):
        menu = random.randrange(1, 61)
        if menu == 1:
            print(color() + r"""
                 _,._
             __.'   _)
            <_,)'.-"a\
              /' (    \
  _.-----..,-'   (`"--^
 //              |
(|   `;      ,   |
  \   ;.----/  ,/
   ) // /   | |\ \
   \ \\`\   | |/ /    Jesus Christ
    \ \\ \  | |\/ Lamb that was slain.
     `" `"  `"` 
""" + bcolors.ENDC)

        if menu == 2:
            print(color() + r"""
 _      xxxx      _
/_;-.__ / _\  _.-;_\
   `-._`'`_/'`.-'
       `\   /`
        |  /
       /-.(
       \_._\
        \ \`;
         > |/
        / //
        |//
        \(\
""" + bcolors.ENDC)

        if menu == 3:
            print(color() + r"""
         ,   ,
        /////|
       ///// |
      /////  |
     |~~~| | |
     |===| |/|
     | B |/| |
     | I | | |
     | B | | |
     | L |  / 
     | E | /
     |===|/
     '---'

  Jesus love's u.
""" + bcolors.ENDC)

        if menu == 4:
            print(color() + r"""
    __                 _____ _____     _     _ 
 __|  |___ ___ _ _ ___|     |  |  |___|_|___| |_ 
|  |  | -_|_ -| | |_ -|   --|     |  _| |_ -|  _|
|_____|___|___|___|___|_____|__|__|_| |_|___|_|

""" + bcolors.ENDC)

        if menu == 5:
            print(color() + r"""
               |
           \       /
             .---. 
        '-.  |   |  .-'
          ___|   |___
     -=  [           ]  =-
         `---.   .---' 
      __||__ |   | __||__
      '-..-' |   | '-..-'
        ||   |   |   ||
        ||_.-|   |-,_||
      .-"`   `"`'`   `"-.
    .'                   '.
""" + bcolors.ENDC)

        if menu == 6:
            print(bcolors.PURPLE + r"""⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡈⠛⢿⣿⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀
⠀⠸⢿⣿⣶⣾⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣴⣾⠇⠀
⠀⠀⢤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⣠⣤⣴⣶⣶⣾⣿⡿⠟⠋⣁⡀⠀
⠀⠀⠘⢉⣩⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣟⠛⠛⠁⠀
⠀⠀⠀⠈⠻⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣟⠿⣿⠃⠀⠀
⠀⠀⠀⠀⠀⠈⠻⠟⣿⣿⣿⣿⣿⣿⣿⣿⣄⣿⣿⣿⣿⣿⣿⣿⣿⡷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⣉⣽⣿⣿⣿⣿⡿⢻⣿⣿⣿⢿⣿⠎⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣦⡀⠈⠉⠉⠁⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣉⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⠋⣽⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⠿⠋⣸⣿⡟⢸⣿⣿⠉⣿⣿⡘⢿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠀⢸⣿⡏⠀⠸⠿⠃⠀⠀⠀⠀
""" + bcolors.ENDC)

        if menu == 7:
            print(color() + r"""
                                         ____
   /\    /\                             /
   \ \  / /                            /
    \ \/ /~~.                         /
     \  //_/                         /
     /  \/                          /
    / /\ \                         /
   / /| \/                       _/
  / / --/                       /
 / / /  |                   ___/
/ / /   |                 _/
\/  \   \_      _________/
---------------/
""" + bcolors.ENDC)

        if menu == 8:
            print(color() + r"""
     .========.        .========.
    // I .'..' \      // VI.'.,".\
    || II .'..'|      || VII..'..|
    || III .'."|      || VIII,'.'|
    || IV ,','.|      || IX.'".'.|
    || V '..'.'|      || X .'..',|
    .\_________/      .\_________/⠀
""" + bcolors.ENDC)

        if menu == 9:
            print(color() + r"""
             .======.
             | KING |
             |      |
             |      |
    .========'      '========.
    |   _      xxxx      _   |
    |  /_;-.__ / _\  _.-;_\  |
    |     `-._`'`_/'`.-'     |
    '========.`\   /`========'
             | |  / |
             |/-.(  |
             |\_._\ |
             | \ \`;|
             |  > |/|
             | / // |
             | |//  |
             | \(\  |
             |  ``  |
             |      |
             |      |
             |      |
             .======.
""" + bcolors.ENDC)

        if menu == 10:
            print(color() + r"""             ,
       (`.  : \               __..----..__
        `.`.| |:          _,-':::''' '  `:`-._
          `.:\||       _,':::::'         `::::`-.
            \\`|    _,':::::::'     `:.     `':::`.
             ;` `-''  `::::::.                  `::\
          ,-'      .::'  `:::::.         `::..    `:\
        ,' /_) -.            `::.           `:.     |
      ,'.:     `    `:.        `:.     .::.          \
 __,-'   ___,..-''-.  `:.        `.   /::::.         |
|):'_,--'           `.    `::..       |::::::.      ::\
 `-'                 |`--.:_::::|_____\::::::::.__  ::|
                     |   _/|::::|      \::::::|::/\  :|
                     /:./  |:::/        \__:::):/  \  :\
                   ,'::'  /:::|        ,'::::/_/    `. ``-.__
                  ''''   (//|/\      ,';':,-'         `-.__  `'--..__
                                                           `''---::::'""" + bcolors.ENDC)

        if menu == 11:
            print(color() + r"""
          _ _
     _(,_/ \ \____________
     |`. \_@_@   `.     ,'
     |\ \ .        `-,-'
     || |  `-.____,-'
     || /  /
     |/ |  |
`..     /   \
  \\   /    |
  ||  |      \
   \\ /-.    |
   ||/  /_   |
   \(_____)-'_)
""" + bcolors.ENDC)

        if menu == 12:
            print(color() + r"""    .__________________________.
    | .___________________. |==|
    | | ................. | |  |
    | | :::Africa ][::::: | |  |
    | | ::::::::::::::::: | |  |
    | | ::::::::::::::::: | |  |
    | | ::::::::::::::::: | |  |
    | | ::::::::::::::::: | |  |
    | | ::::::::::::::::: | | ,|
    | !___________________! |(c|
    !_______________________!__!
   /                            \
  /  [][][][][][][][][][][][][]  \
 /  [][][][][][][][][][][][][][]  \
(  [][][][][____________][][][][]  )
 \ ------------------------------ /
  \______________________________/
""" + bcolors.ENDC)

        if menu == 13:
            print(color() + r"""
                           ___
 _______                  /__/
|.-----.|            ,---[___]*
||     ||           /    printer
||_____||    _____ /        ____
|o_____*|   [o_+_+]--------[=i==]
 |     ________| 850        drive
 |  __|_ 
 '-/_==_\
  /_____\\ 
""" + bcolors.ENDC)

        if menu == 14:
            print(color() + r"""
         __________   __________ __________
        |          |\|          |          |\
        |  *    *  |||  *  *  * |        * ||
        |  *    *  |||          |     *    ||
        |  *    *  |||  *  *  * |  *       ||
        |__________|||__________|__________||
        |          || `---------------------`
        |  *    *  ||
        |          ||
        |  *    *  ||
        |__________||
         `----------`
""" + bcolors.ENDC)


        if menu == 15:
            print(color() + r"""
⠀⠀⠀⠀⠀⠀⠘⣿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣷⣦⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡿⠟⣛⣩⣭⣭⣭⣭⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠞⣡⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀
⠀⠀⠀⠀⠀⠀⡴⢡⣾⣿⡟⣿⡿⣿⢻⣿⣷⣭⣿⣿⣿⣿⣿⣿⣿⡿⠛⣋⣿⠆
⠀⠀⠀⠀⠀⠘⠁⣿⣿⣿⣇⡙⠷⠙⢘⡿⠟⠋⠉⠉⠉⠉⠉⠉⠉⠉⣹⠟⠁⠀
⠀⠀⠀⣀⣠⣴⣿⣿⣿⣿⠿⠋⠀⠈⠁⠀⠀⣧⣦⣦⣄⣦⣠⣤⣤⣾⣷⣶⣤⣄
⠤⠶⠿⠿⠿⠛⠛⠛⠉⣡⡤⠶⠒⠒⠲⠦⣤⣏⡙⠻⠟⠟⠿⣯⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣸⠋⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠲⠶⠞⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢿⣄⠀⠀⠀⠀⢀⣠⡤⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⠟⠞⠁⣀⣀⣤⣶⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠀⠀⠆⢉⡛⠿⠍⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⢉⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⢸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹""" + bcolors.ENDC)

        if menu == 16:
            print(color() + r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⡆⠀⠙⢿⣿⣒⠦⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⠿⠟⠛⠒⠒⠒⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠠⠔⠛⠉⠙⠛⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣍⣀⣀⠀⠀⠀⠀⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣎⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡠⠴⠿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠎⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⠀⠀⠀⠀⢀⣠⣾⠕⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡠⢁⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡉⠉⠉⠙⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣅⡒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣾⣿⠟⢻⠟⠁⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠊
⢀⡾⠋⠀⠀⠀⠀⠀⠀⢀⡨⣻⠋⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⡤⠤⢄⡒⠯⠖⠁
⠘⠁⠀⠀⠀⠀⠀⠀⠴⢫⠞⠁⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠻⣿⣿⣿⠿⣿⣿⢿⣿⣿⢿⣿⣿⣿⣿⡿⢿⣿⣿⢿⣿⣟⢻⣿⣿⡛⠻⠷⠬⠉⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠁⠀⠉⠀⠈⠉⠀⠈⠉⠀⠉⠉⠀⠉⠉⠀⠉⠛⠢⠈⠉⠙⠂⠀
""" + bcolors.ENDC)

        if menu == 17:
            print(color() + r"""
                    /
               ,.. /
             ,'   ';
  ,,.__    _,' /';  .
 :','  ~~~~    '. '~
:' (   )         )::,
'. '. .=----=..-~  .;'
 '  ;'  ::   ':.  '"
   (:   ':    ;)
    \\   '"  ./
     '"      '"⠀
""" + bcolors.ENDC)

        if menu == 18:
            print(color() + r"""
   |\                     /)
 /\_\\__               (_//
|   `>\-`     _._       //`)
 \ /` \\  _.-`:::`-._  //
  `    \|`    :::    `|/
        |     :::     |
        |.....:::.....|
        |:::::::::::::|
        |     :::     |
        \     :::     /
         \    :::    /
          `-. ::: .-'
           //`:::`\\
          //   '   \\
         |/         \\⠀⠀
""" + bcolors.ENDC)

        if menu == 19:
            print(color() + r"""
     ______
    /_____/\
   /_____\\ \
  /_____\ \\ / 
 /_____/ \/ / / 
/_____/ /   \//\ 
\_____\//\   / / 
 \_____/ / /\ /
  \_____/ \\ \ 
   \_____\ \\ 
    \_____\/

""" + bcolors.ENDC)

        if menu == 20:
            print(color() + r"""
             _.-;;-._
      '-..-'|   ||   |
      '-..-'|_.-;;-._|
      '-..-'|   ||   |
      '-..-'|_.-''-._|⠀⠀

""" + bcolors.ENDC)

        if menu == 21:
            print(color() + r"""
 ^...^
<_* *_>
  \_/

  .|||||||||.          .|||||||||.
 |||||||||||||        |||||||||||||
|||||||||||' .\      /. `|||||||||||
`||||||||||_,__o    o__,_||||||||||'

""" + bcolors.ENDC)

        if menu == 22:
            print(color() + r"""
  .---------.
  |.-------.|
  ||>run#  ||
  ||       ||
  |"-------'|
.-^---------^-.
| ---~   AFRIC|
"-------------'
""" + bcolors.ENDC)

        if menu == 23:
            print(color() + r"""
O     O           ,       
  o o          .:/    
    o      ,,///;,   ,;/ 
      o   o)::::::;;///
         >::::::::;;\\\ 
           ''\\\\\'" ';\ 
              ';\
""" + bcolors.ENDC)

        if menu == 24:
            print(color() + r"""
                  .----.
      .---------. | == |
      |.-"'''"-.| |----|
      ||       || | == |
      ||       || |----|
      |'-.....-'| |::::|
      `"")---(""` |___.|
     /:::::::::::\" _  "
    /:::=======:::\`\`\
    `'''''''''''''`  '-'
""" + bcolors.ENDC)

        if menu == 25:
            print(color() + r"""
  ___   _      ___   _      ___   _      ___   _      ___   _
 [(_)] |=|    [(_)] |=|    [(_)] |=|    [(_)] |=|    [(_)] |=|
  '-`  |_|     '-`  |_|     '-`  |_|     '-`  |_|     '-`  |_|
 /mmm/  /     /mmm/  /     /mmm/  /     /mmm/  /     /mmm/  /
       |____________|____________|____________|____________|
                             |            |            |
                         ___  \_      ___  \_      ___  \_
                        [(_)] |=|    [(_)] |=|    [(_)] |=|
                         '-`  |_|     '-`  |_|     '-`  |_|
                         /mmm/        /mmm/        /mmm/

""" + bcolors.ENDC)

        if menu == 26:
            print(color() + r"""
               O  o
          _\_   o
>('>   \\/  o\ .
       //\___=
          ''
""" + bcolors.ENDC)

        if menu == 27:
            print(color() + r"""
                        ,     ,
                        |\---/|
                       /  , , |
                  __.-'|  / \ /
         __ ___.-'        ._O|
      .-'  '        :      _/
     / ,    .        .     |
    :  ;    :        :   _/
    |  |   .'     __:   /
    |  :   /'----'| \  |
    \  |\  |      | /| |
     '.'| /       || \ |
     | /|.'       '.l \\_
     || ||             '-'
     '-''-' 
""" + bcolors.ENDC)

        if menu == 28:
            print(color() + r"""
                     .
                    / V\
                  / `  /
                 <<   |
                 /    |
               /      |
             /        |
           /    \  \ /
          (      ) | |
  ________|   _/_  | |
<__________\______)\__)
""" + bcolors.ENDC)

        if menu == 29:
            print(color() + r"""
    ,__    _,            ___
     '.`\ /`|     _.-"```   `'.
       ; |  /   .'             `} 
       _\|\/_.-'                 }
   _.-"a                 {        }
.-`  __    /._          {         }\
'--"`  `""`   `\   ;    {         } \
               |   } __ _\       }\  \
               |  /;`   / :.   }`  \  \
               | | | .-' /  / /     '. '._
             .'__/-' ````.-'.'        '-._'-._
             ```        ````              `"''`
""" + bcolors.ENDC)

        if menu == 30:
            print(color() + r"""
    \\_//
   __/".
  /__ |
  || ||
⠀""" + bcolors.ENDC)

        if menu == 31:
            print(color() + r"""
               _ 
        ,-----' |
        | //  : |
        | //  : |
        | //  : |
        `-----._|               _
         _/___\_               ||]
   _____[_______]_[~~--         []
  [____________________]       '/
    ||| /          |||  ,___,'./
    ||| \          |||  ______|
    ||| /          ||| I==||
    ||| \          |||  __||__
-----||-/-----------||-o--o---o---
""" + bcolors.ENDC)

        if menu == 32:
            print(color() + r""" ___________________
 | _______________ |
 | |XXXXXXXXXXXXX| |
 | |XXXXXXXXXXXXX| |
 | |XXXXXXXXXXXXX| |
 | |XXXXXXXXXXXXX| |
 | |XXXXXXXXXXXXX| |
 |_________________|
     _[_______]_
 ___[___________]___
|         [_____] []|__
|         [_____] []|  \__
L___________________J     \ \___\/
 ___________________      /\
                         (__)
""" + bcolors.ENDC)

        if menu == 33:
            print(color() + r""" ___________
||         ||            _______
||Africana ||           | _____ |
||         ||           ||_____||
||_________||           |  ___  |
|  + + + +  |           | |___| |
    _|_|_   \           |       |
   (_____)   \          |       |
              \    ___  |       |
       ______  \__/   \_|       |
      |   _  |      _/  |       |
      |  ( ) |     /    |_______|
      |___|__|    /
           \_____/
""" + bcolors.ENDC)

        if menu == 34:
            print(color() + r"""
                        . - ~ ~ ~ - .
      ..     _      .-~               ~-.
     //|     \ `..~                      `.
    || |      }  }              /       \  \
(\   \\ \~^..'                 |         }  \
 \`.-~  o      /       }       |        /    \
 (__          |       /        |       /      `.
  `- - ~ ~ -._|      /_ - ~ ~ ^|      /- _      `.
              |     /          |     /     ~-.     ~- _
              |_____|          |_____|         ~ - . _ _~_-_
""" + bcolors.ENDC)

        if menu == 35:
            print(color() + r"""
   _____
  | ___ |
  ||   || A.F
  ||___||
  |   _ |
  |_____|
 /_/_|_\_\----.
/_/__|__\_\   )
             (
             []
""" + bcolors.ENDC)

        if menu == 36:
            print(color() + r"""
               _,.---.---.---.--.._ 
           _.-' `--.`---.`---'-. _,`--.._
          /`--._ .'.     `.     `,`-.`-._\
         ||   \  `.`---.__`__..-`. ,'`-._/
    _  ,`\ `-._\   \    `.    `_.-`-._,``-.
 ,`   `-_ \/ `-.`--.\    _\_.-'\__.-`-.`-._`.
(_.o> ,--. `._/'--.-`,--`  \_.-'       \`-._ \
 `---'    `._ `---._/__,----`           `-. `-\
           /_, ,  _..-'                    `-._\
           \_, \/ ._(
            \_, \/ ._\
             `._,\/ ._\
               `._// ./`-._
                 `-._-_-_.-'
""" + bcolors.ENDC)

        if menu == 37:
            print(color() + r"""
                         ,.---.   
               ,,,,     /    _ `.
                \\\\   /      \  )
                 |||| /\/``-.__\/
                 ::::/\/_
 {{`-.__.-'(`(^^(^^^(^ 9 `.========='
{{{{{{ { ( ( (  (   (-----:=
 {{.-'~~'-.(,(,,(,,,(__6_.'=========.
                 ::::\/\ 
                 |||| \/\  ,-'/\
                ////   \ `` _/  )
               ''''     \  `   /
                         `---''
""" + bcolors.ENDC)

        if menu == 38:
            print(color() + r"""
       ___________
      |.---------.|
      ||         ||
      ||         ||
      ||         ||
      |'---------'|
       `)__ ____('
       [=== -- o ]--.
     __'---------'__ \
    [::::::::::: :::] )
     `'''''''''' ''`/T\
                    \_/
""" + bcolors.ENDC)

        if menu == 39:
            print(color() + r"""
   .===========.        
   |   |       |        
   |  /|\      |        
   | /A|F\     |        
   |___________|        
   |_________-_|_,-.    
  [_____________]   )   
  .,,,,,,,,,, ,,.  (_   
 /,,,,,,,,,,, ,,,\ (>`\ 
(______.-``-._____) \__)
""" + bcolors.ENDC)

        if menu == 40:
            print(color() + r"""
   The good Shepherd is Jesus.
           __  _
    .-.'  `; `-._  __  _
   (_,         .-:'  `; `-._
 ,'o"(        (_,           )
(__,-'      ,'o"(            )>
   (       (__,-'            )
    `-'._.--._(             )
       |||  |||`-'._.--._.-'
                  |||  |||
""" + bcolors.ENDC)

        if menu == 41:
            print(color() + r"""
             ,.-----__    
          ,:::://///,:::-. 
         /:''/////// ``:::`;/|/
        /'   ||||||     :://'`\
      .' ,   ||||||     `/(  e \
-===~__-'\__X_`````\_____/~`-._ `.
            ~~        ~~       `~-'
""" + bcolors.ENDC)

        if menu == 42:
            print(color() + r"""
  .::::::::..          ..::::::::.
 :::::::::::::        :::::::::::::
:::::::::::' .\      /. `:::::::::::
`::::::::::_,__o    o__,_::::::::::'
""" + bcolors.ENDC)

        if menu == 43:
            print(color() + r"""
.--.
|__| .-------.
|=.| |.-----.|
|--| || A.F ||
|  | |'-----'|
|__|~')_____(' ~)
     [=======] ()
""" + bcolors.ENDC)

        if menu == 44:
            print(color() + r"""
               __
    ..=====.. |==|
    ||     || |= |
 _  ||     || |^*| _
|=| o=,===,=o |__||=|
|_|  _______)~`)  |_|
    [=======]  ()  

""" + bcolors.ENDC)

        if menu == 45:
            print(color() + r"""
           {)          
        c==//\         
   _-~~/-._|_|         
  /'_,/,   //'~~~\;;,  
  `~  _( _||_..\ | ';; 
    /'~|/ ~' `\<\>  ;  
    "  |      /  |     
       "      "  "
""" + bcolors.ENDC)

        if menu == 46:
            print(color() + r"""
  |
  |
  + \
  \\.G_.*=.
   `(#'/.\|
    .>' (_--.
 _=/d   ,^\
~~ \)-'   '
   / |   a:f
  '  '
""" + bcolors.ENDC)

        if menu == 47:
            print(color() + r"""
                            _(\_/) 
                          ,((((^`\
                         ((((  (6 \ 
                       ,((((( ,    \
   ,,,_              ,(((((  /"._  ,`,
  ((((\\ ,...       ,((((   /    `-.-'
  )))  ;'    `"'"'""((((   (      
 (((  /            (((      \
  )) |                      |
 ((  |        .       '     |
 ))  \     _ '      `t   ,.')
 (   |   y;- -,-""'"-.\   \/  
 )   / ./  ) /         `\  \
    |./   ( (           / /'
    ||     \\          //'|
    ||      \\       _//'||
    ||       ))     |_/  ||
    \_\     |_/          ||
    `'"                  \_\ 
""" + bcolors.ENDC)

        if menu == 48:
            print(color() + r"""
       _ ____
     /( ) _   \
    / //   /\` \,  ||--||--||-
      \|   |/  \|  ||--||--||-
~^~^~^~~^~~~^~~^^~^^^^^^^^^^^^
""" + bcolors.ENDC)

        if menu == 49:
            print(color() + r"""
      _
     |-|  __
     |=| [Ll]
     "^" ====`o
             _
       __   |-|
      [Ll]  |=|
      ====`o"^"
      ____
""" + bcolors.ENDC)

        if menu == 50:
            print(color() + r"""
      .
\_____)\_____
/--v____ __`<
        )/
        '
""" + bcolors.ENDC)

        if menu == 51:
            print(color() + r"""
       .
      ":"
    ___:____     |"\/"|
  ,'        `.    \  /
  |  O        \___/  |
~^~^~^~^~^~^~^~^~^~^~^~^~
 __v_
(____\/{
""" + bcolors.ENDC)

        if menu == 52:
            print(color() + r"""
              _         _
  __   ___.--'_`.     .'_`--.___   __
 ( _`.'. -   'o` )   ( 'o`   - .`.'_ )
 _\.'_'      _.-'     `-._      `_`./_
( \`. )    //\`         '/\\    ( .'/ )
 \_`-'`---'\\__,       ,__//`---'`-'_/
  \`        `-\         /-'        '/
   `                               '
""" + bcolors.ENDC)

        if menu == 53:
            print(color() + r"""
            _   _
           (.)_(.)
        _ (   _   ) _
       / \/`-----'\/ \
     __\ ( (     ) ) /__
     )   /\ \._./ /\   (
      )_/ /|\   /|\ \_(
""" + bcolors.ENDC)

        if menu == 54:
            print(color() + r"""                          _______
      ______________     |[_____]|
     |.------------.|    |[_____]|
     ||            ||    |[====o]|
     ||            ||    |[_.--_]|
     ||            ||    |[_____]|
     ||            ||    |      :|
     ||____________||    |      :|
 .==.|""  ......    |.==.|      :|
 |::| '-.________.-' |::||      :|
 |''|  (__________)-.|''||______:|
 `""`_.............._\""`______
    /:::::::::::'':::\`;'-.-.  `\
   /::=========.:.-::"\ \ \--\   \
   \`''''''''''''''''`/  \ \__)   \
    `''''''''''''''''`    '========' 
""" + bcolors.ENDC)

        if menu == 55:
            print(color() + r"""
   .----.
   |C>_ |
 __|____|__
|  ______--|
`-/.::::.\-'a
 `--------'
""" + bcolors.ENDC)

        if menu == 56:
            print(color() + r"""
....._      
 `.   ``-.                               .-----.._
   `,     `-.                          .:      /`
     :       `"..                 ..-``       :
     /   ...--:::`n            n.`::...       :
     `:``      .` ::          /  `.     ``---..:.
       `\    .`  ._:   .-:   ::    `.     .-``
         :  :    :_\\_/: :  .::      `.  /
         : /      \-../:/_.`-`         \ :
         :: _.._  q` p ` /`             \|
         :-`    ``(_. ..-----hh``````/-._:
                     `:      ``     /     `
                     E:            /
                      :          _/
                      :    _..-``
                      l--``
""" + bcolors.ENDC)

        if menu == 57:
            print(color() + r"""
     ___________________________
    |[]                        []|
    |[]                        []|
    |                            |
    |            . .             |
    |          `    _`           |
    |         `  ()|_|`          |
    |         `       `          |
    |          ` . . `           |
    |      ________________      |
    |     |          ____  |     |
    |     |         |    | |     |
    |     |         |    | |     |
    |     |         |    | |     |
    |()   |         |_  _| |   ()|
    |)    |           --   |    (|
    |_____|[]______________|\___/
""" + bcolors.ENDC)

        if menu == 58:
            print(color() + r"""
 ___,___,_______,____
|  :::|///./||'||    \
|  :::|//.//|| || AF) |
|  :::|/.///|!!!|     |
|   _______________   |
|  |:::::::::::::::|  |
|  |_______________|  |
|  |_______________|  |
|  |_______________|  |
|  |_______________|  |
||_|    africana   ||_|
|__|_______________|__|
""" + bcolors.ENDC)

        if menu == 59:
            print(color() + r"""
     ,--.     .--.
    /    \. ./    \
   /  /\/  "  \/\  \
  / _/ /~~~v~~~\ \_ \
 /    /####|####\    \
;  /\{#####|#####}/\  \
|_/  {#####|#####}  \_:
|    {#####|#####}    |
|   /{#####|#####}\   |
|  / {#####|#####} \  |
| /  {#####|#####}  \ |
|  \ \#####|#####/ /  |
|   \ \####|####/ /   |
 \   \ \###|###/ /   /
  \  /   ~~~~~   \  / 
""" + bcolors.ENDC)

        if menu == 60:
            print(color() + r"""
         _______
        |.-----.|
        ||x . x||
        ||_.-._||
        `--)-(--`
       __[=== o]___
      |:::::::::::|\
      `-=========-`()
""" + bcolors.ENDC)

        if menu == 61:
            print(color() + r"""
            a@@@@a             
        a@@@@@@@@@@@@a         
      a@@@@@@by@@@@@@@@a       
    a@@@@@S@C@E@S@W@@@@@@a     
    @@@@@@@@@@@@@@@@@@@@@@     
     `@@@@@@`\\//'@@@@@@'      
          ,,  ||  ,, God is good.
         /(-\ || /.)m          
    ,---' /`-'||`-'\ `----,    
   /( )__))   ||   ((,==( )\   
_ /_//___\\ __|| ___\\ __\\ ____ 
    ``    `` /MM\   ''   ''
""" + bcolors.ENDC)

        if menu == 777:
            print(color() + r"""
                    .-=====-.
                    | .'''. |
                    | |   | |
                    | |   | |
                    | '---' |
                    |       |
                    |       |
 .-================-'       '-================-.
j|  _                                          |
g|.'o\                                    __   |
s| '-.'.                                .'o.`  |
 '-==='.'.=========-.       .-========.'.-'===-'
        '.`'._    .===,     |     _.-' /
          '._ '-./  ,//\   _| _.-'  _.'
             '-.| ,//'  \-'  `   .-'
                `//'_`--;    ;.-'
                  `\._ ;|    |
                     \`-'  . |
                     |_.-'-._|
                     \  _'_  /
                     |; -:- | 
                     || -.- \ 
                     |;     .\
                     / `'\'`\-;
                    ;`   '. `_/
                    |,`-._;  .;
                    `;\  `.-'-;
                     | \   \  |
                     |  `\  \ |
                     |   )  | |
                     |  /  /` /
                     | |  /|  |
                     | | / | /
                     | / |/ /|
                     | \ / / |
                     |  /o | |
                     |  |_/  |
                     |       |
                     |       |
                     |       |
                     |       |
                     |       |
                     |       |
                     |       |
                     '-=====-'
""" + bcolors.ENDC)

beauty = banners()
if ' __name__' == '__main__':
        sys.exit(beauty())
