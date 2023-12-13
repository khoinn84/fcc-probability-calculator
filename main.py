# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main

prob_calculator.random.seed(95)
hat2 = prob_calculator.Hat(blue=2, red=2, green=6)
#print(hat2.contents)
#hat2.draw(3)
#hat1 = prob_calculator.Hat(yellow=3, blue=2, green=6)
#hat2 = prob_calculator.Hat(red=5, orange=4)
#hat3 = prob_calculator.Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)


#probability = prob_calculator.experiment(
#    hat = hat2,
#    expected_balls={"blue": 2,"red": 1},
#    expected_balls={"blue": 1},
#    num_balls_drawn=4,
#    num_experiments=100)
#print("Probability:", probability)

# Run unit tests automatically
main(module='test_module', exit=False)
