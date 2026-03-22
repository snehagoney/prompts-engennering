# Short 03 — Multi-shot Prompting

## Task
Write one multi-shot prompt and run it locally.

## Guidelines
- Provide at least 5 examples then a new input.
- Keep format consistent.
- Choose one: support ticket tagging, email intent labeling, product category tagging, simple error classification, short text formatting.

## Code Example
```python
from helper import get_completion

prompt = """
Input: 'Cancel subscription' -> Intent: Account
Input: 'Reset my password' -> Intent: Account
Input: 'Recommend lunch options' -> Intent: Chat
Input: 'Error 404 on dashboard' -> Intent: Bug
Input: 'Schedule onboarding session' -> Intent: Meeting

Now classify:
Input: 'Why is the invoice total higher this month?'
"""

response = get_completion(prompt)
print(response)
```

## Expected
Intent: Billing
