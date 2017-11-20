import pygame
from pygame import display, draw, time, event
from random import randint

HEIGHT = 600
WIDTH = 800
MAX_RADIUS = 50


def random_circle():
    a = randint(1 + MAX_RADIUS, WIDTH - MAX_RADIUS)
    b = randint(1 + MAX_RADIUS, HEIGHT - MAX_RADIUS)
    return a, b, 1, [randint(0, 255), randint(0, 255), randint(0, 255)]


clock = time.Clock()

screen = display.set_mode([WIDTH, HEIGHT])
screen.fill([0, 0, 0])

radius = 10
circles = []

while event.poll().type != pygame.KEYDOWN:
    screen.fill([0, 0, 0])
    if radius <= MAX_RADIUS:
        radius = radius + 1
    circles.append(random_circle())

    for i, circle in enumerate(circles):
        x, y, r, color = circle
        circles[i] = (x, y, r + 1, color)

    circles = [x for x in circles if x[2] <= MAX_RADIUS]

    for x, y, r, c in circles:
        draw.circle(screen, c, (x, y), r, 1)

    display.flip()
    clock.tick(60)
