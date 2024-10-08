from pico2d import *
import random

class Ball:
    def __init__(self, image, x, y, fall_speed):
        self.image = load_image(image)
        self.x = x
        self.y = y
        self.fall_speed = fall_speed
        self.ground_level = 0 if '21x21' in image else 0

    def update(self):
        if self.y > self.ground_level:
            self.y -= self.fall_speed
            if self.y < self.ground_level:
                self.y = self.ground_level

    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

balls = []
for i in range(20):
    x = random.randint(0, 800)
    y = 599
    fall_speed = random.uniform(2, 10)
    if random.randint(0, 1) == 0:
        balls.append(Ball('ball21x21.png', x, y, fall_speed))
    else:
        balls.append(Ball('ball41x41.png', x, y, fall_speed))

running = True

while running:
    handle_events()

    for ball in balls:
        ball.update()

    clear_canvas()
    for ball in balls:
        ball.draw()
    update_canvas()

    delay(0.03)

close_canvas()