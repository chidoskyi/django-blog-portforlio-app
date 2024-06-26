# Generated by Django 5.0.3 on 2024-04-01 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0018_rename_reaction_type_comment_reaction_types'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='reaction_types',
            new_name='reaction_type',
        ),
        migrations.RemoveField(
            model_name='reaction',
            name='reaction_types',
        ),
        migrations.AddField(
            model_name='reaction',
            name='reaction_type',
            field=models.CharField(choices=[('👍', '👍'), ('👎', '👎'), ('❤️', '❤️'), ('😲', '😲'), ('😢', '😢'), ('🤣', '🤣'), ('😡', '😡'), ('❤️\u200d🩹', '❤️\u200d🩹'), ('🤗', '🤗')], default=1, max_length=10),
        ),
    ]
