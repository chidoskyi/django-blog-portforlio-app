# Generated by Django 5.0.3 on 2024-03-31 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0010_comment_reaction_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='reaction_type',
        ),
    ]