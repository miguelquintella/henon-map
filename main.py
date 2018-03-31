import matplotlib.pyplot as plt

#the points are created with a class, the point class. The coordinates are changed with the formula of the henon map, and appended to a list of points. 

class point():
    def __init__(self, x, y, a = 1.4, b = 0.3):
        self.x = x
        self.y = y
    
    def location(self):
        return (self.x, self.y)

    #translocates the point to the next location

    def next_location(self):

        xn = self.x
        yn = self.y

        self.x = 1.0 - self.a * xn ** 2 + yn
        self.y = self.b * xn

        return (self.x, self.y)

def list_of_locations(x0, y0, count, plot = True):
    p = point(x0, y0, )
    locations = []
    for i in range(count):
        location = p.location()
        locations.append(location)
        p.next_location()

    if plot == True:
        plt.plot(*zip(*locations), 'bo', markersize=1)
        plt.show()
    return locations

#testing
if __name__ == '__main__':
    list_of_locations(1.0, 0.0 , 1000000)
