# Generated by Django 3.2.6 on 2021-09-05 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome da categoria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, null=True, verbose_name='Pergunta')),
                ('first_answer', models.CharField(max_length=255, null=True, verbose_name='1ª Pergunta')),
                ('second_answer', models.CharField(max_length=255, null=True, verbose_name='2ª Pergunta')),
                ('third_answer', models.CharField(max_length=255, null=True, verbose_name='3ª Pergunta')),
                ('correct_answer', models.CharField(choices=[('1', 'Primeira Pergunta'), ('2', 'Segunda Pergunta'), ('3', 'Terceira Pergunta')], max_length=1, verbose_name='Resposta Correta')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='questions.category', verbose_name='Categoria')),
                ('registered_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Usuário Criador')),
            ],
            options={
                'verbose_name': 'Pergunta',
                'verbose_name_plural': 'Perguntas',
                'db_table': 'question',
            },
        ),
    ]
