# Generated by Django 5.0.3 on 2024-03-31 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_remove_reply_reaction_remove_comment_reaction_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='likes',
        ),
    ]
