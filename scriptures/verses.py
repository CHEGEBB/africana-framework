import random
from src.core.bcolors import *

class bible_verse(object):
    def __init__(self):
        pass

    def verses(self):
        verse = random.randrange(0, 105)
        if verse == 0:
            print(bcolors.GREEN + "  ~[ " + color() + " God saw the light, that it was good: & God divided the " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Gen.1:4  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 1:
            print(bcolors.GREEN + "  ~[ " + color() + "   I will bless thee…  and thou shalt be a blessing    " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Gen.12:2 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 2:
            print(bcolors.GREEN + "  ~[ " + color() + "    I am thy shield, and thy exceeding great reward    " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Gen.15:1 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 3:
            print(bcolors.GREEN + "  ~[ " + color() + "Fear ye not stand still & see the salvation of the LORD" + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ex.14:13 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 4:
            print(bcolors.GREEN + "  ~[ " + color() + "      I will make all My goodness pass before thee     " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ex.33:19 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 5:
            print(bcolors.GREEN + "  ~[ " + color() + "           The LORD God, merciful and gracious         " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ex.34:6  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 6:
            print(bcolors.GREEN + "  ~[ " + color() + "              I set my tabernacle among you            " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Lev.26:11" + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 7:
            print(bcolors.GREEN + "  ~[ " + color() + "      I will walk among you, and will be your God      " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Lev.26:12" + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 8:
            print(bcolors.GREEN + "  ~[ " + color() + "     The LORD is longsuffering, and of great mercy     " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Num.14:18" + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 9:
            print(bcolors.GREEN + "  ~[ " + color() + " Thou shalt love the LORD thy God with all thine heart " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Deut.6:5 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 10:
            print(bcolors.GREEN + "  ~[ " + color() + " Shall ye lay up these my words in your heart & in you " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Deu.11:18" + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 11:
            print(bcolors.GREEN + "  ~[ " + color() + "       Thou shalt rejoice before the LORD thy God      " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Deu.12:18" + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 12:
            print(bcolors.GREEN + "  ~[ " + color() + " Blessed shalt thou be in the city & blessed shalt thou " + bcolors.GREEN + "]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Deut.28:3" + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 13:
            print(bcolors.GREEN + "  ~[ " + color() + " Blessed shall be the fruit of thy body & the fruit of " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Deut.28:4" + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 14:
            print(bcolors.GREEN + "  ~[ " + color() + "        Blessed shall be thy basket and thy store      " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Deut.28:5" + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 15:
            print(bcolors.GREEN + "  ~[ " + color() + " Blessed shalt thou be when thou comest in, & blessed s" + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Deut.28:6" + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 16:
            print(bcolors.GREEN + "  ~[ " + color() + " They shall come out against thee one way and flee befo" + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Deut.28:7" + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 17:
            print(bcolors.GREEN + "  ~[ " + color() + " And the LORD shall make thee the head, & not the tail " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Deu.28:13" + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 18:
            print(bcolors.GREEN + "  ~[ " + color() + " Be strong & of a good courage fear not nor be afraid  " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Deut.31:6" + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 19:
            print(bcolors.GREEN + "  ~[ " + color() + "        I will not fail thee, nor forsake thee         " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Josh.1:5 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 20:
            print(bcolors.GREEN + "  ~[ " + color() + "        Only be thou strong and very courageous        " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Josh.1:7 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC) 
        if verse == 21:
            print(bcolors.GREEN + "  ~[ " + color() + " This Book of the Law shall not depart out of thy mout " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Josh.1:8 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC) 
        if verse == 22:
            print(bcolors.GREEN + "  ~[ " + color() + " Have not I commanded thee? Be strong & of a good cour " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Josh.1:9 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC) 
        if verse == 23:
            print(bcolors.GREEN + "  ~[ " + color() + " Be not afraid neither be thou dismayed: for the LORD  " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Josh.1:9 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC) 
        if verse == 24:
            print(bcolors.GREEN + "  ~[ " + color() + " Sanctify yourselves: for to morrow the LORD will do w " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Josh.3:5 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC) 
        if verse == 25:
            print(bcolors.GREEN + "  ~[ " + color() + "   The LORD your God, He it is that fighteth for you   " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Jos.23:10" + bcolors.YELLOW + "   ]~" + bcolors.ENDC) 
        if verse == 26:
            print(bcolors.GREEN + "  ~[ " + color() + "            Nay; but we will serve the LORD!           " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Jos.24:21" + bcolors.YELLOW + "   ]~" + bcolors.ENDC) 
        if verse == 27:
            print(bcolors.GREEN + "  ~[ " + color() + "         I will never break my covenant with you       " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Judg.2:1 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC) 
        if verse == 28:
            print(bcolors.GREEN + "  ~[ " + color() + " Them that love him be as the sun when he goeth forth  " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Judg.5:31" + bcolors.YELLOW + "   ]~" + bcolors.ENDC) 
        if verse == 29:
            print(bcolors.GREEN + "  ~[ " + color() + "   Thy people shall be my people, and thy God my God   " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ruth 1:16" + bcolors.YELLOW + "   ]~" + bcolors.ENDC) 
        if verse == 30:
            print(bcolors.GREEN + "  ~[ " + color() + "           He will keep the feet of His saints         " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "1Sam.2:9 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC) 
        if verse == 31:
            print(bcolors.GREEN + "  ~[ " + color() + " Only fear the LORD, and serve Him in truth with all y " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Sam.12:24" + bcolors.YELLOW + "   ]~" + bcolors.ENDC) 
        if verse == 32:
            print(bcolors.GREEN + "  ~[ " + color() + "           I will shew thee what thou shalt do         " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "1Sam.16:3" + bcolors.YELLOW + "   ]~" + bcolors.ENDC) 
        if verse == 33:
            print(bcolors.GREEN + "  ~[ " + color() + " Man looketh on the outward appearance, but the LORD.. " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "1Sam.16:7" + bcolors.YELLOW + "   ]~" + bcolors.ENDC) 
        if verse == 34:
            print(bcolors.GREEN + "  ~[ " + color() + "    Yet he hath made with me an everlasting covenant   " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "2Sam.23:5" + bcolors.YELLOW + "   ]~" + bcolors.ENDC) 
        if verse == 35:
            print(bcolors.GREEN + "  ~[ " + color() + "   Give therefore thy servant an understanding heart   " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "1Kin.3:9 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC) 
        if verse == 36:
            print(bcolors.GREEN + "  ~[ " + color() + "  The LORD your God ye shall fear; & he shall deliver  " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "2Ki.17:39" + bcolors.YELLOW + "   ]~" + bcolors.ENDC) 
        if verse == 37:
            print(bcolors.GREEN + "  ~[ " + color() + " Serve Him with a perfect heart & with a willing mind  " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "1Chr.28:9" + bcolors.YELLOW + "   ]~" + bcolors.ENDC) 
        if verse == 38:
            print(bcolors.GREEN + "  ~[ " + color() + "   The LORD searcheth all hearts, & understandeth all   " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "1Chr.28:9" + bcolors.YELLOW + "   ]~" + bcolors.ENDC) 
        if verse == 39:
            print(bcolors.GREEN + "  ~[ " + color() + "       If thou seek him, he will be found of thee      " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "1Chr.28:9" + bcolors.YELLOW + "   ]~" + bcolors.ENDC) 
        if verse == 40:
            print(bcolors.GREEN + "  ~[ " + color() + "   The LORD is able to give thee much more than this   " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "2Chr.25:9" + bcolors.YELLOW + "   ]~" + bcolors.ENDC) 
        if verse == 41:
            print(bcolors.GREEN + "  ~[ " + color() + " Will not turn away His face from you, if ye return un " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "2Chr.30:9" + bcolors.YELLOW + "   ]~" + bcolors.ENDC) 
        if verse == 42:
            print(bcolors.GREEN + "  ~[ " + color() + "      He did it with all his heart, and prospered      " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "2Ch.31:21" + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 43:
            print(bcolors.GREEN + "  ~[ " + color() + " The hand of our God is upon all them for good that se " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ezdr 8:22" + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 44:
            print(bcolors.GREEN + "  ~[ " + color() + "           The joy of the LORD is your strength        " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Neh.8:10 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 45:
            print(bcolors.GREEN + "  ~[ " + color() + " & who knoweth whether thou art come to the kingdom for" + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Esth.4:14" + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 46:
            print(bcolors.GREEN + "  ~[ " + color() + " Till he fill thy mouth with laughing & thy lips with  " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Job 8:21 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 47:
            print(bcolors.GREEN + "  ~[ " + color() + "              I know that my redeemer liveth           " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Job 19:25" + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 48:
            print(bcolors.GREEN + "  ~[ " + color() + " Blessed is the man that walketh not in the counsel of " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.1:1   " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 49:
            print(bcolors.GREEN + "  ~[ " + color() + "       The LORD knoweth the way of the righteous       " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.1:6   " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 50:
            print(bcolors.GREEN + "  ~[ " + color() + "  Serve the LORD with fear, and rejoice with trembling " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.2:11  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 51:
            print(bcolors.GREEN + "  ~[ " + color() + "    Blessed are all they that put their trust in Him   " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.2:12  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 52:
            print(bcolors.GREEN + "  ~[ " + color() + "    But thou, O LORD, art a shield for me, my glory    " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.3:3   " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 53:
            print(bcolors.GREEN + "  ~[ " + color() + "          Lead me, O LORD, in thy righteousness        " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.5:8   " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 54:
            print(bcolors.GREEN + "  ~[ " + color() + "         For thou, LORD, wilt bless the righteous      " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.5:12  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 55:
            print(bcolors.GREEN + "  ~[ " + color() + "        For the righteous God trieth the hearts        " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.7:9   " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 56:
            print(bcolors.GREEN + "  ~[ " + color() + "    I will praise thee, O LORD, with my whole heart    " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.9:1   " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 57:
            print(bcolors.GREEN + "  ~[ " + color() + " For thou, LORD, hast not forsaken them that seek Thee " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.9:10  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 58:
            print(bcolors.GREEN + "  ~[ " + color() + "            The LORD is King for ever and ever         " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.10:16 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 59:
            print(bcolors.GREEN + "  ~[ " + color() + "    LORD, thou hast heard the desire of the humble     " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.10:17 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 60:
            print(bcolors.GREEN + "  ~[ " + color() + " The LORD is the portion of mine inheritance and of my " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.16:5  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 61:
            print(bcolors.GREEN + "  ~[ " + color() + "            Hide me under the shadow of thy wings      " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.17:8  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 62:
            print(bcolors.GREEN + "  ~[ " + color() + "          I will love thee, O LORD, my strength         " + bcolors.GREEN + "]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.18:1  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 63:
            print(bcolors.GREEN + "  ~[ " + color() + "   The LORD is my rock,my fortress, and my deliverer   " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.18:2  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 64:
            print(bcolors.GREEN + "  ~[ " + color() + "              For thou wilt light my candle            " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.18:28 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 65:
            print(bcolors.GREEN + "  ~[ " + color() + "       The LORD my God will enlighten my darkness      " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.18:28 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 66:
            print(bcolors.GREEN + "  ~[ " + color() + "         It is God that girdeth me with strength       " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.18:32 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 67:
            print(bcolors.GREEN + "  ~[ " + color() + "        The LORD liveth; and blessed be my rock        " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.18:46 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 68:
            print(bcolors.GREEN + "  ~[ " + color() + "         Let the God of my salvation be exalted        " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.18:46 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 69:
            print(bcolors.GREEN + "  ~[ " + color() + " The heavens declare the glory of God; & the firmament " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.19:1  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 70:
            print(bcolors.GREEN + "  ~[ " + color() + "  The law of the LORD is perfect, converting the soul  " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.19:7  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 71:
            print(bcolors.GREEN + "  ~[ " + color() + " The testimony of the LORD is sure making wise the sim " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.19:7  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 72:
            print(bcolors.GREEN + "  ~[ " + color() + " The statutes of the LORD are right rejoicing the hear " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.19:8  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 73:
            print(bcolors.GREEN + "  ~[ " + color() + " The commandment of the LORD is pure, enlightening the " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.19:8  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 74:
            print(bcolors.GREEN + "  ~[ " + color() + "    The fear of the LORD is clean, enduring for ever   " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.19:9  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 75:
            print(bcolors.GREEN + "  ~[ " + color() + " The judgments of the LORD are true & righteous altoge " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.19:9  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 76:
            print(bcolors.GREEN + "  ~[ " + color() + " Some trust in chariots, & some in horses: but we will " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.20:7  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 77:
            print(bcolors.GREEN + "  ~[ " + color() + "        They shall praise the LORD that seek Him       " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.22:26 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 78:
            print(bcolors.GREEN + "  ~[ " + color() + "  All the ends of the world shall remember & turn unto " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.22:27 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 79:
            print(bcolors.GREEN + "  ~[ " + color() + "                 A seed shall serve Him                " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.22:30 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 80:
            print(bcolors.GREEN + "  ~[ " + color() + "        The LORD is my shepherd; I shall not want      " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.23:1  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 81:
            print(bcolors.GREEN + "  ~[ " + color() + " The LORD strong and mighty, the LORD mighty in battle " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.24:8  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 82:
            print(bcolors.GREEN + "  ~[ " + color() + "   O my God, I trust in Thee: let me not be ashamed    " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.25:2  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 83:
            print(bcolors.GREEN + "  ~[ " + color() + "       Shew me thy ways, O LORD; teach me Thy paths.   " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.25:4  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 84:
            print(bcolors.GREEN + "  ~[ " + color() + " Good & upright is the LORD: therefore will He teach s " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.25:8  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 85:
            print(bcolors.GREEN + "  ~[ " + color() + "   The secret of the LORD is with them that fear Him   " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.25:14 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 86:
            print(bcolors.GREEN + "  ~[ " + color() + " Mine eyes are ever toward the LORD for He shall pluck " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.25:15 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 87:
            print(bcolors.GREEN + "  ~[ " + color() + "                 Teach me Thy way, O LORD              " + bcolors.GREEN + " ]~ " + color() +  "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps 27:11 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 88:
            print(bcolors.GREEN + "  ~[ " + color() + " Wait on the LORD: be of good courage, and He shall st " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.27:14 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 89:
            print(bcolors.GREEN + "  ~[ " + color() + "           The LORD is my strength and my shield       " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.28:7  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 90:
            print(bcolors.GREEN + "  ~[ " + color() + "        My heart trusted in Him, and I am helped       " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.28:7  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 91:
            print(bcolors.GREEN + "  ~[ " + color() + " The voice of the LORD is powerful the voice of the LOR " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.29:4  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 92:
            print(bcolors.GREEN + "  ~[ " + color() + "      The LORD will give strength unto His people      " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.29:11 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 93:
            print(bcolors.GREEN + "  ~[ " + color() + "       The LORD will bless his people with peace       " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.29:11 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 94:
            print(bcolors.GREEN + "  ~[ " + color() + "                  In his favour is life              " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.30:5  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 95:
            print(bcolors.GREEN + "  ~[ " + color() + " Be of good courage and he shall strengthen your heart " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.31:24 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 96:
            print(bcolors.GREEN + "  ~[ " + color() + "     Blessed is he whose transgression is forgiven     " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.32:1  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 97:
            print(bcolors.GREEN + "  ~[ " + color() + " I will instruct thee and teach thee in the way which  " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.32:8  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 98:
            print(bcolors.GREEN + "  ~[ " + color() + " He that trusteth in the LORD, mercy shall compass him " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.32:10 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 99:
            print(bcolors.GREEN + "  ~[ " + color() + "              Be glad in the LORD, and rejoice         " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.32:11 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 100:
            print(bcolors.GREEN + "  ~[ " + color() + " For the word of the LORD is right; and all His works  " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.33:4  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 101:
            print(bcolors.GREEN + "  ~[ " + color() + "      The earth is full of the goodness of the LORD    " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.33:5  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 102:
            print(bcolors.GREEN + "  ~[ " + color() + " Our soul waiteth for the LORD: He is our help and our s" + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.33:20 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 103:
            print(bcolors.GREEN + "  ~[ " + color() + "       They looked unto Him, and were lightened        " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.34:5  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 104:
            print(bcolors.GREEN + "  ~[ " + color() + "         O taste and see that the LORD is good         " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.34:8  " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
        if verse == 105:
            print(bcolors.GREEN + "  ~[ " + color() + " They that seek the LORD shall not want any good thing " + bcolors.GREEN + " ]~ " + color() + "\n\n                        " + bcolors.YELLOW + "~[   " + color() + "Ps.34:10 " + bcolors.YELLOW + "   ]~" + bcolors.ENDC)
scriptures = bible_verse()
if ' __name__' == '__main__':
        sys.exit(scriptures())
