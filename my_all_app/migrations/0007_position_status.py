# Generated by Django 3.2.3 on 2021-07-08 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_all_app', '0006_alter_position_position_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='status',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]