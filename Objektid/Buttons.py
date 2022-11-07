#Made by EgonVM 2019
from pygame import *
import random

class Button:
    def __init__(self, off = "None", on = "None", clicked = "None"):
        try:
            self.off = image.load(off)
            self.on = image.load(on)
            self.clicked = image.load(clicked)
        except:
            self.off = image.load("Pildid/Undefined.png")
            self.on = image.load("Pildid/Undefined.png")
            self.clicked = image.load("Pildid/Undefined.png")
        self.height = self.off.get_height()
        self.width = self.off.get_width()
        self.beclicked = False
    def place(self, window, hiire_x, hiire_y, bx, by):
        if not self.beclicked:
            if hiire_x > bx and hiire_x < bx + self.width and hiire_y > by and hiire_y < by + self.height:
                window.blit(self.on, [bx, by])
            else:
                window.blit(self.off, [bx, by])
        else:
            window.blit(self.clicked, [bx, by])
            
    def click(self, window, hiire_x, hiire_y, bx, by):
        if hiire_x > bx and hiire_x < bx + self.width and hiire_y > by and hiire_y < by + self.height:
            self.beclicked = True
            return self.beclicked
        else:
            self.beclicked = False
            return self.beclicked
    
    def do(self, hiire_x, hiire_y, bx, by):
        if hiire_x > bx and hiire_x < bx + self.width and hiire_y > by and hiire_y < by + self.height:
            return True
        else:
            return False
        
        
        
class ConButton: #Con is short for conditional.
    def __init__(self, off = "None", on = "None", clicked = "None", locked = "None", canclick = True):
        try:
            self.off = image.load(off)
            self.on = image.load(on)
            self.clicked = image.load(clicked)
            self.locked = image.load(locked)
        except:
            self.off = image.load("Pildid/Undefined.png")
            self.on = image.load("Pildid/Undefined.png")
            self.clicked = image.load("Pildid/Undefined.png")
            self.locked = image.load("Pildid/Undefined.png")
        self.height = self.off.get_height()
        self.width = self.off.get_width()
        self.beclicked = False
        self.canclick = canclick
    def place(self, window, hiire_x, hiire_y, bx, by):
        if not self.canclick:
            if not self.beclicked:
                if hiire_x > bx and hiire_x < bx + self.width and hiire_y > by and hiire_y < by + self.height:
                    window.blit(self.on, [bx, by])
                else:
                    window.blit(self.off, [bx, by])
            else:
                window.blit(self.clicked, [bx, by])
        else:
            window.blit(self.locked, [bx, by])
            
    def click(self, window, hiire_x, hiire_y, bx, by):
        if hiire_x > bx and hiire_x < bx + self.width and hiire_y > by and hiire_y < by + self.height and self.canclick:
            self.beclicked = True
            return self.beclicked
        else:
            self.beclicked = False
            return self.beclicked
    
    def do(self, hiire_x, hiire_y, bx, by):
        if hiire_x > bx and hiire_x < bx + self.width and hiire_y > by and hiire_y < by + self.height and self.canclick:
            return True
        else:
            return False
        
    def lock(self):
        if self.canclick:
            self.canclick = False
        
    def unlock(self):
        if not self.canclick:
            self.canclick = True
        
        
        
class ChoButton: #Cho is short for choice.
    def __init__(self, off = "None", on = "None", clicked = "None", chosen = "None", ischosen = False):
        try:
            self.off = image.load(off)
            self.on = image.load(on)
            self.clicked = image.load(clicked)
            self.chosen = image.load(chosen)
        except:
            self.off = image.load("Pildid/Undefined.png")
            self.on = image.load("Pildid/Undefined.png")
            self.clicked = image.load("Pildid/Undefined.png")
            self.locked = image.load("Pildid/Undefined.png")
        self.height = self.off.get_height()
        self.width = self.off.get_width()
        self.beclicked = False
        self.ischosen = ischosen
    def place(self, window, hiire_x, hiire_y, bx, by):
        if not self.ischosen:
            if not self.beclicked:
                if hiire_x > bx and hiire_x < bx + self.width and hiire_y > by and hiire_y < by + self.height:
                    window.blit(self.on, [bx, by])
                else:
                    window.blit(self.off, [bx, by])
            else:
                window.blit(self.clicked, [bx, by])
        else:
            window.blit(self.chosen, [bx, by])
            
    def click(self, window, hiire_x, hiire_y, bx, by):
        if hiire_x > bx and hiire_x < bx + self.width and hiire_y > by and hiire_y < by + self.height:
            self.beclicked = True
            return self.beclicked
        else:
            self.beclicked = False
            return self.beclicked
    
    def do(self, hiire_x, hiire_y, bx, by):
        if hiire_x > bx and hiire_x < bx + self.width and hiire_y > by and hiire_y < by + self.height:
            return True
        else:
            return False
        
    def choose(self):
        if not self.ischosen:
            self.ischosen = True
        
    def unchoose(self):
        if self.ischosen:
            self.ischosen = False
            
            
