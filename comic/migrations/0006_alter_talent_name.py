# Generated by Django 3.2.7 on 2021-12-01 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0005_auto_20211201_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talent',
            name='name',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]
