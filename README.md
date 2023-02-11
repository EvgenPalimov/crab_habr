## Проект "Крабр круче, чем Хабр!"

## Командная разработка по методологии Agile:Scrum

## Сайт для обучения

### Базовая документация к проекту

Основные системные требования:

* Ubuntu 20.04 LTS
* Python 3.9
* Django 4.1
* Зависимости (Python) из requirements.txt

Сайт для размещения статей на тему IT и Digital технологий. Реализован 
механизм регистрации и авторизации. Имеется личный кабинет с возможностью 
добавления и редактирования статей. Реализован механизм уведомлений, лайков и 
комментариев. Реализована административная панель для управления данными на 
базе стандартной админки Django.

### Установка необходимого ПО

#### Обновляем информацию о репозиториях

```
apt update
```

#### Установка nginx, Git, virtualenv, gunicorn

```
apt install nginx
```

Git

```
apt install git-core
```

virtualenv

```
apt install python3-venv
```

gunicorn

```
apt install gunicorn
```

#### Настраиваем виртуальное окружение

При необходимости, для установки менеджера пакетов pip выполняем команду:

```
apt install python3-pip
```

Создаем и активируем виртуальное окружение:

```
python3 -m venv env
source env/bin/activate
```

Ставим зависимости:

```
pip3 install -r requirements.txt
```

#### Суперпользователь

```
python3 manage.py createsuperuser
```

к примеру (логин/пароль): admin:admin

#### Выполнение миграций и сбор статических файлов проекта

Выполняем миграции:

```
python3 manage.py migrate
```

#### Заполнить базу данных тестовыми данными (необязательно)

```
python3 manage.py fill_db
```

#### Тест запуска

```
python3 manage.py runserver
```

Настроим параметры службы «gunicorn»

```
sudo nano /etc/systemd/system/gunicorn.service

[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=django
Group=www-data
WorkingDirectory=/home/django/crab_habr
ExecStart=/home/django/crab_habr/env/bin/gunicorn --error-logfile "/var/log/gunicorn/error.log" --access-logfile "/var/log/gunicorn/access.log" --workers 3 --bind unix:/home/django/crab_habr/crab_habr.sock crab_habr.wsgi

[Install]
WantedBy=multi-user.target

```

Активирование и запуск сервиса

```
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
sudo systemctl status gunicorn
```

Настройки параметров для nginx

```
sudo nano /etc/nginx/sites-available/crab_habr

server {
  listen 80;
  server_name 81.200.145.185;
  location = /favicon.ico {
    alias /home/django/crab_habr/static/favicon.ico;
  }
  location /static/ {
    root /home/django/crab_habr;
  }
  location /media/ {
    root /home/django/crab_habr;
  }
  location / {
    include proxy_params;
    proxy_pass http://unix:/home/django/crab_habr/crab_habr.sock;
  }
}
```

Перезапускаем службу «nginx»

```
sudo systemctl restart nginx
```

#### Активируем сайт

```
sudo ln -s /etc/nginx/sites-available/crab_habr /etc/nginx/sites-enabled
```

### После этого в браузере можно ввести ip-адрес сервера и откроется проект.
