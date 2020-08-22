'''
    PRIORITY!
x - re-add the box for type "h" for help" and "map available"
x - make a system for earning points
x - add point triggers
o - level select gives incorrect number of points

    The To-Do list (problems in no particular order):
x - Add title
x?- Add more jokes to the title screen
x?- Add starting level
x - Add level select and "cheat"
x - Add "help" screen
x - Add the map
o - Rework "help" screen
        in its current state it is a bit barren and I think it should be
        specifically tailored to the level your on.
x - Add canteen mechanic
x - Add the city (kind of)
x - Rework the map
o - Rewrite the "look around" section at the lvtwotwn level
o - Add in the lvtwovil level
x - Add a new level after crossing the river
? - Rework the city
o - Make more notes like these to speed up the programming process
o - Create a new and improved storyboard
o - rework the tdnc variable and whole "that does not compute" system.
        also change level one with the canteen to stop piggybacking off of
        the tdnc variable, honestly just make a new one no problem

        hey old me what does this mean??? the tdnc variable has more or
        less been completely removed, you know?? it was you who removed
        it!
o - add "look city" from lvone

    Storyboard
You spawn in, have to go to the town to get something then go to the city,
once there you realise you needed some item from the village too (if you
didn't already grab it), die, and have to restart. it is a rogue like and
this story is a wip too, have to figure out more stuff and precise details

x - add credits screen
 
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

def clr():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

hdmd = 'off)'
bt = 0

input(' Press ENTER if there are no errors: ')

def main():
    global hdmd, tdnc, crri, tc, canteen, bt, cf, sal, lkmap, pnts, pnsp, pnt1, pnt2, pnt3

    if bt == 0:
        pnt1 = 0
        pnt2 = 0
        pnt3 = 0
        sal = 0
        crri = 0
        tc = 0
        canteen = 0
        cf = 0
        lkmap = 0
        pnts = 0
        tdnc = 0

    def pts():
        global pnts, pnsp
        if len(str(pnts)) == 1:
            pnsp = str(pnts) + '  '
        elif len(str(pnts)) == 2:
            pnsp = str(pnts) + ' '
        else:
            pnsp = str(pnts)

    def mm():
        clr()
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

    def crd():
        clr()
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

    def stpl():
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

    def hfwy():
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

    def river():
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

    def dead():
        clr()
        global bt
        bt = 0
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

    def twn():
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

    def hepl():
        clr()
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
        print('| This window is currently WIP                                                                                   |')
        print('|________________________________________________________________________________________________________________|')
        print()
        input(' Press ENTER to continue: ')

    def salscr():
        global ma, mb, mc, md, me, mf, mg, mh, mi, mj
        ma = '| \______       \ /    \   _/               |          |'
        mb = ' \_____  \       [     _]_/. ___ .  . ___ . |          |'
        mc = ' _     \  |       \  _/     |   |    |   |  |          |'
        md = '| \____/  |        \/       |___|    |___|  |          |'
        me = ' \_______/          |      \'     \'  \'     \' |          |'
        mf = ' _ _ _ _ _ _ _ _ _ _ ] _ _ _ _ _ _ _ _ _ _ _|          |'
        mg = '                    /                       |          |'
        mh = '                    |                       |          |'
        mi = '        x  .                 , #                       |'
        mj = '                  #               .              .     |'
        print(' ________________________________________________________________________________________________________________')
        print('|                        |    |       ___________         ' + ma)
        print('|                        |    |      |           |        ' + mb)
        print('|                        |\   |      |           |        ' + mc)
        print('|                        | \  |      |           |        ' + md)
        print('|       xX                  \ |      |   _____   |        ' + me)
        print('|                            \|_ _ _ |  |____]|*\'| _ _ _ _' + mf)
        print('|            ,                |      |           |        ' + mg)
        print('|                .            |      |           |        ' + mh)
        print('|                       x                      ,          ' + mi)
        print('|                              .                          ' + mj)
        print('|________________________________________________________________________________________________________________|')


    def twrp():
        clr()
        river()
        global tc, pnt1, pnts

        if pnt1 == 0:
            pnts = pnts + 1
            pnt1 = 1
        pts()

        if tc:
            print('| There is a river in the way.                                                                                   |')

        else:
            print('| You arrive at the river.                                                                                       |')

        print('| 1. Attempt to cross the river                                                                                  |')

        if cf:
            print('| 2. Fill your canteen at the river                                                                              |')

        else:
            print('| 2. ?????                                                                                                       |')

        print('| 3. Leave                                                     ___________________ _________________ ____________|')
        print('|_____________________________________________________________| Type "h" for help |  Map available  | Pnts = ' + pnsp + ' |')
        print('                                                              |___________________|_________________|____________|')
        a = input(' > ')
        a = a.lower()

        if a == '1' or a == 'one' or a == 'attempt to cross the river' or a == 'cross the river' or a == 'cross river':

            def ride():
                dead()
                print('| Congratulations! You are dead.                                                                                 |')
                print('| The rock you jumped on was loose and gave in under your feet. You feel off and hit your head on the riverbed   |')
                print('| causing you to slowly bleed out over the course of an hour.                                                    |')
                print('| Thank you for playing Caught in the middle!                  ___________________ _________________ ____________|')
                print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                print('                                                              |___________________|_________________|____________|')
                input(' Press ENTER to restart: ')
                main()

            def risu():
                global crri
                clr()

                if crri:
                    stpl()
                    crri = 0

                else:
                    hfwy()
                    crri = 1

                print('| You crossed the river successfully.                                                                            |')
                print('|                                                                                                                |')
                print('|                                                                                                                |')
                print('|                                                              ___________________ _________________ ____________|')
                print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                print('                                                              |___________________|_________________|____________|')

                input(' Press ENTER to continue: ')

            def rian():
                clr()
                river()
                print('| 1. Jump on to the first rock                                                                                   |')
                print('| 2. Jump on to the second rock                                                                                  |')
                print('| 3. Jump on to the third rock                                                                                   |')
                print('| 4. Jump over the rocks to the other riverbank                ___________________ _________________ ____________|')
                print('|_____________________________________________________________| Type "h" for help |  Map available  | Pnts = ' + pnsp + ' |')
                print('                                                              |___________________|_________________|____________|')
                a = input(' Write a number: ')
                a = a.lower()

                if a == '1' or a == 'one' or a == '3' or a == 'three':
                    ride()

                elif a == '2' or a == 'two':

                    if hdmd == 'off)':
                        risu()

                    else:
                        ride()

                elif a == '4' or a == 'four':
                    risu()

                elif a == 'leave' or a == 'cancel':
                    lvone()

                elif a == 'exit' or a == 'exit game' or a == 'stop game':
                    bt = 0
                    main()

                elif a == 'help' or a == 'please help' or a == '?' or a == 'h':
                    hepl()
                    rian()

                elif a == 'look map' or a == 'look at map' or a == 'look at the map' or a == 'use map' or a == 'use the map' or a == 'map':
                    igmap()
                    rian()

                else:
                    rian()

            rian()

        elif a == '2' or a == 'two' or a == 'fill canteen' or a == 'fill the canteen':
            if cf:
                global canteen, tdnc
                clr()
                river()

                if canteen:
                    print('| Your canteen is already full.                                                                                  |')
                    print('|                                                                                                                |')
                    print('|                                                                                                                |')
                    print('|                                                              ___________________ _________________ ____________|')
                    print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                    print('                                                              |___________________|_________________|____________|')
                    input(' Press ENTER to continue: ')
                    twrp()

                else:
                    print('| You quench your thirst at the river and then proceed to fill your canteen.                                     |')
                    print('|                                                                                                                |')
                    print('|                                                                                                                |')
                    print('|                                                              ___________________ _________________ ____________|')
                    print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                    print('                                                              |___________________|_________________|____________|')
                    canteen = 1
                    tdnc = 1
                    input(' Press ENTER to continue: ')
                    twrp()  

            else:
                twrp()

        elif a == '3' or a == 'three' or a == 'leave':
            lvone()
        
        elif a == 'look map' or a == 'look at map' or a == 'look at the map' or a == 'use map' or a == 'use the map' or a == 'map':
            igmap()
            twrp()

        elif a == 'help' or a == 'please help' or a == '?' or a == 'h':
            hepl()
            twrp()

        elif a == 'exit' or a == 'exit game' or a == 'stop game':
            bt = 0
            main()

        else:
            twrp()

    def igmap():
        global lkmap
        clr()
        print(' ________________________________________________________________________________________________________________')
        print('|  __  |                           |                     |' + ma)
        print('| / _\ |                           | Map Legend:         |' + mb)
        print('| \__/ |  .               .        | OO = City           |' + mc)
        print('|______| /|   x____O      |\     _/| O = Town            |' + md)
        print('|                              _/  | x = Village         |' + me)
        print('|        _ --- _            _-\'    | .                   |' + mf)
        print('|     _-\'        \_        /    _--| |\ = Mountain       |' + mg)
        print('|  _-\'          W  \      /    /   | _ = Road/Path       |' + mh)
        print('|-\' OO              \'-_ _-----\'    | Dotted line = River |' + mi)
        print('|                            \'-_--_| W = Where I woke up |' + mj)
        print('|__________________________________|_____________________|_______________________________________________________|')
        print('|                                                                                                                |')

        if lkmap:
            print('| You take the map out of your pocket and unfurl it.                                                             |')
            print('|                                                                                                                |')
            print('|                                                                                                                |')

        else:
            print('| You take the map out of your pocket and unfurl it. In one of the map\'s corners there\'s a legend. From looking  |')
            print('| at your surroundings you are able to point out precisely where you woke up and you write a "W" there to mark   |')
            print('| that position. You also have a compass which is pointing north.                                                |')
            lkmap = 1

        print('|                                                              ___________________ _________________ ____________|')
        print('|_____________________________________________________________| Help unavailable  |    Map open     | Pnts = ' + pnsp + ' |')
        print('                                                              |___________________|_________________|____________|')
        input(' Press ENTER to continue: ')

    def start():

        def lvse():
            global bt, canteen, cf, crri
            clr()
            mm()
            print('| Welcome to the Level Select! Choose level to go to:                                                            |')
            print('| 1. Start   2. Town   3. Saloon/Factory                                                                         |')
            print('|                                                                                                                |')
            print('|                                                                                       _________________________|')
            print('|______________________________________________________________________________________| Type "cancel" to cancel |')
            print('                                                                                       |_________________________|')
            a = input(' > ')
            a = a.lower()

            if a == '1' or a == 'start':
                bt = 1
                pnsp = 0
                main()

            elif a == '2' or a == 'town':
                canteen = 1
                bt = 2
                cf = 1
                crri = 1
                pnt1 = 1
                pnt2 = 1
                pnts = 2
                main()

            elif a == '3' or a == 'saloon' or a == 'factory':
                canteen = 1
                bt = 2
                cf = 1
                crri = 1
                bt = 4
                pnt1 = 1
                pnt2 = 1
                pnt3 = 1
                pnts = 3
                main()

            elif a == 'cancel':
                clr()
                start()

            else:
                lvse()

        mm()
        print('| 1. Play                                                5. About the developer                                  |')
        print('| 2. Info                                                6. Credits and a special thanks                         |')
        print('| 3. Settings (Hardmode is', hdmd, '                         7. Exit                                                 |')
        print('| 4. Level Select                                                                                                |')
        print('|________________________________________________________________________________________________________________|')
        print()
        a = input(' Write a number: ')
        a = a.lower()

        if a == '1' or a == 'one':
            clr()

        elif a == '2' or a == 'two':
            mm()
            print('| Caught in the middle is a text adventure game inspired by early 80\'s games like Space Quest and Monkey Island, |')
            print('| but with my own personal twist on it. Here\'s quick tip on how to win:                                          |')
            print('|                                                                                                                |')
            print('| *Don\'t* die!                                                                                                   |')
            print('|________________________________________________________________________________________________________________|')
            print()
            input(' Press ENTER to continue: ')
            clr()
            start()

        elif a == '3' or a == 'three':

            def toh():
                global hdmd
                mm()

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

                    clr()
                    start()

                elif a == 'n' or a == 'no':
                    if hdmd == 'off)':
                        hdmd = 'off)'

                    else:
                        hdmd = 'on) '

                    clr()
                    start()

                else:
                    toh()

            toh()

        elif a == '4' or a == 'four':
            mm()
            print('| Please enter the password                                                                                      |')
            print('|                                                                                                                |')
            print('|                                                                                                                |')
            print('|                                                                                                                |')
            print('|________________________________________________________________________________________________________________|')
            print()
            password = input(' > ')

            if password == 'un1cornBallz':
                lvse()

            else:
                clr()
                mm()
                print('| Incorrect Password                                                                                             |')
                print('|                                                                                                                |')
                print('|                                                                                                                |')
                print('|                                                                                                                |')
                print('|________________________________________________________________________________________________________________|')
                print()
                input(' Press ENTER to continue: ')
                start()

        elif a == '5' or a == 'five':
            mm()
            print('| Hi! I am DonTristan, the developer of this game. Thank you so much for installing it. The development of this  |')
            print('| game started with me not doing what I was supposed to do in school and ended up with what you see now. It has  |')
            print('| been a labour of love and I\'ve pulled out my hair at every step but in the end, I believe it was all worth it. |')
            print('| If you wish to support me further you can visit my website at http://dontristan.com/, thank you!               |')
            print('|________________________________________________________________________________________________________________|')
            print()
            input(' Press ENTER to continue: ')
            clr()
            start()

        elif a == '6' or a == 'six':
            crd()
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
            clr()
            start()

        elif a == '7' or a == 'seven' or a == 'exit' or a == 'exit game':
            clr()
            exit()

        elif a == 'cheat':
            lvse() 

        else:
            clr()
            start()

    if bt == 0:
        start()

    def lvone():
        global lv, tdnc, cf, bt
        lv = 'lvone()'
        clr()
        pts()
        if crri:
            hfwy()

        else:
            stpl()

        if tdnc == 0:
            print('| You feel parched.                                                                                              |')
            print('| The sun is setting.                                                                                            |')

        elif tdnc == 1:
            print('| The sun is setting.                                                                                            |')
            print('|                                                                                                                |')

        print('|                                                                                                                |')
        print('|                                                              ___________________ _________________ ____________|')
        print('|_____________________________________________________________| Type "h" for help |  Map available  | Pnts = ' + pnsp + ' |')
        print('                                                              |___________________|_________________|____________|')
        a = input(' > ')
        a = a.lower()

        if a == 'look' or a == 'look around' or a == 'look town' or a == 'look at town' or a == 'look at the town' or a == 'look village' or a == 'look at village' or a == 'look at the village':
            clr()

            if crri:
                hfwy()

            else:
                stpl()

            print('| You are in the middle of a desert. In front of you you see a town. The town is made up of several smaller      |')
            print('| houses and one larger house. To the left of the town you see a small village consisting of some smaller huts   |')
            print('| and crop fields. To either side of both the town and the small village there are two mountains.                |')
            print('|                                                              ___________________ _________________ ____________|')
            print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
            print('                                                              |___________________|_________________|____________|')
            input(' Press ENTER to continue: ')
            lvone()

        elif a == 'help' or a == 'please help' or a == '?' or a == 'h':
            hepl()
            lvone()

        elif a == 'look sun' or a == 'look at the sun' or a == 'look at sun' or a == 'look horizon' or a == 'look at horizon' or a == 'look at the horizon':
            clr()

            if crri:
                hfwy()

            else:
                stpl()

            print('| The sun is setting. It is now somewhere between red and orange in colour. The sky itself has become slightly   |')
            print('| orange, then pink before turning dark blue and then to black. There are no clouds to be seen anywhere.         |')
            print('|                                                                                                                |')
            print('|                                                              ___________________ _________________ ____________|')
            print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
            print('                                                              |___________________|_________________|____________|')
            input(' Press ENTER to continue: ')
            lvone()

        elif a == 'look self' or a == 'look me' or a == 'look at self':
            cf = 1
            clr()

            if crri:
                hfwy()

            else:
                stpl()

            print('| You look at yourself and audibly say "hell yeah". After this self flattery you notice a map, and a canteen on  |')
            print('| your hip that you had completely forgotten about.                                                              |')
            print('|                                                                                                                |')
            print('|                                                              ___________________ _________________ ____________|')
            print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
            print('                                                              |___________________|_________________|____________|')
            input(' Press ENTER to continue: ')
            lvone()

        elif a == 'look canteen' or a == 'drink canteen' or a == 'look at canteen' or a == 'look flask' or a == 'drink from canteen' or a == 'drink flask' or a == 'drink from flask' or a == 'drink from canteen' or a == 'use canteen' or a == 'use the canteen' or a == 'use flask' or a == 'use the flask':
            cf = 1
            clr()

            if crri:
                hfwy()

            else:
                stpl()

            if cf:
                print('| You take the canteen from your hip and notice immediately that it feels very light. You cross your fingers as  |')
                print('| you peer inside. You find that it is completely dried up. Your feel even more parched now than before.         |')

            else:
                print('| You find a canteen on your hip. You immediately notice that it feels very light. you cross your fingers as you |')
                print('| peer inside. You find that it is completely dried up. Your feel even more parched now than before.             |')
           
            print('|                                                                                                                |')
            print('|                                                              ___________________ _________________ ____________|')
            print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
            print('                                                              |___________________|_________________|____________|')
            input(' Press ENTER to continue: ')
            lvone()

        elif a == 'look mountain' or a == 'look at mountain' or a == 'look at the mountain' or a == 'look mountains' or a == 'look at mountains' or a == 'look at the mountains':
            clr()

            if crri:
                hfwy()

            else:
                stpl()

            print('| You gaze over at the mountains. They both have a sudden drop right after the peak. You wonder if they might    |')
            print('| once have been one whole mountain and not what appears to be two halves.                                       |')
            print('|                                                                                                                |')
            print('|                                                              ___________________ _________________ ____________|')
            print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
            print('                                                              |___________________|_________________|____________|')
            input(' Press ENTER to continue: ')
            lvone()

        elif a == 'look map' or a == 'look at map' or a == 'look at my map' or a == 'use map' or a == 'use the map' or a == 'map':
            igmap()
            lvone()

        elif a == 'exit' or a == 'exit game' or a == 'stop game':
            bt = 0
            main()

        #needs a rework for continuity
        elif a == 'walk city' or a == 'walk to city' or a == 'walk to the city':
            global tc

            if crri:
                tc = 1
                twrp()

            dead()
            print('| Congratulations! You are dead.                                                                                 |')

            if canteen:
                print('| Even with your water from your canteen it was not enough and you died from thirst on your way to the city.     |')

            else:
                print('| You died from thirst on your way to the city.                                                                  |')

            print('| Thank you for playing Caught in the middle half of a mountain!                                                 |')
            print('|                                                              ___________________ _________________ ____________|')
            print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
            print('                                                              |___________________|_________________|____________|')
            input(' Press ENTER to restart: ')
            bt = 0
            main()

        elif a == 'walk town' or a == 'walk to the town' or a == 'walk to town' or a == 'walk river' or a == 'walk to river' or a == 'walk to the river' or a == 'walk village' or a == 'walk to the village' or a == 'walk to village':
            if 'town' in str(a):
                tc = 1
                clr()

                if crri:
                    bt = 2
                    main()

                else:
                    twrp()
                    bt = 2
                    main()

            elif 'river' in str(a):
                tc = 0
                twrp()
                bt = 1
                main()
                
            else:

                tc = 1
                clr()

                if crri:
                    bt = 3
                    main()

                else:
                    twrp()
                    bt = 3
                    main()

        else:
            lvone()

    if bt == 0 or bt == 1:
        lvone()

    def lvtwotwn():
        global bt, canteen, sal, tc

        def lvfac():
            clr()
            global pnt3, pnts
            if pnt3 == 0:
                pnts = pnts + 1
                pnt3 = 1
            pts()
            salscr()
            print('| You go to the saloon and try to open the door but it\'s locked                                                  |')
            print('| 1. Knock                                                                                                       |')
            print('| 2. Force open                                                                                                  |')
            print('| 3. Wait around                                                                                                 |')
            print('| 4. Leave                                                     ___________________ _________________ ____________|')
            print('|_____________________________________________________________| Type "h" for help |  Map available  | Pnts = ' + pnsp + ' |')
            print('                                                              |___________________|_________________|____________|')
            a = input(' > ')
            a = a.lower()

            if a == '1' or a == 'knock' or a == 'knock on door':
                print('wip')

            elif a == '2' or a == 'force door' or a == 'force open' or a == 'force open door':
                print('wip')
                
            elif a == '3' or a == 'wait' or a == 'wait around':
                print('wip')

            elif a == '4' or a == 'leave':
                clr() 

            elif a == 'help' or a == 'please help' or a == '?' or a == 'h':
                hepl()
                lvfac()     

            elif a == 'look map' or a == 'look at map' or a == 'look at the map' or a == 'use map' or a == 'use the map' or a == 'map':
                igmap()
                lvfac()

            elif a == 'exit' or a == 'exit game' or a == 'stop game':
                bt = 0
                main()

            else:
                lvfac()

        if bt == 4:
            lvfac()

        if canteen:
            global pnt2, pnts
            if pnt2 == 0:
                pnts = pnts + 1
                pnt2 = 1
            pts()
            clr()
            twn()

            print('| You arrive at the town. The large building appears to be the town hall. There are also multiple residential    |')

            if sal:
                print('| buildings and what you previously thought to be a saloon.                                                      |')

            else:
                print('| buildings and a saloon.                                                                                        |')

            print('|                                                                                                                |')
            print('|                                                              ___________________ _________________ ____________|')
            print('|_____________________________________________________________| Type "h" for help |  Map available  | Pnts = ' + pnsp + ' |')
            print('                                                              |___________________|_________________|____________|')

            a = input(' > ')
            a = a.lower()

            if a == 'lick cactus' or a == 'lick the cactus' or a == 'lick a cactus':
                dead()
                print('| Congratulations! You are dead.                                                                                 |')
                print('| You died from shoving your face in a cactus.                                                                   |')
                print('| Thank you for playing Caught in the middle half of a mountain!                                                 |')
                print('|                                                              ___________________ _________________ ____________|')
                print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                print('                                                              |___________________|_________________|____________|')
                input(' Press ENTER to restart: ')
                bt = 0
                main()

            elif a == 'look cactus' or a == 'look cacti' or a == 'look at cactus' or a == 'look at the cactus' or a == 'look at cacti' or a == 'look at the cacti':
                clr()
                twn()
                print('| There are multiple cacti scattered around the town. They look both larger and spinier than any other cacti     |')
                print('| you\'ve seen before.                                                                                            |')
                print('|                                                                                                                |')
                print('|                                                              ___________________ _________________ ____________|')
                print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                print('                                                              |___________________|_________________|____________|')
                input(' Press ENTER to continue: ')
                lvtwotwn()

            elif a == 'help' or a == 'please help' or a == '?' or a == 'h':
                hepl()
                lvtwotwn()

            elif a == 'look' or a == 'look around' or a == 'look surroundings':
                clr()
                twn()
                print('| You find yourself in a small town in the desert. You tried reading the name of the town from a sign you saw    |')
                print('| when you first entered, but you couldn\'t seem to understand the language. There are multiple houses around     |')

                if sal:
                    print('| the town including a town hall and a factory.                                                                  |')

                else:
                    print('| the town including a town hall and what looks like a saloon.                                                   |')

                print('|                                                              ___________________ _________________ ____________|')
                print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                print('                                                              |___________________|_________________|____________|')
                input(' Press ENTER to continue: ')
                lvtwotwn()

            #the whole saloon thing is interesting to me because you need to wait around for the password, else you won't be able to progress in a later part
            #I haven't decided when that is yet but it's gonna be a surprise, you will need the password >:)
            elif a == 'look saloon' or a == 'look at saloon' or a == 'look at the saloon' or a == 'look bar' or a == 'look at bar' or a == 'look at the bar' or a == 'look factory' or a == 'look at factory' or a == 'look at the factory':
                clr()
                twn()

                if sal:
                    print('| You look at the factory.                                                                                       |')

                else:
                    print('| You look at what you assumed to be a saloon, only to find out it looks to be some sort of factory.             |')

                print('| Through the windows you see heavy machinery, but no workers.                                                   |')
                print('|                                                                                                                |')
                print('|                                                              ___________________ _________________ ____________|')
                print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
                print('                                                              |___________________|_________________|____________|')
                sal = 1
                input(' Press ENTER to continue: ')
                lvtwotwn()

            elif a == 'walk saloon' or a == 'walk to saloon' or a == 'walk to the saloon' or a == 'walk factory' or a == 'walk to factory' or a == 'walk to the factory':
                lvfac()

            elif a == 'look map' or a == 'look at map' or a == 'look at the map' or a == 'use map' or a == 'use the map' or a == 'map':
                igmap()
                lvtwotwn()

            elif a == 'exit' or a == 'exit game' or a == 'stop game':
                bt = 0
                main()

            elif a == 'walk river' or a == 'walk to river' or a == 'walk to the river':
                tc = 0
                twrp()

            elif a == 'walk plain' or a == 'walk to plain' or a == 'walk to the plain' or a == 'walk plains' or a == 'walk to plains' or a == 'walk to the plains' or a == 'walk desert' or a == 'walk to desert' or a == 'walk to the desert' or a == 'leave' or a == 'leave town':
                bt = 1
                main()

            else:
                clr()
                lvtwotwn()


        else:
            dead()
            print('| Congratulations! You are dead.                                                                                 |')
            print('| You died from thirst on your way to the town.                                                                  |')
            print('| Thank you for playing Caught in the middle half of a mountain!                                                 |')
            print('|                                                              ___________________ _________________ ____________|')
            print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
            print('                                                              |___________________|_________________|____________|')
            input(' Press ENTER to restart: ')
            main()

    if bt == 2 or bt == 4:
        lvtwotwn()

    def lvtwovil():
        global bt
        clr()
        twn()
        print('| The village is currently WIP                                                                                   |')
        print('|                                                                                                                |')
        print('|                                                                                                                |')
        print('|                                                              ___________________ _________________ ____________|')
        print('|_____________________________________________________________| Help unavailable  | Map unavailable | Pnts = ' + pnsp + ' |')
        print('                                                              |___________________|_________________|____________|')
        input(' Press ENTER to restart: ')
        bt = 0
        main()
 
    if bt == 3:
        lvtwovil()
main()