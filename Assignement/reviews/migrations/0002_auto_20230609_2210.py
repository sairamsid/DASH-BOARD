# Generated by Django 3.0.14 on 2023-06-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboarddata',
            name='end_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashboarddata',
            name='start_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
