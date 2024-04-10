from .graph import graph
import cv2

class Plotter:
    def __init__(points):
        self.points = points

    def scale(self, ratio):
        scale_matrix = np.identity(4)
        scale_matrix[:3] *= ratio
        for point in self.points:
            point.coordinate = np.matmul(scale_matrix,point.coordinate)

    def rotate(self, ratio):
        Rx = np.array([[1, 0, 0, 0],
                       [0, cos(x_axis_rotation), -sin(x_axis_rotation), 0],
                       [0, sin(x_axis_rotation), cos(x_axis_rotation), 0],
                       [0, 0, 0, 1]])
        Ry = np.array([[cos(y_axis_rotation), 0, sin(y_axis_rotation), 0],
                       [0, 1, 0, 0],
                       [-sin(y_axis_rotation), 0, cos(y_axis_rotation), 0],
                       [0, 0, 0, 1]])
        rotate_matrix = np.matmul(Ry, Rx))
        for point in self.points:
            point.coordinate = np.matmul(rotate_matrix,point.coordinate)

    def get_range(self):
        x_min = x_max = self.points[0].coordinate[0]
        y_min = y_max = self..points[0].coordinate[1]
        for point in self.points:
            if(point.coordinate[0] > x_max):
                x_max = point.coordinate[0]
            if(point.coordinate[0] < x_min):
                x_min = point.coordinate[0]
            if(point.coordinate[1] > y_max):
                y_max = point.coordinate[1]
            if(point.coordinate[1] < y_min):
                y_min = point.coordinate[1]

        return floor(x_min), ceil(x_max), floor(y_min), ceil(y_max)

    def plot(self):
        x_min, y_min, x_max, y_max = self.get_range()
        image = np.full((y_max-y_min, x_min-x_max ,3), 255, dtype='uint8')
        for p1, p2 in zip(self.points, self.points[1:]):
            p1_cv2 = np.array(p1.coordinate[:2], dtype="uint32")
            p2_cv2 = np.array(p2.coordinate[:2], dtype="uint32")
            image = cv2.line(digital_image, p1_cv2, p2_cv2, (0,0,0), 1)

        return image
