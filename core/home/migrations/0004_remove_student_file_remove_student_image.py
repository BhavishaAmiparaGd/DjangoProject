# Generated by Django 5.0 on 2024-01-01 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_student_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='file',
        ),
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
    ]
