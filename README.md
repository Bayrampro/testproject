после того как вы загрузили мой проект с github вы должны создать виртуальное окружение

в командной строке введите:
python -m venv venv

проект должен выглядеть таким образом:
   testproject
       testproject
       venv
       MySQL settings

после установите необходимые пакеты с репозитория pypi:
pip install -r requirements.txt

сейчас в настройках проекта (в settings.py) установлен настройки MySQL:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

но вы также можете разкомментировать СУБД по умолчанию в джанго sqlite3

я скачал все таки не без труда MySQL на свой компютер и вы убедитесь что у вас установлен

далее зайдите через терминал в оболочку MySQL
mysql -u root -p

Создайте нового пользователя и назначьте ему пароль с помощью следующей команды:
CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';

CREATE DATABASE database CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

Выполните миграции Django, чтобы создать необходимые таблицы в базе данных MySQL:
python manage.py migrate

можете запустить сервер Django
python manage.py runserver
