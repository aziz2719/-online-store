from django.db import models

class Order(models.Model):
    CHOICES = (
        ('W','Wait'),
        ('M','Order is made'),
        ('R','Rejected'),
    )
    customer = models.ForeignKey('users.Profile', models.SET_NULL, related_name='customer_order', null=True)
    courier = models.ForeignKey('users.Courier', models.SET_NULL, related_name='courier_order', null=True)
    date = models.DateTimeField('Дата заказа', auto_now_add=True)
    total_price = models.DecimalField('Цена', max_digits=10, decimal_places=0)
    address = models.CharField('Адрес доставки', max_length=255)
    status = models.CharField(max_length=100, choices=CHOICES)

class OrderProduct(models.Model):
    good_quantity = models.PositiveSmallIntegerField('Количество товара', default=1) 
    product = models.ForeignKey('products.Product', models.SET_NULL, related_name='prodect_order', null=True)
    order = models.ForeignKey(Order, models.CASCADE, 'product')