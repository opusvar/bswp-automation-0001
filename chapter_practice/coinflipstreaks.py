
# write a program to generate a list of randomly selected heads and tails values
# determine how often a streak of 6 heads or 6 tails in a randomly generated list of heads and tails.
# all of the code should loop to generate 10,000 times so we can find out what percentage of 
# coin flips contain a streak of six heads or tails in a row.
# use random.randint(0,1) 

# template code 
"""
import random 

number_of_streaks = 0

for experimentNumber in range(10000):
    # Code creates a list of 100 heads or tails values
    # Code checks to see if there is a streak of 6 heads or tails in a row
    print ('Chance of streak: %s%%'(number_of_streaks / 100))

"""


import random


def coin_flip_simulation():
    number_of_streaks = 0
    
    for experiment_outcomes in range(10_000):
        set_of_100 = []
        while len(set_of_100) < 100:
            set_of_100.append(random.randint(0, 1))
        else:
            print("100 values added to set_of_100. Value count:", len(set_of_100))
            return set_of_100

print(coin_flip_simulation())





    