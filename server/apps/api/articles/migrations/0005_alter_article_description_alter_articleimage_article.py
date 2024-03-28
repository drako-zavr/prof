# Generated by Django 4.2.6 on 2024-03-07 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_rename_articleimages_articleimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='articleimage',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='articles.article', verbose_name='Новость'),
        ),
    ]
