from django.db import models

from company.models import Company
from utils.models import TimestampMixin

CATEGORY_EMPTY = ""
CATEGORY_ENERGY = "ENERGY"
CATEGORY_WATER = "WATER"
CATEGORY_GAS = "GAS"
CATEGORY_ADMINISTRATION_FEE = "ADMINISTRATION_FEE"
CATEGORY_CLEANING_FEE = "CLEANING_FEE"
CATEGORY_RESERVE_FUND = "RESERVE_FUND"
CATEGORY_OTHER = "OTHER"
CATEGORY_FEE_APP = "APP_FEE"


CATEGORY_CHOICES = [
    (CATEGORY_EMPTY, "----------------"),
    (CATEGORY_ENERGY, "Conta de Energia"),
    (CATEGORY_WATER, "Conta de Água"),
    (CATEGORY_GAS, "Conta de Gás"),
    (CATEGORY_ADMINISTRATION_FEE, "Taxa de Administração"),
    (CATEGORY_CLEANING_FEE, "Taxa de Limpeza"),
    (CATEGORY_RESERVE_FUND, "Fundo de Reserva"),
    (CATEGORY_OTHER, "Outro"),
]


class Product(TimestampMixin):
    class Meta:
        db_table = "product"
        verbose_name = "product"
        verbose_name_plural = "products"

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Empresa",
    )

    description = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Descrição da Produto",
    )
    value = models.DecimalField(
        max_length=255,
        blank=True,
        null=True,
        max_digits=12,
        decimal_places=2,
        verbose_name="valor",
    )

    category = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        choices=CATEGORY_CHOICES,
        verbose_name="Categoria",
    )

    def __str__(self):
        return f'{self.description}'


