### Предупреждение
Данный проект является выполнением тестового задания

### Инструкция для запуска
1. Клонирование репозитория `git clone https://github.com/Randommist/TZ_userbot.git`
2. Создание проекта в google console и добавление api: Google Sheets API, Google Drive API. Получение json ключа и помещение его в директорию `~/.config/gspread/service_account.json` для linux и `%APPDATA%\gspread\service_account.json` для windows. Подробнее тут https://docs.gspread.org/en/latest/oauth2.html#enable-api-access
3. Зарегистрировать приложение на https://my.telegram.org/apps
4. Переименовать .env-example в .env и заполнить нужными значениями
5. Установка зависимострей. Для этого вам нужен poetry. `poetry install`
6. Запуск проекта: `poetry shell` затем `python userbot/main.py`