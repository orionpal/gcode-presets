import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

class WoodSimulation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.wood = np.ones((height, width, 3)) * 165 / 255  # Initial color: brown
        self.fig, self.ax = plt.subplots()
        self.im = self.ax.imshow(self.wood)
        self.drill_x = 0
        self.drill_y = 0

    def animate_cut(self):
        anim = FuncAnimation(self.fig, self._update_cut, frames=self.width, interval=100, blit=True)
        plt.show()

    def _update_cut(self, frame):
        new_wood = np.copy(self.wood)
        for i in range(frame):
            x = i
            y = i
            alpha = min(1, (frame - i) / 10)
            new_wood[y, x] = [1 - alpha, 1 - alpha, 1 - alpha]  # Change wood color
        self.im.set_array(new_wood)
        return self.im,

    def draw_drill_line(self, start_x, start_y, end_x, end_y, radius):
        # Calculate the parameters of the line
        dx = end_x - start_x
        dy = end_y - start_y
        distance = np.sqrt(dx**2 + dy**2)
        step_x = dx / distance
        step_y = dy / distance

        # Draw the line using the drill bit radius
        for t in np.arange(0, 1, radius / distance):
            x = int(start_x + t * dx)
            y = int(start_y + t * dy)
            self.draw_semi_circle(x, y, radius)

    def draw_semi_circle(self, center_x, center_y, radius):
        for i in range(center_x - radius, center_x + radius + 1):
            for j in range(center_y - radius, center_y + radius + 1):
                if (i - center_x) ** 2 + (j - center_y) ** 2 <= radius ** 2:
                    self.wood[j, i] = [1, 1, 1]  # White color



# Example usage
wood_simulator = WoodSimulation(1000, 1000)  # Create a wood simulation with 100x100 size
# wood_simulator.animate_cut()  # Animate cutting along the full diagonal of the wood
wood_simulator.draw_drill_line(20, 20, 80, 80, 10)  # Draw a drill line from (20, 20) to (80, 80) with radius 10



def draw_circle(radius, start_angle=0, end_angle=360):
    # Initialize variables
    x = 0
    y = radius
    d = 3 - 2 * radius

    # Loop until x is less than or equal to y
    while x <= y:
        # Calculate the angle of the current point
        angle = math.degrees(math.atan2(y, x))
        # Check if the angle is within the specified range
        if start_angle <= angle <= end_angle:
            # Plot points if angle is within the specified range
            plot_points(x, y)
        # Calculate the decision parameter and update y
        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        x += 1

def plot_points(x, y):
    # Plot points in all octants using symmetry
    points = [(x, y), (-x, y), (x, -y), (-x, -y),
              (y, x), (-y, x), (y, -x), (-y, -x)]
    for point in points:
        # Plot each point
        plot_pixel(point)

def plot_pixel(point):
    # Draw a pixel at the given point (x, y)
    pass  # You can implement this function based on your chosen display method.
