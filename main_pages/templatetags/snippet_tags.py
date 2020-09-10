from django import template

register = template.Library()

@register.simple_tag
def get_persons(position):
    from snippets.models import Person
    return Person.objects.filter(position=position).all()

@register.simple_tag
def get_papers(pub_type):
    from snippets.models import Paper
    return Paper.objects.filter(pub_type=pub_type).all()

@register.simple_tag
def get_courses():
    from snippets.models import Course
    return Course.objects.all()

@register.simple_tag
def get_lab_info():
    from snippets.models import LabInfo
    return LabInfo.objects.all()[0]
