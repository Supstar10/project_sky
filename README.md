# Онлайн-магазин товаров
Добро пожаловать в наш проект по созданию онлайн-магазина.
Этот проект разработан с использованием Python и фреймворка Django.
## Описание
Наш онлайн-магазин предлагает широкий ассортимент товаров, включая одежду, обувь, электронику и многое другое. 
Пользователи могут просматривать товары, добавлять их в корзину и оформлять заказы или продавать вещи.
## Установка

Следуйте этим шагам, чтобы скачать и установить проект на своем локальном компьютере:
### 1. Клонирование репозитория

Сначала клонируйте репозиторий на свой компьютер:

```bash
git clone https://github.com/Supstar10/project_sky.git
```
### 2. Установка зависимостей
Перейдите в директорию проекта и установите необходимые зависимости:

cd ваш_репозиторий
pip install -r requirements.txt

### 3. Настройка базы данных
Создайте базу данных (например, PostgreSQL) и настройте параметры подключения в файле settings.py.
### 4. Применение миграций
Примените миграции для создания необходимых таблиц в базе данных:

python manage.py migrate
### 5. Создание суперпользователя
Создайте суперпользователя для доступа к административной панели:

python manage.py createsuperuser
### 6. Запуск сервера
Запустите сервер разработки:

python manage.py runserver
Теперь вы можете открыть браузер и перейти по адресу http://127.0.0.1:8000, чтобы увидеть ваш онлайн-магазин в действии.
# Вклад
Если вы хотите внести свой вклад в проект, пожалуйста, создайте форк репозитория и отправьте pull request с вашими изменениями.
# Спасибо за интерес к нашему проекту! Если у вас есть вопросы, не стесняйтесь обращаться.