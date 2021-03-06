# Generated by Django 2.1.2 on 2019-04-12 03:04

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('committee', models.CharField(choices=[('Executive', 'Executive'), ('Academics', 'Academics'), ('Externals', 'Externals'), ('Extracurricular', 'Extracurricular'), ('Finance', 'Finance'), ('Internals', 'Internals'), ('Membership', 'Membership'), ('Publicity', 'Publicity'), ('Matrix Project', 'Matrix Project')], default='', max_length=100)),
                ('level', models.CharField(choices=[('Associate', 'Associate'), ('Director', 'Director'), ('Project Manager', 'Project Manager'), ('Project Head', 'Project Head'), ('Member', 'Member')], default='', max_length=100)),
                ('project', models.CharField(max_length=100)),
                ('number_of_people', models.IntegerField(default=1)),
                ('job_description', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), size=None)),
                ('objectives', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), size=None)),
                ('timeline', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), size=None)),
                ('important_skills', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), size=None)),
                ('challenges_faced', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), size=None)),
                ('opportunities', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), size=None)),
                ('role_history', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), size=None)),
                ('document_resources', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), size=None)),
                ('resources', django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=250), size=None)),
            ],
        ),
    ]
