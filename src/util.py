import math

class Util:

    @staticmethod
    def calculate_distance(p1, p2):
        return math.sqrt((p2[1] - p1[1])**2 + (p2[0] - p1[0])**2)

    @staticmethod
    def calculate_angle(p1, p2):
        return math.atan2(p2[1] - p1[1], p2[0] - p1[0])
    
    @staticmethod
    def calculate_forces(line):
        angle = Util.calculate_angle(*line)
        force = Util.calculate_distance(*line) * 50
        fx = math.cos(angle) * force
        fy = math.sin(angle) * force
        return fx, fy
