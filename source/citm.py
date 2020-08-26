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

def main():
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

    def manmen(): # main menu
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
        global ma, mb, mc, md, me, mf, mg, mh, mi, mj
        ma = '  \__ /                                                |'
        mb = '     \ .-\'                               .             |'
        mc = '______\_---______________________________|\ ___________|'
        md = '-_   _-_                                 | \_          |'
        me = '_|   |o|_-_                              | \ \__       |'
        mf = ' | _-_/_|o|                              |  \'   \      |'
        mg = '\__|o| _-_                               | |  \  \_    |'
        mh = '-_\____|o|                               |  \  |   \   |'
        mi = 'o|__/                                    |      \   \  |'
        mj = '                                                       |'
        print(' ________________________________________________________________________________________________________________')
        print('|                                                \ __/    ' + ma)
        print('|             .                               \'-. /       ' + mb)
        print('|__________ _/|______________________________---_/________' + mc)
        print('|          / /|               _          _             _--' + md)
        print('|       __/ | |              |o|________|o|____        |__' + me)
        print('|      /   /  |                   |====        \_______| O' + mf)
        print('|    _/       |               ====|====                   ' + mg)
        print('|   /  /   |  |               ====|==--                  _' + mh)
        print('|  /  /   /   |               =-==|  _                   |' + mi)
        print('|                                  \|o|                   ' + mj)
        print('|________________________________________________________________________________________________________________|')
        print('|                                                                                                                |')

    def hlfway(): # half way
        global ma, mb, mc, md, me, mf, mg, mh, mi, mj
        ma = '  \__ /                                                |'
        mb = '     \ .-\'                                .            |'
        mc = '-\'-__ \_--- _---_ ________________________|\_ _________|'
        md = '____|       ]\'0\'[                         |  \_        |'
        me = ']0[ |         |  _---_                    | \_ \       |'
        mf = '  \_   _---_  |__]\'0 [                    |   \ \__    |'
        mg = '    \'-_]\'0\'[ / _---_                      | |      \   |'
        mh = '      \_____/__]\'0\'[                      | | \' \   \_ |'
        mi = ' _---_   _/                               |  \   |    \|'
        mj = ' ] 0\'[__/                                 |       \    |'
        print(' ________________________________________________________________________________________________________________')
        print('|                                                \ __/    ' + ma)
        print('|       .                                     \'-. /       ' + mb)
        print('|____ _/|_________ _._ __________ _._ _______---_/_____ __' + mc)
        print('|    / /|         ] 0 [__________] 0 [_____             |_' + md)
        print('| __/ | |                 | ======         \'-___________| ' + me)
        print('|/    | |          ==-=== | ==.===                        ' + mf)
        print('|    /  |          ===¤== | ===-==                        ' + mg)
        print('|       |          ===|== | =-====                        ' + mh)
        print('|/   |  |          =-==== | ==_._                         ' + mi)
        print('|   /   |          ====-=  \_]\'0 [                        ' + mj)
        print('|________________________________________________________________________________________________________________|')
        print('|                                                                                                                |')

    def rvrscr(): # river screen
        global ma, mb, mc, md, me, mf, mg, mh, mi, mj
        ma = '     .                xXXx            | ._/        .   |'
        mb = '  o               .            .xX    |.|      .       |'
        mc = '       .     xCx   .       ____________________________|'
        md = '__________________________/        ~                   |'
        me = '                                -        ~ ~        .  |'
        mf = '   .    -      ~     .-     .    ~        -            |'
        mg = '  - -      ~~ -   -          ~  ____________________   |'
        mh = '   ____________________________/      xXCXXxcx      \__|'
        mi = '__/  xXx.                                              |'
        mj = '                                        xx             |'
        print(' ________________________________________________________________________________________________________________')
        print('|      .                       |.| |                      ' + ma)
        print('|                      .       \_ .|     xxCXx   .        ' + mb)
        print('|          xXcx                  | |              xxX     ' + mc)
        print('|_______________________           xx.       .          __' + md)
        print('|       ~            .  \________________ _ ___________/  ' + me)
        print('|    ~           ~  ~           -        / \   _      ~~  ' + mf)
        print('|   .    -     ~            ~     ~ ~       _ / \         ' + mg)
        print('|__________________  ~  .        ~  ~      / \     . ~    ' + mh)
        print('|                  \______________________________________' + mi)
        print('|         . .                        .                    ' + mj)
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
        global ma, mb, mc, md, me, mf, mg, mh, mi, mj
        ma = '                        _                              |'
        mb = '-___                  _| |                             |'
        mc = '| ¤|           .     | |.|_          .                 |'
        md = '|  |___---___        | | | |                           |'
        me = '    |¤ |-|  |        \_  |.|    \'       xx             |'
        mf = '____|  |-|  |          | ._/     ,                     |'
        mg = '__---___      x        | |             .               |'
        mh = '¤ |-| ¤|         ,  xXX                                |'
        mi = '  |-|  |                                   xXxx,       |'
        mj = 'x             X                  .                     |'
        print(' ________________________________________________________________________________________________________________')
        print('|                                                         ' + ma)
        print('|         .             _         __.--\'--.__        ___--' + mb)
        print('|                     _|.|    ,   | ¤  ¤  ¤ |  .xXCx |¤ |-' + mc)
        print('|              ,     |.| |        |_________|    .   |  |-' + md)
        print('|    .    .#x,       | |.|        | ¤ |-| ¤ | ___-S-___  |' + me)
        print('|         #&#=       \_. |    .Xx |   |-|   | || | ¤ ¤|  |' + mf)
        print('|         -X#-.. _,  .x| |Xc            \_____||-|_   | /_' + mg)
        print('|    .#+.     xC                         ___---___ \___/ |' + mh)
        print('|    %#X#.  .                 xxX        |  |-| ¤|  \____|' + mi)
        print('|    -##-_.,. _. ,  .       .            |  |-|  |____/   ' + mj)
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
        global ma, mb, mc, md, me, mf, mg, mh, mi, mj
        ma = '| \______       \ /    \   _/                        | |'
        mb = ' \_____  \       [     _]_/. ___ .  . ___ .  . ___ . | |'
        mc = ' _     \  |       \  _/     |   |    |   |    |   |  | |'
        md = '| \____/  |        \/       |___|    |___|    |___|  | |'
        me = ' \_______/          |      \'     \'  \'     \'  \'     \' | |'
        mf = ' _ _ _ _ _ _ _ _ _ _ ] _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ | |'
        mg = '                    /                                | |'
        mh = '                    |                                | |'
        mi = '        x  .                 , #                       |'
        mj = '                  #               .              .     |'
        print(' ________________________________________________________________________________________________________________')
        print('|          |.  |   .|    |    |       ___________         ' + ma)
        print('|          | \'   .  |    |    |      |           |        ' + mb)
        print('|          \___    .|    |\   |      |           |        ' + mc)
        print('|              |.   |    | \  |      |           |        ' + md)
        print('|       xX     |  . |       \ |      |   _____   |        ' + me)
        print('|                            \|_ _ _ |  |____]|  | _ _ _ _' + mf)
        print('|            ,                |      |         *\'|        ' + mg)
        print('|                .            |      |           |        ' + mh)
        print('|                       x                      ,          ' + mi)
        print('|                              .                          ' + mj)
        print('|________________________________________________________________________________________________________________|')
        print('|                                                                                                                |')

    def facins():
        clrscr()
        global ma, mb, mc, md, me, mf, mg, mh, mi, mj
        ma = '           ||    |                    ___----___       |'
        mb = '           ||    |   _______.        /__----__ /|      |'
        mc = '      <   _||    |\'" _____./|       |  _____  |||      |'
        md = '  _,.-|^\'"_|     |\'"      | |       | | ___ | |||      |'
        me = ' /_,.-=^\'"          .||.  |/| _____ | | |_| | ||| _____|'
        mf = '||          _____  | [] | | |_ _ _ _|_|_ _ _|_|_|_ _ _ |'
        mg = '||  |  |   |o o x|  \'--\'  |/_/_/_/_/_/_/_/_/_/_/_/_/_/_|'
        mh = '||  *  *   |x x o|        || o o o o o o o o o o o o o |'
        mi = '|           """""         ||                 .         |'
        mj = '                        .                       .      |'
        print(' ________________________________________________________________________________________________________________')
        print('|     _.-^\'|   |                                          ' + ma)
        print('|_.-^\'     |   |                                          ' + mb)
        print('|          |   |                        ______            ' + mc)
        print('|          |   |                       |      |           ' + md)
        print('|          |   |_____________________  |______| __________' + me)
        print('|          |  /                     . /______/|           ' + mf)
        print('|          | /          -         .   ||     ||     -     ' + mg)
        print('|          |/                         |      |            ' + mh)
        print('|          |        .        -                    .       ' + mi)
        print('|          |                           .                  ' + mj)
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
        a = input(' > ')
        a = a.lower()

        if a == '1' or a == 'one' or a == 'attempt to cross the river' or a == 'cross the river' or a == 'cross river':

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
                a = input(' Write a number: ')
                a = a.lower()

                if a == '1' or a == 'one' or a == '3' or a == 'three':
                    rivded()

                elif a == '2' or a == 'two':

                    if hdmd == 'off)':
                        rivsur()

                    else:
                        rivded()

                elif a == '4' or a == 'four':
                    rivsur()

                elif a == 'leave' or a == 'cancel':
                    lvlone()

                elif a == 'exit' or a == 'exit game' or a == 'stop game':
                    bktk = 0
                    main()

                elif a == 'help' or a == 'please help' or a == '?' or a == 'h':
                    hlpscr()
                    rivatc()

                elif a == 'look map' or a == 'look at map' or a == 'look at the map' or a == 'use map' or a == 'use the map' or a == 'map':
                    ingmap()
                    rivatc()

                else:
                    rivatc()

            rivatc()

        elif a == '2' or a == 'two' or a == 'fill canteen' or a == 'fill the canteen':
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

        elif a == '3' or a == 'three' or a == 'leave':
            lvlone()
        
        elif a == 'look map' or a == 'look at map' or a == 'look at the map' or a == 'use map' or a == 'use the map' or a == 'map':
            ingmap()
            aririv()

        elif a == 'help' or a == 'please help' or a == '?' or a == 'h':
            hlpscr()
            aririv()

        elif a == 'exit' or a == 'exit game' or a == 'stop game':
            bktk = 0
            main()

        else:
            aririv()

    def ingmap(): # in-game map
        global lkmp
        clrscr()
        print(' ________________________________________________________________________________________________________________')
        print('|  __  |                           |                     |' + ma)
        print('| / _\ |                           | Map Legend:         |' + mb)
        print('| \__/ |  .               .        | OO = City           |' + mc)
        print('|______| /|   x____O      |\     _/| O = Town            |' + md)
        print('|                              _/  | x = Village         |' + me)
        print('|        _ --- _            _-\'    | .                   |' + mf)
        print('|     _-\'        \_        /    _--| |\ = Mountain       |' + mg)
        print('|  _-\'          W  \      /    /   | Full line = Road    |' + mh)
        print('|-\' OO              \'-_ _-----\'    | Dotted line = River |' + mi)
        print('|                            \'-_--_| W = Where I woke up |' + mj)
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
            manmen()
            print('| Welcome to the Level Select! Choose level to go to:                                                            |')
            print('| 1. Start   2. Town   3. Saloon/Factory                                                                         |')
            print('|                                                                                                                |')
            print('|                                                                                       _________________________|')
            print('|______________________________________________________________________________________| Type "cancel" to cancel |')
            print('                                                                                       |_________________________|')
            a = input(' > ')
            a = a.lower()

            if a == '1' or a == 'start':
                bktk = 1
                pnts = 0
                ptsclc()
                main()

            elif a == '2' or a == 'town':
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

            elif a == '3' or a == 'saloon' or a == 'factory':
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

            elif a == 'cancel':
                clrscr()
                sttmen()

            else:
                lvlsel()

        global bktk
        manmen()
        print('| 1. Play                                                5. About the developer                                  |')
        print('| 2. Info                                                6. Credits and a special thanks                         |')
        print('| 3. Settings (Hardmode is', hdmd, '                         7. Exit                                                 |')
        print('| 4. Level Select                                                                                                |')
        print('|________________________________________________________________________________________________________________|')
        print()
        a = input(' Write a number: ')
        a = a.lower()

        if a == '1' or a == 'one':
            bktk = 1
            ptsclc()
            clrscr()

        elif a == '2' or a == 'two':
            manmen()
            print('| Caught in the middle is a text adventure game inspired by early 80\'s games like Space Quest and Monkey Island, |')
            print('| but with my own personal twist on it. Here\'s quick tip on how to win:                                          |')
            print('|                                                                                                                |')
            print('| *Don\'t* die!                                                                                                   |')
            print('|________________________________________________________________________________________________________________|')
            print()
            input(' Press ENTER to continue: ')
            clrscr()
            sttmen()

        elif a == '3' or a == 'three':

            def tohdmd(): # turn on hdmd
                global hdmd
                manmen()

                if hdmd == 'off)':
                    print('| Turn on hardmode?                                                                                              |')

                else:
                    print('| Turn off hardmode?                                                                                             |')

                print('|                                                                                                                |')
                print('|                                                                                                                |')
                print('|                                                                                                                |')
                print('|________________________________________________________________________________________________________________|')
                print()
                a = input(' y/n: ')
                a = a.lower()

                if a == 'y' or a == 'yes':
                    if hdmd == 'off)':
                        hdmd = 'on) '

                    else:
                        hdmd = 'off)'

                    clrscr()
                    sttmen()

                elif a == 'n' or a == 'no':
                    if hdmd == 'off)':
                        hdmd = 'off)'

                    else:
                        hdmd = 'on) '

                    clrscr()
                    sttmen()

                else:
                    tohdmd()

            tohdmd()

        elif a == '4' or a == 'four':
            manmen()
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
                manmen()
                print('| Incorrect Password                                                                                             |')
                print('|                                                                                                                |')
                print('|                                                                                                                |')
                print('|                                                                                                                |')
                print('|________________________________________________________________________________________________________________|')
                print()
                input(' Press ENTER to continue: ')
                sttmen()

        elif a == '5' or a == 'five':
            manmen()
            print('| Hi! I am DonTristan, the developer of this game. Thank you so much for installing it. The development of this  |')
            print('| game started with me not doing what I was supposed to do in school and ended up with what you see now. It has  |')
            print('| been a labour of love and I\'ve pulled out my hair at every step but in the end, I believe it was all worth it. |')
            print('| If you wish to support me further you can visit my website at http://dontristan.com/, thank you!               |')
            print('|________________________________________________________________________________________________________________|')
            print()
            input(' Press ENTER to continue: ')
            clrscr()
            sttmen()

        elif a == '6' or a == 'six':
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

        elif a == '7' or a == 'seven' or a == 'exit' or a == 'exit game':
            clrscr()
            exit()

        elif a == 'cheat':
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
        a = input(' > ')
        a = a.lower()

        if a == 'look' or a == 'look around' or a == 'look town' or a == 'look at town' or a == 'look at the town' or a == 'look village' or a == 'look at village' or a == 'look at the village':
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

        elif a == 'help' or a == 'please help' or a == '?' or a == 'h':
            hlpscr()
            lvlone()

        elif a == 'look sun' or a == 'look at the sun' or a == 'look at sun' or a == 'look horizon' or a == 'look at horizon' or a == 'look at the horizon':
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

        elif a == 'look self' or a == 'look me' or a == 'look at self':
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

        elif a == 'look canteen' or a == 'drink canteen' or a == 'look at canteen' or a == 'look flask' or a == 'drink from canteen' or a == 'drink flask' or a == 'drink from flask' or a == 'drink from canteen' or a == 'use canteen' or a == 'use the canteen' or a == 'use flask' or a == 'use the flask':
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

        elif a == 'look mountain' or a == 'look at mountain' or a == 'look at the mountain' or a == 'look mountains' or a == 'look at mountains' or a == 'look at the mountains':
            clrscr()

            if crri:
                hlfway()

            else:
                sttplc()

            print('| You gaze over at the mountains. They both have a sudden drop right after the peak. You wonder if they might    |')
            print('| once have been one whole mountain and not what appears to be two halves                                        |')
            print('|                                                                                                                |')
            print('|                                                              ___________________ _________________ ____________|')
            print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
            print('                                                              |___________________|_________________|____________|')
            input(' Press ENTER to continue: ')
            lvlone()

        elif a == 'look map' or a == 'look at map' or a == 'look at my map' or a == 'use map' or a == 'use the map' or a == 'map':
            ingmap()
            lvlone()

        elif a == 'exit' or a == 'exit game' or a == 'stop game':
            bktk = 0
            main()

        # needs a rework for continuity, actually add the city level when it comes to that
        elif a == 'walk city' or a == 'walk to city' or a == 'walk to the city':
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
        elif a == 'walk town' or a == 'walk to the town' or a == 'walk to town' or a == 'walk river' or a == 'walk to river' or a == 'walk to the river' or a == 'walk village' or a == 'walk to the village' or a == 'walk to village':
            if 'town' in str(a):
                rotv = 1
                clrscr()

                if crri:
                    bktk = 2
                    main()

                else:
                    aririv()
                    bktk = 2
                    main()

            elif 'river' in str(a):
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

            def lvlins(): # inside screen
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

                print('|                                       ______________________ ___________________ _________________ ____________|')
                print('|______________________________________| Type "leave" to leave| Type "h" for help |  Map available  | Pnts = ' + pnsp + ' |')
                print('                                       |______________________|___________________|_________________|____________|')
                a = input(' > ')
                a = a.lower()

                if a == 'take chair' or a == 'take the chair' or a == 'steal chair' or a == 'steal the chair':
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
                    
                elif a == 'take machinery' or a == 'take the machinery' or a == 'take machine' or a == 'take the machine' or a == 'take heavy machinery' or a == 'take the heavy machinery' or a == 'take heavy machine' or a == 'take the heavy machine':
                    facins()
                    print('| The machinery is far to heavy to move.                                                                         |')
                    print('|                                                                                                                |')
                    print('|                                                                                                                |')
                    print('|                                                              ___________________ _________________ ____________|')
                    print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                    print('                                                              |___________________|_________________|____________|')
                    input(' Press ENTER to continue: ')
                    lvlins()

                elif a == 'leave':
                    lvlfac()

                elif a == 'exit':
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
            a = input(' Write a number: ')
            a = a.lower()

            if a == '1' or a == 'knock' or a == 'knock on door':
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
                    a = input(' > ')
                    a = a.lower()

                    if a == 'knarkle':
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

            elif a == '2' or a == 'wait' or a == 'wait around':
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

            elif a == '3' or a == 'force door' or a == 'force open' or a == 'force open door':
                made = 1
                lvlins()

            elif a == 'leave':
                clrscr() 

            elif a == 'help' or a == 'please help' or a == '?' or a == 'h':
                hlpscr()
                lvlfac()     

            elif a == 'look map' or a == 'look at map' or a == 'look at the map' or a == 'use map' or a == 'use the map' or a == 'map':
                ingmap()
                lvlfac()

            elif a == 'exit' or a == 'exit game' or a == 'stop game':
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

            a = input(' > ')
            a = a.lower()

            if a == 'lick cactus' or a == 'lick the cactus' or a == 'lick a cactus':
                dedscr()
                print('| Congratulations! You are dead.                                                                                 |')
                print('| You died from shoving your face in a cactus.                                                                   |')
                print('| Thank you for playing Caught in the middle!                                                                    |')
                print('|                                                              ___________________ _________________ ____________|')
                print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                print('                                                              |___________________|_________________|____________|')
                input(' Press ENTER to restart: ')
                main()

            elif a == 'look cactus' or a == 'look cacti' or a == 'look at cactus' or a == 'look at the cactus' or a == 'look at cacti' or a == 'look at the cacti':
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

            elif a == 'help' or a == 'please help' or a == '?' or a == 'h':
                hlpscr()
                lvl2tw()

            elif a == 'look' or a == 'look around' or a == 'look surroundings':
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

            elif a == 'look saloon' or a == 'look at saloon' or a == 'look at the saloon' or a == 'look bar' or a == 'look at bar' or a == 'look at the bar' or a == 'look factory' or a == 'look at factory' or a == 'look at the factory':
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

            elif a == 'walk saloon' or a == 'walk to saloon' or a == 'walk to the saloon' or a == 'walk factory' or a == 'walk to factory' or a == 'walk to the factory':
                lvlfac()

            elif a == 'look map' or a == 'look at map' or a == 'look at the map' or a == 'use map' or a == 'use the map' or a == 'map':
                ingmap()
                lvl2tw()

            elif a == 'exit' or a == 'exit game' or a == 'stop game':
                bktk = 0
                main()

            elif a == 'walk river' or a == 'walk to river' or a == 'walk to the river':
                rotv = 0
                aririv()

            elif a == 'walk plain' or a == 'walk to plain' or a == 'walk to the plain' or a == 'walk plains' or a == 'walk to plains' or a == 'walk to the plains' or a == 'walk desert' or a == 'walk to desert' or a == 'walk to the desert' or a == 'leave' or a == 'leave town':
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