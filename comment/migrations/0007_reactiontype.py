# Generated by Django 5.0.3 on 2024-03-31 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0006_reaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReactionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction_type', models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]