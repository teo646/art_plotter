from math import sin, cos, pi
import numpy as np

def get_distance(p1, p2):
    return np.linalg.norm(p1.coordinate-p2.coordinate)

class Point:
    def __init__(x,y,z):
        self.coordinate = np.array([x,y,z,1])

#put x(t),y(t),z(t), and range of t as parameter
class Graph:
    def __init__(x_func=cos, y_fun=sin, z_func=(lambda t: 0), t_range=(0,2*pi)):
        self.x_func=x_func
        self.y_func=y_func
        self.z_func=z_func
        self.t_range=t_range

    def get_points(self):
        unit_line_length = 0.05
        current_t = t_range[0]
        points = []
        while(current_t < t_range[1]):
            current_point = Point(self.x_func(current_t), self.y_func(current_t),\
                    self.z_func(current_t))
            points.append(current_point)
            current_t += unit_line_length/get_distance(Point[0,0,0], current_point)
        
        return points


