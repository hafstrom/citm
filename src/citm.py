'''
    HIGH PRIORITY!
o - add more flavour events to lvlfac, like "look man", "look chair", "look", "look machinery", etc.
o - add "look" (describe current scene) to every level
o - Rewrite the "look around" section at the lvl2tw level
o - add "look city" from lvlone

    Medium Priority
o - Make more notes like these to speed up the programming process
o - Create a new and improved storyboard
o - add points for filling canteen, crossing the river for the first time
o - Add in the lvl2vl level
? - Rework the city
o - walk mountains

    low priority
o - rework the tdnc variable and whole "that does not compute" system.
        old tdnc variable has been ripped out completely, as it looks now
        it seems very unnecessary but maybe add it in later?

o - Rework "help" screen
        in its current state it is a bit barren and I think it should be
        specifically tailored to the level your on.

    Finished
x - Add title
x - Add more jokes to the title screen
x - Add starting level
x - Add level select and "cheat"
x - Add "help" screen
x - Add the map
x - Add canteen mechanic
x - Add the city (kind of)
x - Rework the map
x - Add a new level after crossing the river
x - add in lvlfac
x - re-add the box for type "h" for help" and "map available"
x - make a system for earning points
x - add point triggers
x - level select gives incorrect number of points
x - add credits screen

    Storyboard
You spawn in, have to go to the town to get something then go to the city,
once there you realise you needed some item from the village too (if you
didn't already grab it), die, and have to restart. it is a rogue like and
this story is a wip too, have to figure out more stuff and precise details
 
    AFTER GAME IS COMPLETE:
? - Make a "lite" version with graphics removed to improve filesize and
    performance, some visual things might be required, in which case
    just scrap this idea
            this idea is probably not possbile, considering the graphics and
            actually seeing things is important to the gameplay. but it
            probably be technically playable, if not enjoyable

    Legend:
O = still open problem
X = fixed problem
? = possible problem
x?= fixed problem but might need something more added
'''

import time, os
from os import system, name

def clrscr(): # clear screen
    if name == 'nt':
        system('cls')
    else:
        system('clear')

hdmd = 'off)'
bktk = 0

