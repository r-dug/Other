# required import libs-
import pygame
# graphics and logic
from Network import Network
# network module we built
import pickle
# for saving information to disk


pygame.font.init()

# creates the window in pygame graphics
width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Greenbox")

class Button:
    def __init__(self, text, x, y, color):
        self.text = textwrapself.x = # XXX: self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, window):
        pygame.draw.rect(win, self.color, (self.x, self.y, welf.width, self.height))
        fort = pygame.font.SysFont('comicsans', 40)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))
    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 1

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x,self.y,self.width,self.height)



def redrawWindow(win, player, player2):
    win.fill((128,128,128))

    if not (game.connected()):
        font = pygame.font.SysFont('comicsans', 80)
        text = font.render('Waiting for Player...', 1, (255,0,0), True)
        win.blit(text, (width/2-text.get_width()/2, height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont('comicsans', 60)
        text = font.render('Your move', 1, (0,255,0))
        win.blit(text, (80,200))

        text = font.render('Opponents', 1, (0,255,0))
        win.blit(text, (380, 200))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        if game.bothWent():
            text1 = font.render(move1, 1, (0,0,0))
            text2 = font.render(move2, 1, (0,0,0))
        else:
            if game.p1Went and p = 0:
                text1 = font.render(move1, 1, (0,0,0))
            elif game.p1went:
                text1 = font.render('Locked in', 1, (0,0,0))
            else:
                text1 = font.render('Waiting...', 1, (0,0,0))

            if game.p2Went and p=1:
                text2 = font.render(move2, 1, (0,0,0))
            elif game.p1went:
                text2 = font.render('Locked in', 1, (0,0,0))
            else:
                text2 = font.render('Waiting...', 1, (0,0,0))
        if p=1:
            win.blit(text2, (100,350))
            win.blit(text1, (400, 350))
        else:
            win.blit(text1, (100,350))
            win.blit(text2, (400, 350))

        for btn in btns:
            btn.draw(win)

    pygame.display.update()

btns = [Button("Rock", 50, 500, (0,0,0)), Button("Scissors", 250, 500, (255,0,0)), Button("Paper", 450, 500, (0,255,0))]

def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getPos())
    print(f'You are player{player}')

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print('Could not run game')
            break

        if game.bothWent():
            redrawWindow(win, game, player)
            pygame.time.delay(500)
            try:
                game = n.send('reset')
            except:
                run = False
                print('Could not run game')
                break


        p2Pos = n.send(make_pos((p.x, p.y)))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p1.move()
        redrawWindow(win, p1)

main()
