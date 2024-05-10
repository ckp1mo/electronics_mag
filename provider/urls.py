from django.urls import path

from provider.apps import ProviderConfig
from provider.views import RetailListCreateAPIView, FactoryListCreateAPIView, RetailRetrieveUpdateDestroyAPIView, \
    EntrepreneurRetrieveUpdateDestroyAPIView, EntrepreneurListCreateAPIView, FactoryRetrieveUpdateDestroyAPIView

app_name = ProviderConfig.name


urlpatterns = [
    path('retail-list-create/', RetailListCreateAPIView.as_view()),
    path('retail-det-upd-del/<int:pk>/', RetailRetrieveUpdateDestroyAPIView.as_view()),
    path('entr-list-create/', EntrepreneurListCreateAPIView.as_view()),
    path('entr-det-upd-del/<int:pk>/', EntrepreneurRetrieveUpdateDestroyAPIView.as_view()),
    path('factory-list-create/', FactoryListCreateAPIView.as_view()),
    path('factory-det-upd-del/<int:pk>/', FactoryRetrieveUpdateDestroyAPIView.as_view()),
]
