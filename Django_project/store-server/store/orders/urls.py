from django.urls import path

from orders.views import (OrderCreateView, OrderDetailView, OrdersHistoryView,
                          SuccessTemplateView)

app_name = 'orders'

urlpatterns = [
    path('create', OrderCreateView.as_view(), name='create'),
    path('', OrdersHistoryView.as_view(), name='history'),
    path('success', SuccessTemplateView.as_view(), name='success'),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order')
]
