from PIL import Image
import numpy as np


class Sphere:
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius


class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def interacts_with_sphere(self, s):
        a = np.dot(self.direction, self.direction)
        b = 2 * np.dot(self.direction, self.origin - s.centre)
        c = np.dot(self.origin - s.centre, self.origin - s.centre) - s.radius ** 2

        discr = b ** 2 - (4 * a * c)

        return discr >= 0


img = Image.new('RGB', [500, 500], 255)
data = img.load()

sphere = Sphere([0, 20, 100], 60)

total = []
for x in range(-250, 249):
    row = []
    for y in range(-250, 249):
        ray = Ray(np.array([0, 0, 0]), np.array([x, y, 50]))
        if ray.interacts_with_sphere(sphere):
            row.append((
                255, 0, 0
            ))
        else:
            row.append((
                255, 255, 255
            ))
    total.append(row)

for x in range(0, len(total)):
    for y in range(0, len(total[x])):
        value = total[x][y]
        data[x, y] = value

img.save('image.png')
