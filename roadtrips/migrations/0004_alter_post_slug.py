# Generated by Django 3.2.21 on 2023-09-08 16:54

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roadtrips', '0003_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True),
        ),
    ]
