# Generated by Django 3.2.9 on 2022-03-09 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_delete_devmember'),
    ]

    operations = [
        migrations.CreateModel(
            name='DevProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200)),
                ('middle_name', models.CharField(blank=True, max_length=200)),
                ('last_name', models.CharField(blank=True, max_length=200)),
                ('job_title', models.CharField(blank=True, max_length=30)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(blank=True, max_length=30)),
                ('phone', models.CharField(blank=True, default='N/A', max_length=20)),
                ('mobile', models.CharField(blank=True, default='N/A', max_length=20)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('dev_avatar', models.ImageField(default='default/avatar.png', upload_to='dev_profiles/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]