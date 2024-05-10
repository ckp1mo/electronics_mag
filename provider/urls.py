from django.urls import path

from provider.apps import ProviderConfig
from provider.views import RetailListCreateAPIView, FactoryListCreateAPIView, RetailRetrieveUpdateDestroyAPIView, \
    EntrepreneurRetrieveUpdateDestroyAPIView, EntrepreneurListCreateAPIView, FactoryRetrieveUpdateDestroyAPIView

app_name = ProviderConfig.name


urlpatterns = [
    # CRUD для модели Retail
    path('retail-list-create/', RetailListCreateAPIView.as_view(), name='retail-list-create'),
    path('retail-det-upd-del/<int:pk>/', RetailRetrieveUpdateDestroyAPIView.as_view(), name='retail-det-upd-del'),
    # CRUD для модели Entrepreneur
    path('entr-list-create/', EntrepreneurListCreateAPIView.as_view(), name='entr-list-create'),
    path('entr-det-upd-del/<int:pk>/', EntrepreneurRetrieveUpdateDestroyAPIView.as_view(), name='entr-det-upd-del'),
    # CRUD для модели Factory
    path('factory-list-create/', FactoryListCreateAPIView.as_view(), name='factory-list-create'),
    path('factory-det-upd-del/<int:pk>/', FactoryRetrieveUpdateDestroyAPIView.as_view(), name='factory-det-upd-del'),
]
