from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext as _

from utils.models import TimestampMixin

ADMINISTRATOR = 'administrator'
USER = 'user'

PERMISSION_CHOICE = [
    (ADMINISTRATOR, 'Adminiatrador'),
    (USER, 'Usuario'),
]

class User(AbstractBaseUser, PermissionsMixin, TimestampMixin):
    class Meta:
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = 'users'


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

    is_staff = models.BooleanField(
        _('Is Staff'),
        default=False,
    )

    phone = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Telefone"),
    )
    email = models.EmailField(max_length=255, unique=True, verbose_name=_("Email"))

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


