# Generated by Django 2.2.6 on 2019-10-11 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20191011_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authentic',
            name='pair_key',
            field=models.TextField(),
        ),
    ]
