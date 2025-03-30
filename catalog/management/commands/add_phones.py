from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        categ_name, _ = Category.objects.get_or_create(name='Мобильные телефоны')

        phones = [
            {'name': 'Samsung',
             'description': 'Последние флагманы Samsung',
             'price': 180000,
             'created_at': '2025-01-01',
             'updated_at': '2025-01-01',
             'category': categ_name},
            {'name': 'IPhone',
             'description': 'Топовые айфоны PRO MAX',
             'price': 210000,
             'created_at': '2024-12-12',
             'updated_at': '2024-12-12',
             'category': categ_name},
            {'name': 'Poco',
             'description': 'Лучшие телефоны из Азии',
             'price': 90000,
             'created_at': '2025-02-02',
             'updated_at': '2025-02-02',
             'category': categ_name}
        ]

        for phone in phones:
            product, created = Product.objects.get_or_create(**phone)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Продукт успешно добавлен: {product.name}'))
            else:
                self.stdout.write(
                    self.style.WARNING(f'Такой продукт уже существует: {product.name}'))
