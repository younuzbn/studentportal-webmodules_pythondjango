# Generated by Django 3.2.23 on 2024-01-06 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_id_card_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='id_card',
            name='STUDENT',
        ),
    ]
