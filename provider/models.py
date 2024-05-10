from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Contact(models.Model):
    # Поля модели контакты
    email = models.EmailField(unique=True, verbose_name='Email')
    country = models.CharField(max_length=70, verbose_name='Страна')
    town = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=200, verbose_name='Улица')
    house_num = models.CharField(max_length=10, verbose_name='Номер дома')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Product(models.Model):
    # Поля для модели Продукт
    product_name = models.CharField(max_length=100, unique=True, verbose_name='Название продукта')
    product_model = models.CharField(max_length=100, verbose_name='Модель')
    date_at = models.DateField(auto_now_add=True, verbose_name='Дата выпуска')

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Factory(models.Model):
    # Поля модели Завод
    name = models.CharField(max_length=50, unique=True, verbose_name='Название завода')
    # Связь с моделью Contact
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name='Контакты')
    # Связь с моделью Product
    product = models.ManyToManyField(Product, related_name='factories',
                                     verbose_name='Продукт')
    date_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.name} - {self.contact}"

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'


class Retail(models.Model):
    # Поля для модели Розичной сети
    name = models.CharField(max_length=50, unique=True, verbose_name='Название сети')
    # связь с моделью Contact
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, verbose_name='Контакты')
    # связь с моделью Product
    product = models.ManyToManyField(Product, related_name='retails', verbose_name='Продукты', blank=True)
    # Выбор поставщика, связь с моделью Factory или Entrepreneur
    supplier_type = models.ForeignKey(ContentType, limit_choices_to=models.Q(app_label='provider',
                                                                             model__in=['factory', 'entrepreneur']),
                                      on_delete=models.CASCADE, verbose_name='Поставщик')
    supplier_id = models.PositiveIntegerField()
    supplier = GenericForeignKey('supplier_type', 'supplier_id')
    # связь с моделью Debt
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Сумма долга')
    date_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.name} - {self.contact}, {self.supplier}"

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'


class Entrepreneur(models.Model):
    # Поля модели Предпринимателя
    name = models.CharField(max_length=50, unique=True, verbose_name='Предприниматель')
    # связь с моделью Contact
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name='Контакты')
    # связь с моделью Product
    product = models.ManyToManyField(Product, related_name='entrepreneurs', verbose_name='Продукты', blank=True)
    # Выбор поставщика, связь с моделью Factory или Retail
    supplier_type = models.ForeignKey(ContentType,
                                      limit_choices_to=models.Q(app_label='provider', model__in=['factory', 'retail']),
                                      on_delete=models.CASCADE, verbose_name='Поставщик')
    supplier_id = models.PositiveIntegerField()
    supplier = GenericForeignKey('supplier_type', 'supplier_id')
    # связь с моделью Debt
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Сумма долга')
    date_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.name} - {self.contact}, {self.supplier}"

    class Meta:
        verbose_name = 'Предприниматель'
        verbose_name_plural = 'Предприниматели'
