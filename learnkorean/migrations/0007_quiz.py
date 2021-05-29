# Generated by Django 3.2.3 on 2021-05-29 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learnkorean', '0006_listening'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('answer', models.IntegerField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learnkorean.lesson')),
            ],
        ),
    ]
