from django.db import models, transaction
from django.forms import model_to_dict
from django.utils.text import slugify
from django.utils.translation import gettext as _


class CreateDateTimeMixin(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'), null=True, blank=True)


class UpdateDateTimeMixin(models.Model):
    class Meta:
        abstract = True

    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'), null=True, blank=True)


class ActiveMixin(models.Model):
    class Meta:
        abstract = True

    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))


class TimestampMixin(CreateDateTimeMixin, UpdateDateTimeMixin):
    class Meta:
        abstract = True


class DefaultMixin(models.Model):
    class Meta:
        abstract = True

    default = models.BooleanField(default=False, blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        with transaction.atomic():
            if self.default:
                clazz = self.__class__
                clazz.objects.exclude(pk=self.pk).update(default=False)
            super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)


class TaskMixin(models.Model):
    class Meta:
        abstract = True

    done = models.BooleanField(default=False)
    processing = models.BooleanField(default=False)
    message = models.TextField(default=None, blank=True,
                               null=True)


class ModelDiffMixin(object):
    """
    A model mixin that tracks model fields' values and provide some useful api
    to know what fields have been changed.
    """

    def __init__(self, *args, **kwargs):
        super(ModelDiffMixin, self).__init__(*args, **kwargs)
        self.__initial = self._dict

    @property
    def diff(self):
        d1 = self.__initial
        d2 = self._dict
        diffs = [(k, (v, d2[k])) for k, v in d1.items() if v != d2[k]]
        return dict(diffs)

    @property
    def has_changed(self):
        return bool(self.diff)

    @property
    def changed_fields(self):
        return self.diff.keys()

    def get_field_diff(self, field_name):
        """
        Returns a diff for field if it's changed and None otherwise.
        """
        return self.diff.get(field_name, None)

    def save(self, *args, **kwargs):
        """
        Saves model and set initial state.
        """
        super(ModelDiffMixin, self).save(*args, **kwargs)
        self.__initial = self._dict

    @property
    def _dict(self):
        return model_to_dict(self, fields=[
            field.name for field in self._meta.fields
        ])


class SlugMixin(models.Model):
    class Meta:
        abstract = True

    SLUGIFY_FIELD = None
    EXCLUDE_NAMES = []

    def save(self, *args, **kwargs):
        assert self.SLUGIFY_FIELD, _("You need to specify a field to be the slug")
        # TODO change _ to dead with vars
        assert hasattr(self, self.SLUGIFY_FIELD), _(
            "The field {} need to exists on the model".format(self.SLUGIFY_FIELD)
        )
        slug_field = self._meta.get_field(self.SLUGIFY_FIELD)
        max_length = getattr(slug_field, "max_length", 50)
        if not self.slug:
            original_slug = slugify(getattr(self, self.SLUGIFY_FIELD))[0:max_length]
            self.slug = original_slug
            if self.slug in self.EXCLUDE_NAMES:
                append = "-{}".format(1)
                self.slug = "{}{}".format(original_slug[0 : max_length - len(append)], append)
            model = self._meta.model
            counter = 0

            while model.objects.filter(slug=self.slug).order_by("-id").exists():
                counter += 1
                append = "-{}".format(counter)
                self.slug = "{}{}".format(original_slug[0 : max_length - len(append)], append)
                counter = model.objects.filter(slug=self.slug).order_by("-id").count()

        return super().save(*args, **kwargs)