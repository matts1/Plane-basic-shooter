import pyglet
from pyglet.window import key
from functions import rotate_movement, in_bounds

class PlaneSprite(pyglet.sprite.Sprite):
    def __init__(self):
        image = pyglet.resource.image('images/plane.png')
        image.anchor_x = image.width / 2
        image.anchor_y = image.height / 2
        super(PlaneSprite, self).__init__(image)

    def update(self, keys):
        for val, [x, y] in {"LEFT": [-4, 0], "RIGHT": [4, 0], "UP": [0, 2], "DOWN": [0, -2]}.items():
            if eval("keys[key." + val + "]"):
                self.x += x
                self.y += y
