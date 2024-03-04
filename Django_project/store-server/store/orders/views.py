from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from orders.forms import OrderForm
from orders.models import Order


class OrderCreateView(TitleMixin, CreateView):
    form_class = OrderForm
    model = Order
    template_name = 'orders/order-create.html'
    title = 'Store - Оформление заказа'
    success_url = reverse_lazy('orders:success')

    def form_valid(self, form):
        form.instance.user_created_order = self.request.user
        return super(OrderCreateView, self).form_valid(form)


class SuccessTemplateView(TitleMixin, TemplateView):
    template_name = 'orders/order-success.html'
    title = 'Store - Спасибо за заказ!'


class OrdersHistoryView(TitleMixin, ListView):
    model = Order
    title = 'Store - Заказы'
    template_name = 'orders/orders.html'
    ordering = '-created'

    def get_queryset(self):
        queryset = super(OrdersHistoryView, self).get_queryset()
        return queryset.filter(user_created_order=self.request.user)


class OrderDetailView(DetailView):
    template_name = 'orders/order.html'
    model = Order

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        context['title'] = f'Store - Заказ #{self.object.id}'
        return context
