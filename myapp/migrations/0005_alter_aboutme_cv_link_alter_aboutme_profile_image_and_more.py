# Generated by Django 5.1.4 on 2025-01-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_portfolio_project_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='cv_link',
            field=models.FileField(upload_to='resumes/'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='project_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
