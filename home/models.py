from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    type_users = (
        (1, "Admin"),
        (2, "Driver"),
        (3, "Customer"),
    )
    phone = models.CharField(max_length=25, null=True, blank=True)
    type = models.IntegerField(default=0, choices=type_users)
    firebase_token = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Order(models.Model):
    STATUS = (
        ('yangi', 'Yangi'),
        ('olindi', 'Olindi'),
        ('yetkazildi', 'Yetkazildi!')
    )
    status = models.CharField(max_length=100, choices=STATUS, default='yangi')
    qayerdan = models.CharField(max_length=1000)
    qayerga = models.CharField(max_length=1000)

    person_count = models.CharField(max_length=100, default=1)
    price = models.IntegerField(default=100000)

    client_phone = models.CharField(max_length=100)
    client_name = models.CharField(max_length=200)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_customer')

    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver', blank=True, null=True)

    def __str__(self):
        return f'{self.qayerdan} => {self.qayerga}'


class ArchiveOrder(models.Model):
    STATUS = (
        ('yangi', 'Yangi'),
        ('olindi', 'Olindi'),
        ('yetkazildi', 'Yetkazildi')
    )
    status = models.CharField(max_length=100, choices=STATUS, default='yangi')
    qayerdan = models.CharField(max_length=1000)
    qayerga = models.CharField(max_length=1000)

    person_count = models.CharField(max_length=100, default=1)
    price = models.IntegerField(default=100000)

    client_phone = models.CharField(max_length=100)
    client_name = models.CharField(max_length=200)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='archorder_customer')

    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='archdriver', blank=True, null=True)

    def __str__(self):
        return f'{self.qayerdan} => {self.qayerga}'


class TempOrder(models.Model):
    STATUS = (
        ('yangi', 'Yangi'),
        ('olindi', 'Olindi')
    )
    status = models.CharField(max_length=100, choices=STATUS, default='yangi')
    qayerdan = models.CharField(max_length=1000)
    qayerga = models.CharField(max_length=1000)

    person_count = models.CharField(max_length=100, default=1)
    price = models.IntegerField(default=100000)

    client_phone = models.CharField(max_length=100)
    client_name = models.CharField(max_length=200)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='temp_order_customer')

    def __str__(self):
        return f'{self.qayerdan} => {self.qayerga}'
