from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from common.views import TitleMixin


class OrderCreateView(TitleMixin, TemplateView):
    template_name = 'orders/order-create.html'
    title = 'Store - Оформление заказа'