from pico2d import *
import random

import game_world


class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1000), random.randint(0, 1000)

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def handle_collision(self, other, group):
        if group == 'boy:ball':
            game_world.remove_object(self)

    def get_bb(self):
        return self.x-10, self.y-10, self.x+10, self.y+10