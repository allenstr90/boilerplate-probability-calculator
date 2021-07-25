import copy
import random


# Consider using the modules imported above.

class Hat:
    def __init__(self, **input):
        self.contents = []
        for k, v in input.items():
            for x in range(v):
                self.contents.append(k)

    def draw(self, cant):
        balls = []
        if cant > len(self.contents):
            balls = self.contents
            self.contents = []
        else:
            for _ in range(cant):
                balls.append(self.contents.pop(random.randint(0, len(self.contents) - 1)))
        return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        draw = hat_copy.draw(num_balls_drawn)
        match = True
        for k, v in expected_balls.items():
            if draw.count(k) < v:
                match = False
                break
        if match:
            m += 1

    return m / num_experiments
