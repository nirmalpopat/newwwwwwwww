# Generated by Django 3.2.4 on 2021-07-08 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0007_usermodel1_pri'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel1',
            name='pri',
            field=models.CharField(max_length=100),
        ),
    ]
