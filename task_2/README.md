#Bot with Google 
Бот работает локально
## Getting started
Для запуска проекта локально использовать команды
`python3 -m venv venv` - создание виртуального окружения
`source venv/bin/activate` - активация виртуального окружения на unix
`source venv/Scripts/activate` - активаци виртуально окружения на windows
`pip3 install -r requirements.txt` - установка необходимых зависимостей
`python3 bot.py` - запуск бота
Так же для работы приложения необходим креды для авторизации


## Start point
Точкой входа считать файл bot.py


## Instructions 
- Бот принимает любое текстовое сообщение и добавляет это в excel табличку в google drive. Ссылка на табличку
https://docs.google.com/spreadsheets/d/1zCaYlpdVLzn7hdgmODPLz7KXom0V-zk_toJ0s7FI4pg/edit#gid=0
- Ошибки возникающие в процессе выполнения логируются в формате: "Время  текст ошибки"

