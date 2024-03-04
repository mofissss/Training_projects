from random import choice

from django.db import models

from products.models import Basket
from users.models import User


class Order(models.Model):
    class Status(models.IntegerChoices):
        CREATED = 0, 'Создан'
        PAID = 1, 'Оплачен'
        ON_THE_WAY = 2, 'В пути'
        DELIVERED = 3, 'Доставлено'

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=256)
    delivery_address = models.CharField(max_length=256)
    basket_history = models.JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)
    user_created_order = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.PositiveIntegerField(choices=Status.choices, default=Status.CREATED)

    def __str__(self):
        return f'Order #{self.id} - {self.first_name} {self.last_name}'

    def update_after_payment(self):
        baskets = Basket.objects.filter(user=self.user_created_order)
        self.basket_history = {
            'purchased_items': [basket.de_json() for basket in baskets],
            'total_sum': float(baskets.total_sum())
        }
        baskets.delete()

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.update_after_payment()
        self.status = 1 if choice([True, False]) else 0
        return super(Order, self).save()
