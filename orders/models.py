from django.db import models


class Courier(models.Model):
    name = models.CharField(max_length=127, verbose_name='имя')
    chat_id = models.IntegerField(primary_key=True, verbose_name='id чата в тг')
    status = models.CharField(max_length=127, choices=(
        ('NOT_ON_SHIFT', 'не на смене'),
        ('READY_FOR_ORDER', 'готов к заказу'),
        ('DELIVERING_ORDER', 'выполняет заказ'),
        ('RETURNING', 'возвращается'),
        ('INACTIVE', 'не активен'),
    ))
    shift_start = models.DateTimeField(null=True, blank=True, verbose_name='начало следующей смены')
    order_finished = models.DateTimeField(null=True, blank=True, verbose_name='последний заказ завершен')


class Client(models.Model):
    name = models.CharField(max_length=127, verbose_name='имя')
    telephone_number = models.CharField(max_length=12, verbose_name='номер телефона')
    address = models.CharField(max_length=255, verbose_name='адрес')


class Order(models.Model):
    number = models.IntegerField(primary_key=True, verbose_name='номер заказа')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент')
    list_of_products = models.TextField(verbose_name='список продуктов')
    cost = models.FloatField(verbose_name='стоимость')
    deadline = models.TimeField(verbose_name='крайнее время доставки')
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE, verbose_name='курьер')
    status = models.CharField(max_length=127, choices=(
        ('NEW', 'новый'),
        ('PREPARED', 'готов'),
        ('ON_THE_WAY', 'доставляется'),
        ('DELIVERED', 'доставлен'),
    ))
    comments = models.TextField(null=True, blank=True, verbose_name='комментарии')
