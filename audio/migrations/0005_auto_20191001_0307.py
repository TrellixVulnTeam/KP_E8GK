# Generated by Django 2.2.3 on 2019-10-01 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0004_auto_20190930_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='file',
            name='size',
            field=models.IntegerField(default=0),
        ),
    ]