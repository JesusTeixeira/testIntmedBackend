# Generated by Django 3.0 on 2021-10-03 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20211003_1537'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Consultas',
            new_name='Consulta',
        ),
        migrations.RenameModel(
            old_name='Medicos',
            new_name='Medico',
        ),
    ]
