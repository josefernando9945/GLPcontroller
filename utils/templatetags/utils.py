import datetime
import json
import locale
import re

from django import template
from django.utils.safestring import mark_safe

# locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
register = template.Library()


@register.simple_tag
def define(val=None):
    return val


@register.filter()
def currency(value):
    return locale.currency(value, grouping=True)


@register.filter()
def str_to_list(str):
    try:
        result = json.loads(mark_safe("{'result':" + str + "}").replace("\'", "\""))
        return result.get("result")
    except:
        return []


@register.filter()
def str_to_dict(data):
    if isinstance(data, dict):
        return data
    try:
        return json.loads(data.replace("'", "\""))
    except:

        return {}


@register.filter()
def money(value):
    try:
        return '${:,.2f}'.format(float(value))
    except:
        return "$0,00"


@register.filter(name='field_type')
def field_type(field):
    return field.field.widget.__class__.__name__


@register.filter(name='add_style')
def add_style(value, arg):
    return value.as_widget(attrs={'style': arg})


@register.filter
def to_char(value):
    return chr(98 - value)


@register.filter(name='filter_queryset')
def filter_queryset(qs, value, arg):
    data = {
        value: arg
    }
    return qs.filter(**data)


@register.filter
def next(some_list, current_index):
    """
    Returns the next element of the list using the current index if it exists.
    Otherwise returns an empty string.
    """
    try:
        return some_list[int(current_index) + 1]  # access the next element
    except:
        return ''  # return empty string in case of exception


@register.filter
def previous(some_list, current_index):
    """
    Returns the previous element of the list using the current index if it exists.
    Otherwise returns an empty string.
    """
    try:
        return some_list[int(current_index) - 1]  # access the previous element
    except:
        return ''  # return empty string in case of exception


@register.simple_tag
def set(val):
    return val


@register.filter
def multiply(value, arg):
    return value * arg


@register.simple_tag
def profile_picture_url(user):
    if user:
        if not user.picture:
            return f"https://ui-avatars.com/api/?name={user.name}&size=512&background=7c5ffa&color=FFF"
        return user.picture.url
    return f"https://ui-avatars.com/api/?name=nova instancia&size=512&background=7c5ffa&color=FFF"

@register.filter()
def youtube_embed(url):
    if not '/embed/' in url:
        url = url.replace('/watch?v=', '/embed/')
    html = f"<div class='embed-container'><iframe src='{url}' frameborder='0' allowfullscreen></iframe></div>"
    return html


@register.filter()
def get_invite(token):
    from invite.models import Invite
    token = Invite.objects.filter(pk=token).first()
    return token