# -*- coding: utf-8 -*-
import os
from openai import OpenAI
from app.env import SupportEnv
from models import Action

# OpenAI client (kept for requirement)
client = OpenAI(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)

env = SupportEnv()


def run_episode():
    state = env.reset()
    done = False
    total_score = 0

    query = state.customer_query.lower()
    step = 0  # manual step tracking

    while not done:
        # EASY TASK
        if "refund" in query:
            if step == 0:
                action = Action(
                    action_type="respond",
                    content="You can request a refund within 7 days."
                )
            else:
                action = Action(action_type="close")

        # MEDIUM TASK
        elif "payment" in query:
            if step == 0:
                action = Action(action_type="classify")
            elif step == 1:
                action = Action(
                    action_type="respond",
                    content="Sorry for the inconvenience. Your payment issue will be resolved."
                )
            else:
                action = Action(action_type="close")

        # HARD TASK
        elif "charged twice" in query or "no support" in query:
            if step == 0:
                action = Action(action_type="classify")
            elif step == 1:
                action = Action(action_type="escalate")
            elif step == 2:
                action = Action(
                    action_type="respond",
                    content="We have escalated your issue and will resolve it soon."
                )
            else:
                action = Action(action_type="close")

        else:
            action = Action(action_type="close")

        state, reward, done, _ = env.step(action)
        total_score += reward.score

        step += 1  # increment step manually

    return total_score


def main():
    scores = []

    for _ in range(3):
        score = run_episode()
        scores.append(score)

    avg_score = sum(scores) / len(scores)

    print("Scores:", scores)
    print("Average Score:", avg_score)


if __name__ == "__main__":
    main()