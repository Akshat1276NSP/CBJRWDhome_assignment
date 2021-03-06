import pygame, random
pygame.init()

clock = pygame.time.Clock()

sw = 800
sh = 600
screen = pygame.display.set_mode((sw,sh))

font_32 = pygame.font.SysFont('Arial', 32)
font_64 = pygame.font.SysFont('Arial', 64)

score = 0

#ARCADE MODE
def arcade_mode():
    life = 10
    clicked = False
    game_font = pygame.font.SysFont('Arial', 60)
    xy = [100,100]
    font = pygame.font.SysFont('Arial', 32)

    sCoord = (10,10)
    def score_print(scr):
        screen.blit(font.render("Score: "+str(scr), True, (0,0,0)), sCoord)

    def generate_box(x,y):
        return(pygame.Rect(x,y,100,100))

    def isClicked(xy, mx, my):
        global score
        if xy[0] < mx < xy[0]+100 and xy[1] < my < xy[1]+100:
            score += 1
            return True
        return False

    def draw_lifes(lifes):
        for i in range(lifes):
            pygame.draw.circle(screen, (100,100,0), (760 - 30*i, 20), 15) 


    start = pygame.time.get_ticks()
    MainRun = True
    while MainRun:
        screen.fill((200,200,200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MainRun = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicked = False

        box = generate_box(xy[0], xy[1])
        pygame.draw.rect(screen, (255,0,0), box)
  
        mx,my = pygame.mouse.get_pos()
        current_time = pygame.time.get_ticks() 

        if (current_time - start > 1000) and not(clicked):
            life -= 1
            print(life)
            start = pygame.time.get_ticks()
            xy = [random.randint(0,700), random.randint(0,500)]

        if clicked:
            if (current_time - start < 1000) and isClicked(xy, mx, my):
                clicked = False
                pygame.draw.rect(screen, (0,255,0), box)
                xy = [random.randint(0,700), random.randint(0,500)]
                start = pygame.time.get_ticks()

            elif (current_time - start < 1000) and not(isClicked(xy, mx, my)):
                clicked = False
                life -= 1
                pygame.draw.rect(screen, (0,0,255), box)
                xy = [random.randint(0,700), random.randint(0,500)]
                start = pygame.time.get_ticks()
                print(life)

        draw_lifes(life)
        score_print(score)

        if life <= 0:
            screen.fill((200,200,200))
            msg = pygame.font.SysFont('Arial',64)
            mCoord = (180,200)
            screen.blit(msg.render("GAME OVER!!", True, (0,0,0)), mCoord)

            fs = pygame.font.SysFont('Arial',32)
            fsCoord = (280,300)
            screen.blit(fs.render("FINAL SCORE: "+str(score), True, (0,0,0)), fsCoord)


        clock.tick(60)
        pygame.display.update()


# TIME OUT
def time_out_mode(st):
    start_time = st

    game_font = pygame.font.SysFont('Arial', 60)
    xy = [100,100]

    font = pygame.font.SysFont('Arial', 32)
    sCoord = (10,10)
    def score_print(scr):
        screen.blit(font.render("Score: "+str(scr), True, (0,0,0)), sCoord)

    tCoord = (600,10)
    def timer(t):
        screen.blit(font.render("Time Left: "+str(t), True, (0,0,0)), tCoord)

    def generate_box(x,y):
        return(pygame.Rect(x,y,100,100))

    def isClicked(xy, mx, my):
        global score
        if xy[0] < mx < xy[0]+100 and xy[1] < my < xy[1]+100:
            score += 1
            return True
        return False

    clicked = False
    start = pygame.time.get_ticks()
    TimeOutRun = True
    while TimeOutRun:
        screen.fill((200,200,200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                TimeOutRun = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicked = False

        box = generate_box(xy[0], xy[1])
        pygame.draw.rect(screen, (255,0,0), box)

        mx,my = pygame.mouse.get_pos()
        current_time = pygame.time.get_ticks() 
        if (current_time - start > 1000):
            start = pygame.time.get_ticks()
            xy = [random.randint(0,700), random.randint(0,500)]

        if clicked:
            if (current_time - start < 1000) and isClicked(xy, mx, my):
                pygame.draw.rect(screen, (0,255,0), box)
                start = pygame.time.get_ticks()
                xy = [random.randint(0,700), random.randint(0,500)]

        game_time = pygame.time.get_ticks()

        if game_time - start_time >= 60000:
            screen.fill((200,200,200))
            msg = pygame.font.SysFont('Arial',64)
            mCoord = (180,200)
            screen.blit(msg.render("GAME OVER!!", True, (0,0,0)), mCoord)

            fs = pygame.font.SysFont('Arial',32)
            fsCoord = (280,300)
            screen.blit(fs.render("FINAL SCORE: "+str(score), True, (0,0,0)), fsCoord)

            #pygame.display.update()

        score_print(score)
        clock.tick(60)
        pygame.display.update()


# MAIN MENU
clicked = False
mode = 0
state = 0
MainRun = True
while MainRun:
    screen.fill((200,200,200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MainRun = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicked = False
    
    Welcome_Message = font_64.render("Hui-Hui", True, (0,0,200))
    screen.blit(Welcome_Message, (sw//2-110, 20))

    Select_Level = font_32.render("SELECT MODE: ", True, (0,0,200))
    screen.blit(Select_Level, (10, sh-400))

    arcade = font_32.render("TIME-OUT", True, (0,0,200))
    screen.blit(arcade, (290, sh-360))

    zen = font_32.render("ARCADE", True, (0,0,200))
    screen.blit(zen, (290, sh-320))

    Start = font_64.render("START", True, (0,0,200))
    screen.blit(Start, (sw//2-80, sh-100))

    mx,my = pygame.mouse.get_pos()

    if clicked and state==0:
        if 285<mx<420 and sh-360<my<sh-323: mode = 1
        elif 285<mx<420 and sh-320<my<sh-283: mode = 2
        elif sw//2-95<mx<sw//2+95 and sh-105<my<sh-30: state = 1

    if mode == 1: 
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(285,sh-365,200,37),  2)
    elif mode == 2: 
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(285,sh-325,200,37),  2)
    
    if state == 1:
        pygame.draw.rect(screen, (0,255,0), pygame.Rect(sw//2-95,sh-107,230,70),  2)
        if mode == 1:
            MainRun = False
            time_out_mode(pygame.time.get_ticks())
        elif mode == 2:
            MainRun = False
            arcade_mode()

    pygame.display.update()
