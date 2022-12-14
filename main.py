from pygame import *
import random
from Objektid.Buttons import *
from Objektid.Enemy import *
from copy import *

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

def tegutse(meetod, aktiivne):
    tegu = random.randint(1,100) #Muutuja tegu väärtus on juhuslikult üks kuni sada.
    global cooldown
    global turn
    turn = 0
    cooldown = 5000
    if meetod == 'attack': #Kui mangija ründab.
        if tegu >= 70: #On nii suur võimalus vaenlasele palju kahju teha.
            aktiivne.hp -= 40 #Vähendatakse vaenlase HP väärtust.
            aktiivne.text = aktiivne.nimi+' sai nõrgale kohale pihta.' #Muudetakse ekraaniteksti
        elif tegu <= 10: #On nii suur võimalus kõrvale hüpata.
            aktiivne.text = aktiivne.nimi+' hüppas kõrvale.' #Muudetakse ekraaniteksti
        else: #Muidu on tavaline rünnak.
            aktiivne.hp -= 20 #Vähendatakse vaenlase HP väärtust.
            aktiivne.text = aktiivne.nimi+' sai pihta.' #Muudetakse ekraaniteksti
    if meetod == 'magic': #Kui mangija kasutab maagijat.
        if player['mp'] > 0: #Kui mangija MP punktid pole otsas, toimub rünnak.
            tegu = random.randint(1,100) #Muutuja tegu määrab ära, kui suure kahju maagia teeb.
            player['mp'] -= 20
            if tegu <= 20:
                aktiivne.hp -= 20 #Vähendatakse vaenlase HP väärtust.
                aktiivne.text = 'Maagia tegi vähe kahju.' #Muudetakse ekraaniteksti
            elif tegu <= 50:
                aktiivne.hp -= 30 #Vähendatakse vaenlase HP väärtust.
                aktiivne.text = 'Maagia tegi piisavat kahju.' #Muudetakse ekraaniteksti
            elif tegu <= 90:
                aktiivne.hp -= 40 #Vähendatakse vaenlase HP väärtust.
                aktiivne.text = 'Maagia tegi palju kahju.' #Muudetakse ekraaniteksti
            else:
                aktiivne.hp -= 50 #Vähendatakse vaenlase HP väärtust.
                aktiivne.text = 'Maagia tegi väga palju kahju.' #Muudetakse ekraaniteksti
        else: #Kui mangijal pole MP punkte, on käik ära raisatud.
            text = 'Sul pole piisavalt mp\'d. Maagia ei tulnud üldse välja.' #Muudetakse ekraaniteksti.
    if meetod == 'run': #Kui mangija jookseb ära...
        tegu = random.randint(1,100) #Muudan muutujat tegu, et ära määrata, kas ära jooksmine õnnestus või mitte.
        global stage
        if tegu <= 60:
            aktiivne.text = 'Sul õnnestus ära joosta. Võitlus on lõppenud.' #Muudetakse ekraaniteksti
            stage = 'overworld'
            cooldown = 5000
            return True
        else:
            aktiivne.text = 'Sul ebaõnnestus ära joosta. Võitlus kestab edasi.' #Muudetakse ekraaniteksti
            return False
    if meetod == 'heal': #Kui mangija võtab aega, et terveneda...
        tegu = random.randint(1,100) #Muudan muutuja tegu väärtust, et ära määrata, kui palju mangija paraneb.
        aktiivne.text = 'Sa võtsid aega, et terveneda.' #Muudetakse ekraaniteksti.
        if tegu <= 25:
            player['hp'] += 20
        elif tegu <= 50:
            player['hp'] += 40
        elif tegu <= 75:
            player['hp'] += 60
        else:
            player['hp'] += 80

def loeSätted(failinimi = 'Settings.txt'):
    file = open(failinimi, 'r', encoding='UTF-8')
    sätted = {}
    for row in file:
        rida = row.strip('\n').split(': ')
        sätted[rida[0]] = int(rida[1])
    file.close()
    return sätted

def looSätted():
    #Lugemine
    try:
        loeSätted()
    except:
        sätted = {'Akna laius': 900, 'Akna pikkus': 900}
    #Kirjutamine
    file = open('Settings.txt', 'w', encoding='UTF-8')
    esimene = True
    for säte, väärtus in sätted.items():
        if esimene:
            esimene = False
        else:
            file.write('\n')
        file.write(säte+': '+str(väärtus))
    file.close()
    
