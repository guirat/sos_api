# Generated by Django 2.1.5 on 2019-02-24 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_auto_20190120_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='price',
            field=models.FloatField(verbose_name='Price'),
        ),
    ]
