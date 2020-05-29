
import pygame,sys,random,math,shelve
from pygame.locals import *

class card():
    def __init__(self,type,value):
        self.type = type
        self.value = value



def refresh(deck,show,all,cover,temp,flag):
    DISPLAYSURF.fill(blue)
    pygame.draw.rect(DISPLAYSURF,red,(200,880,200,40))
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render('Undo', True, green, red)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (300, 900)
    DISPLAYSURF.blit(textSurfaceObj,textRectObj)
    pygame.draw.rect(DISPLAYSURF,red,(500,880,200,40))
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render('New game', True, green, red)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (600, 900)
    DISPLAYSURF.blit(textSurfaceObj,textRectObj)
    pygame.draw.rect(DISPLAYSURF,red,(800,880,200,40))
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render('Hint', True, green, red)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (900, 900)
    DISPLAYSURF.blit(textSurfaceObj,textRectObj)
    if flag == 1:
        x,y = pygame.mouse.get_pos()
        for i in range(len(temp)):
            a = 'Photos/' + str(temp[i].value) + temp[i].type + '.png'
            img = pygame.image.load(a)
            img = pygame.transform.scale(img,(75,140))
            DISPLAYSURF.blit(img,(x,y+30*i))
    a = 'Photos/red_back.png'
    for i in range(7):
        img = pygame.image.load(a)
        img = pygame.transform.scale(img,(75,140))
        DISPLAYSURF.blit(img,(150*(i+1),200))
    for i in range(7):
        p = all[i]
        k = 0
        for j in p:
            a = 'Photos/' + str(j.value) + j.type + '.png'
            if k < cover[i]:
                a = 'Photos/green_back.png'
            img = pygame.image.load(a)
            img = pygame.transform.scale(img,(75,140))
            DISPLAYSURF.blit(img,(150*i+150,200+30*k))
            k = k+1
    if len(deck) != 0:
        a = 'Photos/green_back.png'
        img = pygame.image.load(a)
        img = pygame.transform.scale(img,(75,140))
        DISPLAYSURF.blit(img,(150,20))
    else:
        a = 'Photos/red_back.png'
        img = pygame.image.load(a)
        img = pygame.transform.scale(img,(75,140))
        DISPLAYSURF.blit(img,(150,20))
    if len(show) !=0:
        a = 'Photos/' + str(show[len(show)-1].value) + show[len(show)-1].type + '.png'
        img = pygame.image.load(a)
        img = pygame.transform.scale(img,(75,140))
        DISPLAYSURF.blit(img,(300,20))
    a = 'Photos/red_back.png'
    img = pygame.image.load(a)
    img = pygame.transform.scale(img,(75,140))
    DISPLAYSURF.blit(img,(600,20))
    img = pygame.image.load(a)
    img = pygame.transform.scale(img,(75,140))
    DISPLAYSURF.blit(img,(750,20))
    img = pygame.image.load(a)
    img = pygame.transform.scale(img,(75,140))
    DISPLAYSURF.blit(img,(900,20))
    img = pygame.image.load(a)
    img = pygame.transform.scale(img,(75,140))
    DISPLAYSURF.blit(img,(1050,20))
    for i in range(7,11):
        if len(all[i]) != 0:
            l = len(all[i])
            p = all[i][l-1]
            a = 'Photos/' + str(p.value) + p.type + '.png'
            img = pygame.image.load(a)
            img = pygame.transform.scale(img,(75,140))
            DISPLAYSURF.blit(img,(600 + 150*(i-7),20))
    pygame.display.update()


def check_final(temp,final):
    if len(temp) == 0 or len(temp) > 1:
        return 0
    if len(final) == 0:
        if temp[0].value == 14:
            return 1
        else:
            return 0
    p = final[len(final)-1]
    if p.value == 14 and temp[0].value == 2 and p.type == temp[0].type:
        return 1
    if p.value == temp[0].value-1 and p.type == temp[0].type:
        return 1
    else:
        return 0


def check_set(temp,set):
    if len(temp) == 0:
        return 0
    if len(set) == 0:
        if temp[0].value == 13:
            return 1
        else:
            return 0
    last = set[len(set)-1]
    if last.value == 14 or temp[0].value == 14:
        return 0
    lc = last.type
    tc = temp[0].type
    if lc == 'H' or lc == 'D':
        lc = 'R'
    else:
        lc = 'B'
    if tc == 'H' or tc == 'D':
        tc = 'R'
    else:
        tc = 'B'
    if last.value == temp[0].value + 1 and lc!=tc:
        return 1
    else:
        return 0

