from django.contrib.contenttypes.models import ContentType
from wagtail.core.models import Page, Site
from django.db import migrations, DatabaseError, transaction

from snippets.models import Person, Paper, LabInfo, Course

import pandas as pd


def clean_model(apps, schema_editor):
    Person.objects.all().delete()
    Paper.objects.all().delete()
    LabInfo.objects.all().delete()
    Course.objects.all().delete()


def initialize_model(apps, schema_editor):
    position_mapping = {
        'Graduate Alumni': 'grad_alumini',
        'PhD Student': 'phd',
        'Master Student': 'master',
        'Adminitration': 'administration'
    }

    people_df = pd.read_csv('.data/initial_data/mll_new_people.csv')
    for i, person in people_df.iterrows():
        if pd.isnull(person['project']):
            person['project'] = ''
        if pd.isnull(person['homepage']):
            person['homepage'] = ''
        Person(
            title=person['title'][:-1].lower(),
            firstname=person['firstname'],
            lastname=person['lastname'],
            project_title=person['project'],
            position=position_mapping[person['position']],
            homepage=person['homepage'],
            email=person['email'],
            class_of=float(person['class']),
        ).save()

    assert len(people_df) == len(Person.objects.all())


    courses_df = pd.read_csv('.data/initial_data/mll_courses.csv')
    for i, course in courses_df.iterrows():
        Course(
            title=course['title'],
            year=course['year'],
            semester=course['semester'].lower(),
            coursepage=course['coursepage'],
            instructor=Person.objects.get(lastname=course['instructor'])
        ).save()

    assert len(courses_df) == len(Course.objects.all())


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initialize_model, reverse_code=clean_model),
    ]
