# Generated by Django 5.0.1 on 2024-01-08 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp1', '0002_alter_visualdate_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisualDateGeography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('table', models.FileField(upload_to='')),
            ],
        ),
        migrations.RenameModel(
            old_name='VisualDate',
            new_name='VisualDateImportance',
        ),
    ]
