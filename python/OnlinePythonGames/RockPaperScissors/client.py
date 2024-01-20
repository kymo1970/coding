import pygame
from network import Network

WIDTH = 500
HEIGHT = 500
mw = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")
mw.fill("#ffffff")

clientNumber = 0


class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3
        
    def draw(self, mw):
        pygame.draw.rect(mw, self.color, self.rect)
            
            
    def move(self):
        key = pygame.key.get_pressed()
            
        if key[pygame.K_LEFT]:
            self.x -= self.vel
            
        if key[pygame.K_RIGHT]:
            self.x += self.vel
            
        if key[pygame.K_UP]:
            self.y -= self.vel
            
        if key[pygame.K_DOWN]:
            self.y += self.vel
            
        self.update()    
            
    def update(self):        
        self.rect = (self.x, self.y, self.width, self.height)    


def readPos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def makePos(tup):
    return str(tup[0]) + "," + str(tup[1])


def redrawWindow(mw, player, player2):    
    mw.fill("#ffffff")
    player.draw(mw)
    player2.draw(mw)
    pygame.display.update()
    
    
def main():
    run = True
    nw = Network()
    startPos = readPos(nw.getPos())
    player = Player(startPos[0], startPos[1], 100, 100, "#ff0000")
    player2 = Player(0, 0, 100, 100, "#00ff00")
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        player2Pos = readPos(nw.send(makePos(player.x, player.y)))
        player2.x = player2Pos[0]
        player2.y = player2Pos[1]
        player2.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()    
                

        player.move()       
        redrawWindow(mw, player, player2)

main()
