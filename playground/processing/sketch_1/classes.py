class myCircle(object):
    def __init__(self, radius):
        self.radius = radius
    def display(self):
        ellipse(50, 50, self.radius, self.radius)
