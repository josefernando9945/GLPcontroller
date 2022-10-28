from django.db import models


class Customer(models.Model):
    objects = None

    class Meta:
        db_table = 'customer'
        verbose_name = 'customer'
        verbose_name_plural = 'customer'

    first_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Nome",
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Sobrenome",
    )

    phone = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Telefone",
    )

    street = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Rua",
    )

    number = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Numero",
    )

    district = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Bairro",
    )

    city = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Cidade",
    )

    def __str__(self):
        return self.first_name
