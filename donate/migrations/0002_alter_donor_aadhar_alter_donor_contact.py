# Generated by Django 4.2.1 on 2023-06-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='aadhar',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='donor',
            name='contact',
            field=models.CharField(max_length=10),
        ),
    ]
