def is_valid_action(action):
    allowed_actions = [
        "refund",
        "replacement",
        "human_support",
        "auto_reply"
    ]

    return action in allowed_actions
print(is_valid_action("refund"))
print(is_valid_action("delete_account"))