# Generated by Django 3.0 on 2021-09-19 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultas',
            name='data_agendamento',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='consultas',
            name='dia',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='consultas',
            name='horario',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='consultas',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Medicos'),
        ),
        migrations.AlterField(
            model_name='especialidade',
            name='nome',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='medicos',
            name='especialidade_medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.Especialidade'),
        ),
        migrations.AlterField(
            model_name='medicos',
            name='nome_medico',
            field=models.CharField(max_length=50),
        ),
    ]
