# Generated by Django 5.0.1 on 2024-01-07 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VisualDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('table', models.JSONField()),
            ],
        ),
    ]