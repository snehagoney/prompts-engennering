from helper import get_completion

prompt = """
Input: 'Cancel subscription' -> Intent: Account
Input: 'Reset my password' -> Intent: Account
Input: 'Bug in app' -> Intent: Bug
Input: 'Schedule call' -> Intent: Meeting
Input: 'Share report' -> Intent: Communication

Now classify:
Input: 'Why is the invoice total higher this month?'
"""

response = get_completion(prompt)
print(response)