def con_str(a):
    if a == 'H':
        return ' of Hearts '
    elif a == 'D':
        return ' of Diamonds'
    elif a == 'S':
        return ' of Spades'
    elif a == 'C':
        return ' of Clubs'

def con_int(a):
    if a <=10:
        return str(a)
    elif a == 11:
        return 'Jack'
    elif a == 12:
        return 'Queen'
    elif a == 13:
        return 'King'
    else:
        return 'Ace'

def complete(deck,show,all,cover,undo):
    qq = 0
    hint1 = []
    while True:
        qq = 0
        for i in range(7):
            hint1 = []
            qb = 0
            if len(all[i]) !=0:
                hint1.append(all[i][len(all[i])-1])
                for j in range(7,11):
                    if check_final(hint1,all[j]) == 1:
                        undo = undo + 1
                        a = 'Save/solitaire' + str(undo)
                        shelf = shelve.open(a)
                        shelf['deck'] = deck
                        shelf['show'] = show
                        shelf['all'] = all
                        shelf['cover'] = cover
                        shelf.close()
                        all[j].append(hint1[0])
                        all[i].pop(len(all[i])-1)
                        if len(all[i]) == cover[i]:
                            cover[i] = cover[i] - 1
                        qq = 1
                        qb = 1
                        break
            if qb == 1:
                break
        hint1 = []
        if len(show) != 0:
            hint1.append(show[len(show)-1])
            for j in range(7,11):
                if check_final(hint1,all[j]) == 1:
                    undo = undo + 1
                    a = 'Save/solitaire' + str(undo)
                    shelf = shelve.open(a)
                    shelf['deck'] = deck
                    shelf['show'] = show
                    shelf['all'] = all
                    shelf['cover'] = cover
                    shelf.close()
                    all[j].append(hint1[0])
                    show.pop(len(show)-1)
                    qq = 1
                    break
        #refresh(deck,show,all,cover,hint1,0)
        if qq == 0:
            break
    return undo


def hint(deck,show,all,cover):
    hint1 = []
    for i in range(7):
        if(len(all[i])) == 0:
            continue
        for j in range(7):
            hint1 = []
            hint1.append(all[i][cover[i]])
            if hint1[0].value == 13 and cover[i] <= 0:
                continue
            if check_set(hint1,all[j]) == 1:
                b = con_int(hint1[0].value)+con_str(hint1[0].type)
                if len(all[j]) == 0:
                    c = 'Empty slot'
                else:
                    c = con_int(all[j][len(all[j])-1].value) + con_str(all[j][len(all[j])-1].type)
                return (b,c)
        for j in range(7,11):
            hint1 = []
            hint1.append(all[i][len(all[i])-1])
            if check_final(hint1,all[j]) == 1:
                b = con_int(hint1[0].value)+con_str(hint1[0].type)
                return (b,'final slot')
    if len(show) != 0:
        hint1 = []
        hint1.append(show[len(show)-1])
        for i in range(7):
            if check_set(hint1,all[i]) == 1:
                b = con_int(hint1[0].value)+con_str(hint1[0].type)
                if len(all[i]) == 0:
                    c = 'Empty slot'
                else:
                    c = con_int(all[i][len(all[i])-1].value) + con_str(all[i][len(all[i])-1].type)
                return (b,c)
        for i in range(7,11):
            if check_final(hint1,all[i]) == 1:
                b = con_int(hint1[0].value)+con_str(hint1[0].type)
                return (b,'final slot')
    return ('','')

