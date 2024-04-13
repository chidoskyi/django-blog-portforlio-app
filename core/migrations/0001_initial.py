# Generated by Django 5.0.3 on 2024-03-28 18:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=500)),
                ('email_info', models.CharField(max_length=500)),
                ('office', models.CharField(max_length=500)),
                ('website', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greetings', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=10000)),
                ('home_img', models.ImageField(upload_to='picture_home/')),
                ('time_added', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.TextField()),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio/')),
                ('details_url', models.URLField()),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('date_subscribed', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.CharField(max_length=10)),
                ('end_year', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='core.about')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.CharField(max_length=10)),
                ('end_year', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='core.about')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('website', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=500)),
                ('freelance', models.CharField(max_length=500)),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profileinfo', to='core.about')),
            ],
        ),
        migrations.CreateModel(
            name='ProgressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('count', models.PositiveSmallIntegerField(default=0)),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progressbar', to='core.about')),
            ],
        ),
    ]