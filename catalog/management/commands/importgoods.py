from django.core.management.base import BaseCommand, CommandError
import io
import uuid
import lxml.etree as ET
import requests
from slugify import slugify
from .models import Category, Product

goods = dict()
url_import = 'http://migen.beget.tech/cml/import0_1.xml'
url_offers = 'http://migen.beget.tech/cml/offers0_1.xml'

content = requests.get(url_import).content  # контент с товаром и группами
content_price = requests.get(url_offers).content  # контент с ценами

tree = ET.parse(io.BytesIO(content))  # дерево с товаром и группами
tree_price = ET.parse(io.BytesIO(content_price))  # дерево с ценами


menu = []  # словарь групп

nms = {'ns': 'urn:1C.ru:commerceml_2'}


class Command(BaseCommand):
    help = 'Add goods from 1C to db shop'

    def add_arguments(self, parser):
        parser.add_argument('good_ids', nargs='+', type=int)

    def handle(self, *args, **options):

        '''формирую список групп'''
        grups = tree.find('ns:Классификатор', nms)
        for i in grups.findall('ns:Группы/ns:Группа', nms):
            id = i.find('ns:Ид', nms).text
            name = i.find('ns:Наименование', nms).text
            x_slug = slugify(name)
            x = {'id': id, 'name': name, 'slug': x_slug, 'parent': 0}
            menu.append(x)
            for j in i.findall('ns:Группы/ns:Группа', nms):
                id = j.find('ns:Ид', nms).text
                name = f"{j.find('ns:Наименование', nms).text}"
                y_parent = i.find('ns:Ид', nms).text
                y_slug = slugify(name)
                y = {'id': id, 'name': name, 'parent': y_parent, 'slug': y_slug}
                menu.append(y)

        '''формирую список товаров'''
        for good in tree.findall('ns:Каталог/ns:Товары/ns:Товар', nms):
            id_good = good.find('ns:Ид', nms).text
            name_good = good.find('ns:Наименование', nms).text
            bar_good = good.xpath('ns:Штрихкод', namespaces=nms)
            '''исправление ошибки при парсинге штрихкода, почему-то у штрихкода пропадает метод .text'''
            for code in bar_good:
                bar_code = int(code.text)
            article = good.find('ns:Артикул', nms).text
            if not article:
                article = 'н/д'
            grup_good = good.find('ns:Группы/ns:Ид', nms).text
            goods[id_good] = {
                'группа': grup_good,
                'Название товара': name_good,
                'Артикул': article,
                'Штрихкод': bar_code,
                'Единица измерения': '',
                'price': '',
                'quentity': '',
            }

        price = tree_price.findall('ns:ПакетПредложений/ns:Предложения/ns:Предложение', nms)
        for pce in price:
            cost = pce.find('ns:Цены/ns:Цена/ns:ЦенаЗаЕдиницу', nms).text
            currency = pce.find('ns:Цены/ns:Цена/ns:Валюта', nms).text
            quentity = pce.find('ns:Количество', nms).text
            pce_id = pce.find('ns:Ид', nms).text
            metrika = pce.find('ns:БазоваяЕдиница', nms).get('НаименованиеПолное')
            goods[pce_id]['Единица измерения'] = metrika
            goods[pce_id]['price'] = int(cost)
            goods[pce_id]['quentity'] = int(quentity)

        for i in range(len(menu)):
            if menu[i]['parent']:
                pr = Category.objects.get(id=uuid.UUID(menu[i]['parent']).hex)
                Category.objects.create(title=menu[i]['name'], id=menu[i]['id'], slug=menu[i]['slug'],
                                        parent=pr)
            else:
                Category.objects.create(title=menu[i]['name'], id=menu[i]['id'], slug=menu[i]['slug'])

        i = 1


        for key in goods.keys():
            cat = Category.objects.get(id=goods[key]['группа'])
            product_slug = f"{slugify(goods[key]['Название товара'])}-{str(i)}"
            Product.objects.create(title=goods[key]['Название товара'], id=key,
                                   sku=goods[key]['Артикул'], barcode=goods[key]['Штрихкод'],
                                   price=goods[key]['price'], categoty=cat, slug=product_slug,
                                   quentity=goods[key]['quentity'])
            i += 1



        self.stdout.write(self.style.SUCCESS('Successfully add "%s" goods' % len(goods)))