#!/usr/bin/python

import sys, time
import cwiid, pygame

pygame.init()

FONDO = (0,0,0)
SIZE = 640,480   

class Observable(object):
    def __init__(self):
        self.observers = []
        
    def attach(self, ob):
        self.observers.append(ob)

    def notify(self, *args):
        for o in self.observers:
            o.update(*args)

        
class WiiMando(Observable):
    def __init__(self):
        Observable.__init__(self)
        raw_input("Press 1+2 and enter...")
        self.x = self.y = 0
        
        self.wm = cwiid.Wiimote()
        self.wm.mesg_callback = self.msg_cb
        self.wm.rpt_mode=cwiid.RPT_ACC
        self.wm.enable(cwiid.FLAG_MESG_IFC)
        self.attach(self)

    def update(self, x, y, z):
        self.x = x
        self.y = y

    def msg_cb(self, msgs):
        for t,args in [x for x in msgs if x[0] == cwiid.MESG_ACC]:
            self.notify(*args)


class Debug(object):
    def update(self, x, y, z):
        print "x:%s, y:%s, z:%s" % (x, y, z)


mote = WiiMando()
mote.attach(Debug())

screen = pygame.display.set_mode(SIZE)

while 1:
    time.sleep(0.05)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    screen.fill(FONDO)   
    pygame.draw.rect(screen, (255,0,0), (mote.x, mote.y, 50, 60), 2)
    pygame.display.flip()     
