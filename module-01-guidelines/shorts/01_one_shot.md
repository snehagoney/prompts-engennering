# Short 01 — One-shot Prompting

## Task
Write one one-shot prompt and run it locally.

## Guidelines
- Provide exactly one example.
- After example, ask for same task on a new input.
- Choose one: tone conversion, title formatting, caption cleanup, simple rewriting, classification style alignment.

## Code Example
```python
from helper import get_completion

prompt = """
Example:
Input: 'this is fine' -> Output: 'this is acceptable'

Now do this:
Input: 'turn that around'
"""

response = get_completion(prompt)
print(response)
```

## Expected
A refined, polite rewrite.
