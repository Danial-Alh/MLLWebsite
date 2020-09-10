from django.db import models
from rest_framework.fields import CharField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtailstreamforms.wagtailstreamforms_fields import EmailField


@register_snippet
class Person(models.Model):
    title = models.CharField(max_length=200, choices=[
        ("mr", "Mr."),
        ("ms", "Ms."),
        ("dr", "Dr.")
    ])  # mr ms dr
    name = models.CharField(max_length=200)
    homepage = models.URLField(blank=True)
    email = models.EmailField()
    project_title = models.CharField(max_length=200, blank=True)
    position = models.CharField(max_length=50, choices=[
        ('administration', 'Administration'),
        ('phd', 'PhD student'),
        ('master', 'Master student'),
        ('grad_alumini', 'Graduate Alumini'),
        ('undergrad', 'Undergraduate student'),
        ('undergrad_alumini', 'Undergraduate Alumini'),
    ])
    class_of = models.IntegerField(default=94)  # 96
    profile_pic = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('name'),
        FieldPanel('homepage'),
        FieldPanel('email'),
        FieldPanel('project_title'),
        FieldPanel('position'),
        FieldPanel('class_of'),
        ImageChooserPanel('profile_pic'),
    ]

    def __str__(self):
        return self.name


@register_snippet
class Paper(models.Model):
    title = models.CharField(max_length=100)  # *
    pub_type = models.CharField(max_length=100, choices=[
        ('journal', 'Journal'),
        ('conference', 'Conference')
    ])  # * # journal / conf
    authors = models.CharField(max_length=100)  # *
    order = models.CharField(max_length=100)  # *
    year = models.CharField(blank=True, max_length=100)
    publisher = models.CharField(blank=True, max_length=100)
    book_title = models.CharField(blank=True, max_length=100)
    pages = models.CharField(blank=True, max_length=100)
    address = models.CharField(blank=True, max_length=100)
    volume = models.CharField(blank=True, max_length=100)
    date = models.DateField(blank=True)  # datepicker / today

    panels = [
        FieldPanel('title'),
        FieldPanel('pub_type'),
        FieldPanel('authors'),
        FieldPanel('order'),
        FieldPanel('year'),
        FieldPanel('publisher'),
        FieldPanel('book_title'),
        FieldPanel('pages'),
        FieldPanel('address'),
        FieldPanel('volume'),
        FieldPanel('date'),
    ]

    def __str__(self):
        pass


@register_snippet
class Course(models.Model):
    title = models.CharField(max_length=100)
    instructor = models.ForeignKey(
        'snippets.Person',
        related_name='tought_courses',
        on_delete=models.CASCADE,
    )
    year = models.CharField(blank=True, max_length=5)
    semester = models.CharField(max_length=10, choices=[
        ('fall', "Fall"),
        ('spring', "Spring")
    ])
    coursepage = models.URLField()
    pic = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('title'),
        SnippetChooserPanel('instructor'),
        FieldPanel('year'),
        FieldPanel('semester'),
        FieldPanel('coursepage'),
        ImageChooserPanel('pic'),
    ]

    def __str__(self):
        pass


@register_snippet
class LabInfo(models.Model):
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=1000)
    intoduction_text = models.CharField(max_length=1000)

    panels = [
        FieldPanel('contact_email'),
        FieldPanel('phone_number'),
        FieldPanel('address'),
        FieldPanel('intoduction_text'),
    ]

    def save(self, *args, **kwargs):
        self.id = 1
        super().save(*args, **kwargs)
