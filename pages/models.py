from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from PIL import Image

# Create your models here.


class DevEduBackground(models.Model):
    level = models.CharField(max_length=100, blank=True)
    inclusive_date = models.CharField(max_length=50, blank=True)
    school_or_institution = models.CharField(max_length=300, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.school_or_institution}-{self.level}"

    class Meta:
        ordering = ['-created_at']

        verbose_name = 'Educational Background'
        verbose_name_plural = 'Educational Backgrounds'


class DevLanguages(models.Model):
    language = models.CharField(max_length=50, blank=True)
    language_percentage = models.CharField(max_length=50, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.language}"

    class Meta:
        ordering = ['-created_at']

        verbose_name = 'Language'
        verbose_name_plural = 'Languages'


class DevProfile(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    middle_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=30, blank=True)
    phone = models.CharField(max_length=20, default="N/A", blank=True)
    mobile = models.CharField(max_length=20, default="N/A", blank=True)

    bio = models.TextField(max_length=1000, blank=True)
    dev_avatar = models.ImageField(
        default='default/avatar.png', upload_to='dev_profiles/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job_title}"

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.dev_avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.dev_avatar.path)

    class Meta:
        verbose_name = 'Developer profile'
        verbose_name_plural = 'Developer Profiles'


class DevProfessionalVolunteerEXP(models.Model):
    inclusive_date = models.CharField(max_length=50, blank=True)
    exp_or_job_title = models.CharField(max_length=100, blank=True)
    company_or_organization = models.CharField(max_length=200, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.exp_or_job_title}-{self.company_or_organization}"

    class Meta:
        ordering = ['-created_at']

        verbose_name = 'Professional/Volunteer Experience'
        verbose_name_plural = 'Professional/Volunteer Experiences'


class DevSkills(models.Model):
    skill = models.CharField(max_length=50, blank=True)
    skill_percentage = models.CharField(max_length=50, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.skill}"

    class Meta:
        ordering = ['-created_at']

        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class DevTrainingsSeminarsWorkshopAttended(models.Model):
    inclusive_date = models.CharField(max_length=50, blank=True)
    training_seminar_workshop_attended = models.CharField(
        max_length=300, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.training_seminar_workshop_attended}"

    class Meta:
        ordering = ['-created_at']

        verbose_name = 'Trainings, Seminars/Workshop Attended'
        verbose_name_plural = 'Trainings, Seminars/Workshop Attended'


class Profile(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    middle_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(
        User, max_length=200, on_delete=models.CASCADE, unique=True)

    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(
        default='default/avatar.png', upload_to='avatars/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} | {self.created_at.strftime( '%d-%m-%Y' )}"

    @staticmethod
    def get_absolute_url():
        return reverse('home')

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)
