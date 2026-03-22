# Short 05 — Zero-shot CoT Prompting

## Task
Write one zero-shot CoT prompt and run it locally.

## Guidelines
- Do not give examples.
- Ask to solve step-by-step.
- Choose one: cost calculation, savings problem, comparison task, planning task, simple business reasoning.

## Code Example
```python
from helper import get_completion

prompt = """
Zero-shot step-by-step reasoning:
A project has 70 tasks. Each developer completes 6 tasks/day. On day 1 there are 4 devs, on day 2 there are 3 devs, and on day 3 there are 5 devs. How many days until completion? Show work.
"""

response = get_completion(prompt)
print(response)
```

## Expected
Detailed reasoning chain + total days.
