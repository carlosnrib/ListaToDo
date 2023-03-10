# Generated by Django 4.1.2 on 2022-10-24 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=256)),
                ('prioridade', models.IntegerField(choices=[(0, 'NENHUMA'), (1, 'ALTA'), (2, 'MÉDIA'), (3, 'BAIXA')], default=0)),
                ('data', models.DateField(null=True)),
                ('feita', models.BooleanField(default=False)),
                ('lista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listas.listas')),
            ],
        ),
    ]
