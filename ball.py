from pico2d import load_image

import game_world


class Ball:
    image = None

    def __init__(self, x, y, velocity, dir):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity, self.dir = x, y, velocity, dir

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity * self.dir

        if self.x < 50 or self.x > 800 - 50:
            game_world.remove_object(self)