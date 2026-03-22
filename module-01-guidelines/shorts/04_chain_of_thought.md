# Short 04 — Chain-of-Thought Prompting

## Task
Write one chain-of-thought prompt and run it locally.

## Guidelines
- Choose a reasoning problem.
- Ask model to think step-by-step.
- Choose one: simple math, cost calculation, comparison, decision-making, planning.

## Code Example
```python
from helper import get_completion

prompt = """
Solve step-by-step:
A workshop requires 18 chairs. Chairs are sold in bundles of 5 for $30 and singles for $8. What is the cheapest way to buy exactly 18 chairs?
"""

response = get_completion(prompt)
print(response)
```

## Expected
Step-by-step reasoning plus total cost.
