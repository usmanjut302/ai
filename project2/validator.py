
allowed_actions = [
    "replacement",
    "refund",
    "human_support",
    "auto_reply"
]

allowed_priorities = [
    "high",
    "medium",
    "low"
]

allowed_categories = [
    "product_issue",
    "product_damage",
    "delivery_issue",
    "account_issue"
]


def validate_ai_result(ai_result):
    if ai_result is None:
        return False

    if not isinstance(ai_result, dict):
        return False

    required_keys = ["category", "priority", "action"]

    if not all(key in ai_result for key in required_keys):
        return False
    for key in required_keys:
        if not isinstance(ai_result[key], str):
            return False
        ai_result[key] = ai_result[key].strip().lower()
        if not ai_result[key]:
            return False
    if ai_result["action"] not in allowed_actions:
        return False
    if ai_result["priority"] not in allowed_priorities:
        return False
    if ai_result["category"] not in allowed_categories:
        return False
    return True


