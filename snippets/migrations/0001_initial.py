# Generated by Django 3.1.1 on 2020-09-10 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=1000)),
                ('intoduction_text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_type', models.CharField(choices=[('journal', 'Journal'), ('conference', 'Conference')], max_length=100)),
                ('authors', models.CharField(max_length=100)),
                ('order', models.CharField(max_length=100)),
                ('year', models.CharField(blank=True, max_length=100)),
                ('publisher', models.CharField(blank=True, max_length=100)),
                ('book_title', models.CharField(blank=True, max_length=100)),
                ('pages', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('volume', models.CharField(blank=True, max_length=100)),
                ('date', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('mr', 'Mr.'), ('ms', 'Ms.'), ('dr', 'Dr.')], max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('homepage', models.URLField(blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('project_title', models.CharField(blank=True, max_length=200)),
                ('position', models.CharField(choices=[('administration', 'Administration'), ('phd', 'PhD student'), ('master', 'Master student'), ('undergrad', 'Undergraduate student'), ('grad_alumini', 'Graduate Alumini'), ('undergrad_alumini', 'Undergraduate Alumini')], max_length=50)),
                ('class_of', models.IntegerField(default=94)),
                ('profile_pic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.CharField(blank=True, max_length=5)),
                ('semester', models.CharField(choices=[('fall', 'Fall'), ('spring', 'Spring')], max_length=10)),
                ('coursepage', models.URLField()),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tought_courses', to='snippets.person')),
                ('pic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
        ),
    ]
