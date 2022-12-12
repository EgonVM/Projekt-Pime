from pygame import *
import random
from Objektid.Buttons import *
from copy import *

class Vaenlane: #Seekord proovin teha vaenlaste klassi, mis sisaldab vaenlast väärtuse.
    def __init__(self, nimi, hp, xp, raskus, pilt, radius = 50, x = 0, y = 0):  #Määran ära väärtused.
        self.nimi = nimi #Vaenlase nimi.
        self.hp = hp #Vaenlase HP hulk.
        self.xp = xp #Kui palju XP punkte annab vaenlane võidu korral.
        self.raskus = raskus #Missugune raskusaste vaenlasel on.
        self.pilt = pilt #Vaenlase kujutis
        self.x = x #Vaenlase asukoht liikumisefaasis.
        self.y = y
        self.radius = radius #See on märkamisraadius. Kui mängija on lähedal, liigub vaenlane tema poole.
        
    def setposition(self, new_x, new_y): #See käsk sätib vaenlase uude kohta.
        self.x = new_x
        self.y = new_y
    
    def get_x(): #Järgmised kaks funktsioonid annavad tagasi vaenlase positsiooni.
        return self.x
    
    def get_y():
        return self.y
    
    def bedone(self, meetod): #Funktsioon, mis määrab ära mangija mõju vaenlasele.
        tegu = random.randint(1,100) #Muutuja tegu väärtus on juhuslikult üks kuni sada.
        global text #Toon muutuja text sisse globaalse väärtusena, et muutuks tekst võitluse ajal.
        global turn
        turn = 0
        if meetod == 'attack': #Kui mangija ründab.
            if self.raskus == "kerge": #Kui raskusaste on kerge, siis...
                if tegu >= 70: #On nii suur võimalus vaenlasele palju kahju teha.
                    self.hp -= 40 #Vähendatakse vaenlase HP väärtust.
                    text = self.nimi+' sai nõrgale kohale pihta.' #Muudetakse ekraaniteksti
                    return text #ja tagastatakse see.
                elif tegu <= 10: #On nii suur võimalus kõrvale hüpata.
                    text = self.nimi+' hüppas kõrvale.' #Muudetakse ekraaniteksti
                    return text
                else: #Muidu on tavaline rünnak.
                    self.hp -= 20 #Vähendatakse vaenlase HP väärtust.
                    text = self.nimi+' sai pihta.' #Muudetakse ekraaniteksti
                    return text
            if self.raskus == "keskmine":
                if tegu >= 80:
                    self.hp -= 40 #Vähendatakse vaenlase HP väärtust.
                    text = self.nimi+' sai nõrgale kohale pihta.' #Muudetakse ekraaniteksti
                    return text
                elif tegu <= 20:
                    text = self.nimi+' hüppas kõrvale.' #Muudetakse ekraaniteksti
                    return text
                else:
                    self.hp -= 20 #Vähendatakse vaenlase HP väärtust.
                    text = self.nimi+' sai pihta.' #Muudetakse ekraaniteksti
                    return text
            if self.raskus == "raske":
                if tegu >= 90:
                    self.hp -= 40 #Vähendatakse vaenlase HP väärtust.
                    text = self.nimi+' sai nõrgale kohale pihta.' #Muudetakse ekraaniteksti
                    return text
                elif tegu <= 30:
                    text = self.nimi+' hüppas kõrvale.' #Muudetakse ekraaniteksti
                    return text
                else:
                    self.hp -= 20 #Vähendatakse vaenlase HP väärtust.
                    text = self.nimi+' sai pihta.' #Muudetakse ekraaniteksti
                    return text
            if self.raskus == "boss":
                if tegu >= 95:
                    self.hp -= 40 #Vähendatakse vaenlase HP väärtust.
                    text = self.nimi+' sai nõrgale kohale pihta.' #Muudetakse ekraaniteksti
                    return text
                elif tegu <= 45:
                    text = self.nimi+' hüppas kõrvale.' #Muudetakse ekraaniteksti
                    return text
                else:
                    self.hp -= 20 #Vähendatakse vaenlase HP väärtust.
                    text = self.nimi+' sai pihta.' #Muudetakse ekraaniteksti
                    return text
        if meetod == 'magic': #Kui mangija kasutab maagijat.
            if player['mp'] > 0: #Kui mangija MP punktid pole otsas, toimub rünnak.
                tegu = random.randint(1,100) #Muutuja tegu määrab ära, kui suure kahju maagia teeb.
                player['mp'] -= 20
                if tegu <= 20:
                    self.hp -= 20 #Vähendatakse vaenlase HP väärtust.
                    text = 'Maagia tegi vähe kahju.' #Muudetakse ekraaniteksti
                    return text
                elif tegu <= 50:
                    self.hp -= 30 #Vähendatakse vaenlase HP väärtust.
                    text = 'Maagia tegi piisavat kahju.' #Muudetakse ekraaniteksti
                    return text
                elif tegu <= 90:
                    self.hp -= 40 #Vähendatakse vaenlase HP väärtust.
                    text = 'Maagia tegi palju kahju.' #Muudetakse ekraaniteksti
                    return text
                else:
                    self.hp -= 50 #Vähendatakse vaenlase HP väärtust.
                    text = 'Maagia tegi väga palju kahju.' #Muudetakse ekraaniteksti
                    return text
            else: #Kui mangijal pole MP punkte, on käik ära raisatud.
                text = 'Sul pole piisavalt mp\'d. Maagia ei tulnud üldse välja.' #Muudetakse ekraaniteksti.
        if meetod == 'run': #Kui mangija jookseb ära...
            global aktiivne #Toos sisse muutuja aktiivne, mille väärtus sätitakse õnnestumise korral nulliks.
            tegu = random.randint(1,100) #Muudan muutujat tegu, et ära määrata, kas ära jooksmine õnnestus või mitte.
            global stage
            global aktiivne
            if tegu <= 60:
                text = 'Sul õnnestus ära joosta. Võitlus on lõppenud.' #Muudetakse ekraaniteksti
                stage = 'overworld'
                cooldown = 10000
                aktiivne = 0
                return text
            else:
                text = 'Sul ebaõnnestus ära joosta. Võitlus kestab edasi.' #Muudetakse ekraaniteksti
                return text
        if meetod == 'heal': #Kui mangija võtab aega, et terveneda...
            tegu = random.randint(1,100) #Muudan muutuja tegu väärtust, et ära määrata, kui palju mangija paraneb.
            text = 'Sa võtsid aega, et terveneda.' #Muudetakse ekraaniteksti.
            if tegu <= 25:
                player['hp'] += 20
            elif tegu <= 50:
                player['hp'] += 40
            elif tegu <= 75:
                player['hp'] += 60
            else:
                player['hp'] += 80
            return text #Tagastan ekraaniteksti.
    
    def attack(self):
        tegu = random.randint(1,100)
        global text
        global turn
        turn = 1
        if self.raskus == 'kerge':
            if tegu <= 45:
                text = self.nimi+' püüdis sind rünnata, kuid sa hüppasid kõrvale.' #Muudetakse ekraaniteksti
                return text
            elif tegu >= 95:
                player['hp'] -= 40
                text = self.nimi+' ründas sind. Sa said suurt kahju.' #Muudetakse ekraaniteksti
                return text
            else:
                player['hp'] -= 20
                text = self.nimi+' ründas sind.' #Muudetakse ekraaniteksti
                return text
        if self.raskus == 'keskmine':
            if tegu <= 30:
                text = self.nimi+' püüdis sind rünnata, kuid sa hüppasid kõrvale.' #Muudetakse ekraaniteksti
                return text
            elif tegu >= 90:
                player['hp'] -= 40
                text = self.nimi+' ründas sind. Sa said suurt kahju.' #Muudetakse ekraaniteksti
                return text
            else:
                player['hp'] -= 20
                text = self.nimi+' ründas sind.' #Muudetakse ekraaniteksti
                return text
        if self.raskus == 'raske':
            if tegu <= 20:
                text = self.nimi+' püüdis sind rünnata, kuid sa hüppasid kõrvale.' #Muudetakse ekraaniteksti
                return text
            elif tegu >= 80:
                player['hp'] -= 40
                text = self.nimi+' ründas sind. Sa said suurt kahju.' #Muudetakse ekraaniteksti
                return text
            else:
                player['hp'] -= 20
                text = self.nimi+' ründas sind.' #Muudetakse ekraaniteksti
                return text
        if self.raskus == 'boss':
            if tegu <= 10:
                text = self.nimi+' püüdis sind rünnata, kuid sa hüppasid kõrvale.' #Muudetakse ekraaniteksti
                return text
            elif tegu >= 70:
                player['hp'] -= 40
                text = self.nimi+' ründas sind. Sa said suurt kahju.' #Muudetakse ekraaniteksti
                return text
            else:
                player['hp'] -= 20
                text = self.nimi+' ründas sind.' #Muudetakse ekraaniteksti
                return text

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
aken = display.set_mode([x_suurus, y_suurus])
display.set_caption('Projekt Pime: RPG')
display.set_icon(image.load('icon.png'))
font = {'80': font.Font(None, 80), '40': font.Font(None, 40)}
player = {'x': int(x_suurus/2), 'y': int(y_suurus-100), 'kiirus_x': 0, 'kiirus_y': 0, 'hp': 200, 'maxhp': 200, 'mp': 100, 'maxmp': 100, 'xp': 0, 'level': 1, 'pilt': image.load('Pildid/Kuju.png')}
turn = 1
stage = 'loading'
game = True
isclicked = False
aktiivne = 0
turn = 1 #1 on mängija, 2 on vaenlane
text = ''
cooldown = 0
vaenlastearv = 3

