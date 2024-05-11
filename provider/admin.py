from django.contrib import admin
from django.utils.safestring import mark_safe
from provider.models import Retail, Entrepreneur, Factory, Contact, Product
from provider.serializers import RetailSerializer, EntrepreneurSerializer


class SupplierAdmin(admin.ModelAdmin):
    """Общий класс для представления в административной панели"""
    list_display = (
        'name', 'contact', 'supplier_type', 'supplier_id', 'debt', 'get_supplier_detail_url', 'get_retail_town',
        'get_retail_country')
    list_filter = ('contact__town',)

    def get_retail_country(self, obj):
        # Достаем значение Страны
        return obj.contact.country

    get_retail_country.short_description = 'Страна'

    def get_retail_town(self, obj):
        # Достаем значение город
        return obj.contact.town

    get_retail_town.short_description = 'Город'

    def get_retail_debt(self, obj):
        # Достаем поле с долгом
        return obj.debt

    get_retail_debt.short_description = 'Долг'

    def reset_debt(self, request, queryset):
        # Обнуление долга
        queryset.update(debt=0)

    reset_debt.short_description = 'Обнулить долг'
    # Регистрация действия
    actions = [reset_debt]


class RetailAdmin(SupplierAdmin, admin.ModelAdmin):

    def get_supplier_detail_url(self, obj):
        serializer = RetailSerializer(obj)
        supplier_detail_url = serializer.data['supplier_detail_url']
        return mark_safe(f'<a href="{supplier_detail_url}" target="_blank">Ссылка на поставщика</a>')

    get_supplier_detail_url.short_description = 'Ссылка на поставщика'


class EntrepreneurAdmin(SupplierAdmin, admin.ModelAdmin):

    def get_supplier_detail_url(self, obj):
        serializer = EntrepreneurSerializer(obj)
        supplier_detail_url = serializer.data['supplier_detail_url']
        return mark_safe(f'<a href="{supplier_detail_url}" target="_blank">Ссылка на поставщика</a>')

    get_supplier_detail_url.short_description = 'Ссылка на поставщика'


admin.site.register(Retail, RetailAdmin)
admin.site.register(Entrepreneur, EntrepreneurAdmin)
admin.site.register(Factory)
admin.site.register(Contact)
admin.site.register(Product)
