# Generated by Django 3.2.4 on 2021-07-05 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_auto_20210705_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('user_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]
