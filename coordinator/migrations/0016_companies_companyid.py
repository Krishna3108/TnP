# Generated by Django 3.0.7 on 2020-07-01 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('coordinator', '0015_delete_updatestudents'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='companyID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Details'),
        ),
    ]
