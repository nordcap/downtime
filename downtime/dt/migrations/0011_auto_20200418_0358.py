# Generated by Django 2.2.10 on 2020-04-17 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dt', '0010_auto_20200418_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downtime',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types', to='dt.TypeDownTime', verbose_name='Тип простоя'),
        ),
    ]
