# Generated by Django 2.1.7 on 2019-03-13 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20190313_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='butterfly',
            name='flowers',
            field=models.ManyToManyField(to='main_app.Flower'),
        ),
    ]
