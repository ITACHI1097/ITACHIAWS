# Generated by Django 3.1 on 2020-11-11 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0013_auto_20201028_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='icfes/'),
        ),
    ]
