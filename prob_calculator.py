import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **ballcolor):
        for key, value in ballcolor.items():
            if value != 1:
                print(f"Color {key} has {value} balls")
            else:
                print(f"Color {key} has {value} ball")


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    return True