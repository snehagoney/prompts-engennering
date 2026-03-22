# Short 00 — Zero-shot Prompting

## Task
Write one zero-shot prompt and run it locally.

## Guidelines
- Do not give examples.
- Ask one clear instruction.
- Choose one: summarization, rewriting, translation, idea generation, simple classification.

## Code Example
```python
from helper import get_completion

prompt = """
Turn this paragraph into a compact bulleted summary:
Our team shipped the update with three new features, but we observed a 15% drop in performance metrics. We need a debugging plan before the next sprint.
"""

response = get_completion(prompt)
print(response)
```

## Expected
A three-bullet action summary.
