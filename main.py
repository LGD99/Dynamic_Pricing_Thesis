from Customer_Class import Customer
from Agent import Agent
from Environment_Class import Environment
from Parameters import *

# test = open('test', 'w')
# prices = open('prices', 'w')
#
# environment = Environment()
# environment.generate_customers()
#
# agents = []
# for i in range(NUM_AGENTS):
#     agents.append(Agent())
#
#
# for i in range(100):
#     for i in range(NUM_AGENTS):
#         agents[i].take_action()
#         print(agents[i].prices)
#         environment.get_prices_from_agents(agents[i].prices)
#     print(agents[0].prices,";;",agents[1].prices,";;",agents[2].prices,";;",agents[3].prices,";;",agents[4].prices, file=prices)
#     environment.delete_first_row()
#     environment.customers_decide()
#     environment.calculate_g()
#     environment.generate_state(2)
#     for i in range(NUM_AGENTS):
#         agents[i].clear_prices()
#     environment.clear_prices()
#     for i in range(NUM_CUSTOMERS):
#         print(environment.customers[i].group, ";", environment.customers[i].which_agent, ";", environment.customers[i].which_price, file=test)
#     print(";;", file=test)


agents = []
for i in range(NUM_AGENTS):
    agents.append(Agent())

environment = Environment()

for e in range(EPOCHS):
    environment.generate_customers()
    environment.generate_g()
    for i in range(NUM_BIDS):
        for j in range(NUM_AGENTS):
            agents[j].take_action()
            environment.get_prices_from_agents(agents[j].prices)
        environment.delete_first_row()
        environment.customers_decide()
        environment.calculate_g()
        for j in range(NUM_AGENTS):
            agents[j].states = environment.generate_state(j)
            z=6




