# Generated by Django 3.0.8 on 2020-07-05 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20200705_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyapplicants',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
    ]
