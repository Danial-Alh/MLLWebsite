from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page, Site

# Create your models here.


class SinglePage(Page):
    def get_template(self, request, *args, **kwargs):
        template = "main_pages/{}.html".format(self.slug)
        print(template)
        return template