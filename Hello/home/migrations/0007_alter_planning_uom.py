# Generated by Django 3.2.7 on 2021-09-28 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_planning_uom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planning',
            name='uom',
            field=models.CharField(default='-', max_length=255),
        ),
    ]
