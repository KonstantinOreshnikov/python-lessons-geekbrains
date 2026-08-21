# Python Learning Lab / Учебная лаборатория Python

A bilingual, practice-first path from Python fundamentals to maintainable, tested programs.

Двуязычный практический маршрут от основ Python до поддерживаемых программ с тестами.

## English

This lab consolidates the useful themes from earlier lectures, seminars and exercises into an original curriculum. Course attachments remain private; the repository contains rewritten explanations, original examples and reproducible exercises.

## Русский

Лаборатория объединяет полезные темы ранних лекций, семинаров и заданий в оригинальную программу. Учебные вложения остаются приватными; в репозитории размещены переработанные объяснения, собственные примеры и воспроизводимые упражнения.

## Learning path / Учебный маршрут

1. [Environment and workflow / Окружение и workflow](docs/01-environment-and-workflow.md)
2. [Types and collections / Типы и коллекции](docs/02-types-and-collections.md)
3. [Functions and iteration / Функции и итерации](docs/03-functions-and-iteration.md)
4. [Files and serialization / Файлы и сериализация](docs/04-files-and-serialization.md)
5. [Errors and object-oriented design / Ошибки и ООП](docs/05-errors-and-oop.md)
6. [Testing and code quality / Тестирование и качество](docs/06-testing-and-quality.md)
7. [Practice kata / Практическая задача](exercises/README.md)

## Quick start / Быстрый старт

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows: .venv\Scripts\activate
python -m pip install -e ".[dev]"
python -m pytest
```

## Principles / Принципы

- Prefer readable, small functions with explicit inputs and outputs.
- Use a virtual environment per project.
- Add type hints where they improve understanding; they do not replace runtime validation.
- Use `pathlib`, context managers and explicit text encodings.
- Test behavior, including boundaries and expected errors.
- Never load untrusted `pickle` data.

---

- Предпочитайте небольшие читаемые функции с явными входами и результатами.
- Используйте отдельное виртуальное окружение для каждого проекта.
- Добавляйте type hints там, где они улучшают понимание; они не заменяют runtime-проверки.
- Используйте `pathlib`, контекстные менеджеры и явную кодировку текста.
- Тестируйте поведение, включая границы и ожидаемые ошибки.
- Никогда не загружайте недоверенные данные `pickle`.

## Official references / Официальные источники

- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Python Standard Library](https://docs.python.org/3/library/)
- [PEP 8 — Style Guide](https://peps.python.org/pep-0008/)
- [PEP 257 — Docstrings](https://peps.python.org/pep-0257/)
- [Python Packaging User Guide](https://packaging.python.org/)
- [pytest documentation](https://docs.pytest.org/en/stable/)

## Legacy materials / Исторические материалы

Existing lesson folders remain unchanged during migration. Their later relocation or archival requires a separate reviewed change.

Существующие папки уроков остаются без изменений на время миграции. Их последующий перенос или архивирование потребуют отдельного проверяемого изменения.

## License

MIT. See [LICENSE](LICENSE).
