# Generated by Django 4.2.6 on 2024-03-29 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255, verbose_name='Имя')),
                ('lastname', models.CharField(blank=True, max_length=255, verbose_name='Фамилия')),
                ('midname', models.CharField(blank=True, max_length=255, verbose_name='Отчество')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='Фотография')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Память',
                'verbose_name_plural': 'Память',
                'ordering': ['firstname'],
            },
        ),
    ]