init()
try:
    settings = loeSätted()
except:
    looSätted()
    settings = loeSätted()
x_suurus = settings['Akna laius'] #Miinimum mõlema suuruse puhul on 500.
y_suurus = settings['Akna pikkus']
if x_suurus < 500: #Kui on sätitud väiksemaks kui 500, siis selleks, et mäng ei jookseks kohe kokku, sätitakse ekraani suurus 500 peale.
    x_suurus = 500
if y_suurus < 500:
    y_suurus = 500
nupud = {'Ava': StrButton('Ava')}
aken = display.set_mode([x_suurus, y_suurus])
display.set_caption('Projekt Pime: RPG')
display.set_icon(image.load('icon.png'))
font = {'80': font.Font(None, 80), '40': font.Font(None, 40)}
player = {'x': int(x_suurus/2), 'y': int(y_suurus-100), 'kiirus_x': 0, 'kiirus_y': 0, 'hp': 200, 'maxhp': 200, 'mp': 100, 'maxmp': 100, 'xp': 0, 'level': 1, 'pilt': image.load('Pildid/Kuju.png')}
totalXP = 0
turn = 1
stage = 'loading'
game = True
isclicked = False
run = False #Kas toimub jooksmist?
näide = False #Kas on juba võidusõnumit näidatud?
lnäide = False #Kas leveli tõusmise sõnumit on näidatud?
aktiivne = 0
turn = 1 #1 on mängija, 2 on vaenlane
text = ''
cooldown = 0
vaenlastearv = 3

enemylist = [Vaenlane('Vaenlane', 100, 100, 1.25, 20, image.load('Pildid/Vaenlane.png'))]

