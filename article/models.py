from django.db import models

from core.models import NodeModel, Term


# Create your models here.

class TagArticle(Term):
    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class TermArticle(Term):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.SET_NULL)

    def __str__(self):
        if self.parent == None:
            return f'{self.name}'
        else:
            return f'{self.parent} > {self.name}'

    class Meta():
        verbose_name = 'Раздел сайта'
        verbose_name_plural = 'Разделы сайта'


class TypeArticle(models.Model):
    name = models.CharField('Название типа', max_length=100, unique=True)
    description = models.TextField('Описание типа', blank=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Тип записи'
        verbose_name_plural = 'Типы записей'


class Article(NodeModel):
    tag = models.ManyToManyField(TagArticle, verbose_name='Тег')
    term = models.ManyToManyField(TermArticle, verbose_name='Раздел записи')
    type = models.OneToOneField(TypeArticle, on_delete=models.CASCADE, verbose_name='Тип записи')

    class Meta():
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
