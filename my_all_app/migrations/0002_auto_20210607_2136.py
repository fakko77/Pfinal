# Generated by Django 3.2.2 on 2021-06-07 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_all_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='user',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='user',
            field=models.IntegerField(null=True),
        ),
    ]
