# Generated by Django 5.0.3 on 2024-03-31 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_reaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='reaction',
            name='name',
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AlterField(
            model_name='reaction',
            name='type',
            field=models.CharField(choices=[('👍', '👍'), ('👎', '👎'), ('❤️', '❤️'), ('😲', '😲'), ('😢', '😢'), ('🤣', '🤣'), ('😡', '😡'), ('❤️\u200d🩹', '❤️\u200d🩹'), ('❤️', '❤️')], max_length=10),
        ),
    ]
