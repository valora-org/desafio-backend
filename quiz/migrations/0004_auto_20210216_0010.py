# Generated by Django 3.1.6 on 2021-02-16 00:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0003_auto_20210215_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='category',
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quiz.category'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
