# Files and Serialization / Файлы и сериализация

## English

Use a context manager so files close even when an exception occurs. Use `pathlib.Path` for portable path operations and specify text encoding.

```python
from pathlib import Path
import json

path = Path("data") / "settings.json"
with path.open("r", encoding="utf-8") as stream:
    settings = json.load(stream)
```

JSON is interoperable but supports a limited type model. CSV is tabular but needs explicit delimiter, encoding and schema decisions. `pickle` can preserve Python-specific objects, but loading it can execute arbitrary code: only unpickle data from a trusted, controlled source.

## Русский

Используйте контекстный менеджер, чтобы файл закрывался даже при исключении. Для переносимой работы с путями используйте `pathlib.Path`, а для текста явно задавайте кодировку.

JSON удобен для обмена, но поддерживает ограниченный набор типов. CSV предназначен для таблиц, однако требует явных решений по delimiter, кодировке и схеме. `pickle` сохраняет Python-объекты, но при загрузке способен выполнить произвольный код: открывайте только полностью доверенные данные.

Sources / Источники: [Input and Output](https://docs.python.org/3/tutorial/inputoutput.html), [`pickle` warning](https://docs.python.org/3/library/pickle.html)
