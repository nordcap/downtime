# Generated by Django 2.2.10 on 2020-04-12 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='typedowntime',
            name='comment',
            field=models.CharField(default='', max_length=100, verbose_name='Пояснение (расшифровка)'),
        ),
    ]