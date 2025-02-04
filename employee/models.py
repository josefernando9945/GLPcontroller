
from django.db import models


class Employee(models.Model):
    class Meta:
        db_table = 'employee'
        verbose_name = 'employee'
        verbose_name_plural = 'employees'

    first_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="First name",
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Last name",
    )
    username = models.CharField(
        max_length=255,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Username",
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

    Company = models.ForeignKey('company.Company', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Empresa')

    def __str__(self):
        return self.username
