# Generated by Django 2.2.6 on 2019-10-10 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_01', '0005_auto_20191010_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseinformation',
            name='mk',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='baseinformation',
            name='tpk',
            field=models.TextField(),
        ),
    ]