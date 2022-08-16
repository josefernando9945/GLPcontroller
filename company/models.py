import os

from django.db import models


class Company(models.Model):

    objects = None

    class Meta:
        db_table = 'company'
        verbose_name = 'company'
        verbose_name_plural = 'companys'

    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name='Nome da empresa',
    )

    phone = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Telefone",
    )

    # picture = models.ImageField(
    #     verbose_name="Foto do Perfil",
    #     upload_to=os.path.join("company/profile"),
    #     null=True,
    #     blank=True
    # )

    street = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Rua',
    )

    number = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        verbose_name='Numero',
    )

    district = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Bairro',
    )

    city = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Cidade',
    )

    state = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Estado',
    )

    cep = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        verbose_name='Cep',
    )

    user = models.ForeignKey('account.User', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Usuario')

    def __str__(self):
        return f'{self.name}'
