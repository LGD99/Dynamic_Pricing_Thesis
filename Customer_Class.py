from math import exp
import numpy as np
from random import choice
from Parameters import *


class Customer:

    def __init__(self, group):
        self.group = group
        self.which_agent = -1
        self.which_price = -1

    def get_group(self):
        return self.group

    def accept_bid_probability(self, price):

        acceptance_probability = 0.
        if self.group == 0:
            acceptance_probability = 1

        if self.group == 1:
            b = 18.229
            w = -2.369
            acceptance_probability = (1 / (1 + exp(-(b + w * price))))

        if self.group == 2:
            b = 4.4757
            w = -1.1526
            acceptance_probability = (1 / (1 + exp(-(b + w * price))))

        if self.group == 3:
            b = -1.09195
            w = 0.34000
            acceptance_probability = (1 / (1 + exp(-(b + w * price))))

        # return acceptance possibility
        return acceptance_probability

    def which_agent_price_is_choosen(self, prices):  # the different agents' prices are in the vector

        which_agent = 0

        for i in range(NUM_AGENTS):

            if round(self.accept_bid_probability(prices[i])) == 1:

                if self.accept_bid_probability(prices[i]) == self.accept_bid_probability(prices[which_agent]):
                    which_agent = choice([i, which_agent])

                if self.accept_bid_probability(prices[i]) > self.accept_bid_probability(prices[which_agent]):
                    which_agent = i

        self.which_agent = which_agent
        self.which_price = prices[which_agent]
        #return which_agent






# # Test
# customers = []
# for i in range(4):
#     customers.append(Customer(i))
#
# for i in range(4):
#     for z in range(10):
#         print(customers[i].get_group(), customers[i].accept_bid(z))

#
# customers = []
# for i in range(4):
#     customers.append(Customer(i))
#
# prices = [1, 7, 5, 3, 7
#
#           ]
# for i in range(len(customers)):
#     customers[i].which_agent_price_is_choosen(prices)
#     print(customers[i].get_group(), customers[i].accept_bid_probability(prices[0]), customers[i].accept_bid_probability(prices[1]), customers[i].accept_bid_probability(prices[2]),
#           customers[i].accept_bid_probability(prices[3]),customers[i].accept_bid_probability(prices[4]), customers[i].which_price, customers[i].which_agent)