enemylist = [Vaenlane('Vaenlane', 100, 100, 'kerge', image.load('Pildid/Vaenlane.png'))]

try:
    while game:
        while stage == 'menu': #Avamenüü pärast mängu käivitamist või sinna väljumist.
            for k in event.get():
                if k.type == QUIT: #Kui vajutad ristist kinni, läheb mäng kinni.
                    stage = 'quit'
        
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
                        genereeritu.setposition(gen_x,gen_y)
                        noPosition.append(gen_x)
                        noPosition.append(gen_y)
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
                            cooldown = 500
                            player['kiirus_x'] = 0
                            player['kiirus_y'] = 0
                            text = str(vaenlane.nimi+' ründab!')
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
                    if cooldown == 0:
                        if k.key == K_RIGHT or k.key == K_d: #Kui see on parem nooleklahv, siis pilt liigub paremale.
                            if turn == 1:
                                aktiivne.bedone('heal')
                        if k.key == K_LEFT or k.key == K_a: #Kui see on vasak nooleklahv, siis pilt liigub vasakule.
                            if turn == 1:
                                aktiivne.bedone('magic')
                        if k.key == K_UP or k.key == K_w: #Kui see on ülemine nooleklahv, siis pilt liigub ülesse.
                            if turn == 1:
                                aktiivne.bedone('attack')
                        if k.key == K_DOWN or k.key == K_s: #Kui see on alumine nooleklahv, siis pilt liigub alla.
                            if turn == 1:
                                aktiivne.bedone('run')
                    else:
                        cooldown = 0
                if k.type == KEYUP: #Kui klahvist lastakse lahti, siis pildi liikumine peatub.
                    if k.key == K_RIGHT or k.key == K_d:
                        turn = 0
                    if k.key == K_LEFT or k.key == K_a:
                        turn = 0
                    if k.key == K_UP or k.key == K_w:
                        turn = 0
                    if k.key == K_DOWN or k.key == K_s:
                        turn = 0
            if cooldown > 0:
                cooldown -= 1
            if aktiivne == 0:
                textdisplay = font['40'].render(text, 1, [0, 0, 0])
                aken.blit(textdisplay, [int(x_suurus/2 - textdisplay.get_width()/2), int(y_suurus - textdisplay.get_height() - 20)])
                display.flip()
                time.delay(3000)
                continue
            if aktiivne.hp <= 0 and cooldown == 0:
                text = 'Sa võitsid võitluse! Sa said '+str(aktiivne.xp)+' kogemust juurde.'
                stage = 'overworld'
            aken.fill([255,255,255]) #Täidan ekraani valgega (RGB koodiga), et pilt endast jälgi maha ei jätaks.
            if aktiivne.hp > 0:
                aken.blit(vaenlane.pilt, [int(x_suurus/2-55/2), int(y_suurus/2-84/2)])
            textdisplay = font['40'].render(text, 1, [0, 0, 0])
            aken.blit(textdisplay, [int(x_suurus/2 - textdisplay.get_width()/2), int(y_suurus - textdisplay.get_height() - 20)])
            if player['hp'] > player['maxhp']:
                player['hp'] = player['maxhp']
            näitastaatust(1)
            display.flip() #Uuendan ekraani.
            if aktiivne.hp <= 0 and cooldown <= 0:
                player['xp'] += aktiivne.xp
                time.delay(3000)
                if player['xp'] >= 200 + (100 * player['level']):
                    text = 'Su level tõusis! Su level on nüüd '+str(player['level'] + 1)+'!'
                    textdisplay = font['40'].render(text, 1, [0, 0, 0])
                    aken.blit(textdisplay, [int(x_suurus/2 - textdisplay.get_width()/2), int(y_suurus - textdisplay.get_height() - 20)])
                    display.flip() #Uuendan ekraani.
                    time.delay(3000)
                turn = 1
                aktiivne = 0
            if turn == 0:
                time.delay(3000)
                aktiivne.attack()
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
            stage = 0
except: #See on sellel puhul, kui mängus tekib viga ja see jookseb kokku.
    viga() #Praegu olen siia pannud meelega defineerimata funktsiooni, et vea korral näeks, kus täpselt viga on.

quit() #Sulgeb mooduli.