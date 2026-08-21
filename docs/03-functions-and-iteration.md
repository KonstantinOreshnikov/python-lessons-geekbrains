# Functions and Iteration / Функции и итерации

## English

A function should express one coherent operation. Prefer explicit parameters, return values and names over hidden mutation. Positional-only (`/`) and keyword-only (`*`) markers can make an API harder to misuse.

```python
def weighted_score(values: list[float], /, *, weight: float = 1.0) -> float:
    """Return the weighted sum of values."""
    return sum(value * weight for value in values)
```

An iterable can produce an iterator; an iterator returns items until `StopIteration`. A generator function uses `yield` and creates values lazily, which is useful for streams or large inputs. Do not claim that generators are always faster: their main advantage is incremental production and bounded memory.

## Русский

Функция должна выражать одну логичную операцию. Предпочитайте явные параметры, возвращаемые значения и понятные имена скрытому изменению состояния. Маркеры positional-only (`/`) и keyword-only (`*`) помогают сделать API менее двусмысленным.

Iterable способен создать iterator; iterator выдаёт элементы до `StopIteration`. Генераторная функция использует `yield` и создаёт значения по мере запроса. Это полезно для потоков и больших входов, но не означает автоматического ускорения любого кода.

Sources / Источники: [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions), [Iterators](https://docs.python.org/3/tutorial/classes.html#iterators)
