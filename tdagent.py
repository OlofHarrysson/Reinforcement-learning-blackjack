from carddeck import *

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
        for i in range(self.number_of_epochs):
            print(i)
            observation = self.env.reset()
            terminal = False
            reward = 0
            while not terminal:
                # render method will print you the situation in the terminal
                #self.env.render()
                action = self.make_step(observation, reward, terminal)
                observation, reward, terminal, _ = self.env.step(action)

                # TODO your code will be very likely here
            #self.env.render()

    def make_step(self, observation, reward, terminal):
        # alpha is learning rate
        # model?
        return 1 if observation.player_hand.value() < 17 else 0
