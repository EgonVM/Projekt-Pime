from pygame import *
import random

class Vaenlane: #Seekord proovin teha vaenlaste klassi, mis sisaldab vaenlast väärtuse.
    def __init__(self, nimi, hp, xp, raskus, tugevus, pilt, radius = 50, x = 0, y = 0):  #Määran ära väärtused.
        self.nimi = nimi #Vaenlase nimi.
        self.hp = hp #Vaenlase HP hulk.
        self.xp = xp #Kui palju XP punkte annab vaenlane võidu korral.
        self.raskus = raskus #See on raskuskordaja.
        self.tugevus = tugevus #See number näitab, kui palju kahju vaenlane teeb.
        self.pilt = pilt #Vaenlase kujutis
        self.x = x #Vaenlase asukoht liikumisefaasis.
        self.y = y
        self.radius = radius #See on märkamisraadius. Kui mängija on lähedal, liigub vaenlane tema poole.
        self.text = '' #See on tekst, mida näidatakse mängus.
    
    def __str__(self):
        return f'Vaenlane {self.nimi}: HP: {self.hp}, Rünnak: {self.tugevus}, XP võites: {self.xp}\nLisainfo: See asub kohas ({self.x}, {self.y}) ja selle raskuskordaja on {self.raskus}.'
        
    def setposition(self, new_x, new_y): #See käsk sätib vaenlase uude kohta.
        self.x = new_x
        self.y = new_y
    
    def setStrenght(self, level): #See käsk muudab mängija leveli järgi vaenlase HP'd, XP'd, ja tugevust.
        if level - 1 == 0: #Level 1 väärtused on need samad väärtused, mis alguses on sätitud. Seega tuleb pass ja see jääb vahele, jättes väärtused samaks.
            pass
        else: #Kui on kõrgem level, siis muudetakse neid väärtusi, et vaenlane raskemaks teha.
            level -= 1
            self.hp = int(round(self.hp + level * self.raskus, 0))
            self.xp = int(round(self.xp + level * self.raskus, 0))
            self.tugevus = int(round(self.tugevus + level * self.raskus, 0))
    
    def get_x(): #Järgmised kaks funktsioonid annavad tagasi vaenlase positsiooni.
        return self.x
    
    def get_y():
        return self.y
    
    def attack(self):
        tegu = random.randint(1,100)
        if tegu <= 45:
            self.text = self.nimi+' püüdis sind rünnata, kuid sa hüppasid kõrvale.' #Muudetakse ekraaniteksti
            return 0
        elif tegu >= 95:
            self.text = self.nimi+' ründas sind. Sa said suurt kahju.' #Muudetakse ekraaniteksti
            return self.tugevus*2
        else:
            self.text = self.nimi+' ründas sind.' #Muudetakse ekraaniteksti
            return self.tugevus