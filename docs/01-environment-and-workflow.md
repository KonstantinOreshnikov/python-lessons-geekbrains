# Environment and Workflow / Окружение и workflow

## English

Use a supported Python 3 release and isolate third-party packages per project. A virtual environment prevents one project's dependencies from silently changing another project.

```bash
python -m venv .venv
python -m pip install --upgrade pip
```

Keep generated environments, caches, credentials and local settings out of Git. Prefer `python -m pip` and `python -m pytest`: both commands make the selected interpreter explicit.

A maintainable project normally separates application code, tests and documentation. Record direct dependencies and make setup reproducible; do not treat a global workstation environment as project configuration.

## Русский

Используйте поддерживаемую версию Python 3 и изолируйте сторонние пакеты для каждого проекта. Виртуальное окружение не позволяет зависимостям одного проекта незаметно менять другой.

Не добавляйте в Git окружения, кэши, credentials и локальные настройки. Формы `python -m pip` и `python -m pytest` явно используют выбранный интерпретатор.

Поддерживаемый проект обычно разделяет код приложения, тесты и документацию. Фиксируйте прямые зависимости и делайте установку воспроизводимой; глобальное окружение компьютера не является конфигурацией проекта.

Source / Источник: [Installing packages with pip and venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