class StrButton: #Str is short for String.
    def __init__(self, text = "Undefined"):
        self.text = text
        self.beclicked = False
    def place(self, window, hiire_x, hiire_y, bx, by, size = 50, coloroff = [255, 255, 255], coloron = [0, 102, 255], colorclicked = [0, 51, 153]):
        fontin = font.Font(None, size)
        text = fontin.render(self.text, 1, [0, 0, 0])
        width = text.get_width()
        height = text.get_height()
        if not self.beclicked:
            if hiire_x > bx and hiire_x < bx + width and hiire_y > by and hiire_y < by + height:
                text = fontin.render(self.text, 1, coloron)
            else:
                text = fontin.render(self.text, 1, coloroff)
        else:
            text = fontin.render(self.text, 1, colorclicked)
        window.blit(text, [bx,by])
        
    def click(self, window, hiire_x, hiire_y, bx, by, size):
        fontin = font.Font(None, size)
        text = fontin.render(self.text, 1, [0, 0, 0])
        width = text.get_width()
        height = text.get_height()
        if hiire_x > bx and hiire_x < bx + width and hiire_y > by and hiire_y < by + height:
            self.beclicked = True
            return self.beclicked
        else:
            self.beclicked = False
            return self.beclicked
    
    def do(self, hiire_x, hiire_y, bx, by, size):
        fontin = font.Font(None, size)
        text = fontin.render(self.text, 1, [0, 0, 0])
        width = text.get_width()
        height = text.get_height()
        if hiire_x > bx and hiire_x < bx + width and hiire_y > by and hiire_y < by + height:
            return True
        else:
            return False


class StrConButton: #Str is short for String, Con is short for Contitional.
    def __init__(self, text = "Undefined", canclick = True):
        self.text = text
        self.beclicked = False
        self.canclick = canclick
    def place(self, window, hiire_x, hiire_y, bx, by, size = 50, coloroff = [255, 255, 255], coloron = [0, 102, 255], colorclicked = [0, 51, 153], colorno = [140, 140, 140]):
        fontin = font.Font(None, size)
        text = fontin.render(self.text, 1, [0, 0, 0])
        width = text.get_width()
        height = text.get_height()
        if not self.canclick:
            if not self.beclicked:
                if hiire_x > bx and hiire_x < bx + width and hiire_y > by and hiire_y < by + height:
                    text = fontin.render(self.text, 1, coloron)
                else:
                    text = fontin.render(self.text, 1, coloroff)
            else:
                text = fontin.render(self.text, 1, colorclicked)
        else:
            text = fontin.render(self.text, 1, colorno)
        window.blit(text, [bx,by])
        
    def click(self, window, hiire_x, hiire_y, bx, by, size):
        fontin = font.Font(None, size)
        text = fontin.render(self.text, 1, [0, 0, 0])
        width = text.get_width()
        height = text.get_height()
        if hiire_x > bx and hiire_x < bx + width and hiire_y > by and hiire_y < by + height and self.canclick:
            self.beclicked = True
            return self.beclicked
        else:
            self.beclicked = False
            return self.beclicked
    
    def do(self, hiire_x, hiire_y, bx, by, size):
        fontin = font.Font(None, size)
        text = fontin.render(self.text, 1, [0, 0, 0])
        width = text.get_width()
        height = text.get_height()
        if hiire_x > bx and hiire_x < bx + width and hiire_y > by and hiire_y < by + height and self.canclick:
            return True
        else:
            return False
    
    def lock(self):
        if self.canclick:
            self.canclick = False
        
    def unlock(self):
        if not self.canclick:
            self.canclick = True
            
