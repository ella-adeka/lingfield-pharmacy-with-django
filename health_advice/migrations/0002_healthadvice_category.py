# Generated by Django 3.0.8 on 2020-10-19 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health_advice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthadvice',
            name='category',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='health_advice.HealthAdviceCategory', verbose_name='HealthAdviceCategory'),
            preserve_default=False,
        ),
    ]
