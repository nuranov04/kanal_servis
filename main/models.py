from django.db import models


class Order(models.Model):
    order_number = models.IntegerField()
    amount_dollar = models.IntegerField()
    amount_rub = models.IntegerField()
    deadline = models.DateField()

    def __str__(self):
        return f"{self.id}--{self.amount_rub}"

    class Meta:
        ordering = ('id',)
