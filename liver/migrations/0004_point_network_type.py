# Generated by Django 2.2.1 on 2019-05-14 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liver', '0003_auto_20190514_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='network_type',
            field=models.CharField(default='none', max_length=20),
        ),
    ]
