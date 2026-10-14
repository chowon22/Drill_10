from turtle import speed

from pico2d import *
import random
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image("grass.png")
    def draw(self):
        self.image.draw(400, 30)
    def update(self):
        pass

class Boy:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 90
        self.image = load_image('run_animation.png')
        self.frame = 0
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Zombie:
    def __init__(self):
        self.x = 100
        self.y = 170
        self.image = load_image('zombie_run_animation.png')
        self.frame = 0
    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5
    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_height, 
                             self.x, self.y, frame_width // 2, frame_height // 2)

class Ballon:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 120
        self.speed = random.randint(5, 13)
        self.image = load_image('ball41x41.png')
    def update(self):
        if self.y >= 600 - 20.5:
            pass
        else:
            self.y += self.speed
    def draw(self):
        self.image.clip_draw(0, 0, 41, 41, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    running = True
    global world

    world = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for _ in range(11)]
    world += team

    zombie = Zombie()
    world.append(zombie)

    balloons = [Ballon() for _ in range(20)]
    world += balloons


def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
