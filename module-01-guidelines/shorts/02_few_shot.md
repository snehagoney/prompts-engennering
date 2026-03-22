# Short 02 — Few-shot Prompting

## Task
Write one few-shot prompt and run it locally.

## Guidelines
- Provide at least 3 examples before final input.
- Keep examples format consistent.
- Choose one: sentiment classification, category tagging, short content formatting, resume bullet generation, simple extraction.

## Code Example
```python
from helper import get_completion

prompt = """
Example1: 'The team hit every milestone' -> Positive
Example2: 'Delivery was delayed by two weeks' -> Negative
Example3: 'The report was OK but needs revision' -> Neutral

Now classify:
'Customer support helped immediately and politely.'
"""

response = get_completion(prompt)
print(response)
```

## Expected
Positive sentiment label.
