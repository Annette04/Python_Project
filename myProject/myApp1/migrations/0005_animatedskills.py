# Generated by Django 5.0.1 on 2024-01-10 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp1', '0004_visualdateskills'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimatedSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
