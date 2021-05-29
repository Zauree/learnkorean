# Generated by Django 3.2.3 on 2021-05-29 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learnkorean', '0011_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorire',
            name='product',
        ),
        migrations.RemoveField(
            model_name='favorire',
            name='user',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AlterModelOptions(
            name='favorite',
            options={'verbose_name': 'Менің сөздігім', 'verbose_name_plural': 'Менің сөздігімдегі сөздер'},
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Favorire',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
