from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Имя'
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )
    price = models.IntegerField(
        default=0,
        verbose_name='Цена'
    )

    def __str__(self):
        return self.name
