# Generated by Django 3.1.2 on 2020-11-14 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_foodtype_mealtype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meals',
            old_name='BreakFast',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='meals',
            name='Dinner',
        ),
        migrations.RemoveField(
            model_name='meals',
            name='Lunch',
        ),
    ]
