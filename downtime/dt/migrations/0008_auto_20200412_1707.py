# Generated by Django 2.2.10 on 2020-04-12 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dt', '0007_auto_20200412_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downtime',
            name='smena',
            field=models.CharField(choices=[(1, '1 смена'), (2, '2 смена')], default=1, max_length=1, verbose_name='Смена'),
        ),
    ]
