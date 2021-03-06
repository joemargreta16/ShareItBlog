# Generated by Django 3.2.9 on 2022-03-09 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20220309_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='DevEduBackground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, max_length=100)),
                ('inclusive_date', models.CharField(blank=True, max_length=50)),
                ('training_seminar_workshop_attended', models.CharField(blank=True, max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Educational Background',
                'verbose_name_plural': 'Educational Backgrounds',
            },
        ),
        migrations.AlterModelOptions(
            name='devprofessionalvolunteerexp',
            options={'verbose_name': 'Professional/Volunteer Experience', 'verbose_name_plural': 'Professional/Volunteer Experiences'},
        ),
        migrations.AlterModelOptions(
            name='devprofile',
            options={'verbose_name': 'Developer profile', 'verbose_name_plural': 'Developer Profiles'},
        ),
        migrations.AlterModelOptions(
            name='devtrainingsseminarsworkshopattended',
            options={'verbose_name': 'Trainings, Seminars/Workshop Attended', 'verbose_name_plural': 'Trainings, Seminars/Workshop Attended'},
        ),
        migrations.AlterField(
            model_name='devprofessionalvolunteerexp',
            name='inclusive_date',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='devtrainingsseminarsworkshopattended',
            name='inclusive_date',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
