# Generated by Django 4.1.2 on 2022-11-01 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='contact_no',
            field=models.CharField(max_length=15),
        ),
    ]
