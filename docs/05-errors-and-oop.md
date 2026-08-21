# Errors and Object-Oriented Design / Ошибки и ООП

## English

Catch exceptions that you can meaningfully handle. Avoid a broad bare `except`: it can hide programming errors and interrupts. Use `else` for code that should run only when the protected block succeeds and `finally` for unconditional cleanup.

```python
def parse_positive_int(raw: str) -> int:
    value = int(raw)
    if value <= 0:
        raise ValueError("value must be positive")
    return value
```

Use classes when state and behavior form a meaningful concept with invariants. Prefer composition to deep inheritance. A small function or dataclass is often enough; OOP is a design tool, not a graduation badge.

## Русский

Перехватывайте только те исключения, которые можете осмысленно обработать. Голый `except` способен скрыть ошибки программы и системные прерывания. Используйте `else` для кода после успешного блока и `finally` для обязательной очистки.

Класс полезен, когда состояние и поведение образуют понятную сущность с инвариантами. Предпочитайте композицию глубокой иерархии наследования. Иногда функции или dataclass достаточно: ООП — инструмент, а не медаль за окончание курса.

Sources / Источники: [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html), [Classes](https://docs.python.org/3/tutorial/classes.html)
