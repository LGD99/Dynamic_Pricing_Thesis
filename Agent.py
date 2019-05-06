import random
from math import exp
import numpy as np
# from collections import deque
# from keras.models import Sequential
# from keras.layers import Dense
# from keras.optimizers import Adam

from Parameters import *


class Agent():

    def __init__(self):
        # self.policy_net = self.build_model() # Q1
        # self.target_net = self.policy_net  # Q2
        self.t = 0
        self.prices = np.zeros((1, NUM_PRICES), dtype=int)
        self.epszilon = 1
        self.states = []

    # def build_model(self):
    #     model = Sequential()
    #     model.add(Dense(420, input_dim=210, activation='relu'))
    #     model.add(Dense(10, activation='relu'))
    #     model.compile(loss='mse', optimizer=Adam(lr=0.01))
    #     return model

    def take_action(self):  # Choose a price

        self.epszilon = 1 / exp(self.t / 20)
        if random.random() < self.epszilon:  # random prices
            for i in range(NUM_PRICES):
                self.prices[0,i] = np.random.randint(0, 10)
        else:  # DQN gives prices
            for i in range(NUM_PRICES):
                self.prices[0,i] = np.random.randint(0, 10)
        self.t += 1

    def clear_prices(self):
        self.prices = np.zeros((1, NUM_PRICES), dtype=int)

    def train(self):
        if self.t % 100 == 0:
            z=6
            # self.target_net = self.policy_net