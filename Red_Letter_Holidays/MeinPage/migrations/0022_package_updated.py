# Generated by Django 2.2 on 2019-11-21 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MeinPage', '0021_auto_20191121_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='updated',
            field=models.BooleanField(default=False),
        ),
    ]
