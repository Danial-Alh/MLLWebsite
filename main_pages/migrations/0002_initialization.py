from django.contrib.contenttypes.models import ContentType
from wagtail.core.models import Page, Site
from django.db import migrations, DatabaseError, transaction
from main_pages.models import SinglePage


def initialize_model(apps, schema_editor):
    root_page = Page.get_first_root_node()

    with transaction.atomic():
        for page in Page.objects.child_of(root_page):
            page.delete()
    root_page = Page.get_first_root_node()

    singlepage_content_type = ContentType.objects.get_for_model(SinglePage)

    homepage = SinglePage(title="Machine Learning Lab", slug='home', show_in_menus=False,
                          content_type=singlepage_content_type)
    root_page.add_child(instance=homepage)

    homepage.add_child(instance=SinglePage(title="Research", slug='research', show_in_menus=True,
                                           content_type=singlepage_content_type))
    homepage.add_child(instance=SinglePage(title="People", slug='people', show_in_menus=True,
                                           content_type=singlepage_content_type))
    homepage.add_child(instance=SinglePage(title="Courses", slug='courses', show_in_menus=True,
                                           content_type=singlepage_content_type))
    homepage.add_child(instance=SinglePage(title="News", slug='news', show_in_menus=True,
                                           content_type=singlepage_content_type))
    homepage.add_child(instance=SinglePage(title="Contact Us", slug='contact-us', show_in_menus=True,
                                           content_type=singlepage_content_type))

    Site.objects.create(
        hostname="localhost",
        root_page=homepage,
        is_default_site=True,
        site_name="mll.ce.sharif.edu",
    )


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '__latest__'),
        ('wagtailforms', '__latest__'),
        ('main_pages', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initialize_model),
    ]
