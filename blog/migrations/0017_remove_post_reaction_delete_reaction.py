# Generated by Django 5.0.3 on 2024-03-31 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_reaction_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='reaction',
        ),
        migrations.DeleteModel(
            name='Reaction',
        ),
    ]
