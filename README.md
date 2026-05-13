# JenkinsQA_Python_2026_spring

Проект на **Python** с использованием **Selenium** для автоматизации браузера.

## Структура проекта

* `requirements.txt` — содержит необходимые библиотеки (`selenium`, `webdriver-manager`, `pytest`).
* `.gitignore` — игнорирование временных файлов и папки вирутального окружения.

## Быстрый старт (Windows + PowerShell)

1. **Создайте виртуальное окружение** (выполните в корне проекта):
   ```powershell
   python -m venv venv
   ```

2. **Активируйте виртуальное окружение:**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

3. **Установите зависимости:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Запустите тесты:**
   ```powershell
   pytest -v -s
   ```
