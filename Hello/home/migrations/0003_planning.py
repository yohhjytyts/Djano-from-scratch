# Generated by Django 3.2.7 on 2021-09-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('desc', models.TextField()),
                ('C_name', models.TextField()),
                ('time', models.TextField()),
                ('loc', models.TextField()),
                ('quantity', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('value', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
