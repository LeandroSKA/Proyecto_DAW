# Generated by Django 3.1.4 on 2022-05-29 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='foto',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='foto',
        ),
    ]
