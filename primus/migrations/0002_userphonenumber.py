# Generated by Django 3.2.10 on 2023-12-30 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15, unique=True)),
            ],
        ),
    ]
