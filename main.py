import pygame
from test import f
pygame.init()
pygame.mixer.pre_init()
pygame.mixer.init()

win = pygame.display.set_mode((800,500)) #dimensions of window
pygame.display.set_caption("Night Shift")
# pygame.mixer.pre_init(44100, 16, 2, 4096)
# pygame.mixer.music.("music.mp3") #need to add music
# sound = pygame.mixer.Sound("hit.wav")
hitSound = pygame.mixer.Sound('hit.wav')

f()
walkRight = [pygame.image.load('sprites/R1.png'), pygame.image.load('sprites/R2.png'), pygame.image.load('sprites/R3.png')]
walkLeft = [pygame.image.load('sprites/L1.png'), pygame.image.load('sprites/L2.png'), pygame.image.load('sprites/L3.png')]
idle = pygame.image.load('sprites/F1.png')

#start screen
s1 = pygame.image.load('s1.png')
s2 = pygame.image.load('s2.png')

scene1 = pygame.image.load('scene1.png')
scene2 = pygame.image.load('scene2.png')
scene3 = pygame.image.load('scene3.png')
scene4 = pygame.image.load('scene4.png')
scene5 = pygame.image.load('scene5.png')
scene6 = pygame.image.load('scene6.png')
title = pygame.image.load('title.jpeg')
endscene = pygame.image.load('endscene.png')

r1_bg1 = pygame.image.load('background/r1_bg1.jpeg')
r1_bg2 = pygame.image.load('background/r1_bg2.jpeg')

r2_bg = pygame.image.load('background/r2_bg.png')
r3_bg = pygame.image.load('background/r3_bg.png')
r4_bg = pygame.image.load('background/r4_bg.png')

final1 = pygame.image.load('background/final1.png')
final2 = pygame.image.load('background/final2.png')

win1 = pygame.image.load('background/win1.jpeg')
win2 = pygame.image.load('background/win2.jpeg')

r2_text = pygame.image.load('text/r2_text.png')
r3_text = pygame.image.load('text/r3_text.png')
r4_text = pygame.image.load('text/r4_text.png')

marina = pygame.image.load('marina.png')
dead = pygame.image.load('dead.png')
r5_text = pygame.image.load('marina-3.png')
success = pygame.image.load('win.png')
night_shift = pygame.image.load('nightshift.png')
hello = pygame.image.load('hello.png')

# end = pygame.image.load('endscreen.png')
font = pygame.font.SysFont("comicsansms", 18)

clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = 350
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.attack = False


    def draw(self, win):
        if self.attack:
            if pointer > self.x:
                win.blit(walkRight[2], (reese.x, reese.y))
            else:
                win.blit(walkLeft[2], (reese.x, reese.y))
        else:
            if self.walkCount + 1 > 2:
                self.walkCount = 0

            if not(self.standing):
                if self.left:
                    win.blit(walkLeft[self.walkCount], (self.x,self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(walkRight[self.walkCount], (self.x,self.y))
                    self.walkCount +=1
            else:
                # if self.right:
                #     win.blit(walkRight[0], (self.x, self.y))
                # else:
                #     win.blit(walkLeft[0], (self.x, self.y))
                win.blit(idle, (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)


class enemy(object):
    walkRight = [pygame.image.load('enemy/R1.png'), pygame.image.load('enemy/R2.png')]
    walkLeft = [pygame.image.load('enemy/L1.png'), pygame.image.load('enemy/L2.png')]
    gotHit = pygame.image.load('enemy/F2.png')
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = 350
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True
        self.attacked = False


    def draw(self,win):


        if self.visible:
            self.move()
            if self.attacked:
                win.blit(self.gotHit, (self.x, self.y))
            else:
                if self.walkCount + 1 > 2:
                    self.walkCount = 0

                if self.vel > 0:
                    win.blit(self.walkRight[self.walkCount], (self.x, self.y))
                    self.walkCount += 1
                else:
                    win.blit(self.walkLeft[self.walkCount], (self.x, self.y))
                    self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)

        else:
            win.blit(dead, (self.x, self.y))
#pygame.draw.rect(win, (255,0,0), self.hitbox,2)


    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        # pygame.mixer.Channel(0).play(pygame.mixer.Sound('sound\gun_fire.wav'), maxtime=600)

        hitSound.play()
        # pygame.mixer.Channel(1).play(pygame.mixer.Sound("hit.wav")) #need to add music

        print('kachOW! You just HIT annie')
        if self.health > 0:
            self.health -= 0.5
        else:
            self.visible = False

screen = 0
startLoop = 0
standStill = [0, 0, 0, 0, 0, 0]
screen1loop = 0
can_pass = False
def redrawGameWindow(screen):
    global screen1loop
    global standStill
    global pointer
    global startLoop
    print(screen)

    if screen == 0:
        win.blit(title,(0,0))

    # if screen == 0: ### START SCREEN ####
    #     global startLoop
    #     win.blit(s1,(0,0))
    #
    #     if startLoop <= 10:
    #         win.blit(s2, (0,0))
    #     startLoop = (startLoop + 1) % 20
        pygame.display.update()

        return

    if screen == 1:
        bg = r1_bg1
        if screen1loop <= 10:
            bg = r1_bg2
        win.blit(bg, (0,0))
        screen1loop = (screen1loop + 1) % 20
        if reese.x >= 99 and standStill[screen] < 50:
            standStill[screen] += 1
            reese.x = 99
            dialogue(bg, scene1)

        pygame.display.update()

    if screen == 2:
        if keys[pygame.K_SPACE]:
            reese.attack = True
            if reese.x + 30 > annie1.hitbox[0] and reese.x - 30 < annie1.hitbox[0] + annie1.hitbox[2]:
                annie1.attacked = True
                annie1.hit()
            else:
                annie1.attacked = False
        else:
            reese.attack = False
            annie1.attacked = False

        win.blit(r2_bg, (0,0))
        if not annie1.visible:
            win.blit(r2_text, (0,0))
            can_pass = True
        if standStill[screen] < 60:
            reese.x = 6
            dialogue(r2_bg, scene2)
            standStill[screen] += 1
            can_pass = False

        if standStill[screen] > 59 and standStill[screen] < 120:
            reese.x = 6
            standStill[screen] += 1

            dialogue(hello, scene3)
        annie1.draw(win)
        if not annie1.visible and standStill[screen] > 99 and standStill[screen] < 140:
            dialogue(r2_bg, scene4)
            standStill[screen] += 1


    if screen == 3:
        pointer = annie2.x
        win.blit(r3_bg, (0,0))

        if keys[pygame.K_SPACE]:
            reese.attack = True
            if reese.x + 30 > annie2.hitbox[0] and reese.x - 30 < annie2.hitbox[0] + annie2.hitbox[2]:
                annie2.attacked = True
                annie2.hit()
            else:
                annie2.attacked = False
        else:
            reese.attack = False
            annie2.attacked = False
        win.blit(r3_bg, (0,0))
        if not annie2.visible:
            win.blit(r3_text, (0,0))
            can_pass = True
        if standStill[screen] < 60:
            can_pass = False
            reese.x = 6
            dialogue(r3_bg, scene5)
            standStill[screen] += 1

        annie2.draw(win)
        if not annie2.visible and standStill[screen] > 99 and standStill[screen] < 140:
            dialogue(r3_bg, scene5)



    if screen == 4:

        if abs(reese.x - annie4.x) < abs(reese.x - annie3.x) or not annie3.visible:
            pointer = annie4.x
        elif abs(reese.x - annie4.x) > abs(reese.x - annie3.x):
            pointer = annie3.x
        win.blit(r4_bg, (0,0))
        if keys[pygame.K_SPACE]:
            reese.attack = True
            if reese.x + 30 > annie3.hitbox[0] and reese.x - 30 < annie3.hitbox[0] + annie3.hitbox[2]:
                annie3.attacked = True
                annie3.hit()
            else:
                annie3.attacked = False
            if reese.x + 30 > annie4.hitbox[0] and reese.x - 30 < annie4.hitbox[0] + annie4.hitbox[2]:
                annie4.attacked = True
                annie4.hit()
            else:
                annie4.attacked = False
        else:
            reese.attack = False
            annie3.attacked = False
            annie4.attacked = False
        win.blit(r4_bg, (0,0))

        if standStill[screen] < 60:
            reese.x = 6
            dialogue(r4_bg, scene6)
            can_pass = False
            standStill[screen] += 1
        annie3.draw(win)
        annie4.draw(win)

        if not annie3.visible and not annie4.visible and standStill[screen] > 99 and standStill[screen] < 140:
            dialogue(r4_bg, scene4)
        if not annie3.visible and not annie4.visible:
            win.blit(r4_text, (-60,20))
            can_pass = True

        screen1loop = 0

    if screen == 5:
        bg = final1
        if screen1loop <= 10:
            bg = final2
        screen1loop = (screen1loop + 1) % 20
        win.blit(bg, (0,0))
        win.blit(marina,(600,350))
        win.blit(r5_text, (0,0))
        if reese.x >= 99 and standStill[screen] < 50:
            standStill[screen] += 1
            reese.x = 99
            win.blit(success, (reese.x + 20, reese.y - 70))
            reese.draw(win)
            pygame.display.update()
        if (reese.x >= 200) and (standStill[screen] < 250):
            standStill[screen] += 1
            reese.x = 200
            win.blit(night_shift, (reese.x + 20, reese.y - 70))
            reese.draw(win)
            pygame.display.update()
        if reese.x >= 400 and standStill[screen] < 300 and standStill[screen]> 249:
            standStill[screen] += 1
            reese.x = 400
            win.blit(endscene, (30, 30))
            reese.draw(win)
            pygame.display.update()
        if standStill[screen] > 299:
            bg = win1
            if screen1loop <= 10:
                bg = win2
            screen1loop = (screen1loop + 1) % 20
            win.blit(bg, (0,0))
    reese.draw(win)
    pygame.display.update()


def dialogue(background, text):
    win.blit(background, (0,0))
    win.blit(text, (reese.x + 20, reese.y - 100))
    reese.draw(win)
    pygame.display.update()

reese = player(20, 400,190, 190)
annie1 = enemy(200, 385, 64, 64, 450)
annie2 = enemy(200, 385, 64, 64, 450)
annie3 = enemy(300, 385, 64, 64, 450)
annie4 = enemy(200, 385, 64, 64, 450)

pointer = annie1.x

start = False

while True:
    print(can_pass)
    print(annie1.visible)
    pointer = annie1.x

    clock.tick(20) #Frames per second
    keys = pygame.key.get_pressed()

    if screen == -1:
        if any(keys):
            screen = 0
    #### START  SCREEN ####
    if screen == 0:
        if any(keys):
            screen = 1

    #### QUIT GAME ####
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()

    #### MOVE CHARACTER ###

    if keys[pygame.K_LEFT] and reese.x > 0:
        reese.x -= reese.vel
        reese.left = True
        reese.right = False
        reese.standing = False
    elif keys[pygame.K_RIGHT] and reese.x < 800:
        reese.x += reese.vel
        reese.right = True
        reese.left = False
        reese.standing = False
    else:
        reese.standing = True
        reese.walkCount = 0

        if reese.x > 230 and reese.x < 440 and keys[pygame.K_UP] and screen == 1:
            reese.x = 1
            screen += 1

    if reese.x >= 800 and screen < 5 and screen > 1 and (not annie1.visible or not annie2.visible or not (annie3.visible or annie4.visible)):
        reese.x = 1
        screen += 1
    if reese.x <= 0 and screen > 1:
        if screen == 2:
            reese.x = 359
        else:
            reese.x = 799
        screen -= 1

    #### REDRAW GAME WINDOW ####
    redrawGameWindow(screen)


pygame.quit()
