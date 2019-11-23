# Generated by Django 2.2 on 2019-11-22 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MeinPage', '0025_package_visable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='visable',
        ),
        migrations.AddField(
            model_name='hotel',
            name='updated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hotel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
