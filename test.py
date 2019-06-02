import pygame
pygame.init()

win = pygame.display.set_mode((800,500)) #dimensions of window
# music = pygame.mixer.music.load("nothing") #need to add music
pygame.display.set_caption("janitor")
# pygame.mixer.music.play(-1)

walkRight = [pygame.image.load('sprites/R1.png'), pygame.image.load('sprites/R2.png'), pygame.image.load('sprites/R3.png')]
walkLeft = [pygame.image.load('sprites/L1.png'), pygame.image.load('sprites/L2.png'), pygame.image.load('sprites/L3.png')]
idle = pygame.image.load('sprites/F1.png')

#start screen
s1 = pygame.image.load('s1.png')
s2 = pygame.image.load('s2.png')

scene1 = pygame.image.load('scene1.png')
scene2 = pygame.image.load('scene2.png')
scene3 = pygame.image.load('scene3.png')


r1_bg = pygame.image.load('background/r1_bg.png')
r2_bg = pygame.image.load('background/r2_bg.png')
r3_bg = pygame.image.load('background/r3_bg.png')
r4_bg = pygame.image.load('background/r4_bg.png')


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


    def draw(self, win):
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


    def draw(self,win):

        self.move()
        if self.visible:
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
        print('kachOW! You just HIT annie')
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False


screen = 0
startLoop = 0
standStill = [0, 0, 0, 0, 0, 0]
def redrawGameWindow(screen):
    global standStill
    print(reese.x)
    if screen == 0: ### START SCREEN ####
        global startLoop
        win.blit(s1,(0,0))

        if startLoop <= 10:
            win.blit(s2, (0,0))
        startLoop = (startLoop + 1) % 20
        pygame.display.update()

        return

    if screen == 1:
        win.blit(r1_bg, (0,0))
        if reese.x >= 99 and standStill[screen] < 50:
            standStill[screen] += 1
            reese.x = 99
            dialogue(r1_bg, scene1)

    if screen == 2:
        win.blit(r2_bg, (0,0))
        if keys[pygame.K_SPACE]:
            if annie.x > reese.x:
                win.blit(walkRight[2], (reese.x, reese.y))
                print("reese on left")
            else:
                win.blit(walkLeft[2], (reese.x, reese.y))
                print("reese on right")


            if reese.x + 30 > annie.hitbox[0] and reese.x - 30 < annie.hitbox[0] + annie.hitbox[2]:

                win.blit(enemy.gotHit, (annie.x, annie.y))
                annie.hit()
            else:
                annie.draw(win)

        annie.draw(win)

    if screen == 3:
        win.blit(r3_bg, (0,0))
    if screen == 4:
        win.blit(r4_bg, (0,0))

    reese.draw(win)
    pygame.display.update()

def dialogue(background, text):
    win.blit(background, (0,0))
    win.blit(text, (reese.x + 20, reese.y - 55))
    reese.draw(win)
    pygame.display.update()

reese = player(20, 400,190, 190)
annie = enemy(100, 385, 64, 64, 450)

def attack(background):
    win.blit(background, (0,0))
    #### ATTACK SCENE ####
    if annie.x > reese.x:
        win.blit(walkRight[2], (reese.x, reese.y))
    else:
        win.blit(walkLeft[2], (reese.x, reese.y))

    if reese.x + 30 > annie.hitbox[0] and reese.x - 30 < annie.hitbox[0] + annie.hitbox[2]:
        win.blit(enemy.gotHit, (annie.x, annie.y))
        annie.hit()
    else:
        annie.draw(background)


while True:
    clock.tick(20) #Frames per second
    keys = pygame.key.get_pressed()
    screen = 2

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

        if reese.x > 230 and reese.x < 440 and keys[pygame.K_UP]:
            reese.x = 1
            screen += 1


    #### REDRAW GAME WINDOW ####
    redrawGameWindow(screen)

pygame.quit()
