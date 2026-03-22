# Short 06 — Advanced Prompting

## Task
Write one advanced prompt and run it locally.

## Guidelines
- No examples.
- Ask for reasoning and specific output structure.
- Choose one: planning + bullets, multi-step decision, data extraction + summary.

## Code Example
```python
from helper import get_completion

prompt = """
Act as a product strategy advisor.\n\nTask:\n- Outline 4 steps to reduce monthly churn by 20%.\n- Include a short risks section at end.\n\nOutput format:\n1. ...\n2. ...\n3. ...\n4. ...\nRisks: ...\n"""

response = get_completion(prompt)
print(response)
```

## Expected
4-step plan and risk note.
