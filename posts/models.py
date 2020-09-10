from django.db import models
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core.blocks import RichTextBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtailstreamforms.blocks import WagtailFormBlock

from wagtailstreamforms.models import AbstractFormSetting


class AdvancedFormSetting(AbstractFormSetting):
    to_address = models.EmailField(default="d@d.com")


class PostPage(Page):
    body = StreamField(
        [
            ('content', RichTextBlock()),
            ('form', WagtailFormBlock())
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]
