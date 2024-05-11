from rest_framework import serializers

from provider.models import Contact, Product, Factory, Retail, Entrepreneur


class ContactSerializer(serializers.ModelSerializer):
    """Сериализатор для модели контакты"""

    class Meta:
        model = Contact
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для модели продуктов"""

    class Meta:
        model = Product
        fields = '__all__'


class FactorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Завод"""

    class Meta:
        model = Factory
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    """Основной сериализатор для ретейлеров
    supplier_detail_url - добавляется поле со ссылкой поставщика
    retail_town - поле для отображения города ретейлера
    country - оле для отображения страны"""
    supplier_detail_url = serializers.SerializerMethodField()
    retail_town = serializers.CharField(source='contact.town', read_only=True)
    country = serializers.CharField(source='contact.country', read_only=True)

    def get_supplier_detail_url(self, obj):
        """Метод получения ID поставщика. Берется объект, если модель поставщика равна модели объекта, значит ID
        поставщика передается в адресную строку и возвращается значением в поле supplier_detail_url"""
        supplier_model = obj.supplier_type.model
        if supplier_model == 'factory':
            return f"http://localhost:8000/admin/provider/factory/{obj.supplier_id}/change/"
        elif supplier_model == 'entrepreneur':
            return f"http://localhost:8000/admin/provider/entrepreneur/{obj.supplier_id}/change/"
        else:
            return None

    def update(self, instance, validated_data):
        """Переопределяем метод обновления.
        Убираем возможность изменения долго через API запрос"""
        validated_data.pop('debt', None)  # Удаляем поле 'debt' из данных перед обновлением
        return super().update(instance, validated_data)


class RetailSerializer(SupplierSerializer):
    """Сериализатор для модели Розничной сети.
    Наследуемся от SupplierSerializer, перенимаем все изменения"""
    class Meta:
        model = Retail
        fields = '__all__'


class EntrepreneurSerializer(SupplierSerializer):
    """Сериализатор для модели Предпринимателя.
    Переопределение метода get_supplier_detail_url.
    Измененно условие elif и возвращаемая строка."""

    class Meta:
        model = Entrepreneur
        fields = '__all__'

    def get_supplier_detail_url(self, obj):
        supplier_model = obj.supplier_type.model
        if supplier_model == 'factory':
            return f"http://localhost:8000/admin/provider/factory/{obj.supplier_id}/change/"
        elif supplier_model == 'retail':
            return f"http://localhost:8000/admin/provider/retail/{obj.supplier_id}/change/"
        else:
            return None
