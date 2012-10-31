import pyglet
from pyglet.window import key
from random import randint
import math
from plane import PlaneSprite
from bullets import BulletSprite
from functions import in_bounds
from effects import BackGround, Island

class Window(pyglet.window.Window):
    def __init__(self):
        # Call the superclass's constructor.
        super(Window, self).__init__()
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        pyglet.clock.schedule_interval(self.update, 0.05)

        self.plane = PlaneSprite()
        self.plane.x = self.width / 2
        self.plane.y = self.height / 2
        self.bullets = []
        self.can_shoot = 1
        self.backs = []
        self.islands = []
        back = BackGround()
        for x in xrange(0, self.width, back.width):
            for y in xrange(0, self.height+ (2 * back.height), back.height):
                newback = BackGround()
                newback.x, newback.y = x, y
                self.backs.append(newback)
        
    def update(self, dt):
        if not randint(0, 99):
            island = Island()
            island.x = randint(0, self.width)
            island.y = self.height + 100
            self.islands.append(island)
        toremove = []
        for island in self.islands:
            if island.update():
                toremove.append(island)
        for island in toremove:
            self.islands.remove(island)
            
        self.plane.update(self.keys)
        for back in self.backs:
            back.update(self.height)
        
        if self.keys[key.SPACE]:
            if self.can_shoot >= 1:
                bullet = BulletSprite()
                bullet.x = self.plane.x
                bullet.y = self.plane.y
                self.bullets.append(bullet)
                self.can_shoot = 0
            else: self.can_shoot += 0.1

        toremove = []
        for bullet in self.bullets:
            bullet.update()
            if in_bounds(bullet.x, bullet.y, self.width, self.height, 32, 32) != [bullet.x, bullet.y]:
                if bullet not in toremove:
                    toremove.append(bullet)
        for item in toremove:
            self.bullets.remove(item)

    def on_draw(self):
        # Clear what was drawn last frame.
        self.clear()
        for back in self.backs:
            back.draw()
        for island in self.islands:
            island.draw()
        for bullet in self.bullets:
            bullet.draw()
        self.plane.draw()
        
win = Window()
pyglet.app.run()
