Это Django приложение позволяет генерировать случайные пароли и по желанию отправлять их на электронную почту. 
Для выполнения асинхронных задач по отправке электронных писем используется Celery, а для кэширования сессий и очередей задач Celery используется Redis. 
Приложение также упаковано в Docker контейнеры для простого развертывания.

## Требования

- Docker
- Docker Compose

## Установка

1. Клонируйте этот репозиторий: git clone https://github.com/Aliaksandrsw/password_generator
2. Перейдите в директорию проекта  password_generator
3. Создайте файл `.env` из примера `.env.example`:
4. Настройте переменные окружения в файле `.env`
   1. Откройте файл `.env` в текстовом редакторе.
   2. Замените значение `SECRET_KEY` на новый случайно сгенерированный секретный ключ Django.
      Вы можете сгенерировать его с помощью следующей команды в Python:
      from django.core.management.utils import get_random_secret_key
      print(get_random_secret_key())
   3. Установите DEBUG=True для режима разработки или DEBUG=False для продакшена.
   4. Замените DJANGO_ALLOWED_HOSTS на список хостов, на которых вы планируете развернуть приложение.
   5. Если необходимо, измените CSRF_TRUSTED_ORIGINS и INTERNAL_IPS на соответствующие значения для вашей конфигурации.
   6. Настройте параметры SMTP сервера для отправки электронных писем:

      EMAIL_HOST - хост SMTP сервера (например, smtp.gmail.com для Gmail)
      EMAIL_PORT - порт SMTP сервера (обычно 587 для TLS/STARTTLS)
      EMAIL_USE_TLS - установите True для использования TLS/STARTTLS
      EMAIL_HOST_USER - ваш email адрес для авторизации на SMTP сервере
      EMAIL_HOST_PASSWORD - пароль для вашего email аккаунта

   7. Сохраните изменения в файле .env.

## Использование

Перейдите на главную страницу приложения http://localhost:8000.
Введите свой электронный адрес в форму.
Нажмите кнопку "Сгенерировать пароль".
Сгенерированный пароль по желанию можно будет отправить на указанный электронный адрес.

## Структура проекта

app/ - Исходный код Django приложения
docker-compose.yml - Файл конфигурации Docker Compose
.env.example - Пример файла с переменными окружения
