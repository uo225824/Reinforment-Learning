from typing import List
import random

#Firts toy model
#The enviroment will give the agent random rewards for a limtited number of steps

class Environment:
    def __init__(self):
        self.steps_left=10

    def get_observation(self)-> List[float]:
        return [0.0,0.0,0.0]


    def get_actions(self)->List[int]:
        return [0,1]

    def is_done(self)->bool:
        return self.steps_left==0


    def action(self,action:int)->float:
        if self.is_done():
            raise Exception("Game is over")
        self.steps_left-=1
        return random.random()


#The agent

class Agent:
    def __init__(self):
        self.total_reward=0.0

    def step(self, env:Environment):
        curretn_obs=env.get_observation()
        action=env.get_actions()
        reward=env.action(random.choice(action))
        self.total_reward+=reward


if __name__ == "__main__":
    env = Environment()
    agent = Agent()

    while not env.is_done():
        agent.step(env)

    print("Total reward got: %.4f" % agent.total_reward)