# Generated by Django 3.2.9 on 2021-11-28 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_alter_option_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='option',
            unique_together=set(),
        ),
    ]
