from django.db import models


class Item(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )
    price = models.IntegerField(
        verbose_name='Цена'
    )

    def __str__(self):
        return self.name
