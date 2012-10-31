import pyglet
from random import randint

class BackGround(pyglet.sprite.Sprite):
    def __init__(self):
        image = pyglet.resource.image('images/back.png')
        super(BackGround, self).__init__(image)
    def update(self, height):
        self.y -= 2
        if self.y + self.height < 0:
            self.y = height

class EnemyExplosion(pyglet.sprite.Sprite):
    def __init__(self):
        image = pyglet.resource.image('images/Enemy/1.png')
        self.frame = 1
        super(EnemyExplosion, self).__init__(image)
    def update(self):
        self.frame += 1
	try:
            self.image = pyglet.resource.image('images/Enemy/' + str(self.frame) + '.png')
        except pyglet.resource.ResourceNotFoundException:
            return 1
        return 0
class EndExplosion(pyglet.sprite.Sprite):
    def __init__(self):
        image = pyglet.resource.image('images/Plane/1.png')
        self.frame = 0
        super(EndExplosion, self).__init__(image)
    def update(self, a = 1):
        self.frame += 1
        try:
            self.image = pyglet.resource.image('images/Plane/' + str(self.frame) + '.png')
        except pyglet.resource.ResourceNotFoundException:
            pass
        return 0
class Island(pyglet.sprite.Sprite):
    def __init__(self):
        filename = "images/island" + str(randint(1,3)) + ".png"
        image = pyglet.resource.image(filename)
        image.anchor_x, image.anchor_y = image.width, image.height
        super(Island, self).__init__(image)
    def update(self):
        self.y -= 2
        if self.y < 0 - self.height:
            return 1
        return 0
