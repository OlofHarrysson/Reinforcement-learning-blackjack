from carddeck import *
import sys
import numpy as np

class TDAgent:
    '''
    Implementaion of an agent that plays the same strategy as the dealer.
    This means that the agent draws a card when sum of cards in his hand
    is less than 17.

    Your goal is to modify train() method to learn the state utility function.
    I.e. you need to change this agent to a passive reinforcement learning
    agent that learns utility estimates using temporal diffrence method.
    '''
    def __init__(self, env, number_of_epochs):
        self.env = env
        self.number_of_epochs = number_of_epochs

    def train(self):

        alpha = 0.1 # Learning rate. TODO: Set arbitrarily
        discount = 1 # Discount rate # TODO: Set arbitrarily

        utility_est = np.zeros(22)

        for i in range(self.number_of_epochs):
            observation = self.env.reset()
            terminal = False
            reward = 0

            state = observation.player_hand.value()
            while not terminal:
                action = self.make_step(observation, reward, terminal)
                observation, reward, terminal, _ = self.env.step(action)

                next_state = observation.player_hand.value()

                if terminal == True:
                    next_state = 0 # Terminal state with utility of 0

                utility_est[state] += alpha * (reward + discount * utility_est[next_state] - utility_est[state])

                state = next_state

                # self.env.render()
                # print("Reward is {:d}".format(reward))
                # print("Action is {:d}".format(action))
                # pause()
                # print(utility_est)
                # sys.exit(1)


        print("################################################")
        print(utility_est)


    def make_step(self, observation, reward, terminal):
        return 1 if observation.player_hand.value() < 17 else 0


def pause():
    programPause = input("Press the <ENTER> key to continue...")
