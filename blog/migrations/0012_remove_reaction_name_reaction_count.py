# Generated by Django 5.0.3 on 2024-03-31 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_reaction_alter_reaction_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reaction',
            name='name',
        ),
        migrations.AddField(
            model_name='reaction',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]