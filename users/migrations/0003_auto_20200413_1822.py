# Generated by Django 2.2.12 on 2020-04-13 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profileviewcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='profile_pics/2019-08-08-000102_NjSNT4p.jpg', upload_to='profile_pics/'),
        ),
    ]
