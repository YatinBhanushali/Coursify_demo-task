# Generated by Django 4.2.3 on 2023-08-02 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='stipend',
            field=models.CharField(max_length=100),
        ),
    ]
