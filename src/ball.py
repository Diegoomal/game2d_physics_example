import pymunk

from object2d import Object2D


class Ball(Object2D):

    def __init__(self) -> None:
        pass

    def create(self, space, radius, mass, pos):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Circle(body, radius)
        shape.mass = mass
        shape.elastiicity = 0.9
        shape.friction = 0.4
        shape.color = (255, 0, 0, 100)
        space.add(body, shape)
        return shape