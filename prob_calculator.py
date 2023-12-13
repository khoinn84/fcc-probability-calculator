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
            for i in range(num_balls_drawn):
                ball_drawn = random.choice(self.contents)
                balls_drawn.append(ball_drawn)
                self.contents.remove(ball_drawn)
                #print("Balls drawn",balls_drawn)
                #print("The rest:\n",tempList)
                #print("==============")
            #print("Balls drawn",balls_drawn)
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
        #if set(expectation).issubset(set(drawnset)):
        #if all(element in drawnset for element in expectation):
        if checkLWL(expectation,drawnset):
            #print(expectation)
            #print(drawnset)
            M += 1
            #print('M',M)
    
    return M / num_experiments

def checkLWL(ls, lb):
    listsmall = copy.deepcopy(ls)
    listbig = copy.deepcopy(lb)
    while len(listsmall) > 0:
        if listsmall[0] not in listbig:
            return False
        else:
            listbig.remove(listsmall[0])
            listsmall.remove(listsmall[0])
    return True
