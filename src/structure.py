import pymunk

from object2d import Object2D


class Structure(Object2D):

    def __init__(self) -> None:
        pass

    def create(self, space, width, height):

        BROWN = (139, 69, 19, 100)
        
        rects = [
            [(600, height - 120), (40, 200), BROWN, 100],
            [(900, height - 120), (40, 200), BROWN, 100],
            [(750, height - 240), (340, 40), BROWN, 150],
        ]
        
        for pos, size, color, mass in rects:
            body = pymunk.Body()
            body.position = pos
            shape = pymunk.Poly.create_box(body, size, radius=2)
            shape.color = color
            shape.mass = mass
            shape.elasticity = 0.4
            shape.friction = 0.4
            space.add(body, shape)