# Generated by Django 3.2.3 on 2021-07-05 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_all_app', '0003_alter_position_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='be',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='tp1',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='tp2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='tp3',
            field=models.FloatField(null=True),
        ),
    ]
