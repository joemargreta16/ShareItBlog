# Generated by Django 3.2.9 on 2022-03-09 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_devprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='DevProfessionalVolunteerEXP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inclusive_date', models.CharField(blank=True, max_length=20)),
                ('exp_or_job_title', models.CharField(blank=True, max_length=100)),
                ('company_or_organization', models.CharField(blank=True, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DevTrainingsSeminarsWorkshopAttended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inclusive_date', models.CharField(blank=True, max_length=20)),
                ('training_seminar_workshop_attended', models.CharField(blank=True, max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='devprofile',
            options={'verbose_name': 'Dev profiles', 'verbose_name_plural': 'Developer Profiles'},
        ),
    ]
