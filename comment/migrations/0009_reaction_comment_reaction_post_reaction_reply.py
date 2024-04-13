# Generated by Django 5.0.3 on 2024-03-31 20:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_remove_post_reaction_delete_reaction'),
        ('comment', '0008_remove_reaction_content_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reaction',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_reactions', to='comment.comment'),
        ),
        migrations.AddField(
            model_name='reaction',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_reactions', to='blog.post'),
        ),
        migrations.AddField(
            model_name='reaction',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_reactions', to='comment.reply'),
        ),
    ]
