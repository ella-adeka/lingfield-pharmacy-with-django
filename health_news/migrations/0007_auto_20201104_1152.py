# Generated by Django 3.1.1 on 2020-11-04 10:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('health_news', '0006_auto_20201031_1202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='healthnews',
            options={'ordering': ['-created_at'], 'verbose_name': 'Health News', 'verbose_name_plural': 'Health News'},
        ),
        migrations.RemoveField(
            model_name='healthnews',
            name='date',
        ),
        migrations.AddField(
            model_name='healthnews',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='healthnews',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
    ]
