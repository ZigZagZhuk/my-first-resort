# Generated by Django 2.0.3 on 2018-03-20 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180223_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Имя')),
                ('patronomic', models.CharField(blank=True, max_length=64, verbose_name='Отчество')),
                ('surname', models.CharField(max_length=64, verbose_name='Фамилия')),
                ('specialization', models.CharField(max_length=64, verbose_name='Специализация')),
                ('room', models.IntegerField(default=None, verbose_name='Кабинет')),
            ],
            options={
                'verbose_name': 'Врач',
                'verbose_name_plural': 'Врачи',
            },
        ),
        migrations.AddField(
            model_name='guest',
            name='doctors',
            field=models.ManyToManyField(help_text='Выберите врачей для постояльца.', to='core.Doctor', verbose_name='Врачи'),
        ),
    ]