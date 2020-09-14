# Generated by Django 2.2.10 on 2020-07-17 09:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio_private_call',
            name='audio_file_path',
            field=models.FileField(blank=True, help_text='Allowed type - .wav', upload_to='upload/audiofiles', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['wav'])]),
        ),
    ]