# Generated by Django 5.0.3 on 2024-04-01 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0017_remove_reaction_reaction_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='reaction_type',
            new_name='reaction_types',
        ),
    ]
