# Generated by Django 2.1.5 on 2019-02-24 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_auto_20190224_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='tickets',
        ),
        migrations.AddField(
            model_name='ticket',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='event.Event', verbose_name='event'),
        ),
    ]