class StrChoButton:
    def __init__(self, text = "Undefined", ischosen = False):
        self.text = text
        self.beclicked = False
        self.ischosen = ischosen
    def place(self, window, hiire_x, hiire_y, bx, by, size = 50, coloroff = [255, 255, 255], coloron = [0, 102, 255], colorclicked = [0, 51, 153], colorno = [140, 140, 140]):
        fontin = font.Font(None, size)
        text = fontin.render(self.text, 1, [0, 0, 0])
        width = text.get_width()
        height = text.get_height()
        if not self.ischosen:
            if not self.beclicked:
                if hiire_x > bx and hiire_x < bx + width and hiire_y > by and hiire_y < by + height:
                    text = fontin.render(self.text, 1, coloron)
                else:
                    text = fontin.render(self.text, 1, coloroff)
            else:
                text = fontin.render(self.text, 1, colorclicked)
        else:
            text = fontin.render(self.text, 1, colorno)
        window.blit(text, [bx,by])
        
    def click(self, window, hiire_x, hiire_y, bx, by, size):
        fontin = font.Font(None, size)
        text = fontin.render(self.text, 1, [0, 0, 0])
        width = text.get_width()
        height = text.get_height()
        if hiire_x > bx and hiire_x < bx + width and hiire_y > by and hiire_y < by + height:
            self.beclicked = True
            return self.beclicked
        else:
            self.beclicked = False
            return self.beclicked
    
    def do(self, hiire_x, hiire_y, bx, by, size):
        fontin = font.Font(None, size)
        text = fontin.render(self.text, 1, [0, 0, 0])
        width = text.get_width()
        height = text.get_height()
        if hiire_x > bx and hiire_x < bx + width and hiire_y > by and hiire_y < by + height:
            return True
        else:
            return False
    
    def choose(self):
        if not self.ischosen:
            self.ischosen = True
        
    def unchoose(self):
        if self.ischosen:
            self.ischosen = False

class TextButton: #Text buttons consist of two things: an empty button and a string of text that goes there.
    def __init__(self, off = "None", on = "None", clicked = "None", text = "Undefined", coloroff = [0,0,0], coloron = [0,0,150], colorclicked = [150,150,0]):
        try:
            self.off = image.load(off)
            self.on = image.load(on)
            self.clicked = image.load(clicked)
        except:
            self.off = image.load("Pildid/Undefined.png")
            self.on = image.load("Pildid/Undefined.png")
            self.clicked = image.load("Pildid/Undefined.png")
        self.height = self.off.get_height()
        self.width = self.off.get_width()
        self.text = text
        self.coloroff = coloroff
        self.coloron = coloron
        self.colorclicked = colorclicked
    
    def place(self, window, hiire_x, hiire_y, isclicked, bx, by, size = 50, tekst = "0", coloroff = "0", coloron = "0", colorclicked = "0"):
        if coloroff == "0":
            coloroff = self.coloroff
        if coloron == "0":
            coloron = self.coloron
        if colorclicked == "0":
            colorclicked = self.colorclicked
        if tekst == "0":
            tekst = self.text
        fontin = font.Font(None, size)
        text = fontin.render(tekst, 1, [0, 0, 0])
        width = text.get_width()
        height = text.get_height()
        if hiire_x > bx and hiire_x < bx + self.width and hiire_y > by and hiire_y < by + self.height:
            if not isclicked:
                text = fontin.render(tekst, 1, coloron)
                window.blit(self.on, [bx, by])
            else:
                text = fontin.render(tekst, 1, colorclicked)
                window.blit(self.clicked, [bx, by])
        else:
            text = fontin.render(tekst, 1, coloroff)
            window.blit(self.off, [bx, by])
        window.blit(text, [int(self.width/2)-int(width/2)+bx,int(self.height/2)-int(height/2)+by])
    
    def do(self, hiire_x, hiire_y, bx, by):
        if hiire_x > bx and hiire_x < bx + self.width and hiire_y > by and hiire_y < by + self.height:
            return True
        else:
            return False
        
