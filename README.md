Rostelecom
Работа с ресурсом https://b2c.passport.rt.ru/ test_selenium_page_elements.py - проверка наличия элементов на странице согласно спецификации test_selenium_auth.py позитивные тесты авторизации по номеру телефона и почте test_selenium_auth_negative.py негативные тесты авторизации по номеру телефона и почте

Настройка проекта:
Создаем виртуапльное окружение командой: python -m venv venv
Активируем виртуальное окружение командой (MacOS/Linux): source venv/bin/activate для Windows другая команда: \env\Scripts\activate.bat
Установка зависимостей: pip install -r requirements.txt
Настроить в IDE(Pycharm) текущий интерпритатор, выбрав текущее виртуальное окружение
В папке driver содержится драйвер для работы с браузером Chome 116 версии. Рекомендуется проверить соответствие версии браузера, при необходимости обновить драйвер
Запуск тестов:
Набираем в терминале команду: pytest -v
