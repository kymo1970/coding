import pygame

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
            
        self.rect = (self.x, self.y, self.width, self.height)    


def redrawWindow(mw, player):
    
    mw.fill("#ffffff")
    player.draw(mw)
    pygame.display.update()
    
    
def main():
    run = True
    player = Player(50, 50, 100, 100, "#ff0000")
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()    
                

        player.move()       
        redrawWindow(mw, player)
        
        
main()        