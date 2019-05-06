from Customer_Class import Customer
from random import randint
from Parameters import *
import numpy as np
from math import exp

class Environment:

    def __init__(self):

        self.customers = []
        self.prices = np.zeros((1, NUM_PRICES), dtype=int)
        self.decisions = np.zeros((NUM_CUSTOMERS, PRICES), dtype=int)
        self.states = []
        self.g = self.generate_g()
        self.fairness = 0

    def generate_g(self):
        g = np.zeros(NUM_GROUPS)
        return g

    def generate_customers(self):
        self.customers.clear()
        for i in range(NUM_CUSTOMERS):
            self.customers.append(Customer(randint(0, NUM_GROUPS-1)))

    def get_prices_from_agents(self, prices):
        # if self.prices.all() == np.zeros((1, NUM_PRICES), dtype=int).all():
        #     self.prices = prices
        # else:
        self.prices = np.concatenate((self.prices, prices), axis= 0 )

    def delete_first_row(self):
        self.prices = np.delete(self.prices, 0, 0)

    def clear_prices(self):
        self.prices = np.zeros((1, NUM_PRICES), dtype=int)

    def customers_decide(self):
        for i in range(NUM_CUSTOMERS):
            if NUM_PRICES == 1:
                self.customers[i].which_agent_price_is_choosen(self.prices[:, 0])
            else:
                self.customers[i].which_agent_price_is_choosen(self.prices[:,self.customers[i].group])

    def calculate_g(self):
        g = np.zeros(NUM_GROUPS)
        p = np.zeros(NUM_GROUPS)
        previous = self.g

        for j in range(NUM_CUSTOMERS):
            g[self.customers[j].group] += 1
            p[self.customers[j].group] += self.customers[j].which_price
        for i in range(NUM_GROUPS):
            if g[i] != 0:
                self.g[i] = (round(p[i] / g[i]) + previous[i])/2

    def calculate_fairness(self):

        tmp = 0
        for i in range(NUM_GROUPS):
            tmp += 10 - self.g[i]
        fairness = tmp * tmp
        tmp = 0
        for i in range(NUM_GROUPS):
            tmp += (10 - self.g[i]) * (10 - self.g[i])
        self.fairness = fairness / (NUM_GROUPS * tmp)

    def calculate_reward(self, price):
        return Betap * exp((-1 * (price/10 - Pt)**2) / Szigmap ) + Betaf * exp((-1 * (self.fairness - Ft)**2) / Szigmaf )

    def generate_state(self, which_agent):
        state = []
        for j in range(NUM_CUSTOMERS):
            #which group - one-hot vector
            group = np.zeros(NUM_GROUPS, dtype=int)
            group[self.customers[j].group] = 1
            #fairness - one-hot vector
            self.calculate_fairness()
            fair = np.zeros(100, dtype=int)
            i=int(round(self.fairness)*100-1)
            fair[i] = 1
            #reward
            if self.customers[j].which_agent == which_agent:
                r = self.calculate_reward(self.customers[j].which_price)
            else:
                r = self.calculate_reward(-0.5)
            #which agent
            agent = np.zeros(NUM_AGENTS,dtype=int)
            agent[self.customers[j].which_agent]=1
            #price
            price = np.zeros(100,dtype=int)
            price[round(int(self.customers[j].which_price/ 10)*100-1)] = 1
            s = np.concatenate((group,fair))
            s = np.concatenate((s,agent))
            s = np.concatenate((s,price))
            s = np.append(s,r)
            state.append(s)
        return state
















 # def get_states(self):
 #
 #     states = []
 #
 #     for i in range(len(self.customers)):
 #         states.append(np.concatenate((self.customers[i].get_group(), self.decisions[i]), axis=None))
 #     return states


#Test
# environment = Environment()
# environment.generate_customers()
#
# prices1 = [1, 3, 6, 9]
# prices2 = [2,3,4,5]
# prices3 = [7,8,9,4]
# prices4 = [8,8,8,8]
#
# environment.get_prices_from_agents(prices1)
# environment.get_prices_from_agents(prices2)
# environment.get_prices_from_agents(prices3)
# environment.get_prices_from_agents(prices4)
#
# print(environment.prices)
#
# environment.clear_prices()
#
# environment.get_prices_from_agents(prices2)
# environment.get_prices_from_agents(prices1)
# environment.get_prices_from_agents(prices4)
# environment.get_prices_from_agents(prices3)
#
# print(environment.prices)

#z = 6
#print(environment.get_states())
#for x in range(len(environment.customers)):
#    print(environment.customers[x].get_group(), environment.decisions[x])

# states = environment.get_states()
# for x in range(len(states)):
#     print(states[x])

