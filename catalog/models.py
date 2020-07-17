import uuid
from django.db import models
from core.models import TimeStampedModel


# Create your models here.
class ProductAttribute(models.Model):
    attr_name = models.CharField('Название атрибута', max_length=200)

    class Meta():
        verbose_name = 'Название атрибута'
        verbose_name_plural = 'Название атрибутов'

    def __str__(self):
        return self.attr_name


class AttributeValue(models.Model):
    attr_name = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE, verbose_name='Имя атрибута')
    attr_value = models.CharField('Значение атрибута', max_length=200)

    class Meta():
        verbose_name = 'Атрибут товара'
        verbose_name_plural = 'Атрибуты товара'

    def __str__(self):
        return f'{self.attr_name}: {self.attr_value}'


class ProductImage(models.Model):
    image = models.ImageField('Фото товара', upload_to='products/%Y/%m/$d', blank=True)

    class Meta():
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товара'


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    title = models.CharField('Категория', max_length=200)
    description = models.TextField('Описание', blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta():
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        if self.parent == None:
            return f'{self.title}'
        else:
            return f'{self.parent} > {self.title}'


class Product(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    sku = models.CharField('Артикул', max_length=200, blank=True)
    barcode = models.CharField('Штрихкод', max_length=40, default='' )
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    price_old = models.DecimalField('Старая цена', max_digits=10, decimal_places=2, blank=True, null=True)
    metrika = models.CharField('Ед.измерения', max_length=200, blank=True, default='Штука')
    quentity = models.IntegerField('Количество', blank=True, null=True)
    categoty = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, )
    attribute = models.ForeignKey(AttributeValue, related_name='attribute_product', on_delete=models.CASCADE, blank=True, null=True, default='')
    image = models.ForeignKey(ProductImage, on_delete=models.SET_NULL, blank=True, null=True)
    rating = models.FloatField('Рейтинг товара', blank=True, null=True)

    class Meta():
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title
