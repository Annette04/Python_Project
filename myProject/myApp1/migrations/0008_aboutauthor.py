# Generated by Django 5.0.1 on 2024-01-11 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp1', '0007_delete_gethhvacancies'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('url', models.URLField()),
            ],
        ),
    ]
