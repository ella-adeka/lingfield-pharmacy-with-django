# Generated by Django 3.0.8 on 2020-10-31 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_news', '0005_auto_20201030_2344'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
