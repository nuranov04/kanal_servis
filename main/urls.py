from django.urls import path

from main.views import OrderListView

urlpatterns = [
    path('', OrderListView.as_view(), name='orders')
]
