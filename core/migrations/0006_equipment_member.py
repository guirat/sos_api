# Generated by Django 2.1.5 on 2019-02-27 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_equipment'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Member'),
        ),
    ]
