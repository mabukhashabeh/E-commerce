from django import template
from ..models import *
register = template.Library()


@register.simple_tag
def get_total_orders():
    """
    this method return total numbers of orders
    :return:
    """
    return Order.objects.count()


@register.inclusion_tag('home.html')
def get_all_category():
    """

    :return:
    """
    categories = Category.objects.all()
    return {'categories': categories}

