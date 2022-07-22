
from django.db import models
from django.utils.translation import gettext as _


class Employee(models.Model):
    class Meta:
        db_table = 'employee'
        verbose_name = 'employee'
        verbose_name_plural = 'employees'

    first_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("First name"),
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Last name"),
    )
    username = models.CharField(
        max_length=255,
        unique=True,
        blank=True,
        null=True,
        verbose_name=_("Username"),
    )

    phone = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Telefone"),
    )

    street = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Endereço"),
    )

    district = models.CharField(
            max_length=255,
            blank=True,
            null=True,
            verbose_name=_("Bairro"),
        )

    city = models.CharField(
            max_length=255,
            blank=True,
            null=True,
            verbose_name=_("Cidade"),
        )

    Company = models.ForeignKey('controller.Company', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Empresa')

    def __str__(self):
        return self.username
