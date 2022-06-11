# Generated by Django 4.0.5 on 2022-06-11 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historyresponse',
            options={'verbose_name': 'отклик', 'verbose_name_plural': 'история откликов'},
        ),
        migrations.RemoveField(
            model_name='bonus',
            name='vacancy',
        ),
        migrations.RemoveField(
            model_name='requirement',
            name='vacancy',
        ),
        migrations.RemoveField(
            model_name='task',
            name='vacancy',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='bonus',
            field=models.ManyToManyField(blank=True, null=True, to='partner.bonus', verbose_name='бонусы волонтера'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='requirements',
            field=models.ManyToManyField(blank=True, null=True, to='partner.requirement', verbose_name='требования'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='task',
            field=models.ManyToManyField(blank=True, null=True, to='partner.task', verbose_name='задачи волонтера'),
        ),
        migrations.AlterField(
            model_name='bonus',
            name='name',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='задача'),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='name',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='требование'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='задача'),
        ),
    ]
