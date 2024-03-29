# Generated by Django 2.2.1 on 2019-05-14 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liver', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='female_lethal',
            old_name='glycose',
            new_name='glucose',
        ),
        migrations.RenameField(
            model_name='male_lethal',
            old_name='mgm',
            new_name='mgp',
        ),
        migrations.AlterField(
            model_name='female_compl',
            name='chr_pan',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='female_compl',
            name='csn',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='female_compl',
            name='ibs',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='female_compl',
            name='lp',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='female_compl',
            name='result',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='female_lethal',
            name='methylprednise',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='female_lethal',
            name='mfa',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='female_lethal',
            name='result',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='female_lethal',
            name='takrolimus',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='male_lethal',
            name='bkk',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='male_lethal',
            name='mfa',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='male_lethal',
            name='result',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='male_lethal',
            name='vrvp',
            field=models.BooleanField(),
        ),
    ]
