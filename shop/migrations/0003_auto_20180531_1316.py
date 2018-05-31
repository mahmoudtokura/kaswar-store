# Generated by Django 2.0.4 on 2018-05-31 12:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0002_usershippingdetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserShippingDetails',
            new_name='UserShippingDetail',
        ),
        migrations.AlterModelOptions(
            name='usershippingdetail',
            options={'verbose_name': 'usershippingdetail', 'verbose_name_plural': 'usershippingdetails'},
        ),
    ]