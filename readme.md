# 365SMS API

**Установка**

**В терминале(Или в командной строке)** ```pip install 365sms```

**Инициализация**

```
from three65smsapi import three65sms

# Это пример, вам нужно подставить вместо 'your api key' свой API ключ(Можно получить тут: https://365sms.ru/account)
client = three65sms(api_key='your api key')
```

**Получение баланса аккаунта**

```
client.getnumbersstatus(country='0', operator='any') # Вместо 0 в country надо подставить id своей страны(Получить тут: https://365sms.ru/api365), в поле operator можно оставить any, но лучше указать оператора(Получить там же где и id страны)
```

**Получение количества доступных номеров**

```
client.getnumbersstatus(country='0', operator='any') # Вместо 0 в country надо подставить id своей страны(Получить тут: https://365sms.ru/api365), в поле operator можно оставить any, но лучше указать оператора(Получить там же где и id страны)
```

**Заказ номера**
```
client.buynumber(service='Сервис', country='ID Страны(Не название)', operator='Оператор')
```

**Изменить статус заказа**

```
client.setnumberstatus(id='id номера(Получаеться при заказе)', status='Статус который примет заказ(id статусов можно найти в документации 365sms(https://365sms.ru/api365))')
```

**Получить статус заказа**

```
client.getnumberstatus(id='id номера(Получаеться при заказе)')
```

**Получить все цены**

```
client.getallprices(service='Сервис', country='ID Страны(Не название)')
```
