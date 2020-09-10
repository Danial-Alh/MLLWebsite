from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtailstreamforms.blocks import WagtailFormBlock


class PostPage(Page):
    content = StreamField(
        [
            ('form', WagtailFormBlock())
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [

        StreamFieldPanel('content')
    ]
