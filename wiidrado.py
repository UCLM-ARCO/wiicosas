import cwiid
import pygame,sys

global x,y

def cb(*args):
    coor=args[0][0][1]
    globals()["x"]=coor[0]
    globals()["y"]=coor[1]

print "Press 1+2 and enter..."
raw_input()
wm = cwiid.Wiimote()
wm.mesg_callback=cb
wm.rpt_mode=cwiid.RPT_ACC
wm.enable(cwiid.FLAG_MESG_IFC)

pygame.init()

color_fondo = 0, 0, 0
size = ancho,alto=320,240
screen = pygame.display.set_mode(size)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    screen.fill(color_fondo)
    pygame.draw.rect(screen, (255,0,0), (x,y+30,50,60), 2)
    
    pygame.display.flip()
     
