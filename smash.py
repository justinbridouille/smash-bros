import  pygame
import time
import random
from math import pi
import pickle


pygame.init()
game=False



menusmash=True
menuoption=True
menuhistoire=True
battleunlock=False
avanckey=0
bosspart1=0
bot1=False
bot1dif=1
bot2=False
bot2dif=1
bot3=False
bot3dif=1
bot4=False
bot4dif=1
menutrophes=True
game_over=False
p=[1,1,1,1]
cchois=1
playernumber=2
smashretour=True
mapretour=True
decoretour=True
menuretour=True

while not game:

    try:
        Fichier = open('data.txt','rb')
        Dept = pickle.load(Fichier)
        Fichier.close()

    except FileNotFoundError:
        Dept=[1,1,True,True]
        Fichier = open('data.txt','wb')
        pickle.dump(Dept,Fichier)
        Fichier.close()
    deblocage=Dept[1]
    avancement=Dept[0]
    musique=Dept[2]
    animation=Dept[3]


    myfont = pygame.font.SysFont("monospace", 50)
    myfont2 = pygame.font.SysFont("monospace", 30)
    press = myfont.render("press any button", 1, (250,250,250))
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((800,400))
    if decoretour==True:
        smashretour=True
        decoretour=True
        menuretour=True
        mapretour=True
        map2retour=True
        deco=False
        while not deco:
            pygame.display.set_caption("smash")
            logo = pygame.image.load('all/logos.png').convert_alpha()
            for y in range(1,350):
                clock.tick(250)
                surface.fill((0,0,0))
                logo1 = pygame.transform.scale(logo,(2*y,y))
                surface.blit(logo1,(400-y,175-0.5*y))
                pygame.display.update(0,0,800,450)
            surface.blit(press, (160, 350))
            pygame.display.update(20,350,780,400)
            deco=True



        puse = False
        while not puse:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    puse = True
    if musique==True:
        pygame.mixer.music.load("all/menumusic.mp3")
        pygame.mixer.music.play(-1)

    def menupr(n,v):
        if cchois==1:
            surface.fill((255,0,0))
        if cchois==2:
            surface.fill((0,191,255))
        if cchois==4:
            surface.fill((30,205,30))
        if cchois==3:
            surface.fill((255,215,0))
        pygame.draw.circle(surface,(255,255,255),(400,200),200)
        pygame.draw.line(surface,(0,0,0),(400,0),(400,400),10)
        pygame.draw.line(surface,(0,0,0),(200,200),(600,200),10)
        pygame.draw.circle(surface,(255,255,255),(400,200),45)
        fond1 = pygame.image.load("fond/fond"+str(cchois)+".png").convert_alpha()
        fond1 = pygame.transform.scale(fond1,(80,80))
        surface.blit(fond1,(360,160))
        pygame.draw.arc(surface,(0,0,0),((350, 150), (100, 100)),n,v,5)
        pygame.draw.arc(surface,(0,0,0),((200, 0), (400, 400)),v,n,10)
        surface.blit(myfont2.render("SMASH", 1, (0,0,0)),(240,120))
        surface.blit(myfont2.render("SETTINGS", 1, (0,0,0)),(420,120))
        surface.blit(myfont2.render("TROPHIES", 1, (0,0,0)),(420,240))
        surface.blit(myfont2.render("ADVENTURE", 1, (0,0,0)),(220,240))
        pygame.display.update(0,0,800,400)


    if menuretour==True:
        smashretour=True
        decoretour=True
        menuretour=True
        mapretour=True
        map2retour=True
        menupr(pi,pi/2)
        choise=False
        while not choise:
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if cchois==3:
                            cchois=2
                            menupr(pi/2,2*pi)
                        if cchois==4:
                            cchois=1
                            menupr(pi,pi/2)
                    if event.key == pygame.K_DOWN:
                        if cchois==1:
                            cchois=4
                            menupr(3*pi/2,pi)
                        if cchois==2:
                            cchois=3
                            menupr(0,3*pi/2)
                    if event.key == pygame.K_LEFT:
                        if cchois==2:
                            cchois=1
                            menupr(pi,pi/2)
                        if cchois==3:
                            cchois=4
                            menupr(3*pi/2,pi)
                    if event.key == pygame.K_RIGHT:
                        if cchois==1:
                            cchois=2
                            menupr(pi/2,2*pi)
                        if cchois==4:
                            cchois=3
                            menupr(0,3*pi/2)
                if event.type == pygame.QUIT:
                    game= True
                    smashretour=False
                    choise=True
                    map2retour=False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game= True
                        smashretour=False
                        choise=True
                        map2retour=False
                    if event.key == pygame.K_RETURN:
                        choise=True
                        if cchois==1:
                            menusmash=False
                        elif cchois==2:
                            menuoption=False
                        elif cchois==3:
                            menutrophes=False
                        elif cchois==4:
                            menuhistoire=False

    def chperso(p):
        chpero1 = pygame.image.load("perso/"+str(p[0])+"/1.png").convert_alpha()
        chpero1 = pygame.transform.scale(chpero1, (70 , 100))
        if playernumber==2:
            surface.blit(chpero1,(100,250))
        if battleunlock==False:
            chpero2 = pygame.image.load("perso/"+str(p[1])+"/1.png").convert_alpha()
            chpero2 = pygame.transform.scale(chpero2, (70 , 100))
            if playernumber==2:
                surface.blit(chpero2,(600,250))
            if playernumber==3:
                surface.blit(chpero1,(100,250))
                surface.blit(chpero2,(350,250))
                chpero3 = pygame.image.load("perso/"+str(p[2])+"/1.png").convert_alpha()
                chpero3 = pygame.transform.scale(chpero3, (70 , 100))
                surface.blit(chpero3,(600,250))
            if playernumber==4:
                surface.blit(chpero1,(100,250))
                surface.blit(chpero2,(250,250))
                chpero3 = pygame.image.load("perso/"+str(p[2])+"/1.png").convert_alpha()
                chpero3 = pygame.transform.scale(chpero3, (70 , 100))
                surface.blit(chpero3,(400,250))
                chpero4 = pygame.image.load("perso/"+str(p[3])+"/1.png").convert_alpha()
                chpero4 = pygame.transform.scale(chpero4, (70 , 100))
                surface.blit(chpero4,(600,250))
        if p[0]==1:
            pygame.draw.rect(surface,(0,0,255),(170,20,70,90),2)
        elif p[0]==2 and deblocage>=2:
            pygame.draw.rect(surface,(0,0,255),(270,20,70,90),2)
        elif p[0]==3 and deblocage>=3:
            pygame.draw.rect(surface,(0,0,255),(370,20,70,90),2)
        elif p[0]==4 and deblocage>=4:
            pygame.draw.rect(surface,(0,0,255),(470,20,70,90),2)
        elif p[0]==5 and deblocage>=5:
            pygame.draw.rect(surface,(0,0,255),(570,20,70,90),2)
        elif p[0]==6 and deblocage>=6:
            pygame.draw.rect(surface,(0,0,255),(170,120,70,90),2)
        elif p[0]==7 and deblocage>=7:
            pygame.draw.rect(surface,(0,0,255),(270,120,70,90),2)
        elif p[0]==8 and deblocage>=8:
            pygame.draw.rect(surface,(0,0,255),(370,120,70,90),2)
        elif p[0]==9 and deblocage>=9:
            pygame.draw.rect(surface,(0,0,255),(470,120,70,90),2)
        elif p[0]==10 and deblocage>=10:
            pygame.draw.rect(surface,(0,0,255),(570,120,70,90),2)
        if battleunlock==False:
            if p[1]==1:
                pygame.draw.rect(surface,(0,255,0),(172,22,68,88),2)
            elif p[1]==2 and deblocage>=2:
                pygame.draw.rect(surface,(0,255,0),(272,22,68,88),2)
            elif p[1]==3 and deblocage>=3:
                pygame.draw.rect(surface,(0,255,0),(372,22,68,88),2)
            elif p[1]==4 and deblocage>=4:
                pygame.draw.rect(surface,(0,255,0),(472,22,68,88),2)
            elif p[1]==5 and deblocage>=5:
                pygame.draw.rect(surface,(0,255,0),(572,22,68,88),2)
            elif p[1]==6 and deblocage>=6:
                pygame.draw.rect(surface,(0,255,0),(172,122,68,88),2)
            elif p[1]==7 and deblocage>=7:
                pygame.draw.rect(surface,(0,255,0),(272,122,68,88),2)
            elif p[1]==8 and deblocage>=8:
                pygame.draw.rect(surface,(0,255,0),(372,122,68,88),2)
            elif p[1]==9 and deblocage>=9:
                pygame.draw.rect(surface,(0,255,0),(472,122,68,88),2)
            elif p[1]==10 and deblocage>=10:
                pygame.draw.rect(surface,(0,255,0),(572,122,68,88),2)
    def chmap(m1):
        cmap= pygame.image.load("map/"+str(m1)+"/1.png").convert_alpha()
        cmap= pygame.transform.scale(cmap, (280 , 140))
        surface.blit(cmap,(10,137))
        if m1==1:
            pygame.draw.rect(surface,(255,0,0),(305,5,160,90),2)
        elif m1==2:
            pygame.draw.rect(surface,(255,0,0),(475,5,160,90),2)
        elif m1==3:
            pygame.draw.rect(surface,(255,0,0),(645,5,160,90),2)
        elif m1==4:
            pygame.draw.rect(surface,(255,0,0),(305,155,160,90),2)
    if menutrophes==False:
        trophe =pygame.image.load('all/trophe.png').convert_alpha()
        trophe = pygame.transform.scale(trophe, (300 , 350))
        myfont5 = pygame.font.SysFont("monospace", 30)
        nope = myfont5.render("tu n'as aucun trophÃ©e", 1, (0,0,0))
        yep = myfont5.render("tu a terminÃ© le jeu a 100%", 1, (0,0,0))
        while not menutrophes:
            surface.fill((255,215,0))
            if deblocage==10:
                surface.blit(trophe,(250,0))
                surface.blit(yep,(150,350))
            else:
                surface.blit(nope,(200,200))
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        smashretour=False
                        decoretour=False
                        menutrophes=True
                        map2retour=False
                        cchois=1
            pygame.display.update(0,0,800,400)


















    if menuoption==False:
        yes =pygame.image.load('all/buttonyes.png').convert_alpha()
        yes = pygame.transform.scale(yes, (200 , 100))
        no =pygame.image.load('all/buttonno.png').convert_alpha()
        no = pygame.transform.scale(no, (200 , 100))
        ccb=1
        option1=musique
        option2=True
        option3=animation
        myfont3 = pygame.font.SysFont("monospace", 30)
        op1 = myfont3.render("music", 1, (250,250,250))
        op2 = myfont3.render("codes", 1, (250,250,250))
        op3 = myfont3.render("animations de fin", 1, (250,250,250))
        while not menuoption:
            surface.fill((0,191,255))
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if ccb>1:
                            ccb-=1
                    if event.key == pygame.K_DOWN:
                        if ccb<3:
                            ccb+=1
                    if event.key == pygame.K_LEFT:
                        if ccb==1:
                            if option1==True:
                                pygame.mixer.music.stop()
                                musique=False
                                option1=False
                        if ccb==3:
                            if option3==True:
                                animation=False
                                option3=False       
                    if event.key == pygame.K_RIGHT:
                        if ccb==1:
                            if option1==False:
                                pygame.mixer.music.load("all/menumusic.mp3")
                                pygame.mixer.music.play(-1)
                                musique=True
                                option1=True
                        if ccb==3:
                            if option3==False:
                                animation=True
                                option3=True
                    if event.key == pygame.K_RETURN:
                        if ccb==2:
                            bal=False
                            ccf= input('code : ')
                            if ccf=="bac":
                                Dept=[11,10,True]
                                Fichier = open('data.txt','wb')
                                pickle.dump(Dept,Fichier)
                                Fichier.close()
                                deblocage=Dept[1]
                                avancement=Dept[0]
                                musique=Dept[2]
                    if event.key == pygame.K_ESCAPE:
                        smashretour=False
                        decoretour=False
                        menuoption=True
                        map2retour=False
                        cchois=1
            if ccb==1:
                pygame.draw.rect(surface,(100,200,210),(100,0,600,100))
            if ccb==2:
                pygame.draw.rect(surface,(100,200,210),(100,100,600,100))
            if ccb==3:
                pygame.draw.rect(surface,(100,200,210),(100,200,600,100))
            surface.blit(op1,(100,30))
            surface.blit(op2,(100,130))
            surface.blit(op3,(100,230))



            if option1==True:
                surface.blit(yes,(400,0))
            if option1==False:
                surface.blit(no,(400,0))
            if option3==True:
                surface.blit(yes,(400,200))
            if option3==False:
                surface.blit(no,(400,200))

            pygame.display.update(0,0,800,400)


    if menuhistoire==False:
        fond =pygame.image.load('story/map.png').convert_alpha()
        fond = pygame.transform.scale(fond, (2400 , 1200))
        perso1 =pygame.image.load('perso/1/1.png').convert_alpha()
        perso1 = pygame.transform.scale(perso1, (30 , 30))
        perso1 = pygame.transform.rotate(perso1,40)
        perso2 = pygame.transform.flip(perso1, 1,0)
        perso2 = pygame.transform.rotate(perso2,80)
        xm=0
        avanckey=0




        avancement=Dept[0]

        cloud1=pygame.image.load('story/cloud.png').convert_alpha()
        cloud1 = pygame.transform.scale(cloud1, (2400 , 1200))


        ym=-775
        haut=False
        bas=False
        perso=perso1
        while not menuhistoire:
            surface.blit(fond,(xm,ym))
            surface.blit(perso,(300,275))
            if avancement==0:
                surface.blit(cloud1,(0,ym-350))
                surface.blit(cloud1,(xm+550,0))
            if avancement==1:
                surface.blit(cloud1,(0,ym-450))
                surface.blit(cloud1,(xm+700,0))
            if avancement==2:
                surface.blit(cloud1,(0,ym-550))
                surface.blit(cloud1,(xm+850,0))
            if avancement==3:
                surface.blit(cloud1,(0,ym-600))
                surface.blit(cloud1,(xm+1000,0))
            if avancement==4:
                surface.blit(cloud1,(0,ym-700))
                surface.blit(cloud1,(xm+1150,0))
            if avancement==5:
                surface.blit(cloud1,(0,ym-750))
                surface.blit(cloud1,(xm+1300,0))
            if avancement==6:
                surface.blit(cloud1,(0,ym-800))
                surface.blit(cloud1,(xm+1400,0))
            if avancement==7:
                surface.blit(cloud1,(0,ym-900))
                surface.blit(cloud1,(xm+1550,0))
            if avancement==8:
                surface.blit(cloud1,(0,ym-950))
                surface.blit(cloud1,(xm+1700,0))
            if avancement==9:
                surface.blit(cloud1,(0,ym-1000))
                surface.blit(cloud1,(xm+1800,0))
            if avancement==10:
                surface.blit(cloud1,(0,ym-1100))
                surface.blit(cloud1,(xm+1970,0))
            pygame.display.update(0,0,800,400)
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        haut=True
                        bas=False
                    if event.key == pygame.K_LEFT:
                        bas=True
                        haut=False
                    if event.key == pygame.K_RETURN:
                        menuhistoire=True
                        menusmash=False
                        bot2=True
                        battleunlock=True
                        p[1]=bbot
                    if event.key == pygame.K_ESCAPE:
                        smashretour=False
                        decoretour=False
                        menuhistoire=True
                        map2retour=False
                        cchois=1



            if haut==True and ym<0 and avanckey<avancement:
                xm-=2
                ym+=1
                perso=perso1
            if bas==True and xm<0 and ym<10 and avancement>0 :
                xm+=2
                ym-=1
                perso=perso2
            if xm==-150:
                avanckey=0
                bas=False
                haut=False
                bbot=1
            if xm==-300:
                avanckey=1
                bas=False
                haut=False
                bbot=2
            if xm==-450:
                avanckey=2
                bas=False
                haut=False
                bbot=3
            if xm==-600:
                avanckey=3
                bas=False
                haut=False
                bbot=4
            if xm==-750:
                avanckey=4
                bas=False
                haut=False
                bbot=5
            if xm==-900:
                avanckey=5
                bas=False
                haut=False
                bbot="Boss1"
            if xm==-1050:
                avanckey=6
                bas=False
                haut=False
                bbot=6
            if xm==-1150:
                avanckey=7
                bas=False
                haut=False
                bbot=7
            if xm==-1300:
                avanckey=8
                bas=False
                haut=False
                bbot=8
            if xm==-1450:
                avanckey=9
                bas=False
                haut=False
                bbot=9
            if xm==-1550:
                avanckey=10
                bas=False
                haut=False
                bbot="Boss2"



    if menusmash==False:
        smashretour=True
        decoretour=True
        menuretour=True
        mapretour=True
        map2retour=True
        myfont6 = pygame.font.SysFont("monospace", 20)
        surface = pygame.display.set_mode((800,400))
        multi=False
        ico1 = pygame.image.load('perso/1/1.png').convert_alpha()
        ico1 = pygame.transform.scale(ico1, (60 , 80))
        ico2 = pygame.image.load('perso/2/1.png').convert_alpha()
        ico2 = pygame.transform.scale(ico2, (60 , 80))
        ico3 = pygame.image.load('perso/3/1.png').convert_alpha()
        ico3 = pygame.transform.scale(ico3, (60 , 80))
        ico4 = pygame.image.load('perso/4/1.png').convert_alpha()
        ico4 = pygame.transform.scale(ico4, (60 , 80))
        ico5 = pygame.image.load('perso/5/1.png').convert_alpha()
        ico5 = pygame.transform.scale(ico5, (60 , 80))
        ico6 = pygame.image.load('perso/6/1.png').convert_alpha()
        ico6 = pygame.transform.scale(ico6, (60 , 80))
        ico7 = pygame.image.load('perso/7/1.png').convert_alpha()
        ico7 = pygame.transform.scale(ico7, (60 , 80))
        ico8 = pygame.image.load('perso/8/1.png').convert_alpha()
        ico8 = pygame.transform.scale(ico8, (60 , 80))
        ico9 = pygame.image.load('perso/9/1.png').convert_alpha()
        ico9 = pygame.transform.scale(ico9, (60 , 80))
        ico10 = pygame.image.load('perso/10/1.png').convert_alpha()
        ico10 = pygame.transform.scale(ico10, (60 , 80))
        while not menusmash:


            surface.fill((80,80,80))
            press1 = myfont6.render("press w to ", 1, (250,250,250))
            press2 = myfont6.render("press u to ", 1, (250,250,250))
            press3 = myfont6.render("add an bot", 1, (250,250,250))
            press4 = myfont6.render("delete an bot", 1, (250,250,250))
            pygame.draw.rect(surface,(255,0,0),(0,0,800,250))
            pygame.draw.rect(surface,(255,255,255),(100,250,100,150),1)
            surface.blit(press1,(645,100))
            surface.blit(press2,(645,200))
            surface.blit(press3,(645,120))
            surface.blit(press4,(645,220))
            if battleunlock==False:
                pygame.draw.rect(surface,(255,255,255),(600,250,100,150),1)
            if playernumber==3:
                pygame.draw.rect(surface,(255,255,255),(350,250,100,150),1)
            if playernumber==4:
                pygame.draw.rect(surface,(255,255,255),(400,250,100,150),1)
                pygame.draw.rect(surface,(255,255,255),(250,250,100,150),1)
            pygame.draw.rect(surface,(80,80,80),(170,20,70,90))
            surface.blit(ico1,(170,20))
            if deblocage>=2:
                pygame.draw.rect(surface,(80,80,80),(270,20,70,90))
                surface.blit(ico2,(270,20))
            if deblocage>=3:
                pygame.draw.rect(surface,(80,80,80),(370,20,70,90))
                surface.blit(ico3,(370,20))
            if deblocage>=4:
                pygame.draw.rect(surface,(80,80,80),(470,20,70,90))
                surface.blit(ico4,(470,20))
            if deblocage>=5:
                pygame.draw.rect(surface,(80,80,80),(570,20,70,90))
                surface.blit(ico5,(570,20))
            if deblocage>=6:
                pygame.draw.rect(surface,(80,80,80),(170,120,70,90))
                surface.blit(ico6,(170,120))
            if deblocage>=7:
                pygame.draw.rect(surface,(80,80,80),(270,120,70,90))
                surface.blit(ico7,(270,120))
            if deblocage>=8:
                pygame.draw.rect(surface,(80,80,80),(370,120,70,90))
                surface.blit(ico8,(370,120))
            if deblocage>=9:
                pygame.draw.rect(surface,(80,80,80),(470,120,70,90))
                surface.blit(ico9,(470,120))
            if deblocage>=10:
                pygame.draw.rect(surface,(80,80,80),(570,120,70,90))
                surface.blit(ico10,(570,120))

            chperso(p)

            pygame.display.update(0,0,800,400)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:

                        p[0]-=5
                        if p[0]<1:
                            p[0]=1
                            sonvic=pygame.mixer.Sound("perso/"+str(p[0])+"/1.wav")
                            sonvic.play()
                    if event.key == pygame.K_DOWN:
                        p[0]+=5
                        if p[0]>deblocage:
                            p[0]=deblocage
                            sonvic=pygame.mixer.Sound("perso/"+str(p[0])+"/1.wav")
                            sonvic.play()
                    if event.key == pygame.K_LEFT:
                        if p[0]>1:
                            p[0]-=1
                            sonvic=pygame.mixer.Sound("perso/"+str(p[0])+"/1.wav")
                            sonvic.play()
                    if event.key == pygame.K_RIGHT:
                        if p[0]<deblocage:
                            p[0]+=1
                            sonvic=pygame.mixer.Sound("perso/"+str(p[0])+"/1.wav")
                            sonvic.play()
                    if event.key == pygame.K_ESCAPE:
                        smashretour=False
                        decoretour=False
                        mapretour=False
                        map2retour=False
                        menusmash=True
                        battleunlock=False
                        bot2=False
                        cchois=1
                    if battleunlock==False:
                        if event.key == pygame.K_w:

                            p[1]-=5
                            if p[1]<1:
                                p[1]=1
                                sonvic=pygame.mixer.Sound("perso/"+str(p[1])+"/1.wav")
                                sonvic.play()
                        if event.key == pygame.K_s:
                            p[1]+=5
                            if p[1]>deblocage:
                                p[1]=deblocage
                                sonvic=pygame.mixer.Sound("perso/"+str(p[1])+"/1.wav")
                                sonvic.play()

                        if event.key == pygame.K_a:
                            if p[1]>1:
                                p[1]-=1
                                sonvic=pygame.mixer.Sound("perso/"+str(p[1])+"/1.wav")
                                sonvic.play()
                        if event.key == pygame.K_z:

                            if playernumber<4:
                                playernumber+=1
                                if playernumber==3:
                                    p[2]=random.randint(1,deblocage)
                                    bot3=True
                                if playernumber==4:
                                    p[3]=random.randint(1,deblocage)
                                    bot4=True
                        if event.key == pygame.K_u:
                            if playernumber>2:
                                playernumber-=1
                                if playernumber==3:
                                    bot4=False
                                if playernumber==2:
                                    bot3=False
                        if event.key == pygame.K_d:
                            if p[1]<deblocage:
                                p[1]+=1
                                sonvic=pygame.mixer.Sound("perso/"+str(p[1])+"/1.wav")
                                sonvic.play()
                       

                    if event.key == pygame.K_RETURN:
                        menusmash=True
        if mapretour==True:
            menumap=False
            if p[1]=="Boss1" or p[1]=="Boss2":
                menumap=True
            m1=1

            map1 = pygame.image.load("map/1/1.png").convert_alpha()
            map1= pygame.transform.scale(map1,(150,75))
            map2 = pygame.image.load("map/2/1.png").convert_alpha()
            map2= pygame.transform.scale(map2,(150,75))
            map3= pygame.image.load("map/3/1.png").convert_alpha()
            map3= pygame.transform.scale(map3,(150,75))
            map4= pygame.image.load("map/4/1.png").convert_alpha()
            map4= pygame.transform.scale(map4,(150,75))
            deb=0
            while not menumap:
                surface.fill((0,191,255))
                pygame.draw.rect(surface,(128,128,128),(300,0,500,400))
                surface.blit(map1,(310,10))
                surface.blit(map2,(480,10))
                surface.blit(map3,(650,10))
                surface.blit(map4,(310,160))
                chmap(m1)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            if deb==0 or deb==1 :
                                deb+=1
                            else:
                                deb=0
                            if m1-3>=1:
                                m1-=3
                        if event.key == pygame.K_DOWN:
                            if m1+3<=4:
                                m1+=3
                            if deb==2 or deb==7 or deb==8 or deb==9:
                                deb+=1
                            else:
                                deb=0
                        if event.key == pygame.K_LEFT:
                            if m1>1:
                                m1-=1
                            if deb==3:
                                deb+=1
                            else:
                                deb=0
                        if event.key == pygame.K_RIGHT:
                            if m1<4:
                                m1+=1

                            if deb==4 or deb==5 or deb==6:
                                deb+=1
                            else:
                                deb=0
                        if event.key == pygame.K_RETURN:
                            menumap=True
                            map=m1
                        if event.key == pygame.K_ESCAPE:
                            menumap=True
                            smashretour=False
                            decoretour=False
                            menuretour=False
                            mapretour=False
                            map2retour=False
                            menusmash=False
                if deb==10 and deblocage==9:
                    deblocage=10
                    print("Nouveau personnage dÃ©bloquÃ©")
                pygame.display.update(0,0,800,400)

    if map2retour==True:
        pygame.mixer.music.stop()
        braises= pygame.image.load("all/braises.png").convert_alpha()
        braises = pygame.transform.scale(braises,(800,2244))
        logo = pygame.image.load('all/logos.png').convert_alpha()
        versus= pygame.mixer.Sound("all/versus.wav")
        versus.play()
        for y in range(1,350):
            clock.tick(500)
            surface.fill((0,0,0))
            logo1 = pygame.transform.scale(logo,(2*y,y))
            surface.blit(logo1,(400-y,175-0.5*y))
            pygame.display.update(0,0,800,450)
        if playernumber==2:
            chperoc1 = pygame.image.load("perso/"+str(p[0])+"/1.png").convert_alpha()
            chperoc1 = pygame.transform.scale(chperoc1, (300 , 450))
            chperoc2 = pygame.image.load("perso/"+str(p[1])+"/1.png").convert_alpha()
            chperoc2 = pygame.transform.scale(chperoc2, (300 , 450))

            for y in range(1,2000):
                clock.tick(1000)
                surface.fill((0,0,0))
                pygame.draw.rect(surface,(139,0,0),(0,0,390,450))
                pygame.draw.rect(surface,(70,130,180),(410,0,390,450))
                surface.blit(chperoc1,(0,0))
                surface.blit(chperoc2,(400,0))
                surface.blit(braises,(0,0-y))
                pygame.display.update(0,0,800,450)
        if playernumber==3:
            chperoc1 = pygame.image.load("perso/"+str(p[0])+"/1.png").convert_alpha()
            chperoc1 = pygame.transform.scale(chperoc1, (200 , 350))
            chperoc2 = pygame.image.load("perso/"+str(p[1])+"/1.png").convert_alpha()
            chperoc2 = pygame.transform.scale(chperoc2, (200 , 350))
            chperoc3 = pygame.image.load("perso/"+str(p[2])+"/1.png").convert_alpha()
            chperoc3 = pygame.transform.scale(chperoc3, (200 , 350))
            for y in range(1,2000):
                clock.tick(1000)
                surface.fill((0,0,0))
                pygame.draw.rect(surface,(139,0,0),(0,0,260,450))
                pygame.draw.rect(surface,(70,130,180),(270,0,260,450))
                pygame.draw.rect(surface,(189,183,107),(546,0,254,450))
                surface.blit(chperoc1,(0,0))
                surface.blit(chperoc2,(255,0))
                surface.blit(chperoc3,(510,0))
                surface.blit(braises,(0,0-y))
                pygame.display.update(0,0,800,450)
        if playernumber==4:
            chperoc1 = pygame.image.load("perso/"+str(p[0])+"/1.png").convert_alpha()
            chperoc1 = pygame.transform.scale(chperoc1, (190 , 350))
            chperoc2 = pygame.image.load("perso/"+str(p[1])+"/1.png").convert_alpha()
            chperoc2 = pygame.transform.scale(chperoc2, (190 , 350))
            chperoc3 = pygame.image.load("perso/"+str(p[2])+"/1.png").convert_alpha()
            chperoc3 = pygame.transform.scale(chperoc3, (190 , 350))
            chperoc4 = pygame.image.load("perso/"+str(p[3])+"/1.png").convert_alpha()
            chperoc4 = pygame.transform.scale(chperoc4, (190 , 350))

            for y in range(1,2000):
                clock.tick(1000)
                surface.fill((0,0,0))
                pygame.draw.rect(surface,(139,0,0),(0,0,190,450))
                pygame.draw.rect(surface,(70,130,180),(210,0,190,450))
                pygame.draw.rect(surface,(189,183,107),(410,0,190,450))
                pygame.draw.rect(surface,(107,142,35),(610,0,190,450))
                surface.blit(chperoc1,(0,50))
                surface.blit(chperoc2,(210,50))
                surface.blit(chperoc3,(410,50))
                surface.blit(chperoc4,(610,50))
                surface.blit(braises,(0,0-y))
                pygame.display.update(0,0,800,450)











        if p[1]=="Boss1" and bosspart1==1:
            bosspart1=2


        if p[1]=="Boss1" and bosspart1==0:
            bosspart1=1







        surfaceW = 800
        surfaceH = 450

        if map==1:
            platform = [1,250,280,100,700]
            pw = [50,50,50,50]
            ph = [70,70,70,70]
            x=[250,530,300,400]
            y=[180,180,180,180]
            if musique==True:
                pygame.mixer.music.load("map/1/music.mp3")
                pygame.mixer.music.play(-1)
        elif map==2:
            platform = [10,260,290,-300,80,400,600,-300,145,300,315,147,231,400,600,238,558,400,600,650,1100,178,205,250,344,178,205,447,545,288,318,285,509,300,315,559,649,260,290,715,1100]
            pw = [35,35,35,35]
            ph = [49,49,49,49]
            x=[190,600,300,450]
            y=[260,260,260,260]
            if musique==True:
                pygame.mixer.music.load("map/2/music.mp3")
                pygame.mixer.music.play(-1)
        elif map==3:
            platform = [5,360,450,-300,1100,318,450,115,690,290,450,125,210,290,450,590,680,35,75,230,570]
            pw=[40,40,40,40]
            ph=[56,56,56,56]
            x=[160,650,300,450]
            y=[240,240,240,240]
            if musique==True:
                pygame.mixer.music.load("map/3/music.mp3")
                pygame.mixer.music.play(-1)
        elif map==4:
            platform = [8,363,600,253,544,-100,-40,427,486,-100,-40,486,543,-100,-70,282,399,-70,-40,253,340,-100,-70,253,282,-70,-40,340,428,-100,-70,398,428]
            pw=[35,35,35,35]
            ph=[49,49,49,49]
            x=[323,460,390,420]
            y=[325,325,325,325]
            tblock1 = pygame.image.load('map/4/block/1.png').convert()
            tblock1 = pygame.transform.scale(tblock1,(29*4,29))
            tblock2 = pygame.image.load('map/4/block/2.png').convert_alpha()
            tblock2 = pygame.transform.scale(tblock2,(29*3,29*2))
            tblock3 = pygame.image.load('map/4/block/3.png').convert_alpha()
            tblock3 = pygame.transform.scale(tblock3,(29*3,29*2))
            tblock4 = pygame.image.load('map/4/block/4.png').convert()
            tblock4 = pygame.transform.scale(tblock4,(29*2,29*2))
            if musique==True:
                pygame.mixer.music.load("map/4/music.mp3")
                pygame.mixer.music.play(-1)
        if p[1]=="Boss1" and bosspart1==1:
            map=664
            platform=[35,390,600,0,2140,390,600,2200,2670,390,600,2760,4748,390,600,4810,6577,265,295,497,528,265,295,620,776,141,170,683,714,325,600,868,932,298,600,1179,1240,265,600,1427,1489,264,600,1770,1830,233,262,1985,2016,265,294,2390,2483,265,294,2917,2946,265,294,3103,3164,140,171,2481,2732,140,171,2822,2947,265,294,3292,3320,265,294,3383,3413,265,294,3475,3506,265,294,3661,3694,265,294,4004,4065,140,170,3382,3414,140,170,3753,3847,140,170,3972,4097,264,600,4189,4282,264,600,4345,4438,264,600,4623,4747,264,600,4810,4902,329,600,5058,5118,265,294,5213,5338,328,600,5555,5617,264,600,5647,5897,138,600,5740,5896,357,600,6144,6177]
            pw=[50,10]
            ph=[70,10]
            x=[600,-100]
            y=[200,200]
            if musique==True:
                pygame.mixer.music.load("perso/Boss1/earrape.wav")
                pygame.mixer.music.play(-1)
        if p[1]=="Boss1" and bosspart1==2:
            map=665
            platform=[1,265,410,177,620]
            pw=[35,200]
            ph=[49,100]
            x=[200,600]
            y=[100,100]
            bot2=True
            if musique==True:
                pygame.mixer.music.load("perso/Boss1/bossbattle.wav")
                pygame.mixer.music.play(-1)
        if p[1]=="Boss2":
            map=666
            platform=[1,265,410,177,620]
            pw=[35,100]
            ph=[49,100]
            x=[200,600]
            y=[100,100]
            if musique==True:
                pygame.mixer.music.load("perso/Boss2/bossbattle.wav")
                pygame.mixer.music.play(-1)




        surface = pygame.display.set_mode((surfaceW,surfaceH))#fenetre graph[0]ique
        pygame.display.set_caption("smash")#nom
        fond = pygame.image.load("map/"+str(map)+"/1.png").convert()#fond
        fond = pygame.transform.scale(fond,(800,450))
        if p[1]=="Boss1" and bosspart1==1:
            fond = pygame.image.load("map/664/1.png").convert()#fond
            fond = pygame.transform.scale(fond,(6579,450))
            iconethomas= pygame.image.load("perso/Boss1/lvl1.png").convert_alpha()#fond
            iconethomas = pygame.transform.scale(iconethomas,(333,450))
        surface.blit(fond,(0,0))
        pygame.display.flip()

        image1 = pygame.image.load("perso/"+str(p[0])+"/1.png").convert_alpha()#charge une image
        image1 = pygame.transform.scale(image1,(pw[0],ph[0]))
        image12= pygame.image.load("perso/"+str(p[0])+"/2.png").convert_alpha()#charge une image
        image12 = pygame.transform.scale(image12,(pw[0],ph[0]))
        image22 = pygame.transform.flip(image12, 1 , 0)#retourne l image
        image2 = pygame.transform.flip(image1, 1 , 0)#retourne l image
        image4 = pygame.image.load("perso/"+str(p[1])+"/1.png").convert_alpha()#charge une image
        image4 = pygame.transform.scale(image4,(pw[1],ph[1]))
        image42= pygame.image.load("perso/"+str(p[1])+"/2.png").convert_alpha()#charge une image
        image42 = pygame.transform.scale(image42,(pw[1],ph[1]))
        image32 = pygame.transform.flip(image42, 1 , 0)#retourne l image
        image3 = pygame.transform.flip(image4, 1 , 0)#retourne l image
        if playernumber>=3:
            image5 = pygame.image.load("perso/"+str(p[2])+"/1.png").convert_alpha()#charge une image
            image5 = pygame.transform.scale(image5,(pw[0],ph[2]))
            image52= pygame.image.load("perso/"+str(p[2])+"/2.png").convert_alpha()#charge une image
            image52 = pygame.transform.scale(image52,(pw[2],ph[2]))
            image62 = pygame.transform.flip(image52, 1 , 0)#retourne l image
            image6 = pygame.transform.flip(image5, 1 , 0)#retourne l image
            coup32= pygame.image.load("perso/"+str(p[2])+"/attaque1.png").convert_alpha()
            coup32 = pygame.transform.scale(coup32,(pw[2],ph[2]))
            coup31 = pygame.transform.flip(coup32, 1 , 0)
        if playernumber>=3:
            image7 = pygame.image.load("perso/"+str(p[3])+"/1.png").convert_alpha()#charge une image
            image7 = pygame.transform.scale(image7,(pw[3],ph[3]))
            image72= pygame.image.load("perso/"+str(p[3])+"/2.png").convert_alpha()#charge une image
            image72 = pygame.transform.scale(image72,(pw[3],ph[3]))
            image82 = pygame.transform.flip(image72, 1 , 0)#retourne l image
            image8 = pygame.transform.flip(image7, 1 , 0)#retourne l image
            coup42= pygame.image.load("perso/"+str(p[3])+"/attaque1.png").convert_alpha()
            coup42 = pygame.transform.scale(coup42,(pw[3],ph[3]))
            coup41 = pygame.transform.flip(coup42, 1 , 0)
        coup12= pygame.image.load("perso/"+str(p[0])+"/attaque1.png").convert_alpha()
        coup12 = pygame.transform.scale(coup12,(pw[0],ph[0]))
        coup11 = pygame.transform.flip(coup12, 1 , 0)
        coup22= pygame.image.load("perso/"+str(p[1])+"/attaque1.png").convert_alpha()
        coup22 = pygame.transform.scale(coup22,(pw[1],ph[1]))
        coup21 = pygame.transform.flip(coup22, 1 , 0)
        ejectim=pygame.image.load("all/ejection.png").convert_alpha()
        vie1png=pygame.transform.scale(image1,(20,24))
        vie2png=pygame.transform.scale(image4,(20,24))
        gamesound= pygame.mixer.Sound("all/game.wav")

        sprite = [image1,image3]
        if playernumber>=3:
            sprite = [image1,image3,image5]
            vie3png=pygame.transform.scale(image5,(20,24))
        if playernumber==4:
            vie4png=pygame.transform.scale(image7,(20,24))
            sprite = [image1,image3,image5,image7]
        myfont = pygame.font.SysFont("monospace", 75)
        koson = pygame.mixer.Sound("all/KO.wav")

        smash_ball=pygame.image.load('all/smash_ball.png').convert_alpha()
        smash_ball = pygame.transform.scale(smash_ball,(ph[0]*2,ph[0]*2))
        counter= pygame.image.load('perso/1/attaque3.png').convert_alpha()
        counter = pygame.transform.scale(counter,(ph[0],ph[0]))

        jump = pygame.mixer.Sound("perso/1/jump.wav")
        blockim = pygame.image.load('perso/1/attaque8.png').convert_alpha()
        blockim = pygame.transform.scale(blockim,(pw[0],round(ph[0]*1.5)))
        feum = pygame.image.load('perso/1/attaque2.png').convert_alpha()
        feum = pygame.transform.scale(feum,(round(ph[0]/5),round(ph[0]/5)))
        bill = pygame.image.load('perso/1/attaque4.png').convert_alpha()
        bill = pygame.transform.scale(bill,(round(pw[0]/2),round(ph[0]/2)))
        accr = pygame.image.load('perso/1/attaque5.png').convert_alpha()
        accr1 = pygame.transform.scale(accr,(pw[0],ph[0]))
        accr2 = pygame.transform.flip(accr1,1,0)
        terre = pygame.image.load('perso/1/attaque6.png').convert_alpha()
        terre = pygame.transform.scale(terre,(pw[0]*2,round(ph[0]/2)))
        smashattq= pygame.transform.scale(feum,(pw[0]*4,pw[0]*4))

        tornadem = pygame.image.load('perso/2/attaque6.png').convert_alpha()
        tornadem = pygame.transform.scale(tornadem,(pw[0]*2,ph[0]*2))
        feulm = pygame.image.load('perso/2/attaque2.png').convert_alpha()
        feulm = pygame.transform.scale(feulm,(round(ph[0]/5),round(ph[0]/5)))
        fusee = pygame.image.load('perso/2/attaque4.png').convert_alpha()
        fusee = pygame.transform.scale(fusee,(round(pw[0]/2),round(ph[0]/2)))
        feuarti = pygame.image.load('perso/2/attaque5.png').convert_alpha()
        feuarti = pygame.transform.scale(feuarti,(pw[0]*3,pw[0]*3))
        luigilong1 = pygame.image.load('perso/2/attaque7.png').convert_alpha()
        luigilong1 = pygame.transform.scale(luigilong1,(ph[0],pw[0]))
        luigilong2 = pygame.transform.flip(luigilong1,1,0)
        sautl = pygame.image.load('perso/2/attaque8.png').convert_alpha()
        sautl = pygame.transform.scale(sautl,(ph[0],ph[0]))
        lcorps = pygame.image.load('perso/2/smash2.png').convert_alpha()
        lcorps = pygame.transform.scale(lcorps,(3*ph[0],3*ph[0]))
        luigismash1 = pygame.image.load('perso/2/smash1.png').convert_alpha()
        luigismash1 = pygame.transform.scale(luigismash1,(2*ph[0],2*ph[0]))
        luigismash2 = pygame.transform.flip(luigismash1,1,0)

        theworldsound = pygame.mixer.Sound("perso/3/zawarudo.wav")
        couteaud= pygame.image.load('perso/3/attaque2.png').convert_alpha()
        couteaud = pygame.transform.scale(couteaud,(round(ph[0]/3),round(ph[0]/3)))
        couteaug = pygame.transform.flip(couteaud,1,0)
        couteauh = pygame.transform.rotate(couteaud,90)
        lancecout0 = pygame.image.load('perso/3/attaque3.png').convert_alpha()
        lancecout0 = pygame.transform.scale(lancecout0,(pw[0],ph[0]))
        lancecout1 = pygame.transform.flip(lancecout0,1,0)
        fonc0 = pygame.image.load('perso/3/attaque4.png').convert_alpha()
        fonc0 = pygame.transform.scale(fonc0,(round(ph[0]),round(ph[0])))
        fonc1 = pygame.transform.flip(fonc0,1,0)
        pcharge0 = pygame.image.load('perso/3/attaque5.png').convert_alpha()
        pcharge0 = pygame.transform.scale(pcharge0,(pw[0],ph[0]))
        pcharge1 = pygame.transform.flip(pcharge0,1,0)
        sautdio0 = pygame.image.load('perso/3/attaque6.png').convert_alpha()
        sautdio0 = pygame.transform.scale(sautdio0,(pw[0],ph[0]))
        sautdio1 = pygame.transform.flip(sautdio0,1,0)
        pstand0 = pygame.image.load('perso/3/attaque7.png').convert_alpha()
        pstand0 = pygame.transform.scale(pstand0,(round(pw[0]*1.5),round(ph[0]+pw[0]/2)))
        pstand1 = pygame.transform.flip(pstand0,1,0)
        standcoup0 = pygame.image.load('perso/3/attaque8.png').convert_alpha()
        standcoup0 = pygame.transform.scale(standcoup0,(round(pw[0]*1.5),round(ph[0]+pw[0]/2)))
        standcoup1 = pygame.transform.flip(standcoup0,1,0)
        standfonc0 = pygame.image.load('perso/3/attaque9.png').convert_alpha()
        standfonc0 = pygame.transform.scale(standfonc0,(round(pw[0]*1.5),round(ph[0]+pw[0]/2)))
        standfonc1 = pygame.transform.flip(standfonc0,1,0)

        neterpoingh= pygame.image.load('perso/4/attaque2.png').convert_alpha()
        neterpoingh = pygame.transform.scale(neterpoingh,(round(ph[0]*2),round(ph[0]*2)))
        neterpoingb = pygame.transform.flip(neterpoingh,0,1)
        neterpoing1 = pygame.transform.rotate(neterpoingh,90)
        neterpoing0 = pygame.transform.flip(neterpoing1,1,0)
        neterhaut0 = pygame.image.load('perso/4/attaque3.png').convert_alpha()
        neterhaut0 = pygame.transform.scale(neterhaut0,(ph[0]*2,ph[0]*2))
        neterhaut1 = pygame.transform.flip(neterhaut0,1,0)
        nfonc0 = pygame.image.load('perso/4/attaque4.png').convert_alpha()
        nfonc0 = pygame.transform.scale(nfonc0,(round(ph[0]),round(ph[0])))
        nfonc1 = pygame.transform.flip(nfonc0,1,0)
        netersaut0 = pygame.image.load('perso/4/attaque5.png').convert_alpha()
        netersaut0 = pygame.transform.scale(netersaut0,(pw[0],ph[0]))
        neterhaut1 = pygame.transform.flip(netersaut0,1,0)
        shiva10 = pygame.image.load('perso/4/attaque6.png').convert_alpha()
        shiva10 = pygame.transform.scale(shiva10,(pw[0]*3,ph[0]*3))
        shiva11 = pygame.transform.flip(shiva10,1,0)
        shiva20 = pygame.image.load('perso/4/attaque7.png').convert_alpha()
        shiva20 = pygame.transform.scale(shiva20,(round(pw[0]*3),round(ph[0]*3)))
        shiva21 = pygame.transform.flip(shiva20,1,0)
        goldball = pygame.image.load('perso/4/attaque8.png').convert_alpha()
        goldball = pygame.transform.scale(goldball,(round(ph[0]*1.3),round(ph[0]*1.3)))

        cupshoot0= pygame.image.load('perso/5/attaque2.png').convert_alpha()
        cupshoot0 = pygame.transform.scale(cupshoot0,(round(ph[0]/3),round(ph[0]/3)))
        cupshoot1 = pygame.transform.flip(cupshoot0,0,1)
        cupshooth = pygame.transform.rotate(cupshoot0,90)
        cupdroit0 = pygame.image.load('perso/5/attaque3.png').convert_alpha()
        cupdroit0 = pygame.transform.scale(cupdroit0,(pw[0],ph[0]))
        cupdroit1 = pygame.transform.flip(cupdroit0,1,0)
        cuphaut0 = pygame.image.load('perso/5/attaque4.png').convert_alpha()
        cuphaut0 = pygame.transform.scale(cuphaut0,(pw[0],ph[0]))
        cuphaut1 = pygame.transform.flip(cuphaut0,1,0)
        cupfonc0 = pygame.image.load('perso/5/attaque5.png').convert_alpha()
        cupfonc0 = pygame.transform.scale(cupfonc0,(round(ph[0]),round(pw[0])))
        cupfonc1 = pygame.transform.flip(cupfonc0,1,0)
        cupsaut = pygame.image.load('perso/5/attaque6.png').convert_alpha()
        cupsaut = pygame.transform.scale(cupsaut,(ph[0],ph[0]))
        cupinv0 = pygame.image.load('perso/5/attaque7.png').convert_alpha()
        cupinv0 = pygame.transform.scale(cupinv0,(round(pw[0]*1.3),round(ph[0]/2)))
        cupinv1 = pygame.transform.flip(cupinv0,1,0)
        cuppanic = pygame.image.load('perso/5/attaque8.png').convert_alpha()
        cuppanic = pygame.transform.scale(cuppanic,(round(pw[0]),round(ph[0]/2)))

        sansshootb= pygame.image.load('perso/6/attaque2.png').convert_alpha()
        sansshootb = pygame.transform.scale(sansshootb,(round(pw[0]),round(ph[0])))
        sansshooth = pygame.transform.flip(sansshootb,0,1)
        sansshoot0 = pygame.transform.rotate(sansshootb,90)
        sansshoot1 = pygame.transform.flip(sansshoot0,1,0)
        sansshootult0 = pygame.transform.scale(sansshoot0,(round(ph[0]*2),round(pw[0]*2)))
        sansshootult1 = pygame.transform.scale(sansshoot1,(round(ph[0]*2),round(pw[0]*2)))
        sanshaut0 = pygame.image.load('perso/6/attaque3.png').convert_alpha()
        sanshaut0 = pygame.transform.scale(sanshaut0,(pw[0],ph[0]))
        sanshaut1 = pygame.transform.flip(sanshaut0,1,0)
        sansbas0 = pygame.image.load('perso/6/attaque4.png').convert_alpha()
        sansbas0 = pygame.transform.scale(sansbas0,(pw[0],ph[0]))
        sansbas1 = pygame.transform.flip(sansbas0,1,0)
        sansheart = pygame.image.load('perso/6/attaque5.png').convert_alpha()
        sansheart = pygame.transform.scale(sansheart,(round(ph[0]),round(ph[0])))

        thanothing= pygame.image.load('perso/7/1.png').convert_alpha()
        thanothing=pygame.transform.scale(thanothing,(round(0),round(0)))
        clack=pygame.mixer.Sound("perso/7/clack.wav")

        crashshoot= pygame.image.load('perso/8/attaque2.png').convert_alpha()
        crashshoot = pygame.transform.scale(crashshoot,(round(pw[0]/2),round(ph[0]/2)))
        crashhaut0 = pygame.image.load('perso/8/attaque3.png').convert_alpha()
        crashhaut0 = pygame.transform.scale(crashhaut0,(pw[0],pw[0]))
        crashfonc0 = pygame.image.load('perso/8/attaque4.png').convert_alpha()
        crashfonc0 = pygame.transform.scale(crashfonc0,(ph[0],ph[0]))
        crashfonc1 = pygame.transform.flip(crashfonc0,1,0)
        crashtornade = pygame.image.load('perso/8/attaque5.png').convert_alpha()
        crashtornade = pygame.transform.scale(crashtornade,(round(ph[0]),round(ph[0])))

        jameshoot0= pygame.image.load('perso/9/attaque2.png').convert_alpha()
        jameshoot0 = pygame.transform.scale(jameshoot0,(round(pw[0]),round(ph[0])))
        jameshoot1 = pygame.transform.flip(jameshoot0,1,0)
        jamehaut0 = pygame.image.load('perso/9/attaque3.png').convert_alpha()
        jamehaut0 = pygame.transform.scale(jamehaut0,(pw[0],ph[0]))
        jamehaut1 = pygame.transform.flip(jamehaut0,1,0)
        jamesaut0 = pygame.image.load('perso/9/attaque4.png').convert_alpha()
        jamesaut0 = pygame.transform.scale(jamesaut0,(pw[0],ph[0]))
        jamesaut1 = pygame.transform.flip(jamesaut0,1,0)
        explode = pygame.image.load('perso/9/attaque5.png').convert_alpha()
        explode = pygame.transform.scale(explode,(round(ph[0]),round(ph[0])))
        jamecout0= pygame.image.load('perso/9/attaque6.png').convert_alpha()
        jamecout0 = pygame.transform.scale(jamecout0,(round(ph[0]/2),round(pw[0]/2)))
        jamecout1 = pygame.transform.flip(jamecout0,1,0)

        trumpshoot0= pygame.image.load('perso/10/attaque2.png').convert_alpha()
        trumpshoot0 = pygame.transform.scale(trumpshoot0,(round(pw[0]),round(pw[0])))
        trumpshoot1 = pygame.transform.flip(trumpshoot0,1,0)
        trumphaut0 = pygame.image.load('perso/10/attaque3.png').convert_alpha()
        trumphaut0 = pygame.transform.scale(trumphaut0,(pw[0],ph[0]))
        trumpwall = pygame.image.load('perso/10/attaque4.png').convert_alpha()
        trumpwall = pygame.transform.scale(trumpwall,(pw[0],ph[0]))
        batomique = pygame.image.load('perso/10/attaque5.png').convert_alpha()
        batomique = pygame.transform.scale(batomique,(round(ph[0]*6),round(pw[0]*6)))





    def main(surface,game_over):
        global pourc,vie,x,y,charge,bosspart1,ballpv,balexist,platform,fond

        y_move=[0,0,0,0]
        x_move=[0,0,0,0]
        saut = [0,0,0,0]
        dir=[0,0,0,0]
        eject=[None,None,None,None]
        pourc=[0,0,0,0]
        nsaut=[0,0,0,0]
        ejetem1=[0,0,0,0]
        ejetem2=[0,0,0,0]
        ejetem3=[0,0,0,0]
        pejectx=[0,0,0,0]
        pejecty=[0,0,0,0]
        vie=[3,3,3,3]
        pp=[False,False,False,False]
        dx=[0,0,0,0]
        dy=[0,0,0,0]
        block=[0,0,0,0]
        blockx=[0,0,0,0]
        blocky=[0,0,0,0]
        blockxx=[0,0,0,0]
        blockyx=[0,0,0,0]
        dbouclier=[False,False,False,False]
        bouclier=[10000,10000,10000,10000]
        feu=[False,False,False,False]
        naopp=0
        naoppm=0
        chratt2=[0,0,0,0]
        haut=[False,False,False,False]
        bas=[False,False,False,False]
        gauche=[False,False,False,False]
        droite=[False,False,False,False]
        norm=[False,False,False,False]
        spe=[False,False,False,False]
        chratt3=[False,False,False,False]
        billx=[0,0,0,0]
        billy=[0,0,0,0]
        billt=[0,0,0,0]
        billmt=[0,0,0,0]
        enbas=[0,0,0,0]
        enterre=[0,0,0,0]
        enterret=[0,0,0,0]
        terrex=[0,0,0,0]
        terrey=[0,0,0,0]
        spritem=[0,0,0,0]
        sprint=[0,0,0,0]
        sprintt=[0,0,0,0]
        charge=[0,0,0,0]
        chargenorm=[False,False,False,False]
        chargego=[False,False,False,False]
        ballpv=0
        balexist=False
        objet=[None,None,None,None]
        ballrand=0
        smash=[0,0,0,0]
        smashattqx=[0,0,0,0]
        smashattqy=[0,0,0,0]
        smashattqdir=[0,0,0,0]
        artifice=[0,0,0,0]
        feul=[False,False,False,False]
        tornade=[0,0,0,0]
        ltourn=[False,False,False,False]
        hautl=[False,False,False,False]
        basl=[False,False,False,False]
        normpause=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        botenb=[0,0,0,0]
        standcharge=[0,0,0,0]
        stand=[False,False,False,False]
        standt=[0,0,0,0]
        standvue=[0,0,0,0]
        world=[0,0,0,0]
        sansray=[0,0,0,0]
        tlockx=[0,0,0,0]
        tlocky=[0,0,0,0]
        tlock=[False,False,False,False]
        coupfeu=[5000,5000,5000,5000]
        poison=[0,0,0,0]
        avancementmap=0
        pausemult=1
        tetris=0

        def propulse(dir,pourc):
            l =pourc*2.5/500
            h=-pourc/500
            if dir == 1:
                l= -l

            loup=[l,h,500]
            return loup
        def prox(x1,x2,y1,y2,dir1,dir2,eject,stand,pourc,charge):


            if dir1 == 1:
                if x1> x2 and x1< x2+pw[1]:
                    if y1> y2-ph[1] and y1<y2+ph[1]:
                        pourc+=10+round(charge)
                        eject=propulse(dir1,pourc)

                        if stand==True:
                            eject[2]*=2
                return eject,pourc
            elif dir1 == 0:
                if x1+pw[1]*2> x2 and x1< x2:
                    if y1> y2-ph[1] and y1<y2+ph[1]:
                        pourc+=10+round(charge)
                        eject=propulse(dir1,pourc)

                        if stand==True:
                            eject[2]*=2
                return eject,pourc

        def ballon1(x,y, image):
            surface.blit(image, (x,y))

        while not game_over:#boucle de jeu
            clock.tick(6000)
            y_move[0]=0
            y_move[1]=0
            if playernumber>=3:
                y_move[2]=0
            if playernumber==4:
                y_move[3]=0
            for event in pygame.event.get():#dÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬ ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©tection d ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬ ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©venements( de touches)

                if event.type == pygame.QUIT:
                    game_over= True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over=True
                        if bosspart1==1:
                            bosspart1=0
                if bot1==False:
                    if event.type == pygame.KEYDOWN:#touche appuyÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬ ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©e
                        if event.key == pygame.K_UP:


                            haut[0]=True
                            hautl[0]=True


                        elif event.key == pygame.K_LEFT:
                            x_move[0] = -0.006*pw[0]
                            dir[0] = 1
                            gauche[0]=True

                        elif event.key == pygame.K_RIGHT:
                            droite[0]=True
                            x_move[0] = 0.006*pw[0]
                            dir[0] = 0 #direction personnage








                        if event.key == pygame.K_DOWN:
                            bas[0]=True
                            basl[0]=True


                        if event.key == pygame.K_RETURN:
                            norm[0]=True




                        if event.key == pygame.K_RSHIFT:
                            spe[0]=True



                    if event.type ==pygame.KEYUP:#touche relevÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬ ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©e
                        if event.key == pygame.K_LEFT:
                            x_move[0] = 0
                            gauche[0]=False
                        if event.key == pygame.K_RIGHT:
                            x_move[0] = 0
                            droite[0]=False
                        if event.key == pygame.K_DOWN:
                            dbouclier[0]=False
                            bas[0]=False
                            basl[0]=False
                        if event.key == pygame.K_UP:
                            haut[0]=False
                            hautl[0]=False
                        if event.key == pygame.K_RETURN:
                            norm[0]=False
                            if chargenorm[0]==True:
                                chargego[0]=True
                        if event.key == pygame.K_RSHIFT:
                            spe[0]=False













                if bot2==False:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            haut[1]=True
                            hautl[1]=True



                        elif event.key == pygame.K_a:
                            droite[1]=True
                            x_move[1] = -0.006*pw[1]
                            dir[1] = 1

                        elif event.key == pygame.K_d:
                            gauche[1]=True
                            x_move[1] = 0.006*pw[1]
                            dir[1]=0




                        if event.key == pygame.K_SPACE:
                            norm[1]=True


                            if dbouclier[0]==True and bouclier[0]>0 and eject[0] != None:
                                if bouclier[0]-2000<0:
                                    eject[0][2]=eject[0][2]-bouclier[0]
                                    bouclier[0]=0

                                elif bouclier[0]-2000>0:
                                    pourc[0]-=10
                                    eject[0][2]=0
                                    bouclier[0]-=2000

                        if event.key == pygame.K_s:
                            bas[1]=True
                            basl[1]=True

                        if event.key == pygame.K_v:
                            spe[1]=True




                    if event.type ==pygame.KEYUP:
                        if event.key == pygame.K_w:
                            haut[1]=False
                        if event.key == pygame.K_a:
                            x_move[1] = 0
                            droite[1]=False
                        if event.key == pygame.K_d:
                            x_move[1] = 0
                            gauche[1]=False
                        if event.key == pygame.K_s:
                            dbouclier[1]=False
                            bas[1]=False
                        if event.key == pygame.K_SPACE:
                            norm[1]=False
                            if chargenorm[1]==True:
                                chargego[1]=True
                        if event.key == pygame.K_v:
                            spe[1]=False
                            chratt3[1]=False


            def bottt(v1,v2):
                x_move[v1] = 0
                norm[v1]=False
                gauche[v1]=False
                droite[v1]=False
                haut[v1]=False
                for i in range(1,platform[0]+1):
                    if y[v1]+ph[v1]+5 > platform[1+4*(i-1)] and y[v1] < platform[1+4*(i-1)]+0.084*ph[v1] and x[v1]-5 > platform[3+4*(i-1)] and x[v1]+5 < platform[4+4*(i-1)]:
                        if x[v2]>x[v1] and x[v2]<1100 and x[v2]>-300:
                            x_move[v1] = 0.006*pw[v1]
                            dir[v1]=0
                            gauche[v1]=True
                        if x[v2]<x[v1] and x[v2]<1100 and x[v2]>-300:
                            x_move[v1] = -0.006*pw[v1]
                            dir[v1]=1
                            droite[v1]=True
                        if y[v2]>y[v1]+ph[v1] and y[v2]<450:
                            for r in range(1,platform[0]+1):
                                if y[v2]+ph[v2]+5 > platform[1+4*(r-1)] and y[v2] < platform[1+4*(r-1)]+0.084*ph[v2] and x[v2]-5 > platform[3+4*(r-1)] and x[v2]+5 < platform[4+4*(r-1)]:
                                    if x[v1]-platform[3+4*(i-1)]<platform[4+4*(i-1)]-x[v1]:
                                        botenb[v1]=-250
                                    if x[v1]-platform[3+4*(i-1)]>platform[4+4*(i-1)]-x[v1]:
                                        botenb[v1]=250


                        haut[v1]=False
                        break
                    else:
                        if x[v2]>x[v1] :

                            x_move[v1] = 0.006*pw[v1]
                            dir[v1]=0
                            gauche[v1]=True
                        if x[v2]<x[v1] :

                            x_move[v1] = -0.006*pw[v1]
                            dir[v1]=1
                            droite[v1]=True
                        if saut[v1]==0 and y[v2]<y[v1]:
                            haut[v1]=True
                if botenb[v1]<0:
                    botenb[v1]+=1
                    x_move[v1]=-0.006*pw[v1]
                    haut[v1]=False
                if botenb[v1]>0:
                    botenb[v1]-=1
                    x_move[v1]=0.006*pw[v1]
                    haut[v1]=False
                if y[v1]+ph[v1] > y[v2] and y[v1] < y[v2]+pw[v2] and x[v1]+2*pw[v1] > x[v2] and x[v1]-pw[v1] < x[v2]+pw[v2] and haut[v1]==False:
                    treesd=random.randint(0,round(300/bot2dif))
                    if treesd==1:
                        norm[v1]=True
                if y[v1] > y[v2]+ph[v2] and y[v1] < y[v2]+ph[v2]*2 and x[v1]+2*pw[v1] > x[v2] and x[v1]-pw[v1] < x[v2]+pw[v2] and haut[v1]==False and bot1dif>7:
                    treesd=random.randint(0,round(300/bot2dif))
                    if treesd==1:
                        norm[v1]=True
                        haut[v1]=True
                if y[v1]+ph[v1] > y[v2] and y[v1] < y[v2]+pw[v2] and haut[v1]==False and bot1dif>5:
                    treesd=random.randint(0,round(300/bot2dif))
                    if treesd==1:
                        spe[v1]=True
                        gauche[v1]=False
                        droite[v1]=False
                if y[v1]+ph[v1] > y[v2] and y[v1] < y[v2]+pw[v2] and haut[v1]==False and bot1dif>6:
                    treesd=random.randint(0,round(300/bot2dif))
                    if treesd==1:
                        spe[v1]=True
                        if x[v2]>x[v1] :
                            dir[v1]=0
                            gauche[v1]=True
                        if x[v2]<x[v1]:
                            dir[v1]=1
                            droite[v1]=True
                if bot1dif==0:
                    x_move[v1] = 0
                    norm[v1]=False
                    gauche[v1]=False
                    droite[v1]=False
                    haut[v1]=False
                    bas[v1]=False
                    spe[v1]=False



            if bot1==True:
                if playernumber>=3:
                    if playernumber==4:
                        if x[1]-x[0]<x[2]-x[0]:
                            if x[1]-x[0]<x[3]-x[0]:
                                bottt(0,1)
                            else:
                                bottt(0,3)

                        else:
                            bottt(0,2)
                    else:
                        if x[1]-x[0]<x[2]-x[0]:
                            bottt(0,1)
                        else:
                            bottt(0,2)
                else:
                    bottt(0,1)

            if bot2==True:
                if playernumber>=3:
                    if playernumber==4:
                        if x[0]-x[1]<x[2]-x[1]:
                            if x[0]-x[1]<x[3]-x[1]:
                                bottt(1,0)
                            else:
                                bottt(1,3)

                        else:
                            bottt(1,2)
                    else:
                        if x[0]-x[1]<x[2]-x[1]:
                            bottt(1,0)
                        else:
                            bottt(1,2)
                else:
                    bottt(1,0)
            if bot3==True:

                if playernumber==4:
                    if x[0]-x[2]<x[1]-x[2]:
                        if x[0]-x[2]<x[3]-x[2]:
                            bottt(2,0)
                        else:
                            bottt(2,3)

                    else:
                        bottt(2,1)
                else:
                    if x[0]-x[2]<x[1]-x[2]:
                        bottt(2,0)
                    else:
                        bottt(2,1)


            if bot4==True:
                if x[0]-x[3]<x[1]-x[3]:
                    if x[0]-x[3]<x[2]-x[3]:
                        bottt(3,0)
                    else:
                        bottt(3,2)

                else:
                    bottt(3,1)



            pausemult-=1

            if multi==True:
                if pausemult==0:
                    Fichier = open('dabt.txt','rb')
                    Dab = pickle.load(Fichier)
                    Fichier.close()
                if bot3==False and playernumber>=3:
                    norm[2]=Dab[12]
                    spe[2]=Dab[13]
                    haut[2]=Dab[14]
                    bas[2]=Dab[15]
                    gauche[2]=Dab[17]
                    droite[2]=Dab[16]
                    x[2]=Dab[26]
                    y[2]=Dab[30]
                if bot4==False and playernumber==4:
                    norm[3]=Dab[18]
                    spe[3]=Dab[19]
                    haut[3]=Dab[20]
                    bas[3]=Dab[21]
                    gauche[3]=Dab[22]
                    droite[3]=Dab[23]
                    x[3]=Dab[27]
                    y[3]=Dab[31]
                Dab[0]=norm[0]
                Dab[1]=spe[0]
                Dab[2]=haut[0]
                Dab[3]=bas[0]
                Dab[4]=gauche[0]
                Dab[5]=droite[0]
                Dab[24]=x[0]
                Dab[28]=y[0]

                Dab[6]=norm[1]
                Dab[7]=spe[1]
                Dab[8]=haut[1]
                Dab[9]=bas[1]
                Dab[10]=gauche[1]
                Dab[11]=droite[1]
                Dab[25]=x[1]
                Dab[29]=y[1]
                if pausemult==0:
                    pausemult=10
                    Fichier = open('dabt.txt','wb')
                    pickle.dump(Dab,Fichier)
                    Fichier.close()




            if spritem[0]==200:
                spritem[0]=0
            if spritem[0]<200:
                spritem[0]+=1

            if gauche[0]==True:
                if spritem[0]>=0 and spritem[0]<=100:
                    sprite[0] = image2#retourne l'image
                if spritem[0]>100 and spritem[0]<=200:
                    sprite[0] = image22
                    standvue[0]=0
            if droite[0]==True:
                if spritem[0]>=0 and spritem[0]<=100:
                    sprite[0] = image1#retourne l'image
                if spritem[0]>100 and spritem[0]<=200:
                    sprite[0] = image12
                    standvue[0]=0

            if spritem[1]==200:
                spritem[1]=0
            if spritem[1]<200:
                spritem[1]+=1

            if gauche[1]==True:
                if spritem[1]>=0 and spritem[1]<=100:
                    sprite[1] = image4#retourne l'image
                if spritem[1]>100 and spritem[1]<=200:
                    sprite[1] = image42
            if droite[1]==True:
                if spritem[1]>=0 and spritem[1]<=100:
                    sprite[1] = image3#retourne l'image
                if spritem[1]>100 and spritem[1]<=200:
                    sprite[1] = image32

            if spritem[2]==200:
                spritem[2]=0
            if spritem[2]<200:
                spritem[2]+=1

            if gauche[2]==True:
                if spritem[2]>=0 and spritem[2]<=100:
                    sprite[2] = image5#retourne l'image
                if spritem[2]>100 and spritem[1]<=200:
                    sprite[2] = image52
            if droite[2]==True:
                if spritem[2]>=0 and spritem[2]<=100:
                    sprite[2] = image6#retourne l'image
                if spritem[2]>100 and spritem[2]<=200:
                    sprite[2] = image62

            if spritem[3]==200:
                spritem[3]=0
            if spritem[3]<200:
                spritem[3]+=1

            if gauche[3]==True:
                if spritem[3]>=0 and spritem[3]<=100:
                    sprite[3] = image7#retourne l'image
                if spritem[3]>100 and spritem[3]<=200:
                    sprite[3] = image72
            if droite[3]==True:
                if spritem[3]>=0 and spritem[3]<=100:
                    sprite[3] = image8#retourne l'image
                if spritem[3]>100 and spritem[3]<=200:
                    sprite[3] = image82

            def subtron(v1,v2):
                global ballpv,balexist

                if norm[v1]==True and haut[v1]==False and bas[v1]==False and normpause[v1][v2]==0:
                    eject[v2],pourc[v2]=prox(x[v1],x[v2],y[v1],y[v2],dir[v1],dir[v2],eject[v2],stand[v1],pourc[v2],charge[v1])

                    normpause[v1][v2]=100
                    if stand[v1]==True:
                        standvue[v1]=1
                    if v1==0:
                        if dir[v1]==0:
                            sprite[v1]=coup12
                        if dir[v1]==1:
                            sprite[v1]=coup11
                    if v1==1:
                        if dir[v1]==0:
                            sprite[v1]=coup22
                        if dir[v1]==1:
                            sprite[v1]=coup21
                    if v1==2:
                        if dir[v1]==0:
                            sprite[v1]=coup32
                        if dir[v1]==1:
                            sprite[v1]=coup31
                    if v1==3:
                        if dir[v1]==0:
                            sprite[v1]=coup42
                        if dir[v1]==1:
                            sprite[v1]=coup41
                    if chratt3[v2]==True and eject[v2]!=None:

                        eject[v2][2]=eject[v2][2]/2

                    if dbouclier[v2]==True and bouclier[v2]>0 and eject[v2] != None:
                        if bouclier[v2]-2000<0:
                            eject[v2][2]=eject[v2][2]-bouclier[v2]
                            bouclier[v2]=0

                        elif bouclier[v2]-2000>0:
                            pourc[v2]-=10
                            eject[v2][2]=0
                            bouclier[v2]-=2000
                    if playernumber==2:
                        norm[v1]=False
                    if playernumber==3:
                        if v1==0 and v2==2:
                            norm[0]=False
                        if v1==1 and v2==2:
                            norm[1]=False
                        if v1==2 and v2==1:
                            norm[2]=False
                    if playernumber==4:
                        if v1==0 and v2==3:
                            norm[0]=False
                        if v1==1 and v2==3:
                            norm[1]=False
                        if v1==2 and v2==3:
                            norm[2]=False
                        if v1==3 and v2==2:
                            norm[3]=False
                    if 400+pw[v1]>x[v1] and 400<x[v1]+pw[v1] and 200+pw[v1]>y[v1] and 200<y[v1]+ph[v1] and balexist==True:
                        ballpv-=5
                        if ballpv<=0:
                            objet[v1]=smash_ball
                            balexist=False
                            pygame.display.update(400-ph[v1],200-ph[v1],ph[v1]*2,ph[v1]*2)
                    if eject[v2]==None:
                        chargenorm[v1]=True
                if haut[v1]==True and spe[v1]==False and norm[v1]==False:
                    if nsaut[v1]==0 or nsaut[v1]==1:
                        if p[v1]==1:
                            if musique==True:
                                jump.play()
                        saut[v1] = ph[v1]*10
                        if nsaut[v1]==1:
                            nsaut[v1]=2
                        if nsaut[v1]==0:
                            nsaut[v1]=1
                    haut[v1]=False
                if haut[v1]==True and spe[v1]==True and billmt[v1]==0:
                    if p[v1]==1:
                        billx[v1]=x[v1]+pw[v1]
                        billy[v1]=round(y[v1]+ph[v1]/2)
                        billt[v1]=3000
                        saut[v1]=0
                        billmt[v1]=1
                    if p[v1]==2:
                        billx[v1]=x[v1]+pw[v1]
                        billy[v1]=round(y[v1]+ph[v1]/2)
                        billt[v1]=1000
                        saut[v1]=0
                        billmt[v1]=1
                    if p[v1]==3:
                        if dir[v1]==0:
                            sprite[v1]=lancecout0
                        if dir[v1]==1:
                            sprite[v1]=lancecout1
                        billx[v1]=x[v1]+pw[v1]/2
                        billy[v1]=round(y[v1]+ph[v1]/2)
                        billt[v1]=1000
                        saut[v1]=0
                        billmt[v1]=1
                    if p[v1]==4:
                        billx[v1]=x[v1]-pw[v1]/2
                        billy[v1]=round(y[v1]-ph[v1]*2)
                        billt[v1]=1000
                        saut[v1]=0
                        billmt[v1]=1
                    if p[v1]==5:
                        if dir[v1]==0:
                            sprite[v1]=cuphaut0
                        if dir[v1]==1:
                            sprite[v1]=cuphaut1
                        billx[v1]=x[v1]+pw[v1]/2
                        billy[v1]=round(y[v1])
                        billt[v1]=1000
                        saut[v1]=0
                        billmt[v1]=1
                    if p[v1]==6:
                        billx[v1]=x[v1]
                        saut[v1]=0
                        billy[v1]=round(y[v1]-ph[v1])
                        billmt[v1]=1
                        billt[v1]=400
                    if p[v1]==7:
                        billx[v1]=x[v1]
                        billy[v1]=y[v1]
                        billmt[v1]=1
                    if p[v1]==8:
                        saut[v1]=200
                        billmt[v1]=1
                    if p[v1]==9 and coupfeu[v1]>0:
                        billmt[v1]=6
                        coupfeu[v1]-=1000
                    if p[v1]==10:
                        billx[v1]=x[v1]+pw[v1]
                        billy[v1]=round(y[v1]+ph[v1]/2)
                        billt[v1]=3000
                        saut[v1]=0
                        billmt[v1]=1
                    spe[v1]=False
                    haut[v1]=False
                if haut[v1]==True and norm[v1]==True :
                    if p[v1]==1:
                        block[v1]=3000
                        blockxx[v1]=x[v1]
                        blockyx[v1]=y[v1]-ph[v1]*1.5
                        saut[v1]=100
                        blockx[v1]=x[v1]
                        blocky[v1]=y[v1]-0.5*ph[v1]
                        haut[v1]=False
                        if x[v2]+pw[v1]>blockxx[v1] and x[v2]<blockxx[v1]+pw[v1] and y[v2]+ph[v2]>blockyx[v1] and y[v2]<blockyx[v1]+2*ph[v1]:
                            eject[v2]=propulse(dir[v2],pourc[v2]*5+1)
                        if 400+pw[v1]>blockxx[v1] and 400<blockxx[v1]+pw[v1] and 200+pw[v1]>blockyx[v1] and 200<blockyx[v1]+2*ph[v1] and balexist==True:
                            ballpv-=50
                            if ballpv<=0:
                                objet[v1]=smash_ball
                                balexist=False
                                pygame.display.update(400-ph[v1],200-ph[v1],ph[v1]*2,ph[v1]*2)
                    if p[v1]==2:
                        if nsaut[v1]<2:
                            nsaut[v1]+=1
                            saut[v1]=1500
                            ltourn[v1]=True
                            haut[v1]=False
                    if p[v1]==3:
                        if nsaut[v1]<2:
                            nsaut[v1]+=1
                            saut[v1]=700
                            haut[v1]=False
                            ltourn[v1]=True
                    if p[v1]==4:
                        if nsaut[v1]<2:
                            nsaut[v1]+=1
                            saut[v1]=700
                            haut[v1]=False
                            ltourn[v1]=True
                    if p[v1]==5 and block[v1]==0:
                        block[v1]=700
                        saut[v1]=0
                        blockx[v1]=x[v1]
                        blocky[v1]=y[v1]-pw[v1]
                        haut[v1]=False
                    if p[v1]==6:
                        if dir[v1]==0:
                            sprite[v1]=sanshaut0
                        if dir[v1]==1:
                            sprite[v1]=sanshaut1
                        if x[v1]+ph[v1]*2>x[v2] and x[v1]<x[v2]+ph[v2]*2 and y[v1]+ph[v1]*2>y[v2] and y[v1]<y[v2]+ph[v2]*2:
                            y_move[v2]-=0.9
                    if p[v1]==7 and block[v1]==0:
                        block[v1]=15000
                    if p[v1]==8:
                        if nsaut[v1]<2:
                            nsaut[v1]+=1
                            saut[v1]=1500
                            ltourn[v1]=True
                            haut[v1]=False
                    if p[v1]==9:
                        saut[v1]=10
                        if dir[v1]==0:
                            sprite[v1]=jamesaut0
                        if dir[v1]==1:
                            sprite[v1]=jamesaut1
                    if p[v1]==10:
                        if nsaut[v1]<2:
                            nsaut[v1]+=1
                            saut[v1]=1500
                            haut[v1]=False

                if bas[v1]==True and spe[v1]==True:


                    chratt3[v1]=True
                    x_move[v1]=0
                    y_move[v1]=0
                    saut[v1]=0
                    dbouclier[v1]=False



                if bas[v1]==True and norm[v1]==True:
                    if p[v1]==1:
                        if dir[v1]==0:
                            sprite[v1]=accr1
                        if dir[v1]==1:
                            sprite[v1]=accr2
                        if y[v1]+ph[v1] > y[v2] and y[v1] < y[v2]+pw[v2] and x[v1]+pw[v1] > x[v2] and x[v1] < x[v2]+pw[v2] and saut[v1]==0 and nsaut[v1]==0 and enterret[v1]==0 :
                            enterre[v2]=2000
                            terrex[v2]=x[v2]
                            terrey[v2]=y[v2]
                            enterret[v1]=6000
                        if y[v1]+ph[v1] > y[v2] and y[v1] < y[v2]+pw[v2] and x[v1]+pw[v1] > x[v2] and x[v1] < x[v2]+pw[v2] and nsaut[v1]!=0:
                            enbas[v2]=500
                    if p[v1]==2:
                        tornade[v1]=2
                    if p[v1]==3:
                        standcharge[v1]+=1
                        if dir[v1]==0:
                            sprite[v1]=pcharge0
                        if dir[v1]==1:
                            sprite[v1]=pcharge1
                        if standcharge[v1]==10000:
                            norm[v1]=False
                        if standcharge[v1]==10001:
                            stand[v1]=True
                            standt[v1]=10000
                            standcharge[v1]=0
                    if p[v1]==4:
                        tornade[v1]=2
                    if p[v1]==5:
                        sprite[v1]=cuppanic
                    if p[v1]==6:
                        if dir[v1]==0:
                            sprite[v1]=sansbas0
                        if dir[v1]==1:
                            sprite[v1]=sansbas1
                        if x[v1]+ph[v1]*2>x[v2] and x[v1]<x[v2]+ph[v2]*2 and y[v1]+ph[v1]*2>y[v2] and y[v1]<y[v2]+ph[v2]*2:
                            y_move[v2]+=0.9
                    if p[v1]==7 and tlock[v1]==False and tornade[v1]==0:
                        tlockx[v1]=x[v1]
                        tlocky[v1]=y[v1]
                        norm[v1]=False
                        tlock[v1]=True
                    if p[v1]==7 and tlock[v1]==True and norm[v1]==True:
                        tornade[v1]=2
                        norm[v1]=False
                        tlock[v1]=False
                    if p[v1]==8:
                        tlock[v1]=True
                    if p[v1]==9 and tlock[v1]==False and tornade[v1]==0:
                        tlockx[v1]=x[v1]
                        tlocky[v1]=y[v1]
                        norm[v1]=False
                        tlock[v1]=True
                    if p[v1]==9 and tlock[v1]==True and norm[v1]==True:
                        norm[v1]=False
                        tornade[v1]=6
                        tlock[v1]=False
                    if p[v1]==10 and tornade[v1]==0:
                        tornade[v1]=10000
                        norm[v1]=False
                        if dir[v1]==0:
                            tlockx[v1]=x[v1]+pw[v1]*2
                            tlocky[v1]=y[v1]
                        if dir[v1]==1:
                            tlockx[v1]=x[v1]-pw[v1]*2
                            tlocky[v1]=y[v1]


                if spe[v1]==True and sprintt[v1]==0 and (droite[v1]==True or gauche[v1]==True):
                    sprint[v1]=500
                    if p[v1]==1:
                        sprintt[v1]=1500
                    if p[v1]==2:
                        sprintt[v1]=4000
                    if p[v1]==3:
                        sprintt[v1]=1500
                    if p[v1]==4:
                        sprintt[v1]=1000
                    if p[v1]==5:
                        sprintt[v1]=5000
                        sprint[v1]=1500
                    if p[v1]==6:
                        sprintt[v1]=1500
                    if p[v1]==7:
                        sprintt[v1]=3000
                    if p[v1]==8:
                        sprintt[v1]=1000
                    if p[v1]==9 and coupfeu[v1]>0:
                        coupfeu[v1]-=1000
                        if dir[v1]==0:
                            sprite[v1]=jameshoot0
                        if dir[v1]==1:
                            sprite[v1]=jameshoot1
                        sprintt[v1]=6
                    if p[v1]==10:
                        sprintt[v1]=1500
                    spe[v1]=False

                if bas[v1]==True and spe[v1]==False and norm[v1]==False:
                    dbouclier[v1]=True

                if spe[v1]==True and bas[v1]==False and haut[v1]==False and droite[v1]==False and gauche[v1]==False:
                    if objet[v1]!=None:
                        if objet[v1]==smash_ball:
                            if p[v1]==1:
                                smash[v1]=3000
                                smashattqx[v1]=x[v1]
                                smashattqy[v1]=y[v1]-ph[v1]
                                smashattqdir[v1]=dir[v1]
                            if p[v1]==2:
                                smash[v1]=10000
                                y[v1]=y[v1]-2*ph[v1]
                                x[v1]=x[v1]
                            if p[v1]==3:
                                if musique==True:
                                    theworldsound.play()
                                smash[v1]=2000
                            if p[v1]==4:
                                smash[v1]=4000
                                smashattqdir[v1]=dir[v1]
                            if p[v1]==5:
                                smash[v1]=8000
                                smashattqdir[v1]=pourc[v1]
                            if p[v1]==6:
                                smash[v1]=2000
                                smashattqdir[v1]=dir[v1]
                            if p[v1]==7:
                                if musique==True:
                                    clack.play()
                                smash[v1]=1
                            if p[v1]==8:
                                smash[v1]=800
                                vie[v1]+=1
                            if p[v1]==9:
                                smash[v1]=500

                            if p[v1]==10:
                                smash[v1]=5000

                                for i in range(1,47):
                                    clock.tick(20)
                                    trumred= pygame.image.load("perso/10/redbutton/frame-"+str(i)+".gif").convert_alpha()
                                    trumred = pygame.transform.scale(trumred,(round(800),round(450)))
                                    surface.blit(trumred,(0,0))
                                    pygame.display.update(0,0,800,450)
                                surface.blit(fond,(0,0))
                                pygame.display.update(0,0,800,450)
                                clock.tick(6000)
                            objet[v1]=None
                    if chratt2[v1]==0:
                        chratt2[v1]=500
                        if p[v1] ==1:


                            if feu[v1] ==False:
                                feu[v1]=[0]
                            feu[v1][0]+=1
                            feu[v1].append(x[v1]+pw[v1])
                            feu[v1].append(y[v1]+round(ph[v1]/2))
                            feu[v1].append(dir[v1])
                            feu[v1].append(0)
                            feu[v1].append(300)
                        if p[v1]==2:
                            if feul[v1] ==False:
                                feul[v1]=[0]
                            feul[v1][0]+=1
                            feul[v1].append(x[v1]+round(pw[v1]/2))
                            feul[v1].append(y[v1]+round(ph[v1]/2))
                            feul[v1].append(dir[v1])
                            feul[v1].append(300)
                        if p[v1]==3:
                            if dir[v1]==0:
                                sprite[v1]=lancecout0
                            if dir[v1]==1:
                                sprite[v1]=lancecout1
                            if feul[v1] ==False:
                                feul[v1]=[0]
                            feul[v1][0]+=1
                            feul[v1].append(x[v1]+round(pw[v1]/2))
                            feul[v1].append(y[v1]+round(ph[v1]/2))
                            feul[v1].append(dir[v1])
                            feul[v1].append(300)
                        if p[v1]==5:
                            if dir[v1]==0:
                                sprite[v1]=cupdroit0
                            if dir[v1]==1:
                                sprite[v1]=cupdroit1
                            if feul[v1] ==False:
                                feul[v1]=[0]
                            feul[v1][0]+=1
                            feul[v1].append(x[v1]+round(pw[v1]/2))
                            feul[v1].append(y[v1]+round(ph[v1]/2))
                            feul[v1].append(dir[v1])
                            feul[v1].append(400)
                        if p[v1]==6:
                            sansray[v1]=100
                            chratt2[v1]=0
                        if p[v1]==7:
                            sansray[v1]=100
                            chratt2[v1]=0
                        if p[v1]==8:
                            if feu[v1] ==False:
                                feu[v1]=[0]
                            feu[v1][0]+=1
                            feu[v1].append(x[v1]+round(pw[v1]/2))
                            feu[v1].append(y[v1]+round(ph[v1]/2))
                            feu[v1].append(dir[v1])
                            feu[v1].append(0)
                            feu[v1].append(500)
                            chratt2[v1]=1000
                        if p[v1]==9:
                            if feul[v1] ==False:
                                feul[v1]=[0]
                            feul[v1][0]+=1
                            feul[v1].append(x[v1]+round(pw[v1]/2))
                            feul[v1].append(y[v1]+round(ph[v1]/2))
                            feul[v1].append(dir[v1])
                            feul[v1].append(400)
                        if p[v1]==10:
                            if feu[v1] ==False:
                                feu[v1]=[0]
                            feu[v1][0]+=1
                            feu[v1].append(x[v1]+round(pw[v1]/2))
                            feu[v1].append(y[v1]+round(ph[v1]/2))
                            feu[v1].append(dir[v1])
                            feu[v1].append(0)
                            feu[v1].append(500)
                            chratt2[v1]=1000


                if bas[v1]==False and haut[v1]==False and droite[v1]==False and gauche[v1]==False and chargenorm[v1]==True:
                    charge[v1]+=0.03
                if droite[v1]==True or gauche[v1]==True:
                    charge[v1]=0
                    chargenorm[v1]=False
                if norm[v1]==False and bas[v1]==False and haut[v1]==False and droite[v1]==False and gauche[v1]==False and charge[v1]>0 and chargenorm[v1]==True and chargego[v1]==True:

                    eject[v2],pourc[v2]=prox(x[v1],x[v2],y[v1],y[v2],dir[v1],dir[v2],eject[v2],stand[v1],pourc[v2],charge[v1])

                    if 400+pw[v1]>x[v1] and 400<x[v1]+pw[v1] and 200+pw[v1]>y[v1] and 200<y[v1]+ph[v1] and balexist==True:
                        ballpv-=charge[v1]
                        if ballpv<=0:
                            objet[v1]=smash_ball
                            balexist=False
                            pygame.display.update(400-ph[v1],200-ph[v1],ph[v1]*2,ph[v1]*2)
                    charge[v1]=0
                    chargenorm[v1]=False
                    chargego[v1]=False











            if playernumber==2:
                subtron(0,1)
                subtron(1,0)
            if playernumber==3:
                subtron(0,1)
                subtron(0,2)
                subtron(1,0)
                subtron(1,2)
                subtron(2,0)
                subtron(2,1)
            if playernumber==4:
                subtron(0,1)
                subtron(0,2)
                subtron(0,3)
                subtron(1,0)
                subtron(1,2)
                subtron(1,3)
                subtron(2,0)
                subtron(2,1)
                subtron(2,3)
                subtron(3,0)
                subtron(3,1)
                subtron(3,2)




















            for i in range(0,4):
                if normpause[0][i]>0:
                    normpause[0][i]-=1
                if normpause[1][i]>0:
                    normpause[1][i]-=1
                if normpause[2][i]>0:
                    normpause[2][i]-=1
                if normpause[3][i]>0:
                    normpause[3][i]-=1
            def groot(v1,v2):
                if p[v1]==1:
                    if feu[v1] != False:
                        naopp=0
                        naoppm=0
                        for i in range(1,feu[v1][0]+1):

                            if feu[v1][3+5*(i-1)]==0:
                                feu[v1][1+5*(i-1)]+=0.006*pw[v1]
                            if feu[v1][3+5*(i-1)]==1:
                                feu[v1][1+5*(i-1)]-=0.006*pw[v1]
                            if feu[v1][4+5*(i-1)]<=0 :
                                feu[v1][2+5*(i-1)]+=0.005*ph[v1]
                                for n in range(1,platform[0]+1):
                                    if feu[v1][2+5*(i-1)]+ph[v1]/5 > platform[1+4*(n-1)] and feu[v1][2+5*(i-1)] < platform[1+4*(n-1)]+0.084*(ph[v1]/5) and feu[v1][1+5*(i-1)] > platform[3+4*(n-1)] and feu[v1][1+5*(i-1)] < platform[4+4*(n-1)]:
                                        feu[v1][4+5*(i-1)]=100
                            if feu[v1][4+5*(i-1)]>0 :
                                feu[v1][2+5*(i-1)]-=0.005*ph[v1]
                                feu[v1][4+5*(i-1)]-=1
                            feu[v1][5+5*(i-1)]-=0.006*pw[v1]

                            if feu[v1][2+5*(i-1)]+ph[v1]/5 > y[v2] and feu[v1][2+5*(i-1)] < y[v2]+pw[v2] and feu[v1][1+5*(i-1)]+pw[v1]/5 > x[v2] and feu[v1][1+5*(i-1)] < x[v2]+pw[v2]:
                                if dbouclier[v2]==True:
                                    if bouclier[v2]-1000<0:

                                        bouclier[v2]=0
                                        pourc[v2]+=5

                                    elif bouclier[v2]-1000>0:


                                        bouclier[v2]-=1000
                                else:
                                    pourc[v2]+=5
                                naoppm=1
                                naopp=i



                            if feu[v1][5+5*(i-1)]<=0:
                                naopp=i


                        if feu[v1][5+5*(naopp-1)]<=0 or naoppm==1:

                            feu[v1][0]-=1
                            del feu[v1][1+5*(naopp-1)]
                            del feu[v1][1+5*(naopp-1)]
                            del feu[v1][1+5*(naopp-1)]
                            del feu[v1][1+5*(naopp-1)]
                            del feu[v1][1+5*(naopp-1)]
                            naopp=0
                            naoppm=0
                        if feu[v1][0]==0:
                            feu[v1]=False

                    if billy[v1]+ph[v1]/2 > y[v2] and billy[v1] < y[v2]+pw[v2] and billx[v1]+pw[v1]/2 > x[v2] and billx[v1] < x[v2]+pw[v2] and billt[v1]>1:
                        billt[v1]=1
                        pourc[v2]+=20
                        eject[v2]=propulse(dir[v2],pourc[v2])

                    if enterret[v1]>0:
                        enterret[v1]-=1
                    if enbas[v2]>0:
                        y[v2]+=0.005*ph[v2]
                        enbas[v2]-=1
                    if sprint[v1]>0:
                        sprint[v1]-=1
                        if dir[v1]==0:
                            x_move[v1]=0.5
                        if dir[v1]==1:
                            x_move[v1]=-0.5
                        if sprint[v1]==0:
                            x_move[v1]=0
                    if sprintt[v1]>0:
                        sprintt[v1]-=1
                    if smash[v1]>0:
                        smash[v1]-=1
                        if smashattqdir[v1]==1:
                            smashattqx[v1]-=0.3
                        if smashattqdir[v1]==0:
                            smashattqx[v1]+=0.3
                        if smashattqy[v1]+pw[v1]*4 > y[v2] and smashattqy[v1] < y[v2]+ph[v2] and smashattqx[v1]+pw[v1]*4 > x[v2] and smashattqx[v1] < x[v2]+pw[v2]:
                            pourc[v2]+=0.1
                            if smashattqdir[v1]==0:
                                eject[v2]=[0.1,0,1]
                            if smashattqdir[v1]==1:
                                eject[v2]=[-0.1,0,1]

                if p[v1]==2:
                    if billy[v1]+ph[v1]/2 > y[v2] and billy[v1] < y[v2]+pw[v2] and billx[v1]+pw[v1]/2 > x[v2] and billx[v1] < x[v2]+pw[v2] and billt[v1]>1:
                        billt[v1]=1

                    if artifice[v1]==1500 and billy[v1]+ph[v1]*2 > y[v2] and billy[v1]-ph[v1] < y[v2]+pw[v2] and billx[v1]+pw[v1]*2 > x[v2] and billx[v1]-ph[v1] < x[v2]+pw[v2]:
                        pourc[v2]+=20
                        eject[v2]=propulse(dir[v2],pourc[v2])
                        artifice[v1]=1

                    if feul[v1] != False:
                        naoppm=0
                        naopp=0
                        for i in range(1,feul[v1][0]+1):
                            if feul[v1][3+4*(i-1)]==0:
                                feul[v1][1+4*(i-1)]+=0.006*pw[v1]
                            if feul[v1][3+4*(i-1)]==1:
                                feul[v1][1+4*(i-1)]-=0.006*pw[v1]
                            feul[v1][4+4*(i-1)]-=0.006*pw[v1]

                            if feul[v1][2+4*(i-1)]+ph[v1]/5 > y[v2] and feul[v1][2+4*(i-1)] < y[v2]+pw[v2] and feul[v1][1+4*(i-1)]+pw[v1]/5 > x[v2] and feul[v1][1+4*(i-1)] < x[v2]+pw[v2]:
                                if dbouclier[v2]==True:
                                    if bouclier[v2]-1000<0:

                                        bouclier[v2]=0
                                        pourc[v2]+=5

                                    elif bouclier[v2]-1000>0:


                                        bouclier[v2]-=1000
                                else:
                                    pourc[v2]+=5
                                naoppm=1
                                naopp=i



                            if feul[v1][4+4*(i-1)]<=0:
                                naopp=i


                        if feul[v1][4+4*(naopp-1)]<=0 or naoppm==1:

                            feul[v1][0]-=1
                            del feul[v1][1+4*(naopp-1)]
                            del feul[v1][1+4*(naopp-1)]
                            del feul[v1][1+4*(naopp-1)]
                            del feul[v1][1+4*(naopp-1)]
                            naopp=0
                            naoppm=0
                        if feul[v1][0]==0:
                            feul[v1]=False
                    if tornade[v1]==2:
                        y_move[v1]=0
                        x_move[v1]=0
                        if y[v1]+ph[v1] > y[v2] and y[v1]-ph[v1] < y[v2]+pw[v2] and x[v1]+pw[v1] > x[v2] and x[v1]-pw[v1] < x[v2]+pw[v2]:
                            y[v2]-=1

                    if sprint[v1]>0:
                        sprint[v1]-=1
                        if dir[v1]==0:
                            x_move[v1]=0.5
                            sprite[v1]=luigilong1
                        if dir[v1]==1:
                            x_move[v1]=-0.5
                            sprite[v1]=luigilong2

                        if sprint[v1]==0:
                            x_move[v1]=0
                            if dir[v1]==0:
                                sprite[v1]=image1
                            if dir[v1]==1:
                                sprite[v1]=image2
                        if y[v1]+pw[v1] > y[v2] and y[v1] < y[v2]+pw[v2] and x[v1]+pw[v1] > x[v2] and x[v1] < x[v2]+pw[v2] and sprint[v1]>0:
                            pourc[v2]+=10
                            sprint[v1]=1
                            eject[v2],pourc[v2]=prox(x[v1],x[v2],y[v1],y[v2],dir[v1],dir[v2],eject[v2],stand[v1],pourc[v2],charge[v1])
                    if sprintt[v1]>0:
                        sprintt[v1]-=1
                    if ltourn[v1]!=False:
                        if saut[v1]==0:
                            ltourn[v1]=False
                        sautl1=pygame.transform.rotate(sautl,saut[v1])
                        sprite[v1]=sautl1
                        if y[v1]+ph[v1] > y[v2] and y[v1] < y[v2]+pw[v2] and x[v1]+ph[v1] > x[v2] and x[v1] < x[v2]+pw[v2]:
                            pourc[v2]+=0.01
                    if smash[v1]>0:
                        saut[v1]=0
                        smash[v1]-=1
                        y_move[v1]-=0.005*ph[v1]
                        if hautl[v1]==True:
                            y_move[v1]+=-0.005*ph[v1]

                        if basl[v1]==True:
                            y_move[v1]+=0.005*ph[v1]

                        if y[v1]+ph[v1] > y[v2] and y[v1]-ph[v1] < y[v2]+pw[v2] and x[v1]+ph[v1] > x[v2] and x[v1]-ph[v1] < x[v2]+pw[v2]:
                            pourc[v2]+=0.04

                if p[v1]==3:
                    if billy[v1]+ph[v1]/2 > y[v2] and billy[v1] < y[v2]+pw[v2] and billx[v1]+pw[v1]/2 > x[v2] and billx[v1] < x[v2]+pw[v2] and billt[v1]>1:
                        billt[v1]=1
                        pourc[v2]+=10
                        eject[v2]=propulse(dir[v2],pourc[v2])
                    if ltourn[v1]!=False:
                        if saut[v1]==0:
                            ltourn[v1]=False
                        if dir[v1]==0:
                            sprite[v1]=sautdio0
                        if dir[v1]==1:
                            sprite[v1]=sautdio1
                        if y[v1]+ph[v1] > y[v2] and y[v1] < y[v2]+pw[v2] and x[v1]+ph[v1] > x[v2] and x[v1] < x[v2]+pw[v2]:
                            pourc[v2]+=0.05
                            eject[v2]=[0,-0.3,100]
                    if stand[v1]==True:
                        standt[v1]-=1
                        if standt[v1]==0:
                            stand[v1]=False
                    if sprint[v1]>0:
                        sprint[v1]-=1
                        standvue=2
                        if dir[v1]==0:
                            x_move[v1]=0.5
                            sprite[v1]=fonc0
                        if dir[v1]==1:
                            x_move[v1]=-0.5
                            sprite[v1]=fonc1

                        if sprint[v1]==0:
                            standvue=0
                            x_move[v1]=0
                            if dir[v1]==0:
                                sprite[v1]=image1
                            if dir[v1]==1:
                                sprite[v1]=image2
                        if y[v1]+pw[v1] > y[v2] and y[v1] < y[v2]+pw[v2] and x[v1]+pw[v1] > x[v2] and x[v1] < x[v2]+pw[v2] and sprint[v1]>0:
                            pourc[v2]+=10
                            sprint[v1]=1
                            eject[v2],pourc[v2]=prox(x[v1],x[v2],y[v1],y[v2],dir[v1],dir[v2],eject[v2],stand[v1],pourc[v2],charge[v1])
                    if sprintt[v1]>0:
                        sprintt[v1]-=1
                    if feul[v1] != False:
                        naoppm=0
                        naopp=0
                        for i in range(1,feul[v1][0]+1):

                            if feul[v1][3+4*(i-1)]==0:
                                feul[v1][1+4*(i-1)]+=0.006*pw[v1]
                            if feul[v1][3+4*(i-1)]==1:
                                feul[v1][1+4*(i-1)]-=0.006*pw[v1]
                            feul[v1][4+4*(i-1)]-=0.006*pw[v1]

                            if feul[v1][2+4*(i-1)]+ph[v1]/5 > y[v2] and feul[v1][2+4*(i-1)] < y[v2]+pw[v2] and feul[v1][1+4*(i-1)]+pw[v1]/5 > x[v2] and feul[v1][1+4*(i-1)] < x[v2]+pw[v2]:
                                if dbouclier[v2]==True:
                                    if bouclier[v2]-1000<0:

                                        bouclier[v2]=0
                                        pourc[v2]+=5

                                    elif bouclier[v2]-1000>0:


                                        bouclier[v2]-=1000
                                else:
                                    pourc[v2]+=5
                                naoppm=1
                                naopp=i



                            if feul[v1][4+4*(i-1)]<=0:
                                naopp=i


                        if feul[v1][4+4*(naopp-1)]<=0 or naoppm==1:

                            feul[v1][0]-=1
                            del feul[v1][1+4*(naopp-1)]
                            del feul[v1][1+4*(naopp-1)]
                            del feul[v1][1+4*(naopp-1)]
                            del feul[v1][1+4*(naopp-1)]
                            naopp=0
                            naoppm=0
                        if feul[v1][0]==0:
                            feul[v1]=False
                    if smash[v1]>0:
                        smash[v1]-=1
                        world[v1]+=10
                        if smash[v1]==0:
                            world[v1]=0
                        global zawarudo
                        zawarudo = pygame.Surface((2000,2000), pygame.SRCALPHA)

                        pygame.draw.circle(zawarudo,(105,105,105,80),(1000,1000),round(world[v1]/10))
                if p[v1]==4:
                    if billy[v1]+ph[v1]*2 > y[v2] and billy[v1] < y[v2]+pw[v2] and billx[v1]+pw[v1]*2 > x[v2] and billx[v1] < x[v2]+pw[v2] and billt[v1]>1:

                        pourc[v2]+=0.03
                        eject[v2]=propulse(dir[v2],pourc[v2])
                    if ltourn[v1]!=False:
                        if saut[v1]==0:
                            ltourn[v1]=False
                        if dir[v1]==0:
                            sprite[v1]=netersaut0
                        if dir[v1]==1:
                            sprite[v1]=neterhaut1
                        if y[v1]+ph[v1]*2 > y[v2] and y[v1]+ph[v1] < y[v2]+pw[v2] and x[v1]+ph[v1]*1.5 > x[v2] and x[v1]-ph[v1]/2 < x[v2]+pw[v2]:
                            pourc[v2]+=0.05
                            eject[v2]=[0,-0.3,100]
                    if tornade[v1]==2:
                        y_move[v1]=0
                        x_move[v1]=0
                        if y[v1]+ph[v1]*1.3 > y[v2] and y[v1]-ph[v1] < y[v2]+pw[v2] and x[v1]+pw[v1]*1.3 > x[v2] and x[v1]-pw[v1]*1.3 < x[v2]+pw[v2]:
                            if x[v1]<x[v2]:
                                eject[v2]=[0.8,0,50]
                            if x[v1]>x[v2]:
                                eject[v2]=[-0.8,0,50]
                    if sprint[v1]>0:
                        sprint[v1]-=1
                        if dir[v1]==0:
                            x_move[v1]=0.5
                            sprite[v1]=nfonc0
                        if dir[v1]==1:
                            x_move[v1]=-0.5
                            sprite[v1]=nfonc1
                        if sprint[v1]==0:
                            x_move[v1]=0
                            sprite[v1]=image1
                    if sprintt[v1]>0:
                        sprintt[v1]-=1
                    if chratt2[v1]>0:
                        if dir[v1]==0:
                            if y[v1]+ph[v1] > y[v2] and y[v1]-pw[v1] < y[v2]+pw[v2] and x[v1]+ph[v1]*2 > x[v2] and x[v1]+ph[v1] < x[v2]+pw[v2]:
                                pourc[v2]+=0.01
                                eject[v2]=propulse(dir[v1],pourc[v2])
                        if dir[v1]==1:
                            if y[v1]+ph[v1] > y[v2] and y[v1]-pw[v1] < y[v2]+pw[v2] and x[v1]-ph[v1] > x[v2] and x[v1]-ph[v1]*2 < x[v2]+pw[v2]:
                                pourc[v2]+=0.01
                                eject[v2]=propulse(dir[v1],pourc[v2])
                    if smash[v1]>0:
                        smash[v1]-=1
                        if smashattqdir[v1]==0:
                            if y[v1]+ph[v1] > y[v2] and y[v1]-ph[v1]*2 < y[v2]+pw[v2] and x[v1]+pw[v1]*3 > x[v2] and x[v1] < x[v2]+pw[v2]:
                                pourc[v2]+=0.1
                                eject[v2]=propulse(smashattqdir[v1],pourc[v2])
                        if smashattqdir[v1]==1:
                            if y[v1]+ph[v1] > y[v2] and y[v1]-ph[v1]*2 < y[v2]+pw[v2] and x[v1]+pw[v1] > x[v2] and x[v1]-pw[v1]*2 < x[v2]+pw[v2]:
                                pourc[v2]+=0.1
                                eject[v2]=propulse(smashattqdir[v1],pourc[v2])
                if p[v1]==5:
                    if billy[v1]+ph[v1]/2 > y[v2] and billy[v1] < y[v2]+pw[v2] and billx[v1]+pw[v1]/2 > x[v2] and billx[v1] < x[v2]+pw[v2] and billt[v1]>1:
                        billt[v1]=1
                        pourc[v2]+=10
                        eject[v2]=propulse(dir[v2],pourc[v2])
                    if blocky[v1]+ph[v1] > y[v2] and blocky[v1] < y[v2]+pw[v2] and blockx[v1]+ph[v1] > x[v2] and blockx[v1] < x[v2]+pw[v2] and block[v1]>0:
                        block[v1]=1
                        pourc[v2]+=20
                        eject[v2]=propulse(dir[v2],pourc[v2])
                    if sprint[v1]>0:
                        sprint[v1]-=1
                        if dir[v1]==0:
                            x_move[v1]=0.2
                            sprite[v1]=cupfonc0
                        if dir[v1]==1:
                            x_move[v1]=-0.2
                            sprite[v1]=cupfonc1

                        if sprint[v1]==0:
                            x_move[v1]=0
                            if dir[v1]==0:
                                sprite[v1]=image1
                            if dir[v1]==1:
                                sprite[v1]=image2
                        if y[v1]+pw[v1] > y[v2] and y[v1] < y[v2]+pw[v2] and x[v1]+pw[v1] > x[v2] and x[v1] < x[v2]+pw[v2] and sprint[v1]>0:
                            pourc[v2]+=30
                            sprint[v1]=1
                            eject[v2],pourc[v2]=prox(x[v1],x[v2],y[v1],y[v2],dir[v1],dir[v2],eject[v2],stand[v1],pourc[v2],charge[v1])
                    if sprintt[v1]>0:
                        sprintt[v1]-=1
                    if feul[v1] != False:
                        naoppm=0
                        naopp=0
                        for i in range(1,feul[v1][0]+1):

                            if feul[v1][3+4*(i-1)]==0:
                                feul[v1][1+4*(i-1)]+=0.006*pw[v1]
                            if feul[v1][3+4*(i-1)]==1:
                                feul[v1][1+4*(i-1)]-=0.006*pw[v1]
                            feul[v1][4+4*(i-1)]-=0.006*pw[v1]

                            if feul[v1][2+4*(i-1)]+ph[v1]/5 > y[v2] and feul[v1][2+4*(i-1)] < y[v2]+pw[v2] and feul[v1][1+4*(i-1)]+pw[v1]/5 > x[v2] and feul[v1][1+4*(i-1)] < x[v2]+pw[v2]:
                                if dbouclier[v2]==True:
                                    if bouclier[v2]-1000<0:

                                        bouclier[v2]=0
                                        pourc[v2]+=5

                                    elif bouclier[v2]-1000>0:


                                        bouclier[v2]-=1000
                                else:
                                    pourc[v2]+=5
                                naoppm=1
                                naopp=i



                            if feul[v1][4+4*(i-1)]<=0:
                                naopp=i


                        if feul[v1][4+4*(naopp-1)]<=0 or naoppm==1:

                            feul[v1][0]-=1
                            del feul[v1][1+4*(naopp-1)]
                            del feul[v1][1+4*(naopp-1)]
                            del feul[v1][1+4*(naopp-1)]
                            del feul[v1][1+4*(naopp-1)]
                            naopp=0
                            naoppm=0
                        if feul[v1][0]==0:
                            feul[v1]=False

                    if smash[v1]>0:
                        pourc[v1]=smashattqdir[v1]
                        if eject[v1]!=None:
                            eject[v1][2]=0
                        smash[v1]-=1
                if p[v1]==6:
                    if billy[v1] > y[v2] and  billx[v1]+pw[v1]/2 > x[v2] and billx[v1] < x[v2]+pw[v2] and billt[v1]>1:
                        pourc[v2]+=0.05
                    if sprint[v1]>0:
                        sprint[v1]-=1
                        if dir[v1]==0:
                            x_move[v1]=0.9
                        if dir[v1]==1:
                            x_move[v1]=-0.9
                        if sprint[v1]==0:
                            x_move[v1]=0
                            if dir[v1]==0:
                                sprite[v1]=image1
                            if dir[v1]==1:
                                sprite[v1]=image2
                    if sprintt[v1]>0:
                        sprintt[v1]-=1
                    if sansray[v1]>0:
                        sansray[v1]-=1
                        if dir[v1]==0:
                            if y[v1]+ph[v1] > y[v2] and y[v1]<y[v2]+ph[v2] and x[v1]< x[v2] :
                                pourc[v2]+=0.005
                        if dir[v1]==1:
                            if y[v1]+ph[v1] > y[v2] and y[v1]<y[v2]+ph[v2] and x[v1]> x[v2] :
                                pourc[v2]+=0.005
                    if smash[v1]>0:
                        x_move[v1]=0
                        y_move[v1]=0
                        if smashattqdir[v1]==0:
                            if y[v1]+ph[v1]> y[v2] and y[v1]<y[v2]+ph[v2]*2 and x[v1] < x[v2] :
                                pourc[v2]+=0.05
                                eject[v2]=[0.3,0,100]
                        if smashattqdir[v1]==1:
                            if y[v1]+ph[v1]*2 > y[v2] and y[v1]>y[v2]+ph[v2]*2 and x[v1] > x[v2] :
                                pourc[v2]+=0.05
                                eject[v2]=[-0.3,0,100]
                        sprite[v2]=sansheart
                if p[v1]==7:
                    if billmt[v1]==1:
                        y[v1]-=ph[v1]*3
                    if block[v1]>0:
                        block[v1]-=1
                        if block[v1]>10000:
                            sprite[v1]=thanothing
                    if sprint[v1]>5:
                        sprint[v1]=1
                        if dir[v1]==0:
                            x[v1]+=ph[v1]*3
                        if dir[v1]==1:
                            x[v1]-=ph[v1]*3
                    if sprintt[v1]>0:
                        sprintt[v1]-=1
                    if sansray[v1]>0:
                        sansray[v1]-=1
                        if dir[v1]==0:
                            if y[v1]+ph[v1] > y[v2] and y[v1]<y[v2]+ph[v2] and x[v1]< x[v2] :
                                pourc[v2]+=0.005
                        if dir[v1]==1:
                            if y[v1]+ph[v1] > y[v2] and y[v1]<y[v2]+ph[v2] and x[v1]> x[v2] :
                                pourc[v2]+=0.005
                    if smash[v1]==1:
                        popo=random.randint(0,300)
                        pourc[v2]+=popo
                        smash[v1]=0
                if p[v1]==8:
                    if billmt[v1]==1:
                        sprite[v1]=crashtornade
                        if y[v1]+ph[v1] > y[v2] and y[v1] < y[v2]+pw[v2] and x[v1]+ph[v1] > x[v2] and x[v1] < x[v2]+pw[v2]:
                            pourc[v2]+=0.1
                        if saut[v1]==0:
                            billmt[v1]=0
                            sprite[v1]=image1
                    if ltourn[v1]!=False:
                        if saut[v1]==0:
                            ltourn[v1]=False

                        sprite[v1]=crashhaut0
                        if y[v1]+ph[v1] > y[v2] and y[v1] < y[v2]+pw[v2] and x[v1]+ph[v1] > x[v2] and x[v1] < x[v2]+pw[v2]:
                            pourc[v2]+=0.01
                    if sprint[v1]>0:
                        sprint[v1]-=1
                        standvue=2
                        if dir[v1]==0:
                            x_move[v1]=0.5
                            sprite[v1]=crashfonc0
                        if dir[v1]==1:
                            x_move[v1]=-0.5
                            sprite[v1]=crashfonc1

                        if sprint[v1]==0:
                            standvue=0
                            x_move[v1]=0
                            if dir[v1]==0:
                                sprite[v1]=image1
                            if dir[v1]==1:
                                sprite[v1]=image2
                        if y[v1]+pw[v1] > y[v2] and y[v1] < y[v2]+pw[v2] and x[v1]+pw[v1] > x[v2] and x[v1] < x[v2]+pw[v2] and sprint[v1]>0:
                            pourc[v2]+=0.03
                    if sprintt[v1]>0:
                        sprintt[v1]-=1
                    if feu[v1] != False:
                        naoppm=0
                        naopp=0
                        for i in range(1,feu[v1][0]+1):

                            if feu[v1][3+5*(i-1)]==0:
                                feu[v1][1+5*(i-1)]+=0.006*pw[v1]
                            if feu[v1][3+5*(i-1)]==1:
                                feu[v1][1+5*(i-1)]-=0.006*pw[v1]
                            if feu[v1][4+5*(i-1)]<=0 :
                                feu[v1][2+5*(i-1)]+=0.005*ph[v1]
                                for n in range(1,platform[0]+1):
                                    if feu[v1][2+5*(i-1)]+ph[v1]/5 > platform[1+4*(n-1)] and feu[v1][2+5*(i-1)] < platform[1+4*(n-1)]+0.084*(ph[v1]/5) and feu[v1][1+5*(i-1)] > platform[3+4*(n-1)] and feu[v1][1+5*(i-1)] < platform[4+4*(n-1)]:
                                        feu[v1][4+5*(i-1)]=1
                            if feu[v1][4+5*(i-1)]>0 :
                                feu[v1][2+5*(i-1)]-=0.005*ph[v1]
                                feu[v1][4+5*(i-1)]-=1
                            feu[v1][5+5*(i-1)]-=0.006*pw[v1]

                            if feu[v1][2+5*(i-1)]+ph[v1]/4 > y[v2] and feu[v1][2+5*(i-1)]-ph[v1]/4 < y[v2]+pw[v2] and feu[v1][1+5*(i-1)]+pw[v1]/5 > x[v2] and feu[v1][1+5*(i-1)] < x[v2]+pw[v2]:
                                if dbouclier[v2]==True:
                                    if bouclier[v2]-1000<0:

                                        bouclier[v2]=0
                                        pourc[v2]+=5

                                    elif bouclier[v2]-1000>0:


                                        bouclier[v2]-=1000
                                else:
                                    pourc[v2]+=10
                                naoppm=1
                                naopp=i



                            if feu[v1][5+5*(i-1)]<=0:
                                naopp=i


                        if feu[v1][5+5*(naopp-1)]<=0 or naoppm==1:

                            feu[v1][0]-=1
                            del feu[v1][1+5*(naopp-1)]
                            del feu[v1][1+5*(naopp-1)]
                            del feu[v1][1+5*(naopp-1)]
                            del feu[v1][1+5*(naopp-1)]
                            del feu[v1][1+5*(naopp-1)]
                            naopp=0
                            naoppm=0
                        if feu[v1][0]==0:
                            feu[v1]=False
                if poison[v2]>0:
                    poison[v2]-=1
                    pourc[v2]+=0.003
                if p[v1]==9:
                    if coupfeu[v1]<5000:
                        coupfeu[v1]+=1
                    if feul[v1] != False:
                        naoppm=0
                        naopp=0
                        for i in range(1,feul[v1][0]+1):

                            if feul[v1][3+4*(i-1)]==0:
                                feul[v1][1+4*(i-1)]+=0.006*pw[v1]
                            if feul[v1][3+4*(i-1)]==1:
                                feul[v1][1+4*(i-1)]-=0.006*pw[v1]
                            feul[v1][4+4*(i-1)]-=0.006*pw[v1]

                            if feul[v1][2+4*(i-1)]+ph[v1]/5 > y[v2] and feul[v1][2+4*(i-1)] < y[v2]+pw[v2] and feul[v1][1+4*(i-1)]+pw[v1]/5 > x[v2] and feul[v1][1+4*(i-1)] < x[v2]+pw[v2]:
                                if dbouclier[v2]==True:
                                    if bouclier[v2]-1000<0:

                                        bouclier[v2]=0
                                        pourc[v2]+=5

                                    elif bouclier[v2]-1000>0:


                                        bouclier[v2]-=1000
                                else:
                                    pourc[v2]+=5
                                poison[v2]=10000
                                naoppm=1
                                naopp=i



                            if feul[v1][4+4*(i-1)]<=0:
                                naopp=i


                        if feul[v1][4+4*(naopp-1)]<=0 or naoppm==1:

                            feul[v1][0]-=1
                            del feul[v1][1+4*(naopp-1)]
                            del feul[v1][1+4*(naopp-1)]
                            del feul[v1][1+4*(naopp-1)]
                            del feul[v1][1+4*(naopp-1)]
                            naopp=0
                            naoppm=0
                        if feul[v1][0]==0:
                            feul[v1]=False
                    if smash[v1]>0:
                        smash[v1]-=1
                        if dir[v1]==0:
                            x[v1]+=0.7
                        if dir[v1]==1:
                            x[v1]-=0.7
                        if y[v1]+pw[v1] > y[v2] and y[v1] < y[v2]+pw[v2] and x[v1]+pw[v1] > x[v2] and x[v1] < x[v2]+pw[v2]:
                            smash[v1]=0
                            pourc[v2]+=200
                if p[v1]==10:
                    if billy[v1]+ph[v1]/2 > y[v2] and billy[v1] < y[v2]+pw[v2] and billx[v1]+pw[v1]/2 > x[v2] and billx[v1] < x[v2]+pw[v2] and billt[v1]>1:
                        billt[v1]=1
                        pourc[v2]+=20
                        eject[v2]=propulse(dir[v2],pourc[v2])
                    if sprint[v1]>0:
                        sprint[v1]-=1
                        if dir[v1]==0:
                            x_move[v1]=0.5
                        if dir[v1]==1:
                            x_move[v1]=-0.5
                        if sprint[v1]==0:
                            x_move[v1]=0
                    if feu[v1] != False:
                        naoppm=0
                        naopp=0
                        for i in range(1,feu[v1][0]+1):

                            if feu[v1][3+5*(i-1)]==0:
                                feu[v1][1+5*(i-1)]+=0.006*pw[v1]
                            if feu[v1][3+5*(i-1)]==1:
                                feu[v1][1+5*(i-1)]-=0.006*pw[v1]
                            if feu[v1][4+5*(i-1)]<=0 :
                                feu[v1][2+5*(i-1)]+=0.005*ph[v1]
                                for n in range(1,platform[0]+1):
                                    if feu[v1][2+5*(i-1)]+ph[v1]/5 > platform[1+4*(n-1)] and feu[v1][2+5*(i-1)] < platform[1+4*(n-1)]+0.084*(ph[v1]/5) and feu[v1][1+5*(i-1)] > platform[3+4*(n-1)] and feu[v1][1+5*(i-1)] < platform[4+4*(n-1)]:
                                        feu[v1][4+5*(i-1)]=1
                            if feu[v1][4+5*(i-1)]>0 :
                                feu[v1][2+5*(i-1)]-=0.005*ph[v1]
                                feu[v1][4+5*(i-1)]-=1
                            feu[v1][5+5*(i-1)]-=0.006*pw[v1]

                            if feu[v1][2+5*(i-1)]+ph[v1]/4 > y[v2] and feu[v1][2+5*(i-1)]-ph[v1]/4 < y[v2]+pw[v2] and feu[v1][1+5*(i-1)]+pw[v1]/5 > x[v2] and feu[v1][1+5*(i-1)] < x[v2]+pw[v2]:
                                if dbouclier[v2]==True:
                                    if bouclier[v2]-1000<0:

                                        bouclier[v2]=0
                                        pourc[v2]+=5

                                    elif bouclier[v2]-1000>0:


                                        bouclier[v2]-=1000
                                else:
                                    pourc[v2]+=10
                                naoppm=1
                                naopp=i



                            if feu[v1][5+5*(i-1)]<=0:
                                naopp=i


                        if feu[v1][5+5*(naopp-1)]<=0 or naoppm==1:

                            feu[v1][0]-=1
                            del feu[v1][1+5*(naopp-1)]
                            del feu[v1][1+5*(naopp-1)]
                            del feu[v1][1+5*(naopp-1)]
                            del feu[v1][1+5*(naopp-1)]
                            del feu[v1][1+5*(naopp-1)]
                            naopp=0
                            naoppm=0
                        if feu[v1][0]==0:
                            feu[v1]=False
                if chratt2[v1]>0:
                    chratt2[v1]-=1
            groot(0,1)
            groot(1,0)
            if playernumber>=3:
                groot(2,0)
                groot(2,1)
                groot(0,2)
                groot(1,2)
            if playernumber==4:
                groot(0,3)
                groot(1,3)
                groot(2,3)
                groot(3,0)
                groot(3,1)
                groot(3,2)





            if dbouclier[0]==False and bouclier[0]<10000:

                bouclier[0]+=1
            if dbouclier[0]==True and bouclier[0]>0:
                so1 = 0
                bouclier[0]-=1
                so1 = pygame.Surface((100,100), pygame.SRCALPHA)
                pygame.draw.circle(so1,(255,0,0,85),(50,50),round(0.00008*pw[0]*bouclier[0]))
            if dbouclier[1]==False and bouclier[1]<10000:

                bouclier[1]+=1
            if dbouclier[1]==True and bouclier[1]>0:
                so2 = 0
                bouclier[1]-=1
                so2 = pygame.Surface((100,100), pygame.SRCALPHA)
                pygame.draw.circle(so2,(255,0,0,85),(50,50),round(0.00008*pw[1]*bouclier[1]))
            if dbouclier[2]==False and bouclier[2]<10000:

                bouclier[2]+=1
            if dbouclier[2]==True and bouclier[2]>0:
                so3 = 0
                bouclier[2]-=1
                so3 = pygame.Surface((100,100), pygame.SRCALPHA)
                pygame.draw.circle(so3,(255,0,0,85),(50,50),round(0.00008*pw[2]*bouclier[2]))
            if dbouclier[3]==False and bouclier[3]<10000:

                bouclier[3]+=1
            if dbouclier[3]==True and bouclier[3]>0:
                so4 = 0
                bouclier[3]-=1
                so4 = pygame.Surface((100,100), pygame.SRCALPHA)
                pygame.draw.circle(so4,(255,0,0,85),(50,50),round(0.00008*pw[3]*bouclier[3]))

            def trok(v1,v2):
                global ejection










                if saut[v1] > 0:
                    saut[v1] -=1
                    y_move[v1] += -0.005*ph[v1]
                if saut[v1] ==0:
                    y_move[v1] += 0.005*ph[v1]



                if eject[v1] != None:

                    y_move[v1]=0
                    x[v1]+=eject[v1][0]
                    y[v1]+=eject[v1][1]
                    eject[v1][2]-=1
                    if eject[v1][2]<0:
                        eject[v1]=None




                y[v1] += y_move[v1]
                x[v1] += x_move[v1]
                if p[v1]==3:
                    if smash[v1]>2:
                        y[v2] -= y_move[v2]
                        x[v2] -= x_move[v2]
                        x[v2]+=x_move[v2]/3
                        y[v2]+=y_move[v2]/3

                for i in range(1,platform[0]+1):

                    if y[v1] > platform[2+4*(i-1)]-0.084*ph[v1] and y[v1] < platform[2+4*(i-1)] and x[v1] > platform[3+4*(i-1)] and x[v1] < platform[4+4*(i-1)]:
                        y[v1] = platform[2+4*(i-1)]
                        saut[v1]=0
                        if eject[v1] != None:
                            if eject[v1][1]<0:
                                eject[v1][1] = -eject[v1][1]


                    if y[v1]+ph[v1] > platform[1+4*(i-1)] and y[v1] < platform[1+4*(i-1)]+0.084*ph[v1] and x[v1] > platform[3+4*(i-1)] and x[v1] < platform[4+4*(i-1)]:
                        y[v1] = platform[1+4*(i-1)]-ph[v1]
                        nsaut[v1]=0
                        if eject[v1] != None:
                            if eject[v1][1]>0:
                                eject[v1][1] = -eject[v1][1]

                    if y[v1] > platform[1+4*(i-1)] and y[v1] < platform[2+4*(i-1)] and x[v1] > platform[4+4*(i-1)]-pw[v1] and x[v1] < platform[4+4*(i-1)]:
                        x[v1] = platform[4+4*(i-1)]
                        nsaut[v1]=0
                        if eject[v1] != None:
                            if eject[v1][0]<0:
                                eject[v1][0]=-eject[v1][0]

                    if y[v1] > platform[1+4*(i-1)] and y[v1] < platform[2+4*(i-1)] and x[v1]+50 > platform[3+4*(i-1)] and x[v1] < platform[3+4*(i-1)]+pw[v1]:
                        x[v1] = platform[3+4*(i-1)]-pw[v1]
                        nsaut[v1]=0
                        if eject[v1] != None:
                            if eject[v1][0]>0:
                                eject[v1][0]=-eject[v1][0]








                if vie[v1]>0:
                    if x[v1] < -200 or x[v1] > 1000 or y[v1] > 600  :
                        if pp[v1]==False:
                            dx[v1]=x[v1]
                            dy[v1]=y[v1]
                            if musique==True:
                                koson.play()
                            if bosspart1!=1:
                                surface.blit(fond,(0,0))
                            if x[v1]<0:
                                dx[v1]=-70
                                ejection=pygame.transform.rotate(ejectim,-45+0.225*y[v1])
                                ejetem1[v1]=1000
                            if x[v1]>800:
                                ejection=pygame.transform.rotate(ejectim,225-0.225*y[v1])
                                ejetem2[v1]=1000
                            if y[v1]>450:
                                ejection=pygame.transform.rotate(ejectim,45+0.1125*x[v1])
                                ejetem3[v1]=1000
                            pygame.display.update(x[v1],y[v1],x[v1]+pw[v1]+10,y[v1]+ph[v1]+10)
                            pejecty[v1]=y[v1]
                            pejectx[v1]=x[v1]

                            vie[v1]-=1
                            pp[v1]=True
                            pourc[v1]=0
                            eject[v1]=None



                if y[v1] <0 :
                    pygame.display.update(x[v1]-20,0,x[v1]+pw[v1]+20,ph[v1]+20)



                if x[v1] < 0 or x[v1] > 800 or y[v1] > 450:
                    pygame.display.update(x[v1],y[v1]-50,x[v1]+pw[v1]+220,y[v1]+ph[v1]+50)
            trok(0,1)
            trok(1,0)
            if playernumber>=3:
                trok(2,1)
            if playernumber==4:
                trok(3,1)


            if balexist==False:
                ballrand=random.randint(0,90000)
                if ballrand==500:
                    balexist=True
                    ballpv=100



            if p[1]=="Boss1" and bosspart1==1:
                surface.blit(fond,(0-round(avancementmap),0))
                surface.blit(iconethomas,(0,0))
                if avancementmap<5800:
                    avancementmap+=0.3
                    for i in range(1,platform[0]+1):
                        platform[3+4*(i-1)]-=0.3
                        round(platform[3+4*(i-1)])
                        platform[4+4*(i-1)]-=0.3
                        round(platform[4+4*(i-1)])
                    x[0]-=0.3
                    x[1]=-100
                    y[1]=200
                else:
                    if x[0]>500:
                        game_over=True
                if x[0]<200:
                    vie[0]=0
                    bosspart1=0
            else:
                surface.blit(fond,(0,0))

            if map==1:
                tetris+=1
                if tetris==50000:
                    fond = pygame.image.load("map/1/2.png").convert()
                    fond = pygame.transform.scale(fond,(800,450))
                    surface.blit(fond,(0,0))
                    pygame.display.update(0,0,800,450)
                if tetris==100000:
                    fond = pygame.image.load("map/1/1.png").convert()
                    fond = pygame.transform.scale(fond,(800,450))
                    surface.blit(fond,(0,0))
                    pygame.display.update(0,0,800,450)
                    tetris=0

            if map==3:
                spritew0 = pygame.transform.scale(sprite[0],(10,20))
                spritew1 = pygame.transform.scale(sprite[1],(10,20))
                if x[0]>0 and x[0]<800 and y[0]>0 and y[0]<450:
                    surface.blit(spritew0,(283+round(x[0]/3.34),84+round(y[0]/4.16)))
                if x[1]>0 and x[1]<800 and y[1]>0 and y[1]<450:
                    surface.blit(spritew1,(283+round(x[1]/3.34),84+round(y[1]/4.16)))
                if playernumber>=3:
                    spritew2 = pygame.transform.scale(sprite[2],(10,20))
                    if x[2]>0 and x[2]<800 and y[2]>0 and y[2]<450:
                        surface.blit(spritew2,(283+round(x[2]/3.34),84+round(y[2]/4.16)))
                if playernumber==4:
                    spritew3 = pygame.transform.scale(sprite[3],(10,20))
                    if x[3]>0 and x[3]<800 and y[3]>0 and y[3]<450:
                        surface.blit(spritew3,(283+round(x[3]/3.34),84+round(y[3]/4.16)))
            if map==4:
                tetris+=1
                if tetris >= 50000 and tetris<=60000:
                    platform[5]+=0.04
                    platform[6]+=0.04
                surface.blit(tblock4,(round(platform[7]),round(platform[5])))
                if tetris >= 10000 and tetris<=20000:
                    platform[9]+=0.04
                    platform[10]+=0.04
                surface.blit(tblock4,(round(platform[11]),round(platform[9])))
                if tetris >= 40000 and tetris<=50000:
                    platform[13]+=0.04
                    platform[14]+=0.04
                surface.blit(tblock1,(round(platform[15]),round(platform[13])))
                if tetris >= 30000 and tetris<=40000:
                    platform[17]+=0.04
                    platform[18]+=0.04
                    platform[21]+=0.04
                    platform[22]+=0.04
                surface.blit(tblock2,(round(platform[23]),round(platform[21])))
                if tetris >= 20000 and tetris<=30000:
                    platform[25]+=0.04
                    platform[26]+=0.04
                    platform[29]+=0.04
                    platform[30]+=0.04
                surface.blit(tblock3,(round(platform[27]),round(platform[25]-29)))
                if tetris==61000:
                    platform = [8,363,600,253,544,-100,-40,427,486,-100,-40,486,543,-100,-70,282,399,-70,-40,253,340,-100,-70,253,282,-70,-40,340,428,-100,-70,398,428]
                    tetris=0






            label1 = myfont.render("%"+str(round(pourc[0])), 1, (0,0,0),(255,255,255))
            surface.blit(label1, (20, 350))
            label2 = myfont.render("%"+str(round(pourc[1])), 1, (0,0,0),(255,255,255))
            surface.blit(label2, (600, 350))
            if playernumber==3:
                label3 = myfont.render("%"+str(round(pourc[2])), 1, (0,0,0),(255,255,255))
                surface.blit(label3, (300, 350))
            if vie[0]>0:
                surface.blit(vie1png,(25,420))
                if vie[0]>1:
                    surface.blit(vie1png,(55,420))
                    if vie[0]>=3:
                        surface.blit(vie1png,(85,420))

            if vie[0]==0:
                if playernumber>=3:
                    if vie[2]==0 or vie[1]==0:
                        if musique==True:
                            gamesound.play()
                        game_over=True
                else:
                    if musique==True:
                        gamesound.play()
                    game_over = True

            if vie[1]==0:
                if playernumber>=3:
                    if vie[2]==0 or vie[0]==0:
                        if musique==True:
                            gamesound.play()
                        game_over=True
                else:
                    if musique==True:
                        gamesound.play
                    game_over = True
            if playernumber>=3:
                if vie[2]==0:
                    if playernumber>=3:
                        if vie[1]==0 or vie[0]==0:
                            if musique==True:
                                gamesound.play()
                            game_over=True
                    else:
                        if musique==True:
                            gamesound.play()
                        game_over = True



            if vie[1]>0:
                surface.blit(vie2png,(650,420))
                if vie[1]>1:
                    surface.blit(vie2png,(670,420))
                    if vie[1]>=3:
                        surface.blit(vie2png,(700,420))
            if playernumber==3 and vie[2]>0:
                if vie[2]>0:
                    surface.blit(vie3png,(350,420))
                    if vie[2]>1:
                        surface.blit(vie3png,(370,420))
                        if vie[2]>=3:
                            surface.blit(vie3png,(400,420))
            if playernumber==4:
                if vie[2]>0:
                    label3 = myfont.render("%"+str(round(pourc[2])), 1, (0,0,0),(255,255,255))
                    surface.blit(label3, (220, 350))
                if vie[3]>0:
                    label4 = myfont.render("%"+str(round(pourc[3])), 1, (0,0,0),(255,255,255))
                    surface.blit(label4, (420, 350))
                if vie[2]>0:
                    surface.blit(vie3png,(250,420))
                    if vie[2]>1:
                        surface.blit(vie3png,(270,420))
                        if vie[2]>=3:
                            surface.blit(vie3png,(300,420))
                if vie[3]>0:
                    surface.blit(vie4png,(450,420))
                    if vie[3]>1:
                        surface.blit(vie4png,(470,420))
                        if vie[3]>=3:
                            surface.blit(vie4png,(500,420))

            def prossd(v1,v2):
                global ippx,ippy
                if p[v1]==3:
                    if smash[v1]>2:
                        surface.blit(zawarudo,(x[v1]-1000,y[v1]-1000))

                if stand[v1]==True:

                    if standvue[v1]==0:
                        if dir[v1]==0:
                            surface.blit(pstand0,(round(x[v1]-pw[v1]/2),round(y[v1]-pw[v1]/2)))
                        if dir[v1]==1:
                            surface.blit(pstand1,(round(x[v1]-pw[v1]/2),round(y[v1]-pw[v1]/2)))
                    if standvue[v1]==1:

                        if dir[v1]==0:
                            surface.blit(standcoup0,(round(x[v1]-pw[v1]/2),round(y[v1]-pw[v1]/2)))
                        if dir[v1]==1:
                            surface.blit(standcoup1,(round(x[v1]-pw[v1]/2),round(y[v1]-pw[v1]/2)))
                    if standvue[v1]==2:

                        if dir[v1]==0:
                            surface.blit(standfonc0,(round(x[v1]-pw[v1]/2),round(y[v1]-pw[v1]/2)))
                        if dir[v1]==1:
                            surface.blit(standfonc1,(round(x[v1]-pw[v1]/2),round(y[v1]-pw[v1]/2)))
                ballon1(x[v1],y[v1],sprite[v1])
                if p[1]=="Boss1" and bosspart1==1:
                    pygame.display.update(0,0,800,450)




                if objet[v1]!=None:
                    obj1 = pygame.transform.scale(objet[v1],(round(pw[v1]/2),round(pw[v1]/2)))
                    surface.blit(obj1,(x[v1],y[v1]))

                if chratt3[v1]==True:
                        surface.blit(counter,(x[v1]-10,y[v1]))
                        pygame.display.update(x[v1],y[v1],ph[v1],ph[v1])
                        chratt3[v1]=False
                if p[v1]==1:
                    if feu[v1] !=False:
                        for i in range(1,feu[v1][0]+1):
                            if feu[v1][5+5*(i-1)]>1:
                                surface.blit(feum,(feu[v1][1+5*(i-1)],feu[v1][2+5*(i-1)]))
                            pygame.display.update(feu[v1][1+5*(i-1)]-10,feu[v1][2+5*(i-1)]-10,feu[v1][1+5*(i-1)]+10,feu[v1][2+5*(i-1)]+10)
                            if feu[v1][1+5*(i-1)]<0:
                                pygame.display.update(0,feu[v1][2+5*(i-1)]-20,30,feu[v1][2+5*(i-1)]+20)



                    if billt[v1]==1:
                        pygame.display.update(round(billx[v1]),round(billy[v1]),ph[v1],ph[v1])
                        billt[v1]=0
                        billmt[v1]=0
                    if billt[v1]>=2:
                        surface.blit(bill,(round(billx[v1]),round(billy[v1])))
                        pygame.display.update(round(billx[v1]),round(billy[v1]),ph[v1],ph[v1])
                        billy[v1]-=0.1
                        billt[v1]-=1
                    if enterre[v2]==1:
                        enterre[v2]=0
                        pygame.display.update(terrex[v2]-20,terrey[v2]-20,pw[v2]*3,ph[v1]*3)
                    if enterre[v2]>=2:
                        x[v2]=terrex[v2]
                        y[v2]=terrey[v2]
                        enterre[v2]-=1
                        surface.blit(terre,(round(x[v2]-pw[v2]/2),round(y[v2]+ph[v2]/2)))
                        pygame.display.update(terrex[v2]-20,terrey[v2]-20,pw[v2]*3,ph[v2]*3)
                    if block[v1]==1:
                        pygame.display.update(blockxx[v1],blockyx[v1],50,70)
                        block[v1]=0
                    if block[v1]>1:
                        x[v1]=blockx[v1]
                        y[v1]=blocky[v1]
                        block[v1]-=1
                        surface.blit(blockim,(blockxx[v1],blockyx[v1]))
                        pygame.display.update(blockxx[v1],blockyx[v1],50,70)
                    if smash[v1]==1:
                        pygame.display.update(smashattqx[v1]-10,smashattqy[v1]-10,pw[v1]*5,pw[v1]*5)
                    if smash[v1]>1:
                        surface.blit(smashattq,(smashattqx[v1],smashattqy[v1]))
                        pygame.display.update(smashattqx[v1]-10,smashattqy[v1]-10,pw[v1]*5,pw[v1]*5)
                if p[v1]==2:

                    if feul[v1] !=False:
                        for i in range(1,feul[v1][0]+1):
                            if feul[v1][4+4*(i-1)]>1:
                                surface.blit(feulm,(feul[v1][1+4*(i-1)],feul[v1][2+4*(i-1)]))
                            pygame.display.update(feul[v1][1+4*(i-1)]-10,feul[v1][2+4*(i-1)]-10,feul[v1][1+4*(i-1)]+10,feul[v1][2+4*(i-1)]+10)
                            if feul[v1][1+4*(i-1)]<0:
                                pygame.display.update(0,feul[v1][2+4*(i-1)]-20,30,feul[v1][2+4*(i-1)]+20)
                    if billt[v1]==1:
                        artifice[v1]=1600
                        billt[v1]=0

                    if billt[v1]>=2:
                        surface.blit(fusee,(round(billx[v1]),round(billy[v1])))
                        pygame.display.update(round(billx[v1]),round(billy[v1]),ph[v1],ph[v1])
                        billy[v1]-=0.1
                        billt[v1]-=1
                    if artifice[v1]==1:
                        artifice[v1]=0
                        billmt[v1]=0
                        pygame.display.update(round(billx[v1]-ph[v1]-20),round(billy[v1]-ph[v1]-20),4*ph[v1],4*ph[v1])
                    if artifice[v1]>=2:

                        artifice[v1]-=1
                        surface.blit(feuarti,(round(billx[v1]-ph[v1]),round(billy[v1]-ph[v1])))
                        pygame.display.update(round(billx[v1]-ph[v1]-20),round(billy[v1]-ph[v1]-20),4*ph[v1],4*ph[v1])
                    if tornade[v1]==1:
                        tornade[v1]=0
                        pygame.display.update(round(x[v1]-ph[v1]-20),round(y[v1]-ph[v1]-20),4*ph[v1],4*ph[v1])
                    if tornade[v1]==2:
                        surface.blit(tornadem,(round(x[v1]-pw[v1]/2),round(y[v1]-ph[v1])))
                        pygame.display.update(round(x[v1]-ph[v1]-20),round(y[v1]-ph[v1]-20),4*ph[v1],4*ph[v1])
                        tornade[v1]=1
                    if smash[v1]>9990 and smash[v1]<=10000:
                        ippx=x[v1]
                        ippy=y[v1]
                        surface.blit(lcorps,(round(ippx-ph[v1]*1.5),round(ippy+ph[v1]*1.5)))
                        pygame.display.update(ippx-20-ph[v1],ippy-20,ph[v1]*5,ph[v1]*4)
                    if smash[v1]==1:
                        pygame.display.update(ippx-20-ph[v1],ippy-20,ph[v1]*5,ph[v1]*5)
                    if smash[v1]>2:
                        surface.blit(lcorps,(round(ippx-ph[v1]*1.5),round(ippy+ph[v1]*1.5)))
                        if dir[v1]==0:
                            surface.blit(luigismash2,(round(x[v1]-ph[v1]/2),round(y[v1]-ph[v1]/2)))
                        if dir[v1]==1:
                            surface.blit(luigismash1,(round(x[v1]-ph[v1]/2),round(y[v1]-ph[v1]/2)))
                        pygame.display.update(x[v1]-2*ph[v1],y[v1]-ph[v1],ph[v1]*5,ph[v1]*4)
                if p[v1]==3:
                    if feul[v1] !=False:
                        for i in range(1,feul[v1][0]+1):
                            if feul[v1][4+4*(i-1)]>1:
                                if feul[v1][3+4*(i-1)]==0:
                                    surface.blit(couteaud,(feul[v1][1+4*(i-1)],feul[v1][2+4*(i-1)]))
                                if feul[v1][3+4*(i-1)]==1:
                                    surface.blit(couteaug,(feul[v1][1+4*(i-1)],feul[v1][2+4*(i-1)]))
                            pygame.display.update(feul[v1][1+4*(i-1)]-10,feul[v1][2+4*(i-1)]-10,feul[v1][1+4*(i-1)]+10,feul[v1][2+4*(i-1)]+10)
                            if feul[v1][1+4*(i-1)]<0:
                                pygame.display.update(0,feul[v1][2+4*(i-1)]-20,30,feul[v1][2+4*(i-1)]+20)
                    if billt[v1]==1:
                        pygame.display.update(round(billx[v1]),round(billy[v1]),ph[v1],ph[v1])
                        billt[v1]=0
                        billmt[v1]=0
                    if billt[v1]>=2:
                        surface.blit(couteauh,(round(billx[v1]),round(billy[v1])))
                        pygame.display.update(round(billx[v1]),round(billy[v1]),ph[v1],ph[v1])
                        billy[v1]-=0.3
                        billt[v1]-=1

                    if smash[v1]>1400:
                        pygame.display.update(0,0,800,450)
                    if v1==0:
                        pygame.draw.rect(surface,(0,0,0),(20,350,40,20),2)
                    if v1==1:
                        pygame.draw.rect(surface,(0,0,0),(650,350,40,20),2)
                    if v1==2 and playernumber==3:
                        pygame.draw.rect(surface,(0,0,0),(350,350,40,20),2)
                    if v1==2 and playernumber==4:
                        pygame.draw.rect(surface,(0,0,0),(250,350,40,20),2)
                    if v1==3 and playernumber==4:
                        pygame.draw.rect(surface,(0,0,0),(450,350,40,20),2)
                    if smash[v1]==1:
                        pygame.display.update(0,0,800,450)
                    if standcharge[v1]>0:
                        if v1==0:
                            pygame.draw.rect(surface,(250,0,0),(22,352,round(standcharge[v1]/300),17))
                            if standcharge[v1]==10000:
                                pygame.draw.rect(surface,(0,250,0),(22,352,38,18))
                        if v1==1:
                            pygame.draw.rect(surface,(250,0,0),(651,352,round(standcharge[v1]/300),17))
                            if standcharge[v1]==10000:
                                pygame.draw.rect(surface,(0,250,0),(651,352,38,18))
                        if playernumber==3:
                            if v1==2:
                                pygame.draw.rect(surface,(250,0,0),(350,352,round(standcharge[v1]/300),17))
                                if standcharge[v1]==10000:
                                    pygame.draw.rect(surface,(0,250,0),(351,352,38,18))
                        if playernumber==4:
                            if v1==2:
                                pygame.draw.rect(surface,(250,0,0),(250,352,round(standcharge[v1]/300),17))
                                if standcharge[v1]==10000:
                                    pygame.draw.rect(surface,(0,250,0),(251,352,38,18))
                            if v1==3:
                                pygame.draw.rect(surface,(250,0,0),(450,352,round(standcharge[v1]/300),17))
                                if standcharge[v1]==10000:
                                    pygame.draw.rect(surface,(0,250,0),(451,352,38,18))
                if p[v1]==4:
                    if billt[v1]==1:
                        pygame.display.update(round(billx[v1]),round(billy[v1]),ph[v1]*3,ph[v1]*3)
                        billt[v1]=0
                        billmt[v1]=0
                    if billt[v1]>=2:
                        surface.blit(neterpoingh,(round(billx[v1]),round(billy[v1])),(0,0,ph[v1]*2,ph[v1]*2*1000/billt[v1]))
                        pygame.display.update(round(billx[v1]),round(billy[v1]),ph[v1]*3,ph[v1]*3)
                        billy[v1]-=0.1
                        billt[v1]-=1
                    if ltourn[v1]!=False:
                        if saut[v1]>0:
                            if dir[v1]==0:
                                surface.blit(neterhaut0,(round(x[v1]-ph[v1]/2),round(y[v1]+ph[v1])))
                            if dir[v1]==1:
                                surface.blit(neterhaut1,(round(x[v1]-ph[v1]/2),round(y[v1]+ph[v1])))
                        pygame.display.update(x[v1]-ph[v1]*2,y[v1]+ph[v1],ph[v1]*5,ph[v1]*5)
                    if tornade[v1]==1:
                        tornade[v1]=0
                        pygame.display.update(round(x[v1]-ph[v1]*2),round(y[v1]-ph[v1]*2),4*ph[v1],4*ph[v1])
                    if tornade[v1]==2:
                        surface.blit(goldball,(round(x[v1]-ph[v1]*0.15),round(y[v1]-ph[v1]*0.15)))
                        pygame.display.update(round(x[v1]-ph[v1]*2),round(y[v1]-ph[v1]*2),4*ph[v1],4*ph[v1])
                        tornade[v1]=1
                    if chratt2[v1]==1:
                        pygame.display.update(round(x[v1]),round(y[v1]-ph[v1]*2),4*ph[v1],5*ph[v1])
                    if chratt2[v1]>2:
                        if dir[v1]==0:
                            surface.blit(neterpoing0,(round(x[v1]+ph[v1]),round(y[v1]-pw[v1])),(0,0,ph[v1]*2/(chratt2[v1]-400.1),ph[v1]*2))
                            pygame.display.update(round(x[v1]),round(y[v1]-ph[v1]*2),4*ph[v1],5*ph[v1])
                        if dir[v1]==1:
                            surface.blit(neterpoing1,(round(x[v1]-ph[v1]*3),round(y[v1]-pw[v1])),(0,0,ph[v1]*2/(chratt2[v1]-400.1),ph[v1]*2))
                            pygame.display.update(round(x[v1]-ph[v1]*4),round(y[v1]-ph[v1]),4*ph[v1],4*ph[v1])
                    if smash[v1]==1:
                        pygame.display.update(round(x[v1]-ph[v1]*3),round(y[v1]-ph[v1]*2),6*ph[v1],5*ph[v1])
                    if smash[v1]>2:
                        if smashattqdir[v1]==0:
                            if smash[v1]%2==0:
                                surface.blit(shiva10,(x[v1],round(y[v1]-ph[v1]*2)))
                            else:
                                surface.blit(shiva20,(x[v1],round(y[v1]-ph[v1]*2)))
                            pygame.display.update(round(x[v1]-pw[v1]),round(y[v1]-ph[v1]*3),5*pw[v1],4*ph[v1])
                        if smashattqdir[v1]==1:
                            if smash[v1]%2==0:
                                surface.blit(shiva11,(round(x[v1]-ph[v1]*2),round(y[v1]-ph[v1]*2)))
                            else:
                                surface.blit(shiva21,(round(x[v1]-ph[v1]*2),round(y[v1]-ph[v1]*2)))
                            pygame.display.update(round(x[v1]-pw[v1]*3),round(y[v1]-ph[v1]*3),5*pw[v1],4*ph[v1])
                if p[v1]==5:
                    if feul[v1] !=False:
                        for i in range(1,feul[v1][0]+1):
                            if feul[v1][4+4*(i-1)]>1:
                                if feul[v1][3+4*(i-1)]==0:
                                    surface.blit(cupshoot0,(feul[v1][1+4*(i-1)],feul[v1][2+4*(i-1)]))
                                if feul[v1][3+4*(i-1)]==1:
                                    surface.blit(cupshoot1,(feul[v1][1+4*(i-1)],feul[v1][2+4*(i-1)]))
                            pygame.display.update(feul[v1][1+4*(i-1)]-10,feul[v1][2+4*(i-1)]-10,feul[v1][1+4*(i-1)]+10,feul[v1][2+4*(i-1)]+10)
                            if feul[v1][1+4*(i-1)]<0:
                                pygame.display.update(0,feul[v1][2+4*(i-1)]-20,30,feul[v1][2+4*(i-1)]+20)
                    if billt[v1]==1:
                        pygame.display.update(round(billx[v1]),round(billy[v1]),ph[v1],ph[v1])
                        billt[v1]=0
                        billmt[v1]=0
                    if billt[v1]>=2:
                        surface.blit(cupshooth,(round(billx[v1]),round(billy[v1])))
                        pygame.display.update(round(billx[v1]),round(billy[v1]),ph[v1],ph[v1])
                        billy[v1]-=0.3
                        billt[v1]-=1
                    if block[v1]==1:
                        pygame.display.update(round(blockx[v1]),round(blocky[v1]),ph[v1],ph[v1])
                        block[v1]=0

                    if block[v1]>=2:
                        surface.blit(cupsaut,(round(blockx[v1]),round(blocky[v1])))
                        pygame.display.update(round(blockx[v1]),round(blocky[v1]),ph[v1],ph[v1])
                        blocky[v1]-=0.3
                        block[v1]-=1
                    if smash[v1]>0:
                        if dir[v1]==0:
                            surface.blit(cupinv0,(round(x[v1]),round(y[v1])))
                        if dir[v1]==1:
                            surface.blit(cupinv1,(round(x[v1]),round(y[v1])))
                if p[v1]==6:
                    if billt[v1]==1:
                        pygame.display.update(round(billx[v1]-20),0,ph[v1]+20,billy[v2]+ph[v1]*3)
                        billt[v1]=0
                        billmt[v1]=0
                    if billt[v1]>=2:
                        pygame.draw.rect(surface,(255,255,255),(round(billx[v1]),0,pw[v1],billy[v1]))
                        surface.blit(sansshooth,(round(billx[v1]),round(billy[v1])))
                        pygame.display.update(round(billx[v1]-20),0,ph[v1]+20,billy[v2]+ph[v1]*3)
                        billt[v1]-=1
                    if sansray[v1]==1:
                        pygame.display.update(0,y[v1]-20,800,pw[v1]*2)
                        sansray[v1]=0
                    if sansray[v1]>=2:
                        if dir[v1]==0:
                            pygame.draw.rect(surface,(255,255,255),(round(x[v1]+ph[v1]*2),y[v1],800-x[v1],pw[v1]))
                            surface.blit(sansshoot0,(round(x[v1]+ph[v1]),round(y[v1])))
                            pygame.display.update(round(x[v1]-20),y[v1]-20,800-x[v1],pw[v1]*2)
                        if dir[v1]==1:
                            pygame.draw.rect(surface,(255,255,255),(0,y[v1],x[v1]-ph[v1],pw[v1]))
                            surface.blit(sansshoot1,(round(x[v1]-ph[v1]),round(y[v1])))
                            pygame.display.update(0,y[v1]-20,x[v1],pw[v1]*2)
                        sansray[v1]-=1
                    if smash[v1]==1:
                        smash[v1]=0
                        if smashattqdir[v1]==0:
                            pygame.display.update(round(x[v1]-20),y[v1]-20-ph[v1],800-x[v1],pw[v1]*4)
                        if smashattqdir[v1]==1:
                            pygame.display.update(0,y[v1]-ph[v1]-20,x[v1],pw[v1]*4)
                    if smash[v1]>=2:
                        smash[v1]-=1
                        if smashattqdir[v1]==0:
                            pygame.draw.rect(surface,(255,255,255),(round(x[v1]+ph[v1]*3),y[v1]-pw[v1],800-x[v1],pw[v1]*2))
                            surface.blit(sansshootult0,(round(x[v1]+ph[v1]),round(y[v1]-pw[v1])))
                            pygame.display.update(round(x[v1]-20),y[v1]-20,800-x[v1],pw[v1]*2)
                        if smashattqdir[v1]==1:
                            pygame.draw.rect(surface,(255,255,255),(0,y[v1]-pw[v1],x[v1]-ph[v1]*2,pw[v1]*2))
                            surface.blit(sansshootult1,(round(x[v1]-ph[v1]*2),round(y[v1]-pw[v1])))
                            pygame.display.update(0,y[v1]-ph[v1]-20,x[v1],pw[v1]*4)
                if p[v1]==7:
                    if billmt[v1]==1:
                        billmt[v1]=0
                        pygame.display.update(billx[v1]-10,billy[v1]-10,pw[v1]+20,ph[v1]+20)
                    if tornade[v1]==1:
                        tornade[v1]=0
                        pygame.display.update(0,0,800,450)
                    if tornade[v1]==2:
                        tornade[v1]=1
                        pygame.display.update(x[v1]-10,y[v1]-10,pw[v1]+10,ph[v1]+10)
                        x[v1]=tlockx[v1]
                        y[v1]=tlocky[v1]
                    if sprint[v1]==1:
                        sprint[v1]=0
                        pygame.display.update(0,0,800,450)
                    if sansray[v1]==1:

                        pygame.display.update(0,y[v1],800,ph[v1])

                        sansray[v1]=0
                    if sansray[v1]>=2:
                        if dir[v1]==0:
                            pygame.draw.rect(surface,(139,0,139),(round(x[v1]+pw[v1]),round(y[v1]+pw[v1]/2),800-x[v1],round(pw[v1]/4)))
                            pygame.display.update(round(x[v1]-20),y[v1],800-x[v1],ph[v1])
                        if dir[v1]==1:
                            pygame.draw.rect(surface,(139,0,139),(0,round(y[v1]+pw[v1]/2),x[v1],round(pw[v1]/4)))
                            pygame.display.update(0,y[v1],x[v1]+20,ph[v1])
                        sansray[v1]-=1
                if p[v1]==8:
                    if tlock[v1]==True and pourc[v1]>0:
                        tlock[v1]=False
                        pourc[v1]-=0.005
                        surface.blit(crashshoot,(round(x[v1]),round(y[v1])))
                    if feu[v1] !=False:
                        for i in range(1,feu[v1][0]+1):
                            if feu[v1][5+5*(i-1)]>1:
                                surface.blit(crashshoot,(feu[v1][1+5*(i-1)],feu[v1][2+5*(i-1)]))
                            pygame.display.update(feu[v1][1+5*(i-1)]-10,feu[v1][2+5*(i-1)]-10,feu[v1][1+5*(i-1)]+10,feu[v1][2+5*(i-1)]+10)
                            if feu[v1][1+5*(i-1)]<0:
                                pygame.display.update(0,feu[v1][2+5*(i-1)]-20,30,feu[v1][2+5*(i-1)]+20)
                    if smash[v1]>0:
                        surface.blit(crashshoot,(round(x[v1]),round(y[v1]-800/smash[v1])))
                        pygame.display.update(round(x[v1]-20),round(y[v1]-800/smash[v1]-20),ph[v1],round(ph[v1]+40))
                        smash[v1]-=1
                if p[v1]==9:
                    if billmt[v1]==1:
                        billmt[v1]=0
                        pygame.display.update(0,0,800,450)
                    if billmt[v1]>=2:
                        if dir[v1]==0:
                            sprite[v1]=jamehaut0
                        if dir[v1]==1:
                            sprite[v1]=jamehaut1
                        billmt[v1]-=1
                        if y[v1] > y[v2] and x[v1]+pw[v1]*2 > x[v2] and x[v1] < x[v2]+pw[v1]*2:
                            pourc[v2]+=1
                            eject[v2]=[0,-0.3,50]
                            pygame.draw.line(surface,(100,100,100),(x[v2],y[v2]),(x[v1],y[v1]),3)
                            pygame.display.update(0,0,800,450)
                    if tornade[v1]==1:
                        tornade[v1]=0
                        pygame.display.update(0,0,800,450)
                    if tornade[v1]>=2:
                        tornade[v1]-=1

                        surface.blit(explode,(round(tlockx[v1]),round(tlocky[v1])))
                        pygame.display.update(tlockx[v1]-10,tlocky[v1]-10,ph[v1]*2+20,ph[v1]*2+20)
                        if tlocky[v1]+ph[v1] > y[v2] and tlocky[v1] < y[v2]+pw[v2] and tlockx[v1]+ph[v1] > x[v2] and tlockx[v1] < x[v2]+pw[v2]:
                            pourc[v2]+=10
                            eject[v2]=[dir[v2]*5,-3,100]
                    if sprintt[v1]==1:
                        sprintt[v1]=0
                        pygame.display.update(0,0,800,450)
                    if sprintt[v1]>=2:
                        sprintt[v1]-=1
                        if dir[v1]==0:
                            if y[v1]+pw[v1]*2 > y[v2] and y[v1]<y[v2]+pw[v2]*2 and x[v1] < x[v2]:
                                pourc[v2]+=1
                                eject[v2]=[0.3,0,50]
                                pygame.draw.line(surface,(100,100,100),(x[v2],y[v2]),(x[v1],y[v1]),3)
                                pygame.display.update(0,0,800,450)
                        if dir[v1]==1:
                            if y[v1]+pw[v1]*2 > y[v2] and y[v1]<y[v2]+pw[v2]*2 and x[v1] > x[v2]:
                                pourc[v2]+=1
                                eject[v2]=[-0.3,0,50]
                                pygame.draw.line(surface,(100,100,100),(x[v2],y[v2]),(x[v1],y[v1]),3)
                                pygame.display.update(0,0,800,450)
                    if feul[v1] !=False:
                        for i in range(1,feul[v1][0]+1):
                            if feul[v1][4+4*(i-1)]>1:
                                if feul[v1][3+4*(i-1)]==0:
                                    surface.blit(jamecout0,(feul[v1][1+4*(i-1)],feul[v1][2+4*(i-1)]))
                                if feul[v1][3+4*(i-1)]==1:
                                    surface.blit(jamecout1,(feul[v1][1+4*(i-1)],feul[v1][2+4*(i-1)]))
                            pygame.display.update(feul[v1][1+4*(i-1)]-10,feul[v1][2+4*(i-1)]-10,feul[v1][1+4*(i-1)]+10,feul[v1][2+4*(i-1)]+10)
                            if feul[v1][1+4*(i-1)]<0:
                                pygame.display.update(0,feul[v1][2+4*(i-1)]-20,30,feul[v1][2+4*(i-1)]+20)
                if p[v1]==10:
                    if billt[v1]==1:
                        pygame.display.update(round(billx[v1]),round(billy[v1]),ph[v1],ph[v1])
                        billt[v1]=0
                        billmt[v1]=0
                    if billt[v1]>=2:
                        surface.blit(trumphaut0,(round(billx[v1]),round(billy[v1])))
                        pygame.display.update(round(billx[v1]),round(billy[v1]),ph[v1],ph[v1]*2)
                        billy[v1]-=0.1
                        billt[v1]-=1
                    if tornade[v1]==10000:
                        platform[0]+=1
                        platform.append(tlocky[v1])
                        platform.append(tlocky[v1]+ph[v1])
                        platform.append(tlockx[v1])
                        platform.append(tlockx[v1]+pw[v1])
                    if tornade[v1]>=2:
                        tornade[v1]-=1
                        surface.blit(trumpwall,(tlockx[v1],tlocky[v1]))
                        pygame.display.update(tlockx[v1]-ph[v1],tlocky[v1]-ph[v1],ph[v1]*2,ph[v1]*2)
                    if tornade[v1]==1:
                        tornade[v1]=0
                        ccd = platform[0]
                        del platform[1+4*(ccd-1)]
                        del platform[1+4*(ccd-1)]
                        del platform[1+4*(ccd-1)]
                        del platform[1+4*(ccd-1)]
                        platform[0]-=1
                        pygame.display.update(0,0,800,450)
                    if smash[v1]==1:
                        pygame.display.update(0,0,800,450)
                        smash[v1]=0
                    if smash[v1]>1:
                        smash[v1]-=1
                        surface.blit(batomique,(400-ph[v1]*3,250-ph[v1]*3))
                        pygame.display.update(0,0,800,450)
                        if x[v2]>400:
                            eject[v2]=[0.3,0,100]
                        if x[v2]<400:
                            eject[v2]=[-0.3,0,100]
                        pourc[v2]+=0.02
                    if feu[v1] !=False:
                        for i in range(1,feu[v1][0]+1):
                            if feu[v1][5+5*(i-1)]>1:
                                if feu[v1][3+5*(i-1)]==0:
                                    surface.blit(trumpshoot0,(feu[v1][1+5*(i-1)],feu[v1][2+5*(i-1)]))
                                if feu[v1][3+5*(i-1)]==1:
                                    surface.blit(trumpshoot1,(feu[v1][1+5*(i-1)],feu[v1][2+5*(i-1)]))
                            pygame.display.update(feu[v1][1+5*(i-1)]-10,feu[v1][2+5*(i-1)]-10,feu[v1][1+5*(i-1)]+10,feu[v1][2+5*(i-1)]+10)
                            if feu[v1][1+5*(i-1)]<0:
                                pygame.display.update(0,feu[v1][2+5*(i-1)]-20,30,feu[v1][2+5*(i-1)]+20)
                if chratt3[v2]==True:
                        surface.blit(counter,(x[v2]-10,y[v2]))
                        pygame.display.update(x[v2],y[v2],ph[v1],ph[v1])
                        chratt3[v2]=False
            prossd(0,1)
            prossd(1,0)
            if playernumber>=3:
                prossd(2,0)
                prossd(2,1)
                prossd(0,2)
                prossd(1,2)
            if playernumber==4:
                prossd(0,3)
                prossd(1,3)
                prossd(2,3)
                prossd(3,0)
                prossd(3,1)
                prossd(3,2)

            if dbouclier[0]==True:
                surface.blit(so1,(x[0]+round(pw[0]/2)-50,y[0]+round(ph[0]/2)-50))
            if dbouclier[1]==True:
                surface.blit(so2,((x[1]+round(pw[1]/2)-50,y[1]+round(ph[1]/2)-50)))
            if dbouclier[2]==True:
                surface.blit(so3,((x[2]+round(pw[2]/2)-50,y[2]+round(ph[2]/2)-50)))
            if dbouclier[3]==True:
                surface.blit(so4,((x[3]+round(pw[3]/2)-50,y[3]+round(ph[3]/2)-50)))
            if ejetem1[0]>0:

                ejetem1[0]-=1
                if ejetem1[0]==0 and vie[0]>0:
                    pygame.display.update(0,0,800,400)
                    pp[0]=False
                    pourc[0]=0
                    x[0] = 400
                    y[0] = 100
                if ejetem1[0]>0:
                    x[0]=dx[0]
                    y[0]=dy[0]
                    surface.blit(ejection,(-50,pejecty[0]))
                    pygame.display.update(0,0,800,400)
            if ejetem2[0]>0:
                ejetem2[0]-=1
                if ejetem2[0]==0 and vie[0]>0:
                    pygame.display.update(0,0,800,400)
                    pp[0]=False
                    pourc[0]=0
                    x[0] = 400
                    y[0] = 100

                if ejetem2[0]>0:
                    x[0]=dx[0]
                    y[0]=dy[0]
                    surface.blit(ejection,(550,pejecty[0]))
                    pygame.display.update(0,0,800,400)
            if ejetem1[1]>0:

                ejetem1[1]-=1

                if ejetem1[1]==0 and vie[1]>0:
                    pygame.display.update(0,0,800,400)
                    pp[1]=False
                    pourc[1]=0
                    x[1] = 400
                    y[1] = 100
                if ejetem1[1]>0:
                    x[1]=dx[1]
                    y[1]=dy[1]
                    surface.blit(ejection,(-50,pejecty[1]))
                    pygame.display.update(0,0,800,400)
            if ejetem2[1]>0:

                ejetem2[1]-=1
                if ejetem2[1]==0 and vie[1]>0:
                    pygame.display.update(0,0,800,400)
                    pp[1]=False
                    pourc[1]=0
                    x[1] = 400
                    y[1] = 100
                if ejetem2[1]>0:
                    x[1]=dx[1]
                    y[1]=dy[1]
                    surface.blit(ejection,(550,pejecty[1]))
                    pygame.display.update(0,0,800,400)
            if ejetem1[2]>0:

                ejetem1[2]-=1
                if ejetem1[2]==0 and vie[2]>0:
                    pygame.display.update(0,0,800,400)
                    pp[2]=False
                    pourc[2]=0
                    x[2] = 400
                    y[2] = 100
                if ejetem1[2]>0:
                    x[2]=dx[2]
                    y[2]=dy[2]
                    surface.blit(ejection,(-50,pejecty[2]))
                    pygame.display.update(0,0,800,400)
            if ejetem2[2]>0:
                ejetem2[2]-=1
                if ejetem2[2]==0 and vie[2]>0:
                    pygame.display.update(0,0,800,400)
                    pp[2]=False
                    pourc[2]=0
                    x[2] = 400
                    y[2] = 100

                if ejetem2[2]>0:
                    x[2]=dx[2]
                    y[2]=dy[2]
                    surface.blit(ejection,(550,pejecty[2]))
                    pygame.display.update(0,0,800,400)
            if ejetem1[3]>0:

                ejetem1[3]-=1
                if ejetem1[3]==0 and vie[3]>0:
                    pygame.display.update(0,0,800,400)
                    pp[3]=False
                    pourc[3]=0
                    x[3] = 400
                    y[3] = 100
                if ejetem1[3]>0:
                    x[3]=dx[3]
                    y[3]=dy[3]
                    surface.blit(ejection,(-50,pejecty[3]))
                    pygame.display.update(0,0,800,400)
            if ejetem2[3]>0:
                ejetem2[3]-=1
                if ejetem2[3]==0 and vie[3]>0:
                    pygame.display.update(0,0,800,400)
                    pp[3]=False
                    pourc[3]=0
                    x[3] = 400
                    y[3] = 100

                if ejetem2[3]>0:
                    x[3]=dx[3]
                    y[3]=dy[3]
                    surface.blit(ejection,(550,pejecty[3]))
                    pygame.display.update(0,0,800,400)
            if ejetem3[0]>0:

                ejetem3[0]-=1
                if ejetem3[0]==0 and vie[0]>0:
                    pygame.display.update(0,0,800,400)
                    pp[0]=False
                    pourc[0]=0
                    x[0] = 400
                    y[0] = 100
                if ejetem3[0]>0:
                    x[0]=dx[0]
                    y[0]=dy[0]
                    surface.blit(ejection,(pejectx[0],200))
                    pygame.display.update(0,0,800,400)
            if ejetem3[1]>0:

                ejetem3[1]-=1
                if ejetem3[1]==0 and vie[1]>0:
                    pygame.display.update(0,0,800,400)
                    pp[1]=False
                    pourc[1]=0
                    x[1] = 400
                    y[1] = 100
                if ejetem3[1]>0:
                    x[1]=dx[1]
                    y[1]=dy[1]
                    surface.blit(ejection,(pejectx[1],200))
                    pygame.display.update(0,0,800,400)
            if ejetem3[2]>0:

                ejetem3[2]-=1
                if ejetem3[2]==0 and vie[2]>0:
                    pygame.display.update(0,0,800,400)
                    pp[2]=False
                    pourc[2]=0
                    x[2] = 400
                    y[2] = 100
                if ejetem3[2]>0:
                    x[2]=dx[2]
                    y[2]=dy[2]
                    surface.blit(ejection,(pejectx[2],200))
                    pygame.display.update(0,0,800,400)
            if ejetem3[3]>0:

                ejetem3[3]-=1
                if ejetem3[3]==0 and vie[3]>0:
                    pygame.display.update(0,0,800,400)
                    pp[3]=False
                    pourc[3]=0
                    x[3] = 400
                    y[3] = 100
                if ejetem3[3]>0:
                    x[3]=dx[3]
                    y[3]=dy[3]
                    surface.blit(ejection,(pejectx[3],200))
                    pygame.display.update(0,0,800,400)
            if p[1]=="Boss1" and bosspart1==1:
                pygame.display.update(0,0,800,450)
            else:
                if balexist==True and bosspart1!=1:
                    surface.blit(smash_ball,(400-ph[0],200-ph[0]))
                    pygame.display.update(400-ph[0],200-ph[0],ph[0]*2,ph[0]*2)
                pygame.display.update(x[0]-25,y[0]-25,pw[0]+75,ph[0]+75)#update de l ecran
                pygame.display.update(x[1]-25,y[1]-25,pw[1]+75,ph[1]+75)
                if playernumber>=3:
                    pygame.display.update(x[2]-25,y[2]-25,pw[2]+75,ph[2]+75)
                if playernumber==4:
                    pygame.display.update(x[3]-25,y[3]-25,pw[3]+75,ph[3]+75)
                pygame.display.update(0,350,800,100)
                if map==3:
                    pygame.display.update(283,84,239,108)
                if map==4:
                    pygame.display.update(252,0,292,365)


    if smashretour==True:



        main(surface,game_over)
        if bosspart1!=1:
            smashretour=True
            decoretour=False
            menuretour=True
            mapretour=True
            map2retour=True
        else:
            decoretour=False
            menuretour=False
            map2retour=True
            mapretour=False


        pygame.mixer.music.stop()


        surface = pygame.display.set_mode((800,400))
        fondw = pygame.image.load("all/end.png").convert()
        fondw = pygame.transform.scale(fondw,(1200,600))
        winner = image1
        winneris = myfont.render("WINNER IS PLAYER 1", 100, (0,0,0))
        if vie[1]>0:
            winner = image3
            winneris = myfont.render("WINNER IS PLAYER 2", 1, (0,0,0))

        if vie[0]>0:
            winner = image1
            winneris = myfont.render("WINNER IS PLAYER 1", 1, (0,0,0))
            if bot2==True :
                if p[1]!="Boss1" and p[1]!="Boss2":
                    if deblocage==p[1]-1:
                        deblocage+=1

            if bot2==True and avanckey!=0 and avancement<=10:
                avancement+=1
        if playernumber>=3:
            if vie[2]>0:
                winner = image5
                winneris = myfont.render("WINNER IS PLAYER 3", 1, (0,0,0))
        if playernumber==4:
            if vie[3]>0:
                winner = image7
                winneris = myfont.render("WINNER IS PLAYER 3", 1, (0,0,0))

        if bosspart1!=1:
            avanckey=0
        if animation==True:
            clock.tick(150)
            for n in range(1,300):
    
                fondw1 = pygame.transform.scale(fondw,(1400-n*2,700-n))
                surface.blit(fondw1,(-300+n,-150+0.5*n))
                winner1 = pygame.transform.scale(winner,(round(150/(n/100)),round(180/(n/100))))
                surface.blit(winner1,(400-0.5*round(150/(n/100)),220-round(180/(n/100))))
                pygame.display.update(0,0,800,400)
            clock.tick(500)
            for y in range(1,300):
    
                fondw1 = pygame.transform.scale(fondw,(800+y*2,400+y))
                surface.blit(fondw1,(-y,-0.5*y))
                winner1 = pygame.transform.scale(winner,(round(50*(y/100)),round(60*(y/100))))
                surface.blit(winner1,(400-0.5*round(50*(y/100)),220-round(60*(y/100))))
                pygame.display.update(0,0,800,400)
        else:
            fondw1 = pygame.transform.scale(fondw,(800+300*2,400+300))
            surface.blit(fondw1,(-300,-0.5*300))
            winner1 = pygame.transform.scale(winner,(round(50*(300/100)),round(60*(300/100))))
            surface.blit(winner1,(400-0.5*round(50*(300/100)),220-round(60*(300/100))))
            pygame.display.update(0,0,800,400)
        surface.blit(winneris,(0,100))
        pygame.display.update(0,0,800,400)
        puse = False
        if bot1==True:
            bot1=False
        if bot2==True:
            bot2=False
        if bot3==True:
            bot3=False
        if bot4==True:
            bot4=False
        if bot2==True and bosspart1!=1:
            bot2=False
        while not puse:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    puse= True
                if event.type == pygame.KEYDOWN:
                    puse = True
        if bosspart1==2:
            bosspart1=0
        if bosspart1==1:
            bosspart1=2
        else:
            battleunlock=False
            choise=False
            p[1]=1


    save=[avancement,deblocage,musique,animation]
    Fichier = open('data.txt','wb')
    pickle.dump(save,Fichier)
    Fichier.close()
quit()
