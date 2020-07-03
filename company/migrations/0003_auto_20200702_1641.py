# Generated by Django 3.0.8 on 2020-07-02 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_details_minoffers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='minOffers',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='details',
            name='mobileNumber',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='details',
            name='numberOfRounds',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='details',
            name='phoneNumber',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='details',
            name='stipulatedBond',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='details',
            name='trainingPeriod',
            field=models.CharField(default='0', max_length=10),
        ),
    ]