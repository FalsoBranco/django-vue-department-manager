# Generated by Django 3.2.7 on 2021-09-01 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('department', models.CharField(max_length=500)),
                ('date_of_joining', models.DateField()),
            ],
        ),
    ]