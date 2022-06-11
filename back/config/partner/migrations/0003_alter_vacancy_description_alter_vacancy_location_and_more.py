# Generated by Django 4.0.5 on 2022-06-10 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(help_text='Требования к кандидатам и функционал', max_length=1000, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='location',
            field=models.CharField(help_text='Место проведения мероприятия', max_length=100, verbose_name='местоположение'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='terms',
            field=models.TextField(help_text='Условия работы для волонтера', max_length=100, verbose_name='условия'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='type_of_work',
            field=models.CharField(choices=[('without payment', 'Без оплаты'), ('permanent job', 'Постоянная'), ('internship', 'Стажировка'), ('side job', 'Подработка')], default='without payment', max_length=50, verbose_name='тип работы'),
        ),
    ]
