import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **ballcolor):
        self.contents = []
        for key, value in ballcolor.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, num_balls_drawn):
        if num_balls_drawn >= len(self.contents):
            return self.contents
        else:
            balls_drawn = []
            tempList = copy.deepcopy(self.contents)
            for i in range(num_balls_drawn):
                ball_drawn = random.choice(tempList)
                balls_drawn.append(ball_drawn)
                tempList.remove(ball_drawn)
            #print("Ball drawn",balls_drawn)
            #print("The rest",self.contents)
            return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    expectation = []
  
    for key, value in expected_balls.items():
        for i in range(value):
            expectation.append(key)

    for i in range(num_experiments):
        hatcopy = copy.deepcopy(hat)
        drawnset = hatcopy.draw(num_balls_drawn)
        if set(expectation).issubset(set(drawnset)):
            M += 1
        

    
    return M / num_experiments