def main(): #mainloop
    global hdmd, crri, rotv, cntn, bktk, cafd, slon, lkmp, pnts, pnsp, pt01, pt02, pt03, pt04, pt05, maan, tiwt, yhwt, made, fity # hdmd = hardmode,   crri = crossed river,  rotv = river or town/village,   cntn = canteen full,   bktk = backtrack (allows for going back to previous levels),   cafd = canteen found,   slon = saloon found,   lkmp = look map,   pnts = points,   pt## = point #,   maan = man angry,   tiwt = times waited,   yhwt = how many times you've waited (in text),   made = man dead,   fity = first try (at stealing chair)

    if bktk == 0:
        crri = 0
        rotv = 0
        cntn = 0
        cafd = 0
        slon = 0
        lkmp = 0
        pnts = 0
        pt01 = 1
        pt02 = 1
        pt03 = 1
        pt04 = 1
        pt05 = 1
        maan = 0
        tiwt = 0
        yhwt = 1
        made = 0
        fity = 0

    def ptsclc(): # ptsclc = points calculation
        global pnts, pnsp

        if len(str(pnts)) == 1:
            pnsp = str(pnts) + '  '

        else:
            pnsp = str(pnts) + ' '
        # this system allows for displaying a maximum of 99 points

    def mainmn(): # main menu
        clrscr()
        print(' ________________________________________________________________________________________________________________')
        print('|                                                                                                                |')
        print('|             .                                                                                    .             |')
        print('|           _/|                                                                                    |\            |')
        print('|          / /|   ___                _   _      _         _   _                 _    _    _ _      | \_          |')
        print('|       __/ | |  / __|__ _ _  _ __ _| |_| |_   (_)_ _    | |_| |_  ___    _ __ (_)__| |__| | |___  | \ \__       |')
        print('|      /   /  | | (__/ _` | || / _` | \' \  _|  | | \' \   |  _| \' \/ -_)  | \'  \| / _` / _` | / -_) |  \'   \      |')
        print('|    _/       |  \___\__,_|\_,_\__, |_||_\__|  |_|_||_|   \__|_||_\___|  |_|_|_|_\__,_\__,_|_\___| | |  \  \_    |')
        print('|   /  /   |  |                |___/                                                               |  \  |   \   |')
        print('|  /  /   /   |                                                                                    |      \   \  |')
        print('|  Made in MMXX by DonTristan                                                                      v. 0.4        |')
        print('|________________________________________________________________________________________________________________|')
        print('|                                                                                                                |')

    def crdscr(): # credit screen
        clrscr()
        print(' ________________________________________________________________________________________________________________')
        print('|                                                                                                                |')
        print('|             .                                                                                    .             |')
        print('|           _/|                                                                                    |\            |')
        print('|          / /|                    _____ _              _                     _                    | \_          |')
        print('|       __/ | |                   |_   _| |_  __ _ _ _ | |__    _  _ ___ _  _| |                   | \ \__       |')
        print('|      /   /  |                <3   | | | \' \/ _` | \' \| / /   | || / _ \ || |_| <3                |  \'   \      |')
        print('|    _/       |                     |_| |_||_\__,_|_||_|_\_\    \_, \___/\_,_(_)                   | |  \  \_    |')
        print('|   /  /   |  |                                                 |__/                               |  \  |   \   |')
        print('|  /  /   /   |                                                                                    |      \   \  |')
        print('|  Made in MMXX by DonTristan                                                                      v. 0.4        |')
        print('|________________________________________________________________________________________________________________|')
        print('|                                                                                                                |')

    def sttplc(): # start place
        global mapa, mapb, mapc, mapd, mape, mapf, mapg, maph, mapi, mapj
        mapa = '  \__ /                                                |'
        mapb = '     \ .-\'                               .             |'
        mapc = '______\_---______________________________|\ ___________|'
        mapd = '-_   _-_                                 | \_          |'
        mape = '_|   |o|_-_                              | \ \__       |'
        mapf = ' | _-_/_|o|                              |  \'   \      |'
        mapg = '\__|o| _-_                               | |  \  \_    |'
        maph = '-_\____|o|                               |  \  |   \   |'
        mapi = 'o|__/                                    |      \   \  |'
        mapj = '                                                       |'
        print(' ________________________________________________________________________________________________________________')
        print('|                                                \ __/    ' + mapa)
        print('|             .                               \'-. /       ' + mapb)
        print('|__________ _/|______________________________---_/________' + mapc)
        print('|          / /|               _          _             _--' + mapd)
        print('|       __/ | |              |o|________|o|____        |__' + mape)
        print('|      /   /  |                   |====        \_______| O' + mapf)
        print('|    _/       |               ====|====                   ' + mapg)
        print('|   /  /   |  |               ====|==--                  _' + maph)
        print('|  /  /   /   |               =-==|  _                   |' + mapi)
        print('|                                  \|o|                   ' + mapj)
        print('|________________________________________________________________________________________________________________|')
        print('|                                                                                                                |')

    def hlfway(): # half way
        global mapa, mapb, mapc, mapd, mape, mapf, mapg, maph, mapi, mapj
        mapa = '  \__ /                                                |'
        mapb = '     \ .-\'                                .            |'
        mapc = '-\'-__ \_--- _---_ ________________________|\_ _________|'
        mapd = '____|       ]\'0\'[                         |  \_        |'
        mape = ']0[ |         |  _---_                    | \_ \       |'
        mapf = '  \_   _-s-_  |__]\'0 [                    |   \ \__    |'
        mapg = '    \'-_]0\'\'[ / _---_                      | |      \   |'
        maph = '      \_____/__]\'0\'[                      | | \' \   \_ |'
        mapi = ' _---_   _/                               |  \   |    \|'
        mapj = ' ] 0\'[__/                                 |       \    |'
        print(' ________________________________________________________________________________________________________________')
        print('|                                                \ __/    ' + mapa)
        print('|       .                                     \'-. /       ' + mapb)
        print('|____ _/|_________ _._ __________ _._ _______---_/_____ __' + mapc)
        print('|    / /|         ] 0 [__________] 0 [_____             |_' + mapd)
        print('| __/ | |                 | ======         \'-___________| ' + mape)
        print('|/    | |          ==-=== | ==.===                        ' + mapf)
        print('|    /  |          ===¤== | ===-==                        ' + mapg)
        print('|       |          ===|== | =-====                        ' + maph)
        print('|/   |  |          =-==== | ==_._                         ' + mapi)
        print('|   /   |          ====-=  \_]\'0 [                        ' + mapj)
        print('|________________________________________________________________________________________________________________|')
        print('|                                                                                                                |')

    def rvrscr(): # river screen
        global mapa, mapb, mapc, mapd, mape, mapf, mapg, maph, mapi, mapj
        mapa = '     .                xXXx            | ._/        .   |'
        mapb = '  o               .            .xX    |.|      .       |'
        mapc = '       .     xCx   .       ____________________________|'
        mapd = '__________________________/        ~                   |'
        mape = '                                -        ~ ~        .  |'
        mapf = '   .    -      ~     .-     .    ~        -            |'
        mapg = '  - -      ~~ -   -          ~  ____________________   |'
        maph = '   ____________________________/      xXCXXxcx      \__|'
        mapi = '__/  xXx.                                              |'
        mapj = '                                        xx             |'
        print(' ________________________________________________________________________________________________________________')
        print('|      .                       |.| |                      ' + mapa)
        print('|                      .       \_ .|     xxCXx   .        ' + mapb)
        print('|          xXcx                  | |              xxX     ' + mapc)
        print('|_______________________           xx.       .          __' + mapd)
        print('|       ~            .  \________________ _ ___________/  ' + mape)
        print('|    ~           ~  ~           -        / \   _      ~~  ' + mapf)
        print('|   .    -     ~            ~     ~ ~       _ / \         ' + mapg)
        print('|__________________  ~  .        ~  ~      / \     . ~    ' + maph)
        print('|                  \______________________________________' + mapi)
        print('|         . .                        .                    ' + mapj)
        print('|________________________________________________________________________________________________________________|')
        print('|                                                                                                                |')

    def dedscr(): # dead screen
        clrscr()
        global bktk
        bktk = 0
        print(' ________________________________________________________________________________________________________________')
        print('|                                            _                      _                                            |')
        print('|                                          _| \      .-""""-.      / ¦_                                          |')
        print('|                                          \__ \__  /        \  __/ __/                                          |')
        print('|           __   _____  _   _ _ ___ ___       \__ \_¦        |_/ __/          ___  ___   _   ___                 |')
        print('|           \ \ / / _ \| | | ( ) _ \ __|         \_ \ x    x / _/            |   \| __| / \ |   \                |')
        print('|            \ V / (_) | |_| |/|   / _|           -\'/   .|   \\\'-             | |) | _| / A \| |) |               |')
        print('|             |_| \___/ \___/  |_|_\___|       __/ _\_      _/_ \__          |___/|___/_/ \_\___/                |')
        print('|                                          ___/ __/   |¦||||   \__ \___                                          |')
        print('|                                         /_  _/      \||¦|/      \_  _\                                         |')
        print('|                                           |/                      \|                                           |')
        print('|________________________________________________________________________________________________________________|')
        print('|                                                                                                                |')

    def twnscr(): # town screen
        global mapa, mapb, mapc, mapd, mape, mapf, mapg, maph, mapi, mapj
        mapa = '                        _                              |'
        mapb = '-___                  _| |                             |'
        mapc = '| ¤|           .     | |.|_          .                 |'
        mapd = '|  |___---___        | | | |                           |'
        mape = '    |¤ |-|  |        \_  |.|    \'       xx             |'
        mapf = '____|  |-|  |          | ._/     ,                     |'
        mapg = '__---___      x        | |             .               |'
        maph = '¤ |-| ¤|         ,  xXX                                |'
        mapi = '  |-|  |                                   xXxx,       |'
        mapj = 'x             X                  .                     |'
        print(' ________________________________________________________________________________________________________________')
        print('|                                                         ' + mapa)
        print('|         .             _         __.--\'--.__        ___--' + mapb)
        print('|                     _|.|    ,   | ¤  ¤  ¤ |  .xXCx |¤ |-' + mapc)
        print('|              ,     |.| |        |_________|    .   |  |-' + mapd)
        print('|    .    .#x,       | |.|        | ¤ |-| ¤ | ___-S-___  |' + mape)
        print('|         #&#=       \_. |    .Xx |   |-|   | || | ¤¤¤|  |' + mapf)
        print('|         -X#-.. _,  .x| |Xc            \_____||-|_   | /_' + mapg)
        print('|    .#+.     xC                         ___---___ \___/ |' + maph)
        print('|    %#X#.  .                 xxX        |  |-| ¤|  \____|' + mapi)
        print('|    -##-_.,. _. ,  .       .            |  |-|  |____/   ' + mapj)
        print('|________________________________________________________________________________________________________________|')
        print('|                                                                                                                |')

    def hlpscr(): # help screen
        clrscr()
        print(' ________________________________________________________________________________________________________________')
        print('|                                            ____      ____      ____                                            |')
        print('|                                           /    \    /    \    /    \                                           |')
        print('|                   _    _      _          |  /\  |  |  /\  |  |  /\  |    _    _      _                         |')
        print('|                  | |  | |    | |         |_|  | |  |_|  | |  |_|  | |   | |  | |    | |                        |')
        print('|                  | |__| | ___| |_ __         /  |      /  |      /  |   | |__| | ___| |_ __                    |')
        print('|                  |  __  |/ _ \ | \'_ \       /  /      /  /      /  /    |  __  |/ _ \ | \'_ \                   |')
        print('|                  | |  | |  __/ | |_) |     |__/      |__/      |__/     | |  | |  __/ | |_) |                  |')
        print('|                  |_|  |_|\___|_| .__/       __        __        __      |_|  |_|\___|_| .__/                   |')
        print('|                                | |         |  |      |  |      |  |                   | |                      |')
        print('|                                |_|         |__|      |__|      |__|                   |_|                      |')
        print('|________________________________________________________________________________________________________________|')
        print('|                                                                                                                |')
        print('| Type "h" or "?" or "help" to bring up this window                                                              |')
        print('| Type "look" to look around or type "look" then something to look at that thing specifically                    |')
        print('| Type "walk" then a location to walk there if possible                                                          |')
        print('| This window is currently WIP                                 ___________________ _________________ ____________|')
        print('|_____________________________________________________________| Help screen open  | Map unavailable | Pnts = ' + pnsp + ' |')
        print('                                                              |___________________|_________________|____________|')
        input(' Press ENTER to continue: ')

    def facscr(): # factory screen
        clrscr()
        global mapa, mapb, mapc, mapd, mape, mapf, mapg, maph, mapi, mapj
        mapa = '| \______       \ /    \   _/                        | |'
        mapb = ' \_____  \       [     _]_/. ___ .  . ___ .  . ___ . | |'
        mapc = ' _     \  |       \  _/     |   |    |   |    |   |  | |'
        mapd = '| \____/  |        \/       |___|    |___|    |___|  | |'
        mape = ' \_______/          |      \'     \'  \'     \'  \'     \' | |'
        mapf = ' _ _ _ _ _ _ _ _ _ _ ] _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ | |'
        mapg = '                    /                                | |'
        maph = '                    |                                | |'
        mapi = '        x  .                 , #                       |'
        mapj = '                  #               .              .     |'
        print(' ________________________________________________________________________________________________________________')
        print('|          |.  |   .|    |    |       ___________         ' + mapa)
        print('|          | \'   .  |    |    |      |           |        ' + mapb)
        print('|          \___    .|    |\   |      |           |        ' + mapc)
        print('|              |.   |    | \  |      |           |        ' + mapd)
        print('|       xX     |  . |       \ |      |   _____   |        ' + mape)
        print('|                            \|_ _ _ |  |____]|  | _ _ _ _' + mapf)
        print('|            ,                |      |         *\'|        ' + mapg)
        print('|                .            |      |           |        ' + maph)
        print('|                       x                      ,          ' + mapi)
        print('|                              .                          ' + mapj)
        print('|________________________________________________________________________________________________________________|')
        print('|                                                                                                                |')

    def facins():
        clrscr()
        global mapa, mapb, mapc, mapd, mape, mapf, mapg, maph, mapi, mapj
        mapa = '           ||    |                    ___----___       |'
        mapb = '           ||    |   _______.        /__----__ /|      |'
        mapc = '      <   _||    |\'" _____./|       |  _____  |||      |'
        mapd = '  _,.-|^\'"_|     |\'"      | |       | | ___ | |||      |'
        mape = ' /_,.-=^\'"          .||.  |/| _____ | | |_| | ||| _____|'
        mapf = '||          _____  | [] | | |_ _ _ _|_|_ _ _|_|_|_ _ _ |'
        mapg = '||  |  |   |o o x|  \'--\'  |/_/_/_/_/_/_/_/_/_/_/_/_/_/_|'
        maph = '||  *  *   |x x o|        || o o o o o o o o o o o o o |'
        mapi = '|           """""         ||                 .         |'
        mapj = '                        .                       .      |'
        print(' ________________________________________________________________________________________________________________')
        print('|     _.-^\'|   |                                          ' + mapa)
        print('|_.-^\'     |   |                                          ' + mapb)
        print('|          |   |                        ______            ' + mapc)
        print('|          |   |                       |      |           ' + mapd)
        print('|          |   |_____________________  |______| __________' + mape)
        print('|          |  /                     . /______/|           ' + mapf)
        print('|          | /          -         .   ||     ||     -     ' + mapg)
        print('|          |/                         |      |            ' + maph)
        print('|          |        .        -                    .       ' + mapi)
        print('|          |                           .                  ' + mapj)
        print('|__________|_____________________________________________________________________________________________________|')
        print('|                                                                                                                |')

    def aririv(): # arrived at river
        clrscr()
        rvrscr()
        global rotv, pt01, pnts, bktk

        if pt01:
            pnts = pnts + 1
            pt01 = 0
            ptsclc()

        if rotv:
            print('| There is a river in the way.                                                                                   |')

        else:
            print('| You arrive at the river.                                                                                       |')

        print('| 1. Attempt to cross the river                                                                                  |')

        if cafd:
            print('| 2. Fill your canteen at the river                                                                              |')

        else:
            print('| 2. ???? ???? ??????? ?? ??? ?????                                                                              |')

        print('| 3. Leave                                                     ___________________ _________________ ____________|')
        print('|_____________________________________________________________| Type "h" for help |  Map available  | Pnts = ' + pnsp + ' |')
        print('                                                              |___________________|_________________|____________|')
        answ = input(' > ')
        answ = answ.lower()

        if answ == '1' or answ == 'one' or answ == 'attempt to cross the river' or answ == 'cross the river' or answ == 'cross river':

            def rivded(): # river dead
                dedscr()
                print('| Congratulations! You are dead.                                                                                 |')
                print('| The rock you jumped on was loose and gave in under your feet. You feel off and hit your head on the riverbed   |')
                print('| causing you to slowly bleed out over the course of an hour.                                                    |')
                print('| Thank you for playing Caught in the middle!                  ___________________ _________________ ____________|')
                print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                print('                                                              |___________________|_________________|____________|')
                input(' Press ENTER to restart: ')
                main()

            def rivsur(): # river survived
                global crri, pt05, pnts
                clrscr()

                if crri:
                    sttplc()
                    crri = 0

                else:
                    hlfway()
                    crri = 1

                if pt05:
                    pnts = pnts + 1
                    pt05 = 0
                    ptsclc()

                print('| You crossed the river successfully                                                                             |')
                print('|                                                                                                                |')
                print('|                                                                                                                |')
                print('|                                                              ___________________ _________________ ____________|')
                print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                print('                                                              |___________________|_________________|____________|')

                input(' Press ENTER to continue: ')

            def rivatc(): # river attempt crossing
                global bktk
                clrscr()
                rvrscr()
                print('| 1. Jump on to the first rock                                                                                   |')
                print('| 2. Jump on to the second rock                                                                                  |')
                print('| 3. Jump on to the third rock                                                                                   |')
                print('| 4. Jump over the rocks to the other riverbank                ___________________ _________________ ____________|')
                print('|_____________________________________________________________| Type "h" for help |  Map available  | Pnts = ' + pnsp + ' |')
                print('                                                              |___________________|_________________|____________|')
                answ = input(' Write a number: ')
                answ = answ.lower()

                if answ == '1' or answ == 'one' or answ == '3' or answ == 'three':
                    rivded()

                elif answ == '2' or answ == 'two':

                    if hdmd == 'off)':
                        rivsur()

                    else:
                        rivded()

                elif answ == '4' or answ == 'four':
                    rivsur()

                elif answ == 'leave' or answ == 'cancel':
                    lvlone()

                elif answ == 'exit' or answ == 'exit game' or answ == 'stop game':
                    bktk = 0
                    main()

                elif answ == 'help' or answ == 'please help' or answ == '?' or answ == 'h':
                    hlpscr()
                    rivatc()

                elif answ == 'look map' or answ == 'look at map' or answ == 'look at the map' or answ == 'use map' or answ == 'use the map' or answ == 'map':
                    ingmap()
                    rivatc()

                else:
                    rivatc()

            rivatc()

        elif answ == '2' or answ == 'two' or answ == 'fill canteen' or answ == 'fill the canteen':
            if cafd:
                global cntn
                clrscr()
                rvrscr()

                if cntn:
                    print('| Your canteen is already full                                                                                   |')
                    print('|                                                                                                                |')
                    print('|                                                                                                                |')
                    print('|                                                              ___________________ _________________ ____________|')
                    print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                    print('                                                              |___________________|_________________|____________|')
                    input(' Press ENTER to continue: ')
                    aririv()

                else:
                    pnts = pnts + 1
                    ptsclc()

                    print('| You quench your thirst at the river and then proceed to fill your canteen                                      |')
                    print('|                                                                                                                |')
                    print('|                                                                                                                |')
                    print('|                                                              ___________________ _________________ ____________|')
                    print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                    print('                                                              |___________________|_________________|____________|')
                    cntn = 1
                    input(' Press ENTER to continue: ')
                    aririv()  

            else:
                aririv()

        elif answ == '3' or answ == 'three' or answ == 'leave':
            lvlone()
        
        elif answ == 'look map' or answ == 'look at map' or answ == 'look at the map' or answ == 'use map' or answ == 'use the map' or answ == 'map':
            ingmap()
            aririv()

        elif answ == 'help' or answ == 'please help' or answ == '?' or answ == 'h':
            hlpscr()
            aririv()

        elif answ == 'exit' or answ == 'exit game' or answ == 'stop game':
            bktk = 0
            main()

        else:
            aririv()

    def ingmap(): # in-game map
        global lkmp
        clrscr()
        print(' ________________________________________________________________________________________________________________')
        print('|  __  |                           |                     |' + mapa)
        print('| / _\ |                           | Map Legend:         |' + mapb)
        print('| \__/ |  .               .        | OO = City           |' + mapc)
        print('|______| /|   x____O      |\     _/| O = Town            |' + mapd)
        print('|                              _/  | x = Village         |' + mape)
        print('|        _ --- _            _-\'    | .                   |' + mapf)
        print('|     _-\'        \_        /    _--| |\ = Mountain       |' + mapg)
        print('|  _-\'          W  \      /    /   | Full line = Road    |' + maph)
        print('|-\' OO              \'-_ _-----\'    | Dotted line = River |' + mapi)
        print('|                            \'-_--_| W = Where I woke up |' + mapj)
        print('|__________________________________|_____________________|_______________________________________________________|')
        print('|                                                                                                                |')

        if lkmp:
            print('| You take the map out of your pocket and unfurl it.                                                             |')
            print('|                                                                                                                |')
            print('|                                                                                                                |')

        else:
            print('| You take the map out of your pocket and unfurl it. In one of the map\'s corners there\'s a legend. From looking  |')
            print('| at your surroundings you are able to point out precisely where you woke up and you write a "W" there to mark   |')
            print('| that position. You also have a compass which is pointing north                                                 |')
            lkmp = 1

        print('|                                                              ___________________ _________________ ____________|')
        print('|_____________________________________________________________| Help unavailable  |    Map open     | Pnts = ' + pnsp + ' |')
        print('                                                              |___________________|_________________|____________|')
        input(' Press ENTER to continue: ')

    def sttmen(): # start menu

        def lvlsel(): # level select
            global bktk, cntn, cafd, crri, pt01, pt02, pt03, pt05, pnts
            clrscr()
            mainmn()
            print('| Welcome to the Level Select! Choose level to go to:                                                            |')
            print('| 1. Start   2. Town   3. Saloon/Factory                                                                         |')
            print('|                                                                                                                |')
            print('|                                                                                       _________________________|')
            print('|______________________________________________________________________________________| Type "cancel" to cancel |')
            print('                                                                                       |_________________________|')
            answ = input(' > ')
            answ = answ.lower()

            if answ == '1' or answ == 'start':
                bktk = 1
                pnts = 0
                ptsclc()
                main()

            elif answ == '2' or answ == 'town':
                cntn = 1
                bktk = 2
                cafd = 1
                crri = 1
                pt01 = 0
                pt02 = 0
                pt05 = 0
                pnts = 4
                ptsclc()
                main()

            elif answ == '3' or answ == 'saloon' or answ == 'factory':
                cntn = 1
                cafd = 1
                crri = 1
                bktk = 4
                pt01 = 0
                pt02 = 0
                pt03 = 0
                pt05 = 0
                pnts = 5
                ptsclc()
                main()

            elif answ == 'cancel':
                clrscr()
                sttmen()

            else:
                lvlsel()

        global bktk
        mainmn()
        print('| 1. Play                                                5. About the developer                                  |')
        print('| 2. Info                                                6. Credits and a special thanks                         |')
        print('| 3. Settings (Hardmode is', hdmd, '                         7. Exit                                                 |')
        print('| 4. Level Select                                                                                                |')
        print('|________________________________________________________________________________________________________________|')
        print()
        answ = input(' Write a number: ')
        answ = answ.lower()

        if answ == '1' or answ == 'one':
            bktk = 1
            ptsclc()
            clrscr()

        elif answ == '2' or answ == 'two':
            mainmn()
            print('| Caught in the middle is a text adventure game inspired by early 80\'s games like Space Quest and Monkey Island, |')
            print('| but with my own personal twist on it. Here\'s quick tip on how to win:                                          |')
            print('|                                                                                                                |')
            print('| *Don\'t* die!                                                                                                   |')
            print('|________________________________________________________________________________________________________________|')
            print()
            input(' Press ENTER to continue: ')
            clrscr()
            sttmen()

        elif answ == '3' or answ == 'three':

            def tohdmd(): # turn on hdmd
                global hdmd
                mainmn()

                if hdmd == 'off)':
                    print('| Turn on hardmode?                                                                                              |')

                else:
                    print('| Turn off hardmode?                                                                                             |')

                print('|                                                                                                                |')
                print('|                                                                                                                |')
                print('|                                                                                                                |')
                print('|________________________________________________________________________________________________________________|')
                print()
                answ = input(' y/n: ')
                answ = answ.lower()

                if answ == 'y' or answ == 'yes':
                    if hdmd == 'off)':
                        hdmd = 'on) '

                    else:
                        hdmd = 'off)'

                    clrscr()
                    sttmen()

                elif answ == 'n' or answ == 'no':
                    if hdmd == 'off)':
                        hdmd = 'off)'

                    else:
                        hdmd = 'on) '

                    clrscr()
                    sttmen()

                else:
                    tohdmd()

            tohdmd()

        elif answ == '4' or answ == 'four':
            mainmn()
            print('| Please enter the password                                                                                      |')
            print('|                                                                                                                |')
            print('|                                                                                                                |')
            print('|                                                                                                                |')
            print('|________________________________________________________________________________________________________________|')
            print()
            password = input(' > ')

            if password == 'un1cornBallz':
                lvlsel()

            else:
                clrscr()
                mainmn()
                print('| Incorrect Password                                                                                             |')
                print('|                                                                                                                |')
                print('|                                                                                                                |')
                print('|                                                                                                                |')
                print('|________________________________________________________________________________________________________________|')
                print()
                input(' Press ENTER to continue: ')
                sttmen()

        elif answ == '5' or answ == 'five':
            mainmn()
            print('| Hi! I am DonTristan, the developer of this game. Thank you so much for installing it. The development of this  |')
            print('| game started with me not doing what I was supposed to do in school and ended up with what you see now. It has  |')
            print('| been a labour of love and I\'ve pulled out my hair at every step but in the end, I believe it was all worth it. |')
            print('| If you wish to support me further you can visit my website at http://dontristan.com/, thank you!               |')
            print('|________________________________________________________________________________________________________________|')
            print()
            input(' Press ENTER to continue: ')
            clrscr()
            sttmen()

        elif answ == '6' or answ == 'six':
            crdscr()
            print('|                                                    Credits                                                     |')
            print('|                                                                                                                |')
            print('| · Code by:                 DonTristan (with help from friends)                                                 |')
            print('| · Original artwork by:     DonTristan                                                                          |')
            print('| · Original game idea by:   DonTristan                                                                          |')
            print('|                                                                                                                |')
            print('|                                                                                                                |')
            print('|                                            A special thanks goes to                                            |')
            print('|                                                                                                                |')
            print('| · Edward Smale and "GantonStepfire" for helping me with coding, motivation, and also for being great friends   |')
            print('| · Google for teaching me how to code                                                                           |')
            print('| · My other friends and family for being great people                                                           |')
            print('| · My cat Ninja for being an amazing pet                                                                        |')
            print('| · http://patorjk.com/ for his amazing Text to ASCII Art generator (that\'s the large letters you see)           |')
            print('|                                                                                                                |')
            print('| And lastly, you, for playing my game :) <3                                                                     |')
            print('|                                                                                                                |')
            print('|                                                                                                                |')
            print('| © Tristan Hafström, 2020. All rights reserved.                                                                 |')
            print('|________________________________________________________________________________________________________________|')
            print()
            input(' Press ENTER to continue: ')
            clrscr()
            sttmen()

        elif answ == '7' or answ == 'seven' or answ == 'exit' or answ == 'exit game':
            exit()

        elif answ == 'cheat':
            lvlsel() 

        else:
            clrscr()
            sttmen()

    if bktk == 0:
        sttmen()

    def lvlone(): # level one
        global lv, cafd, bktk
        clrscr()

        if crri:
            hlfway()

        else:
            sttplc()

        if cntn:
            print('| The sun is setting                                                                                             |')
            print('|                                                                                                                |')

        else:
            print('| You feel parched,                                                                                              |')
            print('| The sun is setting                                                                                             |')
    
        print('|                                                                                                                |')
        print('|                                                              ___________________ _________________ ____________|')
        print('|_____________________________________________________________| Type "h" for help |  Map available  | Pnts = ' + pnsp + ' |')
        print('                                                              |___________________|_________________|____________|')
        answ = input(' > ')
        answ = answ.lower()

        if answ == 'look' or answ == 'look around' or answ == 'look town' or answ == 'look at town' or answ == 'look at the town' or answ == 'look village' or answ == 'look at village' or answ == 'look at the village':
            clrscr()

            if crri:
                hlfway()

            else:
                sttplc()

            print('| You are in the middle of a desert. In front of you you see a town. The town is made up of several smaller      |')
            print('| houses and one larger house. To the left of the town you see a small village consisting of some smaller huts   |')
            print('| and crop fields. To either side of both the town and the small village there are two mountains                 |')
            print('|                                                              ___________________ _________________ ____________|')
            print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
            print('                                                              |___________________|_________________|____________|')
            input(' Press ENTER to continue: ')
            lvlone()

        elif answ == 'help' or answ == 'please help' or answ == '?' or answ == 'h':
            hlpscr()
            lvlone()

        elif answ == 'look sun' or answ == 'look at the sun' or answ == 'look at sun' or answ == 'look horizon' or answ == 'look at horizon' or answ == 'look at the horizon':
            clrscr()

            if crri:
                hlfway()

            else:
                sttplc()

            print('| The sun is setting. It is now somewhere between red and orange in colour. The sky itself has become slightly   |')
            print('| orange, then pink before turning dark blue and then to black. There are no clouds to be seen anywhere          |')
            print('|                                                                                                                |')
            print('|                                                              ___________________ _________________ ____________|')
            print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
            print('                                                              |___________________|_________________|____________|')
            input(' Press ENTER to continue: ')
            lvlone()

        elif answ == 'look self' or answ == 'look me' or answ == 'look at self':
            clrscr()

            if crri:
                hlfway()

            else:
                sttplc()
            
            if cafd:
                global pt04, pnts

                if pt04:
                    pnts = pnts + 1
                    pt04 = 0
                    ptsclc()

                print('| You narcissist.                                                                                                |')
                print('|                                                                                                                |')
                print('|                                                                                                                |')
                print('|                                                              ___________________ _________________ ____________|')
                print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                print('                                                              |___________________|_________________|____________|')
                input(' Press ENTER to continue: ')
                lvlone()

            else:
                cafd = 1
                print('| You look at yourself and audibly say "hell yeah". After this self flattery you notice a map, and a canteen on  |')
                print('| your hip that you had completely forgotten about                                                               |')
                print('|                                                                                                                |')
                print('|                                                              ___________________ _________________ ____________|')
                print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                print('                                                              |___________________|_________________|____________|')
                input(' Press ENTER to continue: ')
                lvlone()

        elif answ == 'look canteen' or answ == 'drink canteen' or answ == 'look at canteen' or answ == 'look flask' or answ == 'drink from canteen' or answ == 'drink flask' or answ == 'drink from flask' or answ == 'drink from canteen' or answ == 'use canteen' or answ == 'use the canteen' or answ == 'use flask' or answ == 'use the flask':
            clrscr()

            if crri:
                hlfway()

            else:
                sttplc()

            if cafd:
                print('| You take the canteen from your hip and notice immediately that it feels very light. You cross your fingers as  |')
                print('| you peer inside. You find that it is completely dried up. Your feel even more parched now than before          |')

            else:
                cafd = 1
                print('| You find a canteen on your hip. You immediately notice that it feels very light. you cross your fingers as you |')
                print('| peer inside. You find that it is completely dried up. Your feel even more parched now than before              |')
           
            print('|                                                                                                                |')
            print('|                                                              ___________________ _________________ ____________|')
            print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
            print('                                                              |___________________|_________________|____________|')
            input(' Press ENTER to continue: ')
            lvlone()

        elif answ == 'look mountain' or answ == 'look at mountain' or answ == 'look at the mountain' or answ == 'look mountains' or answ == 'look at mountains' or answ == 'look at the mountains':
            clrscr()

            if crri:
                hlfway()

            else:
                sttplc()

            print('| You gaze over at the mountains. They both have a sudden drop right after the peak. You take a moment to wonder |')
            print('| if the may have once been one whole mountain                                                                   |')
            print('|                                                                                                                |')
            print('|                                                              ___________________ _________________ ____________|')
            print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
            print('                                                              |___________________|_________________|____________|')
            input(' Press ENTER to continue: ')
            lvlone()

        elif answ == 'look map' or answ == 'look at map' or answ == 'look at my map' or answ == 'use map' or answ == 'use the map' or answ == 'map':
            ingmap()
            lvlone()

        elif answ == 'exit' or answ == 'exit game' or answ == 'stop game':
            bktk = 0
            main()

        # needs a rework for continuity, actually add the city level when it comes to that
        elif answ == 'walk city' or answ == 'walk to city' or answ == 'walk to the city':
            global rotv

            if crri:
                rotv = 1
                aririv()

            dedscr()
            print('| Congratulations! You are dead.                                                                                 |')

            if cntn:
                print('| Even with your water from your canteen it was not enough and you died from thirst on your way to the city.     |')

            else:
                print('| You died from thirst on your way to the city.                                                                  |')

            print('| Thank you for playing Caught in the middle!                                                                    |')
            print('|                                                              ___________________ _________________ ____________|')
            print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
            print('                                                              |___________________|_________________|____________|')
            input(' Press ENTER to restart: ')
            main()

        # this system is actually quite smart, I might still change it though just for conformity's sake
        elif answ == 'walk town' or answ == 'walk to the town' or answ == 'walk to town' or answ == 'walk river' or answ == 'walk to river' or answ == 'walk to the river' or answ == 'walk village' or answ == 'walk to the village' or answ == 'walk to village':
            if 'town' in str(answ):
                rotv = 1
                clrscr()

                if crri:
                    bktk = 2
                    main()

                else:
                    aririv()
                    bktk = 2
                    main()

            elif 'river' in str(answ):
                rotv = 0
                aririv()
                bktk = 1
                main()
                
            else:

                rotv = 1
                clrscr()

                if crri:
                    bktk = 3
                    main()

                else:
                    aririv()
                    bktk = 3
                    main()

        else:
            lvlone()

    if bktk == 1:
        lvlone()

    def lvl2tw(): # level two town
        global bktk, cntn, slon, rotv

        # the whole saloon thing is interesting to me because you need to wait around for the password, else you won't be able to progress in a later part
        # I haven't decided when that is yet but it's gonna be a surprise, you will need the password >:)
        def lvlfac(): # level factory
            global pt03, pnts, slon, maan, bktk, made

            def lvlins(): # level inside
                global made, fity, bktk, maan
                facins()

                if made:
                    print('| You bust through the door, breaking the lock and sending the door flying into the wall. As you do you hear a   |')
                    print('| loud yell. You look behind the door and find out you\'ve impaled a small gross man on the door handle. Inside   |')
                    print('| there are multiple pieces of heavy machinery too large to move along the walls. There is also a single chair   |')
                    
                else:
                    print('| The man opens the door, letting you in. Along the walls there are multiple pieces of heavy machinery too large |')
                    print('| too large to move and in the middle of the room you find a single chair                                        |')
                    print('|                                                                                                                |')

                print('|                                      _______________________ ___________________ _________________ ____________|')
                print('|_____________________________________| Type "leave" to leave | Type "h" for help |  Map available  | Pnts = ' + pnsp + ' |')
                print('                                      |_______________________|___________________|_________________|____________|')
                answ = input(' > ')
                answ = answ.lower()

                if answ == 'take chair' or answ == 'take the chair' or answ == 'steal chair' or answ == 'steal the chair':
                    if made:
                        facins()
                        print('| Out of respect for deceased, you decide to not steal the chair                                                 |')
                        print('|                                                                                                                |')
                        print('|                                                                                                                |')
                        print('|                                                              ___________________ _________________ ____________|')
                        print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                        print('                                                              |___________________|_________________|____________|')
                        input(' Press ENTER to continue: ')
                        lvlins()

                    else:
                        if fity:
                            facins()
                            maan = 1
                            print('| You try again to go grab the chair, this time the surprisingly strong man runs up to you and drags outside     |')
                            print('|                                                                                                                |')
                            print('|                                                                                                                |')
                            print('|                                                              ___________________ _________________ ____________|')
                            print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                            print('                                                              |___________________|_________________|____________|')
                            input(' Press ENTER to continue: ')
                            lvlfac()

                        else:
                            facins()
                            fity = 1
                            print('| You go up to grab the chair but the man yells at you, startling you and making you stop                        |')
                            print('|                                                                                                                |')
                            print('|                                                                                                                |')
                            print('|                                                              ___________________ _________________ ____________|')
                            print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                            print('                                                              |___________________|_________________|____________|')
                            input(' Press ENTER to continue: ')
                            lvlins()
                    
                elif answ == 'take machinery' or answ == 'take the machinery' or answ == 'take machine' or answ == 'take the machine' or answ == 'take heavy machinery' or answ == 'take the heavy machinery' or answ == 'take heavy machine' or answ == 'take the heavy machine':
                    facins()
                    print('| The machinery is far to heavy to move.                                                                         |')
                    print('|                                                                                                                |')
                    print('|                                                                                                                |')
                    print('|                                                              ___________________ _________________ ____________|')
                    print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                    print('                                                              |___________________|_________________|____________|')
                    input(' Press ENTER to continue: ')
                    lvlins()

                elif answ == 'leave':
                    lvlfac()

                elif answ == 'exit':
                    bktk = 0
                    main()

                else:
                    lvlins()

            if pt03:
                pnts = pnts + 1
                pt03 = 0
                ptsclc()

            facscr()

            if slon:
                print('| You go to the factory and try to open the door but it\'s locked                                                 |')
            
            else:
                print('| You got what you thought was a saloon, only to find out it\'s actually a factory. The door is locked            |')
                slon = 1

            print('| 1. Knock                                                                                                       |')
            print('| 2. Wait around                                                                                                 |')
            print('| 3. Force open                        _______________________ ___________________ _________________ ____________|')
            print('|_____________________________________| Type "leave" to leave | Type "h" for help |  Map available  | Pnts = ' + pnsp + ' |')
            print('                                      |_______________________|___________________|_________________|____________|')
            answ = input(' Write a number: ')
            answ = answ.lower()

            if answ == '1' or answ == 'knock' or answ == 'knock on door':
                if maan:
                    facscr()
                    print('| The man opens the slit. He then immediately closes it again.                                                   |')
                    print('|                                                                                                                |')
                    print('|                                                                                                                |')
                    print('|                                                              ___________________ _________________ ____________|')
                    print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                    print('                                                              |___________________|_________________|____________|')
                    input(' Press ENTER to continue: ')
                    lvlfac()

                elif made:
                    facscr()
                    print('| There\'s no need to knock seeing as the door is busted from your forced entry. For other, related reasons, you  |')
                    print('| do not want to go in there again                                                                               |')
                    print('|                                                                                                                |')
                    print('|                                                              ___________________ _________________ ____________|')
                    print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                    print('                                                              |___________________|_________________|____________|')
                    input(' > ')
                    lvlfac()

                else:
                    facscr()
                    print('| A person opens a slit in the door at about stomach level. You hunch down to eye level and then the little      |')
                    print('| person asks you "Gneeble gloober?"                                                                             |')
                    print('|                                                                                                                |')
                    print('|                                                              ___________________ _________________ ____________|')
                    print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                    print('                                                              |___________________|_________________|____________|')
                    answ = input(' > ')
                    answ = answ.lower()

                    if answ == 'knarkle':
                        lvlins()

                    else:
                        facscr()
                        print('| The man shakes his head, then closes the slit again                                                            |')
                        print('|                                                                                                                |')
                        print('|                                                                                                                |')
                        print('|                                                              ___________________ _________________ ____________|')
                        print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                        print('                                                              |___________________|_________________|____________|')
                        input(' Press ENTER to continue: ')
                        lvlfac()

            elif answ == '2' or answ == 'wait' or answ == 'wait around':
                global tiwt

                if tiwt == 0:
                    facscr()
                    tiwt = 1
                    print('| You wait around.                                                                                               |')
                    print('| Nothing happens                                                                                                |')
                    print('|                                                                                                                |')
                    print('|                                                              ___________________ _________________ ____________|')
                    print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                    print('                                                              |___________________|_________________|____________|')
                    input(' Press ENTER to continue: ')
                    lvlfac()
                
                elif tiwt == 1 and made:
                    tiwt = 2
                    facscr()
                    print('| You decide to keep waiting. This time a short woman appears. She knocks on the door, and when she gets no      |')
                    print('| response she decides to leave                                                                                  |')
                    print('|                                                                                                                |')
                    print('|                                                              ___________________ _________________ ____________|')
                    print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                    print('                                                              |___________________|_________________|____________|')
                    input(' Press ENTER to continue: ')
                    lvlfac()

                elif tiwt == 1:
                    tiwt = 2
                    facscr()
                    print('| You decide to keep waiting. This time a short woman appears and a slit in the door opens. You overhear her     |')
                    print('| saying "knarkle". What could that mean?                                                                        |')
                    print('|                                                                                                                |')
                    print('|                                                              ___________________ _________________ ____________|')
                    print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                    print('                                                              |___________________|_________________|____________|')
                    input(' Press ENTER to continue: ')
                    lvlfac()

                else:
                    tiwt = tiwt + 1

                    if len(str(tiwt)) == 1:
                        yhwt = str(tiwt) + ' times.  '

                    elif len(str(tiwt)) == 2:
                        yhwt = str(tiwt) + ' times. '

                    else:
                        yhwt = str(tiwt) + ' times.'

                    facscr()
                    print('| You decide to keep waiting.                                                                                    |')
                    print('| Nothing happens                                                                                                |')
                    print('|                                                                                                                |')
                    print('| You have waited ' + yhwt + '                                   ___________________ _________________ ____________|')
                    print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                    print('                                                              |___________________|_________________|____________|')
                    input(' Press ENTER to continue: ')
                    lvlfac()

            elif answ == '3' or answ == 'force door' or answ == 'force open' or answ == 'force open door':
                made = 1
                lvlins()

            elif answ == 'leave':
                clrscr() 

            elif answ == 'help' or answ == 'please help' or answ == '?' or answ == 'h':
                hlpscr()
                lvlfac()     

            elif answ == 'look map' or answ == 'look at map' or answ == 'look at the map' or answ == 'use map' or answ == 'use the map' or answ == 'map':
                ingmap()
                lvlfac()

            elif answ == 'exit' or answ == 'exit game' or answ == 'stop game':
                bktk = 0
                main()

            else:
                lvlfac()

        if bktk == 4:
            lvlfac()

        if cntn:
            global pt02, pnts

            if pt02:
                pnts = pnts + 1
                pt02 = 0
                ptsclc()

            clrscr()
            twnscr()

            print('| You arrive at the town. The large building appears to be the town hall. There are also multiple residential    |')

            if slon:
                print('| buildings and what you previously thought to be a saloon.                                                      |')

            else:
                print('| buildings and a saloon                                                                                         |')

            print('|                                                                                                                |')
            print('|                                                              ___________________ _________________ ____________|')
            print('|_____________________________________________________________| Type "h" for help |  Map available  | Pnts = ' + pnsp + ' |')
            print('                                                              |___________________|_________________|____________|')

            answ = input(' > ')
            answ = answ.lower()

            if answ == 'lick cactus' or answ == 'lick the cactus' or answ == 'lick a cactus':
                dedscr()
                print('| Congratulations! You are dead.                                                                                 |')
                print('| You died from shoving your face in a cactus.                                                                   |')
                print('| Thank you for playing Caught in the middle!                                                                    |')
                print('|                                                              ___________________ _________________ ____________|')
                print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                print('                                                              |___________________|_________________|____________|')
                input(' Press ENTER to restart: ')
                main()

            elif answ == 'look cactus' or answ == 'look cacti' or answ == 'look at cactus' or answ == 'look at the cactus' or answ == 'look at cacti' or answ == 'look at the cacti':
                clrscr()
                twnscr()
                print('| There are multiple cacti scattered around the town. They look both larger and spinier than any other cacti     |')
                print('| you\'ve seen before                                                                                             |')
                print('|                                                                                                                |')
                print('|                                                              ___________________ _________________ ____________|')
                print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                print('                                                              |___________________|_________________|____________|')
                input(' Press ENTER to continue: ')
                lvl2tw()

            elif answ == 'help' or answ == 'please help' or answ == '?' or answ == 'h':
                hlpscr()
                lvl2tw()

            elif answ == 'look' or answ == 'look around' or answ == 'look surroundings':
                clrscr()
                twnscr()
                print('| You find yourself in a small town in the desert. You tried reading the name of the town from a sign you saw    |')
                print('| when you first entered, but you couldn\'t seem to understand the language. There are multiple houses around     |')

                if slon:
                    print('| the town including a town hall and a factory                                                                   |')

                else:
                    print('| the town including a town hall and what looks like a saloon                                                    |')

                print('|                                                              ___________________ _________________ ____________|')
                print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                print('                                                              |___________________|_________________|____________|')
                input(' Press ENTER to continue: ')
                lvl2tw()

            elif answ == 'look saloon' or answ == 'look at saloon' or answ == 'look at the saloon' or answ == 'look bar' or answ == 'look at bar' or answ == 'look at the bar' or answ == 'look factory' or answ == 'look at factory' or answ == 'look at the factory':
                clrscr()
                twnscr()

                if slon:
                    print('| You look at the factory.                                                                                       |')

                else:
                    print('| You look at what you assumed to be a saloon, only to find out it looks to be some sort of factory.             |')

                print('| Through the windows you see heavy machinery, but no workers                                                    |')
                print('|                                                                                                                |')
                print('|                                                              ___________________ _________________ ____________|')
                print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                print('                                                              |___________________|_________________|____________|')
                slon = 1
                input(' Press ENTER to continue: ')
                lvl2tw()

            elif answ == 'walk saloon' or answ == 'walk to saloon' or answ == 'walk to the saloon' or answ == 'walk factory' or answ == 'walk to factory' or answ == 'walk to the factory':
                lvlfac()

            elif answ == 'look map' or answ == 'look at map' or answ == 'look at the map' or answ == 'use map' or answ == 'use the map' or answ == 'map':
                ingmap()
                lvl2tw()

            elif answ == 'exit' or answ == 'exit game' or answ == 'stop game':
                bktk = 0
                main()

            elif answ == 'walk river' or answ == 'walk to river' or answ == 'walk to the river':
                rotv = 0
                aririv()

            elif answ == 'walk plain' or answ == 'walk to plain' or answ == 'walk to the plain' or answ == 'walk plains' or answ == 'walk to plains' or answ == 'walk to the plains' or answ == 'walk desert' or answ == 'walk to desert' or answ == 'walk to the desert' or answ == 'leave' or answ == 'leave town':
                bktk = 1
                main()

            else:
                clrscr()
                lvl2tw()

        else:
            dedscr()
            print('| Congratulations! You are dead.                                                                                 |')
            print('| You died from thirst on your way to the town.                                                                  |')
            print('| Thank you for playing Caught in the middle!                                                                    |')
            print('|                                                              ___________________ _________________ ____________|')
            print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
            print('                                                              |___________________|_________________|____________|')
            input(' Press ENTER to restart: ')
            main()

    if bktk == 2 or bktk == 4:
        lvl2tw()

    def lvl2vl(): # level two village
        global bktk
        clrscr()
        twnscr()
        print('| The village is currently WIP                                                                                   |')
        print('|                                                                                                                |')
        print('|                                                                                                                |')
        print('|                                                              ___________________ _________________ ____________|')
        print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
        print('                                                              |___________________|_________________|____________|')
        input(' Press ENTER to restart: ')
        bktk = 0
        main()
 
    if bktk == 3:
        lvl2vl()
main()