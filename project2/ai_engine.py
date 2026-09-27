
from openai import OpenAI
from config import AI_API_KEY
import json
import time

client = OpenAI(
    api_key=AI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
def analyze_customer_message(message):
    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model="gemini-3.7-flash",
                messages=[
                    {
                        "role": "system",
                        "content": """
You are a customer support AI.

Analyze the customer's message and return ONLY valid JSON.

The JSON must contain exactly these keys:
category
priority
action

Allowed categories:
product_issue
product_damage
delivery_issue
account_issue

Allowed priorities:
high
medium
low

Allowed actions:
replacement
refund
human_support
auto_reply
"""
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        except Exception as e:
            print(f"AI API request failed (attempt {attempt + 1}/3)")
            print("Error:", e)

            if attempt < 2:
                print("Retrying...")
                time.sleep(5)
                continue
            else:
                print("All AI attempts failed")
                return None

        result = response.choices[0].message.content

        try:
            result = result.replace("```json", "")
            result = result.replace("```", "")
            result = result.strip()

            return json.loads(result)

        except json.JSONDecodeError as e:
            print("AI returned invalid JSON")
            print("Error:", e)
            return None