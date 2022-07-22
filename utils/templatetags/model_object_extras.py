import re

from django import template
from django.contrib.admin.utils import label_for_field

register = template.Library()


@register.simple_tag
def model_verbose_name(instance):
    return instance._meta.original_attrs.get("verbose_name").title()


@register.simple_tag
def attribute_verbose_name(value, field):
    if hasattr(value, 'model'):
        value = value.model
    try:
        return label_for_field(field, value._meta.model)
    except:
        try:
            return value._meta.get_field(field).verbose_name.title()
        except:
            return field.title()


@register.simple_tag
def attribute(value, arg):
    """Gets an attribute of an object dynamically from a string name"""
    numeric_test = re.compile("^\d+$")

    if hasattr(value, str(arg)):
        return getattr(value, arg)
    elif hasattr(value, 'has_key') and value.has_key(arg):
        return value[arg]
    elif numeric_test.match(str(arg)) and len(value) > int(arg):
        return value[int(arg)]
    else:
        return arg.title()


@register.filter
def get_type(value):
    return str(type(value))
