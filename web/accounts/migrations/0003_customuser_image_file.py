# Generated by Django 2.2.6 on 2019-12-20 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191220_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