def main_menu(deck,show,all,cover,temp,rem,undo):
    time = pygame.time.Clock()
    q = 0
    while True:
        for i in range(7):
            if cover[i] <=0:
                cover[i] = 0
        if len(all[7]) + len(all[8]) + len(all[9]) + len(all[10]) == 52:
            DISPLAYSURF.fill(blue)
            pygame.draw.rect(DISPLAYSURF,blue,(650,530,200,40))
            fontObj = pygame.font.Font('freesansbold.ttf', 64)
            textSurfaceObj = fontObj.render('You won', True, red, blue)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (750, 550)
            DISPLAYSURF.blit(textSurfaceObj,textRectObj)
            pygame.display.update()
            pygame.time.delay(3000)
            return
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            click = pygame.mouse.get_pressed()
            if event.type == MOUSEBUTTONDOWN:
                if time.tick() < 300:
                    (x,y) = pygame.mouse.get_pos()
                    if x>300 and x<375 and y>20 and y<160:
                        temp = []
                        if len(show) == 0:
                            continue
                        temp.append(show[len(show)-1])
                        for i in range(7,11):
                            az= 0
                            if check_final(temp,all[i]) == 1:
                                undo = undo + 1
                                a = 'Save/solitaire' + str(undo)
                                shelf = shelve.open(a)
                                shelf['deck'] = deck
                                shelf['show'] = show
                                shelf['all'] = all
                                shelf['cover'] = cover
                                shelf.close()
                                all[i].append(temp[0])
                                show.pop(len(show)-1)
                                az = 1
                            if az == 1:
                                break
                    x = int((x-150)/75)
                    if x%2 == 0:
                        x = x/2
                    else:
                        continue
                    if x > 6:
                        continue
                    y = int((y-200)/30)
                    l = len(all[x])
                    if y < 0 and x >=3:
                        undo = complete(deck,show,all,cover,undo)
                    #print(y,l,cover[x])
                    if y >= l-1 and y <= l+3:
                        if y >= len(all[x]):
                            y = len(all[x])-1
                        temp = []
                        if len(all[x]) == 0:
                            continue
                        temp.append(all[x][y])
                            #print('Ok')
                        for i in range(7,11):
                            az = 0
                            if check_final(temp,all[i]) == 1:
                                undo = undo + 1
                                a = 'Save/solitaire' + str(undo)
                                shelf = shelve.open(a)
                                shelf['deck'] = deck
                                shelf['show'] = show
                                shelf['all'] = all
                                shelf['cover'] = cover
                                shelf.close()
                                all[i].append(temp[0])
                                if len(all[x]) - 1 == cover[x]:
                                    cover[x] = cover[x] - 1
                                all[x].pop(len(all[x])-1)
                                az = 1
                            if az == 1:
                                break
                    refresh(deck,show,all,cover,temp,0)

                q = 0
                mouse = pygame.mouse.get_pos()
                x = mouse[0]
                y = mouse[1]
                if x > 200 and x < 400 and y > 880 and y < 920:
                    if undo == 0:
                        continue
                    a = 'Save/solitaire' + str(undo)
                    shelf = shelve.open(a)
                    deck = shelf['deck']
                    show = shelf['show']
                    all = shelf['all']
                    cover = shelf['cover']
                    temp = []
                    undo = undo-1
                    refresh(deck,show,all,cover,temp,0)
                if x > 500 and x < 700 and y > 880 and y < 920:
                    return
                if x > 800 and x < 1000 and y > 880 and y < 920:
                    (b,c) = hint(deck,show,all,cover)
                    pygame.draw.rect(DISPLAYSURF,blue,(200,950,800,40))
                    fontObj = pygame.font.Font('freesansbold.ttf', 32)
                    d = 'Move ' + b + ' to ' + c
                    if b == '' and c == '':
                        d = 'Deal a new card'
                    textSurfaceObj = fontObj.render(d, True, green, blue)
                    textRectObj = textSurfaceObj.get_rect()
                    textRectObj.center = (600, 970)
                    DISPLAYSURF.blit(textSurfaceObj,textRectObj)
                    pygame.display.update()
                if x>150 and x<225 and y>20 and y<160:
                    undo = undo + 1
                    a = 'Save/solitaire' + str(undo)
                    shelf = shelve.open(a)
                    shelf['deck'] = deck
                    shelf['show'] = show
                    shelf['all'] = all
                    shelf['cover'] = cover
                    shelf.close()
                    if(len(deck) == 0):
                        if len(show) == 0:
                            continue
                        for i in range(len(show)):
                            deck.append(show[len(show)-1-i])
                        show = []
                    show.append(deck[len(deck)-1])
                    deck.pop(len(deck)-1)
                    refresh(deck,show,all,cover,temp,0)
                if x>300 and x<375 and y>20 and y<160:
                    temp = []
                    if len(show) == 0:
                        continue
                    undo = undo + 1
                    a = 'Save/solitaire' + str(undo)
                    shelf = shelve.open(a)
                    shelf['deck'] = deck
                    shelf['show'] = show
                    shelf['all'] = all
                    shelf['cover'] = cover
                    shelf.close()
                    temp.append(show[len(show)-1])
                    rem = 11
                x = int((x-150)/75)
                if x%2 == 0:
                    x = x/2
                else:
                    continue
                if x > 6:
                    continue
                y = int((y-200)/30)
                l = len(all[x])
                #print(y,l,cover[x])
                if y < 0 and x >= 3:
                    temp = []
                    x = x+4
                    temp.append(all[x][len(all[x])-1])
                    rem = x
                if y >= cover[x] and y <= l+3:
                    if y >= len(all[x]):
                        y = len(all[x])-1
                    temp = []
                    if len(all[x]) == 0:
                        continue
                    for i in range(y,len(all[x])):
                        temp.append(all[x][i])
                        #print('Ok')
                    rem = x


            elif click[0] == 1 and event.type == MOUSEMOTION:
                q = 1
                x,y = pygame.mouse.get_pos()
                #refresh(deck,show,all,cover,temp,1)
            elif event.type == MOUSEBUTTONUP and q == 1:
                (x,y) = pygame.mouse.get_pos()
                x = int((x-150)/75)
                if x%2 == 0:
                    x = x/2
                else:
                    continue
                if x < 3 and y < 200:
                    continue
                if x >= 3 and y > 20 and y < 160:
                    x = x+4
                    if check_final(temp,all[x]) == 1:
                        undo = undo + 1
                        a = 'Save/solitaire' + str(undo)
                        shelf = shelve.open(a)
                        shelf['deck'] = deck
                        shelf['show'] = show
                        shelf['all'] = all
                        shelf['cover'] = cover
                        shelf.close()
                        for i in range(len(temp)):
                            all[x].append(temp[i])
                        if rem == 11:
                            show.pop(len(show)-1)
                        else:
                            for i in range(len(temp)):
                                l = len(all[rem])
                                all[rem].pop(l-1)
                            if len(all[rem]) == cover[rem]:
                                cover[rem] = cover[rem] - 1
                    temp = []
                    refresh(deck,show,all,cover,temp,0)
                if check_set(temp,all[x]) == 1:
                    undo = undo + 1
                    a = 'Save/solitaire' + str(undo)
                    shelf = shelve.open(a)
                    shelf['deck'] = deck
                    shelf['show'] = show
                    shelf['all'] = all
                    shelf['cover'] = cover
                    shelf.close()
                    for i in range(len(temp)):
                        all[x].append(temp[i])
                    if rem == 11:
                        show.pop(len(show)-1)
                    else:
                        for i in range(len(temp)):
                            l = len(all[rem])
                            all[rem].pop(l-1)
                        if rem >=7:
                            continue
                        if len(all[rem]) == cover[rem]:
                            cover[rem] = cover[rem] - 1
                    temp = []
                refresh(deck,show,all,cover,temp,0)



