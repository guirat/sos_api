# Generated by Django 2.1.5 on 2019-01-13 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20190113_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='ticket_num',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]