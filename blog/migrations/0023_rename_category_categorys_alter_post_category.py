# Generated by Django 5.0.3 on 2024-04-10 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_alter_post_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categorys',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=255),
        ),
    ]
