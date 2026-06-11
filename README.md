Създаваме директория за проекта mkdir my_project след това влизаме в нея cd my_project Създаваме виртуална среда py -m venv venv Активирайте виртуалната среда: venv\Scripts\activate след това инсталираме django в активирана виртуална среда pip install django ъпгрейдваме pip python.exe -m pip install --upgrade pip Проверяваме инсталацията python -m django --version за картинки трябва да се инсталира Pillow pip install Pillow Инсталираме Django Rest Framework: Това позволява да се отдели сървъра от фронтенд интерфейса pip install djangorestframework pip install django-crispy-forms pip install crispy-bootstrap5 създаваме нашия сайт django-admin startproject travel_platform src влизаме cd src
там се намира файла manage.py първо правим миграция за admin, auth, contenttypes, sessions. python manage.py migrate след което създаваме superuser за админпанела python manage.py createsuperuser Разделяне на логиката по функционалности като приложенията ги стздаваме по следния начин python manage.py startapp posts

accounts за за потребителски профили, логин/регистрация posts постове gallery за снимки categories градове, държави, тип пътуване comments за за коментари под постове ratings рейтинг

трябва да ги добавим в settings.py в INSTALLED_APPS което се намира в src/travel_platform/settings.py след което във всяко приложение във файла models.py описваме класовете за таблиците в базата данни urls.py маршрутите admin.py класове за админ панела forms.py класове за форми views.py класове с логиката на Django приложението. свързват базата данни (Models) с потребителския интерфейс Templates. темплейтите на всяко приложение са в папка templates със своите имена posts и т.н base.html го създаваме в главния проект src в папка templates в този файл е header и footer в папката static са js и css

след като си напишем класовете python manage.py makemigrations python manage.py migrate

използваме SQLite не изисква инсталирането на никакви допълнителни пакети. Настройките за нея се намират във файла src/travel_platform/settings.py

Проектът се пуска като се стартира сървъра от терминал папка src

python manage.py runserver
http://127.0.0.1:8000/admin/ появява се админ панел http://127.0.0.1:8000 появява се админ панел
