import pygame, sys, math
from pygame.locals import *


clock = pygame.time.Clock()
WIDTH=800
HEIGHT=600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

class Ball :
    def __init__(self,x,y,r,c,speed=5) :
        self.x = x
        self.y = y
        self.speed = speed
        self.dx = self.speed
        self.dy = self.speed
        self.r = r
        self.col = c    

    def update(self) :
        pass 
        

    def set_d(self,dx,dy) :
        self.dx=dx
        self.dy=dy

    def hit(self,other) : 
        dx = self.x-other.x
        dy = self.y-other.y
        return math.sqrt((dx*dx)+(dy*dy)) < (self.r + other.r) 
        
    def draw(self) :
        pygame.draw.circle(screen, [100,100,255], [self.x,self.y], int(self.r+1))
        pygame.draw.circle(screen, self.col, [self.x,self.y], int(self.r))
        pygame.draw.circle(screen, [255,255,255], [self.x,self.y], 3)


class Player(Ball) :

    def update(self) :
        if self.x > WIDTH-5 : self.dx = -self.speed
        if self.x < 5 : self.dx = self.speed
        if self.y > HEIGHT-5 : self.dy = -self.speed
        if self.y < 5 : self.dy = self.speed
        self.x = self.x + self.dx
        self.y = self.y + self.dy   
        self.r = self.r + 0.001
        
class Obs(Ball) :
    def update(self) :
        self.x = self.x + self.dx
        self.y = self.y + self.dy   
        if self.x > WIDTH :
            self.x = 0
        if self.y > HEIGHT :
            self.y = 0

class PyManMain:
    
    def __init__(self):
        pygame.init()
        self.player = Player(100,100,10,[255,255,0],7)
        self.player.set_d(self.player.speed,0)
        
        self.obs = []

        self.difficulty = 40
        self.ticker = 0
        self.no_obs = 0
        self.score = 0 
        self.font = pygame.font.SysFont(None, 50)
        self.name = sys.argv[1]
        

    def MainLoop(self):
        while 1:        
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.set_d(-self.player.speed,0)
                    if event.key == pygame.K_RIGHT:
                        self.player.set_d(self.player.speed,0)
                    if event.key == pygame.K_UP:
                        self.player.set_d(0,-self.player.speed)
                    if event.key == pygame.K_DOWN:
                        self.player.set_d(0,self.player.speed)
                    #if event.key == pygame.K_SPACE:
                    #    
                    
            clock.tick(20)
            self.score = self.score + self.no_obs
            
            self.ticker = self.ticker + 1
            if (self.ticker % self.difficulty == 0) :
                self.obs.append(Obs(self.player.x,self.player.y+int(self.player.r*3),10,[200,50,100]))
                self.no_obs = self.no_obs + 1

            self.player .update()
            for o in self.obs :
                o.update()
                if self.player.hit(o) :
                    print "BANG!!!! %s" % self.score                    
                    sys.exit()
            

    
            screen.fill([0,0,0])
            self.player.draw()
            [o.draw() for o in self.obs]

            label = self.font.render("%s :: %s" % (self.name,self.score), 1, [255,255,255])
            screen.blit(label, (30, 59))
                
            pygame.display.flip()
                     
                
if __name__ == "__main__":
    MainWindow = PyManMain()
    MainWindow.MainLoop()
