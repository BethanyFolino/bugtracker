# Generated by Django 3.2.6 on 2021-09-02 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_auto_20210902_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date_filed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]