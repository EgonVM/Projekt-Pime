from pygame import *
import random

stage = 'menu'
game = True
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
            for k in event.get():
                if k.type == QUIT: #Kui vajutad ristist kinni, läheb mäng kinni.
                    stage = 'quit'
        
        while stage == 'battle': #Võitluse staadium.
            for k in event.get():
                if k.type == QUIT: #Kui vajutad ristist kinni, läheb mäng kinni.
                    stage = 'quit'
        
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