import numpy as np
import gym
from doomreal import DoomTakeCoverWrapper
from doomrnn import DoomCoverRNNEnv

def make_env(env_name, seed=-1, render_mode=False, load_model=True):
  if env_name == 'doomrnn':
    print('making rnn doom environment')
    
    env = DoomCoverRNNEnv(render_mode=render_mode, load_model=load_model)
  else:
    print('making real doom environment')
    print('here before')
    env = DoomTakeCoverWrapper(render_mode=render_mode, load_model=load_model)
    print('here after')
    
  if (seed >= 0):
    env.seed(seed)
  return env
