import math, random

DEFAULT_SIZE, DEFAULT_BORDER_SHRINK_FACTOR = 1000, 10
DEFAULT_WIDTH, DEFAULT_HEIGHT = DEFAULT_SIZE, DEFAULT_SIZE

class Shape:
    def __init__(self, number_of_sides, width, height, border_shrink_factor, rotation):
        self.number_of_sides = number_of_sides
        self.width, self.height = width, height
        self.distance_from_border = max(width / border_shrink_factor, height / border_shrink_factor)
        self.center = [width / 2, height / 2]
        self.radius = min(self.center[0] - self.distance_from_border, self.center[1] - self.distance_from_border)
        self.corners = [[self.center[0] + self.radius * math.cos(self.rotationInRadians(rotation) + (angle_step * 2 * math.pi / number_of_sides)), self.center[1] + self.radius * math.sin(self.rotationInRadians(rotation) + (angle_step * 2 * math.pi / number_of_sides))] for angle_step in range(number_of_sides)]

    def drawOutline(self, canvas):
        for i in range(len(self.corners)):
            canvas.create_line(self.corners[i][0], self.corners[i][1], self.corners[(i + 1) % len(self.corners)][0], self.corners[(i + 1) % len(self.corners)][1])

    def getStartingPoint(self):
        return [random.random() * self.width, random.random() * self.height]

    def drawFractal(self, canvas, number_of_iterations, weight_of_corners, weight_of_point):
        self.drawOutline(canvas)

        point = self.getStartingPoint()

        for _ in range(number_of_iterations):
            canvas.create_oval(point[0] - 1, point[1] - 1, point[0] + 1, point[1] + 1, fill='red', outline='blue')
            next_corner = random.randint(0, len(self.corners) - 1)
            point = [(self.corners[next_corner][0] * weight_of_corners + point[0] * weight_of_point) / (weight_of_corners + weight_of_point), (self.corners[next_corner][1] * weight_of_corners + point[1] * weight_of_point) / (weight_of_corners + weight_of_point)]
    
    def rotationInRadians(self, degrees):
        return 2 * math.pi * degrees / 360