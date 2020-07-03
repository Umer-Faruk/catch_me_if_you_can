import pygame
import random
import time
try:
    import pkg_resources.py2_warn
    
except ImportError:
    pass


pygame.init()
dis = pygame.display.set_mode((800,600))
pygame.display.set_caption("catch me if you can !")

clock = pygame.time.Clock()


font_style = pygame.font.SysFont("Arial",30)


def message(msg, color, w, h):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [w, h])


     


def collidercheck(r1,r2):
    if r1.colliderect(r2):
     #     print("collution")
         return True
     

def main():
     over = True
     score = 0
     mx=0
     my=0

     bx=0
     by = 0
     gravity = 4

     while over:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    over = False
          mx,my=pygame.mouse.get_pos()
          
          by += gravity

          boll = pygame.Rect(bx,by,20,20)
          pygame.draw.rect(dis,(255,0,0),boll)

          r = pygame.Rect(mx,500,60,20)
          pygame.draw.rect(dis,(255,255,255),r)

          ground = pygame.Rect(0,570,800,20)
          pygame.draw.rect(dis,(0,255,0),ground)

          if collidercheck(r,boll):
               bx = random.randrange(600)
               by = 0 
               if score%100 == 0:
                    gravity += 2
               print(gravity)
               score += 10

          if collidercheck(ground,boll):
               
               message("game Over",(255,255,255),300,250)
               
               by = 571
          if by > 571:
               message("game Over",(255,255,255),300,250)
               
          
          message('score:'+str(score),(255,255,255),0,0)
          # message(str(score),(255,255,255),0,0)
          pygame.display.update()
          dis.fill((0,0,0))
          clock.tick(30)

     pygame.quit()
     quit()

main()
