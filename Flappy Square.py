from pygame import *
from random import seed ,randint
from datetime import datetime

#?  Global Variables
# topWalls = []
# botWalls = []

#?  Global Functions
def wordScroll(string= str):    #?  prints sentences char by char
    for char in string:
        print(char, end="",flush=True)
        time.wait(10)
    print("")
    time.wait(250)

def generate_wall(gap:int):
    #? print("generating wall")
    a = int(gap*2)
    b = int(screenSize.y-gap*2)
    hole = randint( a, b )
    topWalls.append( Rect(screenSize.x,0,50,hole-gap))
    botWalls.append( Rect(screenSize.x,hole+gap,50,screenSize.y-gap-hole))
    


#?  Initialising Display Screen
wordScroll("Setting Display and Clock")

display.init()
display.set_caption("Flappy Square!")
screenSize = Vector2(1200,800)
Screen = display.set_mode(screenSize)
Clock = time.Clock()



#?  Background Image
wordScroll("Setting Background,")

bg = image.load('Clouds bg Large.jpg').convert()
Screen.blit(bg,(0,0))
display.update()

#?  Initialising Font System
font.init()
''' #?  System Fonts Avail to use
['arial', 'arialblack', 'bahnschrift', 'calibri', 'cambria', 'cambriamath', 'candara', 'comicsansms', 'consolas', 'constantia', 'corbel', 'couriernew', 'ebrima', 'franklingothicmedium', 'gabriola', 'gadugi', 'georgia', 'impact', 'inkfree', 'javanesetext', 'leelawadeeui', 'leelawadeeuisemilight', 'lucidaconsole', 'lucidasans', 'malgungothic', 'malgungothicsemilight', 'microsofthimalaya', 'microsoftjhenghei', 'microsoftjhengheiui', 'microsoftnewtailue', 'microsoftphagspa', 'microsoftsansserif', 'microsofttaile', 'microsoftyahei', 'microsoftyaheiui', 'microsoftyibaiti', 'mingliuextb', 'pmingliuextb', 'mingliuhkscsextb', 'mongolianbaiti', 'msgothic', 'msuigothic', 'mspgothic', 'mvboli', 'myanmartext', 'nirmalaui', 'nirmalauisemilight', 'palatinolinotype', 'sansserifcollection', 'segoefluenticons', 'segoemdl2assets', 'segoeprint', 'segoescript', 'segoeui', 'segoeuiblack', 'segoeuiemoji', 'segoeuihistoric', 'segoeuisemibold', 'segoeuisemilight', 'segoeuisymbol', 'segoeuivariable', 'simsun', 'nsimsun', 'simsunextb', 'sitkatext', 'sylfaen', 'symbol', 'tahoma', 'timesnewroman', 'trebuchetms', 'verdana', 'webdings', 'wingdings', 'yugothic', 'yugothicuisemibold', 'yugothicui', 'yugothicmedium', 'yugothicuiregular', 'yugothicregular', 'yugothicuisemilight', 'holomdl2assets', 'agencyfb', 'algerian', 'bookantiqua', 'arialrounded', 'baskervilleoldface', 'bauhaus93', 'bell', 'bernardcondensed', 'bodoni', 'bodoniblack', 'bodonicondensed', 'bodonipostercompressed', 'bookmanoldstyle', 'bradleyhanditc', 'britannic', 'berlinsansfb', 'berlinsansfbdemi', 'broadway', 'brushscript', 'bookshelfsymbol7', 'californianfb', 'calisto', 'castellar', 'centuryschoolbook', 'centaur', 'century', 'chiller', 'colonna', 'cooperblack', 'copperplategothic', 'curlz', 'dubai', 'dubaimedium', 'dubairegular', 'elephant', 'engravers', 'erasitc', 'erasdemiitc', 'erasmediumitc', 'felixtitling', 'forte', 'franklingothicbook', 'franklingothicdemi', 'franklingothicdemicond', 'franklingothicheavy', 'franklingothicmediumcond', 'freestylescript', 'frenchscript', 'footlight', 'fzshuti', 'fzyaoti', 'garamond', 'gigi', 'gillsans', 'gillsanscondensed', 'gillsansultracondensed', 'gillsansultra', 'gloucesterextracondensed', 'gillsansextcondensed', 'centurygothic', 'goudyoldstyle', 'goudystout', 'harlowsolid', 'harrington', 'haettenschweiler', 'hightowertext', 'imprintshadow', 'informalroman', 'blackadderitc', 'edwardianscriptitc', 'kristenitc', 'jokerman', 'juiceitc', 'kunstlerscript', 'widelatin', 'lucidabright', 'lucidacalligraphy', 'lucidafaxregular', 'lucidafax', 'lucidahandwriting', 'lucidasansregular', 'lucidasansroman', 'lucidasanstypewriterregular', 'lucidasanstypewriter', 'lucidasanstypewriteroblique', 'magneto', 'maiandragd', 'maturascriptcapitals', 'mistral', 'modernno20', 'monotypecorsiva', 'extra', 'niagaraengraved', 'niagarasolid', 'ocraextended', 'oldenglishtext', 'onyx', 'msoutlook', 'palacescript', 'papyrus', 'parchment', 'perpetua', 'perpetuatitling', 'playbill', 'poorrichard', 'pristina', 'rage', 'ravie', 'msreferencesansserif', 'msreferencespecialty', 'rockwellcondensed', 'rockwell', 'rockwellextra', 'script', 'showcardgothic', 'lisu', 'youyuan', 'snapitc', 'stcaiyun', 'stencil', 'stfangsong', 'sthupo', 'stkaiti', 'stliti', 'stsong', 'stxihei', 'stxingkai', 'stxinwei', 'stzhongsong', 'twcen', 'twcencondensed', 'twcencondensedextra', 'tempussansitc', 'vinerhanditc', 'vivaldi', 'vladimirscript', 'wingdings2', 'wingdings3', 'dengxian', 'fangsong', 'kaiti', 'simhei', 'mecsoftfont1', 'slfrhnarchitectregular', 'cascadiacoderegular', 'cascadiamonoregular']'''

