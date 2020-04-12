# Generated by Django 2.2.10 on 2020-04-12 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dt', '0002_typedowntime_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='workdowntime',
            name='obj',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='dt.ObjectDownTime', verbose_name='Объект'),
            preserve_default=False,
        ),
    ]