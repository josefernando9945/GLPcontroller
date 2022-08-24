from django.db import models

from product.models import Product
from utils.models import TimestampMixin

CATEGORY_EMPTY = ""
CATEGORY_WATER = "WATER"
CATEGORY_GAS = "GAS"
CATEGORY_OTHER = "OTHER"
CATEGORY_FEE_APP = "APP_FEE"


CATEGORY_CHOICES = [
    (CATEGORY_EMPTY, "----------------"),
    (CATEGORY_WATER, "Conta de Água"),
    (CATEGORY_GAS, "Conta de Gás"),
    (CATEGORY_OTHER, "Outro"),
]


class CostValue(TimestampMixin):
    class Meta:
        db_table = "cost_vaqlue"
        verbose_name = "Valor de Custo"
        verbose_name_plural = "Valores de Custo"

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Condominio",
    )

    description = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Descrição da Conta",
    )
    value = models.DecimalField(
        max_length=255,
        blank=True,
        null=True,
        max_digits=12,
        decimal_places=2,
        verbose_name="valor",
    )

    purchase_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de vencimento",
    )

    category = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        choices=CATEGORY_CHOICES,
        verbose_name="Tipo de conta",
    )

    def __str__(self):
        month_year = self.purchase_date.strftime("%b/%Y")

        description = f"{self.get_category_display()} - {month_year}"
        if self.category == CATEGORY_OTHER and self.description:
            description = f"{self.description} - {month_year}"
        return description


class SaleValue(TimestampMixin):
    class Meta:
        db_table = "sale_value"
        verbose_name = "Valor de Venda"
        verbose_name_plural = "Valores de Venda"

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Condominio",
    )

    description = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Descrição da Conta",
    )
    value = models.DecimalField(
        max_length=255,
        blank=True,
        null=True,
        max_digits=12,
        decimal_places=2,
        verbose_name="valor",
    )

    purchase_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de vencimento",
    )

    category = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        choices=CATEGORY_CHOICES,
        verbose_name="Tipo de conta",
    )

    def __str__(self):
        month_year = self.purchase_date.strftime("%b/%Y")

        description = f"{self.get_category_display()} - {month_year}"
        if self.category == CATEGORY_OTHER and self.description:
            description = f"{self.description} - {month_year}"
        return description



class ProfitMargin(TimestampMixin):
    class Meta:
        db_table = "profit_margin"
        verbose_name = "Margem de Lucro"
        verbose_name_plural = "Margem de Lucro"

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Condominio",
    )

    cost_value = models.ForeignKey(
        CostValue,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Condominio",
    )

    sale_value = models.ForeignKey(
        SaleValue,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Condominio",
    )

    percent = models.DecimalField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Descrição da Conta",
    )
    value = models.DecimalField(
        max_length=255,
        blank=True,
        null=True,
        max_digits=12,
        decimal_places=2,
        verbose_name="valor",
    )


    def __str__(self):
        value = self.value

