from django import template
from ..models import *

register = template.Library()


@register.inclusion_tag('main/categories.html')
def show_categories():
    cats=[]

    #this make a nested arrays for catalog

    return {
        "cats":cats
    }