class TextConButton:
    def __init__(self, off = "None", on = "None", clicked = "None", locked = "None", text = "Undefined", coloroff = [0,0,0], coloron = [0,0,150], colorclicked = [150,150,0], canclick = True):
        try:
            self.off = image.load(off)
            self.on = image.load(on)
            self.clicked = image.load(clicked)
            self.locked = image.load(locked)
        except:
            self.off = image.load("Pildid/Undefined.png")
            self.on = image.load("Pildid/Undefined.png")
            self.clicked = image.load("Pildid/Undefined.png")
            self.locked = image.load("Pildid/Undefined.png")
        self.height = self.off.get_height()
        self.width = self.off.get_width()
        self.text = text
        self.coloroff = coloroff
        self.coloron = coloron
        self.colorclicked = colorclicked
        self.beclicked = False
        self.canclick = canclick
    def place(self, window, hiire_x, hiire_y, bx, by, size = 50, coloroff = 0, coloron = 0, colorclicked = 0):
        if coloroff == 0:
            coloroff = self.coloroff
        if coloron == 0:
            coloron = self.coloron
        if colorclicked == 0:
            colorclicked = self.colorclicked
        fontin = font.Font(None, size)
        text = fontin.render(self.text, 1, [0, 0, 0])
        width = text.get_width()
        height = text.get_height()
        if hiire_x > bx and hiire_x < bx + self.width and hiire_y > by and hiire_y < by + self.height:
            if not self.beclicked:
                    text = fontin.render(self.text, 1, coloron)
                    window.blit(self.on, [bx, by])
            else:
                text = fontin.render(self.text, 1, colorclicked)
                window.blit(self.clicked, [bx, by])
        else:
            text = fontin.render(self.text, 1, coloroff)
            window.blit(self.off, [bx, by])
        window.blit(text, [int(self.width/2)-int(width/2)+bx,int(self.height/2)-int(height/2)+by])
    
    def do(self, hiire_x, hiire_y, bx, by):
        if hiire_x > bx and hiire_x < bx + self.width and hiire_y > by and hiire_y < by + self.height:
            return True
        else:
            return False
    
    def lock(self):
        if self.canclick:
            self.canclick = False
        
    def unlock(self):
        if not self.canclick:
            self.canclick = True
            
class TextChoButton:
    def __init__(self, off = "None", on = "None", clicked = "None", locked = "None", text = "Undefined", coloroff = [0,0,0], coloron = [0,0,150], colorclicked = [150,150,0], ischosen = False):
        try:
            self.off = image.load(off)
            self.on = image.load(on)
            self.clicked = image.load(clicked)
            self.locked = image.load(locked)
        except:
            self.off = image.load("Pildid/Undefined.png")
            self.on = image.load("Pildid/Undefined.png")
            self.clicked = image.load("Pildid/Undefined.png")
            self.locked = image.load("Pildid/Undefined.png")
        self.height = self.off.get_height()
        self.width = self.off.get_width()
        self.text = text
        self.coloroff = coloroff
        self.coloron = coloron
        self.colorclicked = colorclicked
        self.beclicked = False
        self.ischosen = ischosen
    def place(self, window, hiire_x, hiire_y, bx, by, size = 50, coloroff = 0, coloron = 0, colorclicked = 0):
        if coloroff == 0:
            coloroff = self.coloroff
        if coloron == 0:
            coloron = self.coloron
        if colorclicked == 0:
            colorclicked = self.colorclicked
        fontin = font.Font(None, size)
        text = fontin.render(self.text, 1, [0, 0, 0])
        width = text.get_width()
        height = text.get_height()
        if not self.beclicked:
            if hiire_x > bx and hiire_x < bx + self.width and hiire_y > by and hiire_y < by + self.height:
                text = fontin.render(self.text, 1, coloron)
                window.blit(self.on, [bx, by])
            else:
                text = fontin.render(self.text, 1, coloroff)
                window.blit(self.off, [bx, by])
        else:
            text = fontin.render(self.text, 1, colorclicked)
            window.blit(self.clicked, [bx, by])
        window.blit(text, [int(self.width/2)-int(width/2)+bx,int(self.height/2)-int(height/2)+by])
        
    def click(self, window, hiire_x, hiire_y, bx, by):
        if hiire_x > bx and hiire_x < bx + self.width and hiire_y > by and hiire_y < by + self.height:
            self.beclicked = True
            return self.beclicked
        else:
            self.beclicked = False
            return self.beclicked
    
    def do(self, hiire_x, hiire_y, bx, by):
        if hiire_x > bx and hiire_x < bx + self.width and hiire_y > by and hiire_y < by + self.height:
            return True
        else:
            return False
    
    def choose(self):
        if not self.ischosen:
            self.ischosen = True
        
    def unchoose(self):
        if self.ischosen:
            self.ischosen = False