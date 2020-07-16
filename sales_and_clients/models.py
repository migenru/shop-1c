from django.db import models


# Create your models here.

class ShippingAddress(models.Model):
    zipcode = models.IntegerField('Индекс', blank=True, null=True)
    city = models.CharField('Город', max_length=200)
    address = models.CharField('Адрес', max_length=200, help_text='улица, дом (аппартаменты)')


class Client(models.Model):
    user = models.OneToOneField('extuser.ExtUser', on_delete=models.CASCADE, verbose_name='Покупатель')
    shipping = models.OneToOneField(ShippingAddress, on_delete=models.CASCADE, verbose_name='Адрес доставки')

    def __str__(self):
        return f'{self.extuser.ExtUser.first_name} {self.extuser.ExtUser.last_name} - {self.extuser.ExtUser.user_type}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class CartItem(models.Model):
    product = models.OneToOneField('catalog.Product', on_delete=models.DO_NOTHING, verbose_name='Товар')
    quentity = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return f'{self.product.title} - {self.quentity} шт.'


class Cart(models.Model):
    client = models.OneToOneField(Client, on_delete=models.DO_NOTHING)
    card_item = models.ForeignKey(CartItem, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk}: {self.client}'


class Order(models.Model):
    DELIVERY = [
        ('SERVICE', 'Службой доставки'),
        ('PICKUP', 'Самовывовозом из магазина'),
    ]
    METHOD_PAID = [
        ('CASH', 'Наличными при получении'),
        ('ONLINE', 'Онлайн, картой на сайте'),
        ('INVOICE', 'Счет, банковским платежом'),
    ]
    ORDER_STATUS = [
        ('CANCEL',' Отменен'),
        ('WAIT',' В ожидании оплаты'),
        ('PROCESS',' Обработка заказа'),
        ('RETURN',' Возврат товара'),
        ('COMPLETED',' Выполнен'),
        ('GOING',' Товар собирается'),
        ('SEND',' Товар отправлен'),
    ]
    order_date = models.DateTimeField(auto_now_add=True)
    client = models.OneToOneField(Client, on_delete=models.DO_NOTHING)
    cart = models.OneToOneField(Cart, on_delete=models.DO_NOTHING)
    total_cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Итого', blank=True)
    order_notes = models.TextField('Примечание к заказу', )
    delivery = models.CharField(verbose_name='Способ забора товара', choices=DELIVERY, max_length=7, default='SERVICE')
    shipping = models.OneToOneField(ShippingAddress, on_delete=models.CASCADE, verbose_name='Адрес доставки')
    method_paid = models.CharField(verbose_name='Метод оплаты', choices=METHOD_PAID, max_length=7, default='ONLINE')
    order_ispaid = models.BooleanField(verbose_name='Стату оплаты заказа', default=False)
    order_status = models.CharField(verbose_name='Статус заказа', max_length=9, default='WAIT',)

    def __str__(self):
        return f'{self.pk}: {self.client}, Итого: {self.total_cost}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
