import pymunk

from object2d import Object2D


class Boundaries(Object2D):

    def __init__(self) -> None:
        pass

    def create(self, space, width, height):

        rects = [
            [(width/2, height-10), (width, 20)],
            [(width/2, 10), (width, 20)],
            [(10, height/2), (20, height)],
            [(width - 10, height/2), (20, height)],
        ]

        for pos, size in rects:
            body = pymunk.Body(body_type=pymunk.Body.STATIC)
            body.position = pos
            shape = pymunk.Poly.create_box(body, size)
            shape.elastiicity = 0.4
            shape.friction = 0.5
            space.add(body, shape)