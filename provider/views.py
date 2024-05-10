from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from rest_framework import generics, serializers
from django_filters.rest_framework import DjangoFilterBackend
from provider.models import Factory, Retail, Entrepreneur
from provider.serializers import FactorySerializer, RetailSerializer, EntrepreneurSerializer


class RetailListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('contact__country', )

    def perform_create(self, serializer):
        supplier_id = serializer.validated_data.get('supplier_id')
        supplier_type = serializer.validated_data.get('supplier_type')

        if supplier_id and supplier_type:
            content_type = ContentType.objects.get_for_id(supplier_type.id)
            model_class = apps.get_model(content_type.app_label, content_type.model)
            try:
                model_instance = model_class.objects.get(pk=supplier_id)
            except model_class.DoesNotExist:
                raise serializers.ValidationError({'supplier_id': 'Неверный идентификатор поставщика'})
            serializer.save()


class RetailRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()


class EntrepreneurListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()

    def perform_create(self, serializer):
        supplier_id = serializer.validated_data.get('supplier_id')
        supplier_type = serializer.validated_data.get('supplier_type')

        if supplier_id and supplier_type:
            content_type = ContentType.objects.get_for_id(supplier_type.id)
            model_class = apps.get_model(content_type.app_label, content_type.model)
            try:
                model_instance = model_class.objects.get(pk=supplier_id)
            except model_class.DoesNotExist:
                raise serializers.ValidationError({'supplier_id': 'Неверный идентификатор поставщика'})
            serializer.save()


class EntrepreneurRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()


class FactoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()


class FactoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
