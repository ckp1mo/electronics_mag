from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from rest_framework import generics, serializers
from django_filters.rest_framework import DjangoFilterBackend
from provider.models import Factory, Retail, Entrepreneur
from provider.permissions import IsActiveUser
from provider.serializers import FactorySerializer, RetailSerializer, EntrepreneurSerializer


class RetailListCreateAPIView(generics.ListCreateAPIView):
    """Совмещенное представление для создания и просмотра Розничных сетей
    GET-запрос для просмотра всех ретейлеров, POST-запрос на создание объекта.
    Присутствует фильтрация по стране.
    Права доступа только для авторизованных и активных пользователей."""
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('contact__country', )
    permission_classes = [IsActiveUser]

    def perform_create(self, serializer):
        """Переопределенный метод создания гарантирует, что созданный объект будет иметь существующий ID поставщика"""
        # Достаем пару полей из валидированных данных
        supplier_id = serializer.validated_data.get('supplier_id')  # Указанный ID поставщика
        supplier_type = serializer.validated_data.get('supplier_type')  # Указанный тип поставщика, объект ContentType

        if supplier_id and supplier_type:
            # Получаем указанный тип ContentType по его ID
            content_type = ContentType.objects.get_for_id(supplier_type.id)
            # Получаем класс модели по его имени и метке приложения
            model_class = apps.get_model(content_type.app_label, content_type.model)
            try:
                # Попытка получить объект модели поставщика
                model_instance = model_class.objects.get(pk=supplier_id)
            except model_class.DoesNotExist:
                raise serializers.ValidationError({'supplier_id': 'Неверный идентификатор поставщика'})
            serializer.save()


class RetailRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()
    permission_classes = [IsActiveUser]

    def perform_update(self, serializer):
        """Переопределенный метод создания гарантирует, что обновляемый объект будет иметь существующий ID поставщика"""
        # Достаем пару полей из валидированных данных
        supplier_id = serializer.validated_data.get('supplier_id')  # Указанный ID поставщика
        supplier_type = serializer.validated_data.get('supplier_type')  # Указанный тип поставщика, объект ContentType

        if supplier_id and supplier_type:
            # Получаем указанный тип ContentType по его ID
            content_type = ContentType.objects.get_for_id(supplier_type.id)
            # Получаем класс модели по его имени и метке приложения
            model_class = apps.get_model(content_type.app_label, content_type.model)
            try:
                # Попытка получить объект модели поставщика
                model_instance = model_class.objects.get(pk=supplier_id)
            except model_class.DoesNotExist:
                raise serializers.ValidationError({'supplier_id': 'Неверный идентификатор поставщика'})
            serializer.save()


class EntrepreneurListCreateAPIView(RetailListCreateAPIView, generics.ListCreateAPIView):
    """Наследуемся от RetailListCreateAPIView. Сохраняем переопределнный метод, фильтр и права доступа."""
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()


class EntrepreneurRetrieveUpdateDestroyAPIView(RetailRetrieveUpdateDestroyAPIView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()
    permission_classes = [IsActiveUser]


class FactoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [IsActiveUser]


class FactoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [IsActiveUser]
