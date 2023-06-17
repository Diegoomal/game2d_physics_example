import math
import pygame
import pymunk
import pymunk.pygame_util

from util import Util
from ball import Ball
from boundaries import Boundaries
from structure import Structure

class Game:

    def __init__(self) -> None:
        pygame.init()
        self.WIDTH = 1000
        self.HEIGHT = 800
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.run_game = True
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.delta_time = 1 / self.fps
        self.space = pymunk.Space()
        self.space.gravity = (0, 981)
        self.draw_options = pymunk.pygame_util.DrawOptions(self.window)

    def draw(self, space, window, draw_options, line):
        window.fill("white")
        if line:
            pygame.draw.line(window, "black", line[0], line[1], 3)
        space.debug_draw(draw_options)
        pygame.display.update()

    def run(self):

        Boundaries().create(self.space, self.WIDTH, self.HEIGHT)
        Structure().create(self.space, self.WIDTH, self.HEIGHT)

        pressed_pos = None
        ball = None

        while self.run_game:

            line = None
            if ball and pressed_pos:
                line = [pressed_pos, pygame.mouse.get_pos()]

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.run_game = False
                    break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not ball:
                        pressed_pos = pygame.mouse.get_pos()
                        ball = Ball().create(self.space, 30, 10, pressed_pos)
                    elif pressed_pos:
                        ball.body.body_type = pymunk.Body.DYNAMIC
                        fx, fy = Util.calculate_forces(line)
                        ball.body.apply_impulse_at_local_point((fx, fy), (0, 0))
                        pressed_pos = None
                    else:
                        self.space.remove(ball, ball.body)
                        ball = None

            self.draw(self.space, self.window, self.draw_options, line)

            self.space.step(self.delta_time)
            self.clock.tick(self.fps)

        pygame.quit()