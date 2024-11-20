from django.urls import path
from .views import GoodsList
urlpatterns = [
    path('list/', GoodsList.as_view(), name='list')
]