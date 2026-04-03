import sys
import os

# Add current directory to path
sys.path.append(os.path.abspath("."))

from app.env import SupportEnv
from models import Action

env = SupportEnv()
state = env.reset()

print("Initial State:", state)

action = Action(action_type="classify")
state, reward, done, _ = env.step(action)

print("After Step:", state)
print("Reward:", reward)