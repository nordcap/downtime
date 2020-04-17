# Generated by Django 2.2.10 on 2020-04-17 20:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dt', '0009_auto_20200416_0013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_index=True, default=django.utils.timezone.now, verbose_name='Дата работ')),
                ('comment_one', models.CharField(blank=True, default='', max_length=255, verbose_name='Комментарий к работам в 1 смену')),
                ('comment_two', models.CharField(blank=True, default='', max_length=255, verbose_name='Комментарий к работам в 2 смену')),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dt.ObjectDownTime', verbose_name='Объект')),
            ],
            options={
                'verbose_name_plural': 'Производимые работы',
                'ordering': ['-date'],
                'verbose_name': 'Производимые работы',
            },
        ),
        migrations.RemoveField(
            model_name='downtime',
            name='type_downtime',
        ),
        migrations.AddField(
            model_name='downtime',
            name='smena',
            field=models.CharField(choices=[('1', '1 смена'), ('2', '2 смена')], default='1', max_length=1, verbose_name='Смена'),
        ),
        migrations.AddField(
            model_name='downtime',
            name='type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dt.TypeDownTime', verbose_name='Тип простоя'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='WorkDownTime',
        ),
        migrations.AddField(
            model_name='work',
            name='type',
            field=models.ManyToManyField(null=True, through='dt.DownTime', to='dt.TypeDownTime'),
        ),
        migrations.AddField(
            model_name='downtime',
            name='work',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='works', to='dt.Work', verbose_name='Комментарии'),
            preserve_default=False,
        ),
    ]