from pygame import *
from random import randint

win_1 = 700
win_2 = 500

window = display.set_mode((win_1, win_2))
display.set_caption("аизлец")
background = transform.scale(image.load('galaxy.jpg'), (win_1, win_2))
clock = time.Clock()
FPS = 40
mixer.init()
mixer.music.load("space.mp3")

font.init()
font1 = font.Font(None,36)

class GameSprite(sprite.Sprite):
    def __init__(self , player_image , player_x, player_y , player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,70))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def rest(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 630:
            self.rect.x += self.speed
    def fire(self):
        pass

lost = 0

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 450:
            self.rect.x = randint(80, 620)
            self.rect.y = 0 
            lost = lost + 1

ufo_1 = Enemy('ufo.png', randint(80, 620),0,randint(1, 5)) 
ufo_2 = Enemy('ufo.png', randint(80, 620),0,randint(1, 5))
ufo_3 = Enemy('ufo.png', randint(80, 620),0,randint(1, 5))
ufo_4 = Enemy('ufo.png', randint(80, 620),0,randint(1, 5))
ufo_5 = Enemy('ufo.png', randint(80, 620),0,randint(1, 5))

monsters = sprite.Group()
monsters.add(ufo_1)
monsters.add(ufo_2)
monsters.add(ufo_3)
monsters.add(ufo_4)
monsters.add(ufo_5)

rocket = Player('rocket.png',300,420,4)
finish = False
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        
    text_lose = font1.render('пропущено: ' + str(lost),1,(255, 255, 255))

    window.blit(background, (0,0))
    window.blit(text_lose, (20,20))

    rocket.update()
    rocket.rest()
    monsters.update()
    monsters.draw(window)
    display.update()
    clock.tick(FPS)