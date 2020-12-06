# Generated by Django 3.1.4 on 2020-12-06 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_remove_quizpage_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizpage',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizpages', to='game.question'),
        ),
    ]
