Market API

Интернет-магазин продуктов с различным функционалом. 

Ознакомиться с подробной документацией о методах API можно по следующей ссылке:
<host>:<port>/api/schema/swagger-ui/

**Функционал**


*Категории и Подкатегории товаров:*

Возможность создания, редактирования и удаления категорий и подкатегорий товаров в админке.
Категории и подкатегории обязательно имеют наименование, slug-имя и изображение.
Подкатегории связаны с родительской категорией.


*Эндпоинт для просмотра всех категорий с подкатегориями:*

Реализован эндпоинт для просмотра всех категорий с подкатегориями с предусмотренной пагинацией.


*Продукты:*

Возможность добавления, изменения и удаления продуктов в админке.
Продукты относятся к определенной подкатегории или категории, имеют наименование, slug-имя, изображение в 3-х размерах, цену.


*Эндпоинт вывода продуктов с пагинацией:*

Реализован эндпоинт для вывода продуктов с пагинацией. Каждый продукт в выводе содержит поля: наименование, slug, категория, цена, список изображений.


*Корзина:*

Эндпоинты для добавления, изменения (изменение количества), удаления продукта в корзине.
Эндпоинт вывода состава корзины с подсчетом количества товаров и суммы стоимости товаров в корзине.
Возможность полной очистки корзины.


*Авторизация:*

Реализована авторизация по токену.
Операции по эндпоинтам категорий и продуктов могут осуществлять любые пользователи.
Операции по эндпоинтам корзины могут осуществлять только авторизированные пользователи и только со своей корзиной.


*Технологии*

Данный проект реализован на основе Django и Django REST framework. Для хранения данных используется база данных SQLite3. Авторизация пользователей осуществляется по токену.


*Настройка проекта*

Клонировать репозиторий:
git clone <URL репозитория>

Создать и активировать виртуальное окружение:
python -m venv venv
source venv/bin/activate

Установить зависимости:
pip install -r requirements.txt

Применить миграции:
python manage.py migrate

Создать суперпользователя:
python manage.py createsuperuser

Запуск сервера
Для запуска сервера выполните следующую команду:
python manage.py runserver

После запуска сервера вы сможете обращаться к API по адресу http://127.0.0.1:8000/.