pygame.init()
DISPLAYSURF = pygame.display.set_mode((1300,1000))
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
DISPLAYSURF.fill(blue)
while True:
    deck = []
    set1=[]
    set2=[]
    set3=[]
    set4=[]
    set5=[]
    set6=[]
    set7=[]
    fin1=[]
    fin2=[]
    fin3=[]
    fin4=[]
    cover=[]
    check = []
    show = []
    all = []
    rem = 0
    temp = []
    q = 0
    undo = 0
    arr = ['H','D','S','C']
    for j in range(4):
        for i in range(13):
            a = (i+2,arr[j])
            check.append(a)
    random.shuffle(check)
    for i in range(52):
        a = check[i]
        if i == 0:
            set1.append(card(a[1],a[0]))
        elif i>=1 and i<=2:
            set2.append(card(a[1],a[0]))
        elif i>=3 and i<=5:
            set3.append(card(a[1],a[0]))
        elif i>=6 and i<=9:
            set4.append(card(a[1],a[0]))
        elif i>=10 and i<=14:
            set5.append(card(a[1],a[0]))
        elif i>=15 and i<=20:
            set6.append(card(a[1],a[0]))
        elif i>=21 and i<=27:
            set7.append(card(a[1],a[0]))
        else:
            deck.append(card(a[1],a[0]))
    all.append(set1)
    all.append(set2)
    all.append(set3)
    all.append(set4)
    all.append(set5)
    all.append(set6)
    all.append(set7)
    all.append(fin1)
    all.append(fin2)
    all.append(fin3)
    all.append(fin4)
    for i in range(7):
        cover.append(i)
    refresh(deck,show,all,cover,temp,0)
    main_menu(deck,show,all,cover,temp,rem,undo)
