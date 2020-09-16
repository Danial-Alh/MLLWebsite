from django import template

register = template.Library()

@register.simple_tag
def get_in_menu_pages():
    from wagtail.core.models import Page
    result = Page.objects.in_menu().all()
    return result