try:
    while game:
        while stage == 'menu': #Avamenüü pärast mängu käivitamist või sinna väljumist.
            hiire_x, hiire_y = mouse.get_pos()
            for k in event.get():
                if k.type == QUIT: #Kui vajutad ristist kinni, läheb mäng kinni.
                    stage = 'quit'
                if k.type == MOUSEBUTTONDOWN:
                    isclicked = True
                if k.type == MOUSEBUTTONUP:
                    if nupud['Ava'].do(hiire_x, hiire_y, x_suurus/2, y_suurus/2, 50):
                        stage = 'loading'
                    isclicked = False
            nupud['Ava'].place(aken, hiire_x, hiire_y, x_suurus/2, y_suurus/2)
            display.flip()
            time.delay(5)
        
        while stage == 'loading': #Kui jäetakse mäng varem pooleli ja siis tahetakse sealt jätkata.
            vaenlased = []
            noPosition = []
            for i in range(vaenlastearv):
                genereeritu = copy(enemylist[random.randint(0,len(enemylist)-1)])
                while True: #Positsiooni genereerimine: positsioon ei tohi olla teise mängija ega venlase lähedal.
                    gen_x = random.randint(20, x_suurus - 20 - genereeritu.pilt.get_width())
                    gen_y = random.randint(20, y_suurus - 20 - genereeritu.pilt.get_height())
                    if ((gen_x < (player['x'] - 100)) or (gen_x > (player['x'] + 100))) and ((gen_y < (player['y'] - 100)) or (gen_y > (player['y'] + 100))):
                        allowed = True
                        if len(noPosition) > 0:
                            for i in range(0,len(noPosition)):
                                if allowed:
                                    if (i+1)%2 == 0:
                                        if (gen_y > (noPosition[i] + 50)) or (gen_y < (noPosition[i] - 50)):
                                            allowed = True
                                        else:
                                            allowed = False
                                    else:
                                        if (gen_x > (noPosition[i] + 50)) or (gen_x < (noPosition[i] - 50)):
                                            allowed = True
                                        else:
                                            allowed = False
                    else:
                        allowed = False
                    if allowed:
                        genereeritu.setStrenght(player['level'])
                        genereeritu.setposition(gen_x,gen_y)
                        noPosition.append(gen_x)
                        noPosition.append(gen_y)
                        #print(genereeritu) #Selle eesmärk on testida läbi Print käsu, kas vaenlane sai õigesti genereeritud.
                        break
                vaenlased.append(genereeritu)
            stage = 'overworld'
        
        while stage == 'intro': #Kui alustatakse uut mängu, siis tuleb see staadium.
            for k in event.get():
                if k.type == QUIT: #Kui vajutad ristist kinni, läheb mäng kinni.
                    stage = 'quit'
        
        while stage == 'overworld': #Maailmas ringi liikumise staadium.
            hiire_x, hiire_y = mouse.get_pos()
            if player['hp'] <= 0:
                stage = 'lose'
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
                if hiire_x - 27 > player['x']:
                    player['kiirus_x'] = 1
                elif hiire_x - 27 < player['x']:
                    player['kiirus_x'] = -1
                if hiire_y - 42 > player['y']:
                    player['kiirus_y'] = 1
                elif hiire_y - 42 < player['y']:
                    player['kiirus_y'] = -1
            player['x'] += player['kiirus_x'] #X-telje asukoht muutub, kui parem või vasak nooleklahv on alla vajutatud.
            player['y'] += player['kiirus_y'] #Y-telje asukoht muutub, kui ülemine või alumine nooleklahv on alla vajutatud.
            aken.fill([255,255,255])
            if cooldown > 0:
                cooldown -= 1
            for vaenlane in vaenlased:
                if vaenlane.hp > 0:
                    aken.blit(vaenlane.pilt, [vaenlane.x, vaenlane.y])
                    if cooldown <= 0:
                        if player['x'] < vaenlane.x + vaenlane.pilt.get_width() and player['x'] > vaenlane.x - vaenlane.pilt.get_width() and player['y'] < vaenlane.y + vaenlane.pilt.get_height() and player['y'] > vaenlane.y - vaenlane.pilt.get_height():
                            stage = 'battle'
                            aktiivne = vaenlane
                            turn = 1
                            cooldown = 5000
                            player['kiirus_x'] = 0
                            player['kiirus_y'] = 0
                            aktiivne.text = str(vaenlane.nimi+' ründab!')
            if player['x'] >= x_suurus: #Kui mängija läheb ekraanist välja, siis tuleb teha "uus ala"
                stage = 'loading'
                player['x'] = 0 - player['pilt'].get_width() + 1
            elif player['x'] + player['pilt'].get_width() <= 0:
                stage = 'loading'
                player['x'] = x_suurus - 1
            if player['y'] >= y_suurus:
                stage = 'loading'
                player['y'] = 0 - player['pilt'].get_height() + 1
            elif player['y'] + player['pilt'].get_height() <= 0:
                stage = 'loading'
                player['y'] = y_suurus - 1
            aken.blit(player['pilt'], [player['x'], player['y']])
            näitastaatust(0)
            display.flip()
            time.delay(5)
        
        while stage == 'battle': #Võitluse staadium.
            hiire_x, hiire_y = mouse.get_pos()
            if player['hp'] <= 0:
                stage = 'lose'
            for k in event.get():
                if k.type == QUIT: #Kui vajutad ristist kinni, läheb mang kinni.
                    stage = 'quit'
                if k.type == KEYDOWN: #See sätib ära, mis juhtub siis, kui klahvi hoitakse all.
                    if cooldown == 0 and turn == 1:
                        if k.key == K_RIGHT or k.key == K_d: #Kui see on parem nooleklahv, siis pilt liigub paremale.
                            if turn == 1:
                                tegutse('heal', aktiivne)
                        if k.key == K_LEFT or k.key == K_a: #Kui see on vasak nooleklahv, siis pilt liigub vasakule.
                            if turn == 1:
                                tegutse('magic', aktiivne)
                        if k.key == K_UP or k.key == K_w: #Kui see on ülemine nooleklahv, siis pilt liigub ülesse.
                            if turn == 1:
                                tegutse('attack', aktiivne)
                        if k.key == K_DOWN or k.key == K_s: #Kui see on alumine nooleklahv, siis pilt liigub alla.
                            if turn == 1:
                                run = tegutse('run', aktiivne)
                    else:
                        cooldown = 0
                #if k.type == KEYUP: #Kui klahvist lastakse lahti, siis pildi liikumine peatub.
                    #if k.key == K_RIGHT or k.key == K_d:
                        #x
                    #if k.key == K_LEFT or k.key == K_a:
                        #x
                    #if k.key == K_UP or k.key == K_w:
                        #x
                    #if k.key == K_DOWN or k.key == K_s:
                        #x
            textdisplay = font['40'].render(aktiivne.text, 1, [0, 0, 0])
            aken.fill([255,255,255]) #Täidan ekraani valgega (RGB koodiga), et pilt endast jälgi maha ei jätaks.
            if aktiivne.hp > 0:
                aken.blit(aktiivne.pilt, [int(x_suurus/2-55/2), int(y_suurus/2-84/2)])
            näitastaatust(1)
            aken.blit(textdisplay, [int(x_suurus/2 - textdisplay.get_width()/2), int(y_suurus - textdisplay.get_height() - 20)])
            display.flip() #Uuendan ekraani.
            if cooldown > 0:
                cooldown -= 1
            if run:
                textdisplay = font['40'].render(aktiivne.text, 1, [0, 0, 0])
                aken.blit(textdisplay, [int(x_suurus/2 - textdisplay.get_width()/2), int(y_suurus - textdisplay.get_height() - 20)])
                display.flip()
                time.delay(3000)
                continue
            if aktiivne.hp <= 0 and cooldown == 0 and not (näide or lnäide):
                aktiivne.text = 'Sa võitsid võitluse! Sa said '+str(aktiivne.xp)+' kogemust juurde.'
                cooldown = 5000
                näide = True
            elif aktiivne.hp <= 0 and cooldown == 0 and lnäide:
                näide = False
                lnäide = False
                cooldown = 5000
            elif aktiivne.hp <= 0 and cooldown == 0 and (näide or lnäide):
                näide = False
                lnäide = False
                stage = 'overworld'
            if player['hp'] > player['maxhp']:
                player['hp'] = player['maxhp']
            time.delay(5) #Et arvuti ei kkäituks nagu suhkrusõltuvuses kiire väike hiir.
            if aktiivne.hp <= 0 and cooldown <= 0:
                player['xp'] += aktiivne.xp
                totalXP += aktiivne.xp
                if lnäide:
                    aktiivne.text = 'Su level tõusis! Su level on nüüd '+str(player['level'] + 1)+'!'
                    textdisplay = font['40'].render(aktiivne.text, 1, [0, 0, 0])
                    aken.blit(textdisplay, [int(x_suurus/2 - textdisplay.get_width()/2), int(y_suurus - textdisplay.get_height() - 20)])
                    display.flip() #Uuendan ekraani.
                    cooldown = 5000
            if turn == 0 and cooldown <= 0:
                player['hp'] -= aktiivne.attack()
                cooldown = 5000
                turn = 1
        if player['xp'] >= 200 + (100 * player['level']):
            player['level'] += 1
            player['maxhp'] += 100
            player['hp'] = player['maxhp']
            player['maxmp'] += 100
            player['mp'] += int(player['maxmp']/2)
            if player['mp'] > player['maxmp']:
                player['mp'] = player['maxmp']
            player['xp'] -= 200 + (100 * (player['level'] - 1))
            lnäide = True
        if stage != 'battle': #Väljumisprotokoll
            aktiivne = 0
            cooldown = 500
        
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
            stage = 'quit'
        
        while stage == 'win': #Kui mängija saab lõpubossist jagu, siis tuleb see staadium.
            for k in event.get():
                if k.type == QUIT: #Kui vajutad ristist kinni, läheb mäng kinni.
                    stage = 'quit'
        
        while stage == 'quit': #Kui mängu on kinni pandud, siis see koht küsib, kas mängija tahab väljuda, ja siis see paneb mängu kinni.
            game = False
            print('Kokku sai kogutud mängusessiooni ajal '+str(totalXP)+' XP\'d.')
            stage = 0
except: #See on sellel puhul, kui mängus tekib viga ja see jookseb kokku.
    quit() #Programm sulgeb ennast.
    print('Mäng jooksis kokku!')
    viga() #Praegu olen siia pannud meelega defineerimata funktsiooni, et vea korral näeks, kus täpselt viga on.

quit() #Sulgeb mooduli.
