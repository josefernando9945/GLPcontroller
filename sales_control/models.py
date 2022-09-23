from django.db import models

from customer.models import Customer
from product.models import Product, CATEGORY_CHOICES, CATEGORY_OTHER
from utils.models import TimestampMixin


class Sales(TimestampMixin):
    class Meta:
        db_table = "sales"
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Cliente",
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="produto",
    )

    address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Endereço",
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
        verbose_name="Tipo de conta",
    )

    def __str__(self):
        month_year = self.customer




