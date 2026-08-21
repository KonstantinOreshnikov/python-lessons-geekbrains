# Types and Collections / Типы и коллекции

## English

Choose a structure by semantics, not habit:

| Type | Best fit | Key property |
|---|---|---|
| `list` | ordered sequence | mutable, duplicates allowed |
| `tuple` | fixed record or sequence | immutable |
| `dict` | key-to-value mapping | unique hashable keys |
| `set` | membership and uniqueness | no duplicates |

Avoid modifying a collection while iterating over it unless the behavior is deliberate. For transformations, comprehensions are useful when they remain short and readable; use a normal loop for complex branching.

```python
amounts = [120, 80, 120, 45]
positive_unique = {amount for amount in amounts if amount > 0}
by_position = {index: amount for index, amount in enumerate(amounts)}
```

## Русский

Выбирайте структуру по смыслу, а не по привычке: `list` — изменяемая последовательность, `tuple` — фиксированный набор, `dict` — отображение ключей в значения, `set` — уникальность и проверка принадлежности.

Не изменяйте коллекцию во время обхода, если это поведение не задумано явно. Comprehension удобен для коротких читаемых преобразований; при сложных условиях обычный цикл понятнее.

Source / Источник: [Python Tutorial — Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
