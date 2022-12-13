# Generated by Django 4.1.3 on 2022-12-11 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bebe',
            name='hora_nacimiento',
            field=models.TimeField(blank=True, default='22:29:27'),
        ),
        migrations.CreateModel(
            name='AvanceDiario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.PositiveSmallIntegerField(blank=True, default=1)),
                ('tolerancia', models.CharField(blank=True, default='Regular', max_length=7, null=True)),
                ('unidad', models.CharField(blank=True, choices=[('UCI', 'UCI'), ('UTI', 'UTI')], default='EN CAMBIO', max_length=3, null=True)),
                ('cama', models.IntegerField(blank=True, default=1, null=True)),
                ('orina', models.CharField(blank=True, choices=[('Si', 'Si'), ('No', 'No')], default='Si', max_length=2, null=True)),
                ('deposiciones', models.CharField(blank=True, choices=[('Si', 'Si'), ('No', 'No')], default='Si', max_length=2, null=True)),
                ('bebe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.bebe')),
            ],
        ),
    ]