font1 = font.SysFont("bodoniblack",30)
font2 = font.SysFont("impact",36)




#?  Event Settings
wordScroll("Limiting events,")
event.set_blocked(None)                 #?  Blocks ALL Events
allowedEvents = [MOUSEBUTTONDOWN, KEYDOWN, QUIT]
event.set_allowed(allowedEvents)        #?  Allows listed events

#?  bouncing ball
wordScroll("Creating objects,")
ballPos = Vector2(150,screenSize.y*0.4)
square = Rect(150,screenSize.y*0.6,40,40)
draw.rect(Screen,"blue",square,25)
display.update()


#?  Moving walls

end_rect = Rect(-25,0,5,screenSize.y)
Ground = Rect(0,screenSize.y-20,screenSize.x,20)
Ceiling = Rect(0,0,screenSize.x,20)

# key.set_repeat(0)




Difficulty = 1
Running = True
Alive = False
Collision = False
bestScore = 0

while Running:      #?  Main loop
    
    topWalls = []
    botWalls = []
    startTime = None

    #?  Physics variables
    g = -60
    iv = 50
    jv = 100
    dt = 0.05
    gap = 100
    disp = 0
    interval = [1,500000]

    eventList = event.get()
    for stuff in eventList:

        if stuff.type == QUIT:          #?  Enables closing of window
            wordScroll("Closing program...")
            Running = False
            break

        if stuff.type == KEYDOWN:
            if stuff.key == K_ESCAPE:   #?  Enables quitting by pressing ESC
                wordScroll("Quitting program...")
                Running = False
                break

            # #?  Difficulty setter
            # if stuff.key == K_1:
            #     print(f"Setting difficulty...{1}")
            #     Difficulty = 1
            # if stuff.key == K_2:
            #     print(f"Setting difficulty...{2}")
            #     Difficulty = 2
            # if stuff.key == K_3:
            #     print(f"Setting difficulty...{3}")
            #     Difficulty = 3

            #?  Game Starter
            if stuff.key == K_SPACE:    #?  Initialise game variables
                # print("You are alive!")
                seed(None)
                Alive = True
                startTime = datetime.now()
                genWallTime = datetime.now()
                generate_wall(gap)

    counter = 0
    update = False
    while Alive:    #?  Jumping loop

        eventList = event.get()
        for stuff in eventList:
            if stuff.type == QUIT:          #?  Enables closing of window
                wordScroll("Closing program...")
                Alive = False
                Running = False
                display.quit()
                break
            if stuff.type == KEYDOWN:
                if stuff.key == K_ESCAPE:   #?  Enables quitting by pressing ESC
                    wordScroll("Quiting game...")
                    Alive = False
                    Running = True
                    break
                if stuff.key == K_SPACE:
                    # print("Jump!")
                    iv = jv

        sfhljh = datetime.now() - genWallTime
        if sfhljh.seconds >= interval[0] and sfhljh.microseconds >= interval[1]:
        # if len(topWalls) < 1:
            genWallTime = datetime.now()
            generate_wall(gap)
        
        if not update and counter == 2:
            gap = 90
            update = True
            print(counter, interval)
        elif update and counter == 5:
            g = -80
            jv = 120
            update = False
            interval[1] = 250000
            print(counter, interval)
        elif not update and counter == 10:
            gap = 85
            interval[1] = 100000
            update = True
            print(counter, interval)
        elif update and counter == 15:
            g = -100  
            jv = 150
            update = False
            interval = [1, 0]
            print(counter, interval)
        elif not update and counter == 20:
            gap = 80
            update = True
            interval = [0, 900000]
            print(counter, interval)
        elif update and counter == 25:
            gap = 75
            update = False
            interval[1] = 850000
            print(counter, interval)

        if Collision:
            wordScroll("You died!")
            Alive = False
            Collision = False
            if counter > bestScore:
                deathMsg = font2.render(f"You Died! New Highscore: {counter}",False,"Black")
                death_rect = deathMsg.get_rect(center=(screenSize.x/2,screenSize.y/2))
                highScore = font2.render(f"Previous best: {bestScore}",False,"Black")
                Score_rect = highScore.get_rect(center=(screenSize.x/2,screenSize.y*0.6))
                bestScore = counter
            else:
                deathMsg = font2.render(f"You Died! Score: {counter}",False,"Black")
                death_rect   = deathMsg.get_rect(center=(screenSize.x/2,screenSize.y/2))
                highScore = font2.render(f"Highest Score: {bestScore}",False,"Black")
                Score_rect = highScore.get_rect(center=(screenSize.x/2,screenSize.y*0.6))
            Screen.blit(highScore,Score_rect)
            Screen.blit(deathMsg,death_rect)
            display.update()
            Clock.tick(1)
            time.wait(2000)

        else:

            iv   = iv + g*dt                #?  Updates next instantaneous velocity
            disp = iv*dt + 0.5*g*pow(dt,2)  #?  Updates next instantaneous displacement
            square.move_ip(0,-disp) #-= disp
        
            
            

            Screen.blit(bg,(0,0))

            

            draw.rect(Screen,"Black",end_rect,5)
            if topWalls and topWalls[0].colliderect(end_rect):
                    topWalls.pop(0)
                    botWalls.pop(0)
                    counter += 1
                    # generate_wall()
                    
            for i in range(len(topWalls)):
                if square.collidelist([topWalls[i],botWalls[i]]) != -1:
                    Collision = True
                    print("Collision!")
                
                topWalls[i].move_ip(-5,0)
                botWalls[i].move_ip(-5,0)
                draw.rect(Screen,"black",topWalls[i],0,5)
                draw.rect(Screen,"black",botWalls[i],0,5)

            if square.colliderect(Ceiling) or square.colliderect(Ground):
                Collision = True

            distance_message = font1.render(f"Score: {counter}",False,"White")
            distance_rect   = distance_message.get_rect(center=(screenSize.x/2,50))
            Screen.blit(distance_message,distance_rect)

            square = draw.rect(Screen,"blue",square,5,5)
            draw.rect(Screen,"black",Ground)
            draw.rect(Screen,"black",Ceiling)

            display.update()
            Clock.tick(120)


        #?  last line of Alive Loop
        pass
    
    square = Rect(150,screenSize.y*0.6,40,40)
    startingMsg = font1.render(f"Press SPACE to Start!",False,"Black")
    startMsg_rect = startingMsg.get_rect(center=(screenSize.x/2,screenSize.y/2))
    
    #?  Home Page screen
    Screen.blit(bg,(0,0))
    Screen.blit(startingMsg,startMsg_rect)
    
    draw.rect(Screen,"blue",square,5,5)
    display.update()
    Clock.tick(20)

    pass