# Testing and Code Quality / Тестирование и качество

## English

Tests should communicate behavior. Cover normal cases, boundaries and expected failures. Keep tests deterministic and independent; replace uncontrolled clocks, randomness, networks and files with explicit inputs or fixtures when appropriate.

```python
import pytest

def test_rejects_non_positive_value() -> None:
    with pytest.raises(ValueError, match="positive"):
        parse_positive_int("0")
```

PEP 8 prioritizes readability and consistency. Public APIs benefit from concise docstrings. Type hints support readers and static tools but are not enforced by Python at runtime. Formatting, linting and type checking should be automated in CI once the project needs them.

## Русский

Тесты должны описывать поведение. Проверяйте обычные сценарии, граничные значения и ожидаемые ошибки. Делайте тесты детерминированными и независимыми; неконтролируемое время, случайность, сеть и файлы при необходимости заменяйте явными входами или fixtures.

PEP 8 ставит во главу читаемость и последовательность. Публичным API полезны короткие docstrings. Type hints помогают читателю и статическим инструментам, но Python не обеспечивает их runtime-проверку автоматически. Форматирование, linting и type checking стоит автоматизировать в CI по мере развития проекта.

Sources / Источники: [pytest Get Started](https://docs.pytest.org/en/stable/getting-started.html), [PEP 8](https://peps.python.org/pep-0008/), [PEP 257](https://peps.python.org/pep-0257/), [Typing](https://docs.python.org/3/library/typing.html)
