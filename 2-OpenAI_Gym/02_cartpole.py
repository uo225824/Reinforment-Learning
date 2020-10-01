import gym

e=gym.make('CartPole-v0')


obs=e.reset()

obs
#[center of mass,speed,angle to platform,angular speed]

e.action_space
#Two state left and right

e.observation_space

e.step(0)

#We push our platform to the left
#We have array 4x1 with the observation of the new state, a reward 1.0
#done flag with value False, which means that the episode is not over yet and we are more or less okay
#Extra information about the environment, which is an empty dictionary

e.action_space.sample()

e.observation_space.sample()
#take a random  value of the observation_space and action_space



#The random CartPole agent implementation

if __name__=="__main__":
    env=gym.make("CartPole-v0")
    total_reward=0.0
    total_steps=0
    obs=env.reset()

#we created the environment and initialized the counter of steps and the reward accumulator


    while True:
        action=env.action_space.sample()
        obs, reward, done, _ =env.step(action)
        total_reward += reward
        total_steps += 1
        if done:
            break
    print("Episode done in %d steps, total reward %.2f" % (total_steps, total_reward))
    """"we sampled a random action, then asked the environment to execute
        it and return to us the next observation (obs), the reward, and the done flag"""