# Generated by Django 3.2.21 on 2023-09-22 10:36

from django.db import migrations, models
import django.db.models.deletion
import roadtrips.models


class Migration(migrations.Migration):

    dependencies = [
        ('roadtrips', '0005_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=roadtrips.models.get_default_category, on_delete=django.db.models.deletion.CASCADE, to='roadtrips.category'),
        ),
    ]
