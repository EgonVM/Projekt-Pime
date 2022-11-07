from pygame import *
import random

def näitastaatust(statistika):
    draw.rect(aken, [44,0,0], [5, 5, 200, 15])
    draw.rect(aken, [0,0,36], [5, 21, 200, 15])
    draw.rect(aken, [153,255,153], [5, 37, 200, 15])
    draw.rect(aken, [255,0,0], [5, 5, int(player['hp']*200/player['maxhp']), 15])
    draw.rect(aken, [0,0,255], [5, 21, int(player['mp']*200/player['maxmp']), 15])
    draw.rect(aken, [4, 129, 114], [5, 37, int(player['xp']*200/300), 15])
    aken.blit(font['80'].render('Level '+str(player['level']), 1, [0, 0, 0]), [8, 55])
    if statistika == 1:
        aken.blit(font['40'].render('HP: '+str(player['hp'])+'/'+str(player['maxhp']), 1, [0, 0, 0]), [210, 5])
        aken.blit(font['40'].render('MP: '+str(player['mp'])+'/'+str(player['maxmp']), 1, [0, 0, 0]), [210, 28])

init()
aken = display.set_mode([900, 900])
display.set_caption('RPG')
display.set_icon(image.load('icon.png'))
font = {'80': font.Font(None, 80), '40': font.Font(None, 40)}
player = {'x': 500, 'y': 500, 'kiirus_x': 0, 'kiirus_y': 0, 'hp': 200, 'maxhp': 200, 'mp': 100, 'maxmp': 100, 'xp': 0, 'level': 1, 'pilt': image.load('Pildid/Kuju.png')}
turn = 1
stage = 'overworld'
game = True
isclicked = False
try:
    while game:
        while stage == 'menu': #Avamenüü pärast mängu käivitamist või sinna väljumist.
            for k in event.get():
                if k.type == QUIT: #Kui vajutad ristist kinni, läheb mäng kinni.
                    stage = 'quit'
        
        while stage == 'loading': #Kui jäetakse mäng varem pooleli ja siis tahetakse sealt jätkata.
            continue
        
        while stage == 'intro': #Kui alustatakse uut mängu, siis tuleb see staadium.
            for k in event.get():
                if k.type == QUIT: #Kui vajutad ristist kinni, läheb mäng kinni.
                    stage = 'quit'
        
        while stage == 'overworld': #Maailmas ringi liikumise staadium.
            hiire_x, hiire_y = mouse.get_pos()
            for k in event.get():
                if k.type == QUIT: #Kui vajutad ristist kinni, läheb mäng kinni.
                    stage = 'quit'
                if k.type == MOUSEBUTTONDOWN:
                    isclicked = True
                if k.type == MOUSEBUTTONUP:
                    isclicked = False
                    player['kiirus_x'] = 0
                    player['kiirus_y'] = 0
                if k.type == KEYDOWN: #See sätib ära, mis juhtub siis, kui klahvi hoitakse all.
                    if k.key == K_RIGHT or k.key == K_d: #Kui see on parem nooleklahv, siis pilt liigub paremale.
                        player['kiirus_x'] = 1 #Suureneb x-telje asukoht, et paremale minna.
                    if k.key == K_LEFT or k.key == K_a: #Kui see on vasak nooleklahv, siis pilt liigub vasakule.
                        player['kiirus_x'] = -1 #Väheneb x-telje asukoht, et vasakule minna.
                    if k.key == K_UP or k.key == K_w: #Kui see on ülemine nooleklahv, siis pilt liigub ülesse.
                        player['kiirus_y'] = -1 #Väheneb y-telje asukoht, et ülesse minna.
                    if k.key == K_DOWN or k.key == K_s: #Kui see on alumine nooleklahv, siis pilt liigub alla.
                        player['kiirus_y'] = 1 #Suureneb y-telje asukoht, et alla minna.
                if k.type == KEYUP: #Kui klahvist lastakse lahti, siis pildi liikumine peatub.
                    if k.key == K_RIGHT or k.key == K_d:
                        player['kiirus_x'] = 0
                    if k.key == K_LEFT or k.key == K_a:
                        player['kiirus_x'] = 0
                    if k.key == K_UP or k.key == K_w:
                        player['kiirus_y'] = 0
                    if k.key == K_DOWN or k.key == K_s:
                        player['kiirus_y'] = 0
            if isclicked:
                if hiire_x > player['x']:
                    player['kiirus_x'] = 1
                elif hiire_x < player['x']:
                    player['kiirus_x'] = -1
                if hiire_y > player['y']:
                    player['kiirus_y'] = 1
                elif hiire_y < player['y']:
                    player['kiirus_y'] = -1
            player['x'] += player['kiirus_x'] #X-telje asukoht muutub, kui parem või vasak nooleklahv on alla vajutatud.
            player['y'] += player['kiirus_y'] #Y-telje asukoht muutub, kui ülemine või alumine nooleklahv on alla vajutatud.
            aken.fill([255,255,255])
            aken.blit(player['pilt'], [player['x'], player['y']])
            #aken.blit(player['pilt'], [hiire_x, hiire_y])
            näitastaatust(0)
            display.flip()
            time.delay(5)
        
        while stage == 'battle': #Võitluse staadium.
            hiire_x, hiire_y = mouse.get_pos()
            for k in event.get():
                if k.type == QUIT: #Kui vajutad ristist kinni, läheb mäng kinni.
                    stage = 'quit'
            näitastaatust(1)
            display.flip()
        
        while stage == 'pause': #Pausimenüü.
            for k in event.get():
                if k.type == QUIT: #Kui vajutad ristist kinni, läheb mäng kinni.
                    stage = 'quit'
        
        while stage == 'save': #Mängu salvestamise faas.
            continue
        
        while stage == 'lose': #Kui mängija tegelasel saab HP otsa, siis tuleb see staadium.
            for k in event.get():
                if k.type == QUIT: #Kui vajutad ristist kinni, läheb mäng kinni.
                    stage = 'quit'
        
        while stage == 'win': #Kui mängija saab lõpubossist jagu, siis tuleb see staadium.
            for k in event.get():
                if k.type == QUIT: #Kui vajutad ristist kinni, läheb mäng kinni.
                    stage = 'quit'
        
        while stage == 'quit': #Kui mängu on kinni pandud, siis see koht küsib, kas mängija tahab väljuda, ja siis see paneb mängu kinni.
            game = False
            stage = 0
except: #See on sellel puhul, kui mängus tekib viga ja see jookseb kokku.
    viga() #Praegu olen siia pannud meelega defineerimata funktsiooni, et vea korral näeks, kus täpselt viga on.

quit() #Sulgeb mooduli.