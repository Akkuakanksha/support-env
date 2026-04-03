from models import Action
from app.graders.grader import grade_easy, grade_medium, grade_hard

# EASY TEST
print("Easy:", grade_easy("You can request refund within 7 days", ["refund", "7 days"]))

# MEDIUM TEST
actions = [
    Action(action_type="classify"),
    Action(action_type="respond"),
    Action(action_type="close")
]

print("Medium:", grade_medium(actions, ["classify", "respond", "close"]))

# HARD TEST
actions = [
    Action(action_type="classify"),
    Action(action_type="escalate"),
    Action(action_type="respond"),
    Action(action_type="close")
]

print("Hard:", grade_hard(actions, ["classify", "escalate", "respond", "close"]))