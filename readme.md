# SHOP (Django)
## О проекте
Проект шаблона интернет магазина

Реализованы следующие функции:

- импорт товаров из 1С
- построение разделов из категорий товаров
- Блог с комментарием
- раздел "Вопросы и ответы"
- добавление в избранное

## Запуск проекта

- создать виртуальное окружение
- скачать репозиторий
- установить зависимости из requirements.txt
- запустить `python manage.py runserver`
(если выдает ошибку ExtUser - сделать миграцию БД: `python manage.py makemigrations` , `python manage.py migrate`)

Использовать данные для входа:
username: **admin**
password: **smart2020**


## Состав проекта

### app: analitycs

- Учет посещения страниц.
- Занесение пользователя в черный список, если он в течении 1 сек делает 5 запросов.

### app: article

Приложение для создания страниц (статических или блога)

- создание типа страниц (новости, страница, блог или прочее)
- комментирование блога
- тэги и разделы

### app: backoffice

Приложение личного кабинета администратора и покупателя.

#### Конструктор подбора освещения
20 августа добавлена функция подбора.
Фунцкия расположена: `backoffice/views.py -> constructor_light`

##### Администратор
+ редактировать товары
+ создавать страницы (article)
+ создавать ответы


##### Покупатель
+ создавать вопросы 
+ размещать заказы
+ добавлять товар в избранное
+ смотреть историю покупок

### app: catalog
Хранение товаров и разделов. Отображение списка товаров, карточки товара, поиск товаров
+ catalog.other_func - импорт из 1С товаров и разделов в базу сайта
 
 
### app: core
Созданы абстрактные модели:

- TimeStampedModel - модель с полями даты создания и даты редактирования
- Term - модель терминов
- NodeModel - модель ноды (страницы)

### app: extuser
Расширение стандартной модели пользователя.
Добавлены дополнительные поля к пользователю:

- тип пользователя (сотрудник | клиент)
- телефон
- аватарка
- избранные товары

### app: q_and_a
Вопросы и ответы для сайта

### app: sales_and_clients
Приложение корзины покупателя и оформление заказа.